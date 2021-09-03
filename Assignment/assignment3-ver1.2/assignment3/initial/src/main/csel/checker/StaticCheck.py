from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class NumberType(Prim):
    pass


class StringType(Prim):
    pass


class BoolType(Prim):
    pass


class VoidType(Type):
    pass


class Unknown(Type):
    pass


@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type


@dataclass
class MType:
    intype: List[Type]
    restype: Type


@dataclass
class Symbol:
    name: str
    mtype: Type


@dataclass
class RefInfo:
    refEnvi: List[Symbol]
    localEnvi: List[Symbol]
    innerStmt: Stmt = None
    funcName: str = None
    inferredType: Type = None
    typeRequired: bool = True


@dataclass
class ExpRes:
    retType: Type = None


class StaticChecker(BaseVisitor):

    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def visitStmt(self, ast, c):
        self.visit(ast, RefInfo(refEnvi=c.refEnvi[:], localEnvi=[
        ], innerStmt=ast, funcName=c.funcName, inferredType=None, typeRequired=True))

    def visitExpr(self, ast, c):
        return self.visit(ast, RefInfo(refEnvi=c.refEnvi[:], localEnvi=[], innerStmt=c.innerStmt, funcName=c.funcName, inferredType=c.inferredType, typeRequired=c.typeRequired))

    def sameType(self, typeA, typeB):
        return (isinstance(typeA, NumberType) and isinstance(typeB, NumberType)) or (isinstance(typeA, StringType) and isinstance(typeB, StringType)) or (isinstance(typeA, BoolType) and isinstance(typeB, BoolType)) or (isinstance(typeA, ArrayType) and isinstance(typeB, ArrayType) and len(typeA.dimen) == len(typeB.dimen) and self.sameType(typeA.eletype, typeB.eletype))

    def arrayLiteral2Type(self, literal, arrayLiteral):
        if len(literal.value) == 0:
            return None
        mType = None
        for lit in literal.value:
            temp = None
            if isinstance(lit, ArrayLiteral):
                temp = self.arrayLiteral2Type(literal, arrayLiteral)
            else:
                temp = self.literal2Type(lit)
            if mType is None:
                mType = temp
            elif temp is not None:
                if not self.sameType(mType, temp):
                    raise InvalidArrayLiteral(arrayLiteral)
        return mType
    
    def literal2Type(self,literal):
        if isinstance(literal, visitNumberLiteral):
            return NumberType()
        elif isinstance(literal, BooleanLiteral):
            return BoolType()
        elif isinstance(literal, StringLiteral):
            return StringType()
        else:
            return self.arrayLiteral2Type(literal, literal)

    def varDecl2Sym(self,varDecl):
        varType=None
        if varDecl.varInit is not None:
            varType=self.literal2Type(varDecl.varInit)
        if len(varDecl.varDimen)>0:
            varType=ArrayType(varDecl.varDimen, varType)
        return Symbol(varDecl.variable.name, varType)
    
    def funcDecl2Sym(self, funcDecl):
        paraTypes=[]
        for varDecl in funcDecl.param:
            if len(varDecl.varDimen)>0:
                paraTypes.append(ArrayType(varDecl.varDimen,None))
            else:
                paraTypes.append(None)
        return Symbol(funcDecl.name.name,MType(paraTypes,None))


    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("str2num",MType([StringType()],NumberType())),
            Symbol("num2str",MType([NumberType()],StringType())),
            Symbol("str2bool",MType([StringType()],BoolType())),
            Symbol("bool2str",MType([BoolType()],StringType())),           
            ###
            Symbol("read", MType([], StringType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printSLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        #[self.visit(x, c) for x in ast.decl]
        hasMain=False
        for decl in ast.decl:
            if isinstance(decl,VarDecl):
                if self.lookup(decl.variable.name,self.global_envi,lambda x: x.name) is None:
                    self.global_envi.append(self.varDecl2Sym(decl))
                else:
                    raise Redeclared(Variable(),decl.variable.name)
            else:
                if self.lookup(decl.name.name,self.global_envi,lambda x: x.name) is None:
                    self.global_envi.append(self.funcDecl2Sym(decl))
                    if decl.name.name=="main":
                        hasMain=True
                else:
                    raise Redeclared(Function(),decl.name.name)

        if not hasMain:
            raise NoEntryPoint()

        for decl in ast.decl:
            if isinstance(decl,FuncDecl):
                self.visit(decl,RefInfo(refEnvi=self.global_envi[:],localEnvi=[],funcName=decl.name.name))                        

    def visitFuncDecl(self, ast, c):
        for para in ast.param:
            if self.lookup(para.variable.name,c.localEnvi,lambda x:x.name) is None:
                c.localEnvi.append(self.varDecl2Sym(para))

                temp=self.lookup(para.variable.name, c.refEnvi, lambda x: x.name)
                if temp is not None:
                    c.refEnvi.remove(temp)
                c.refEnvi.append(self.varDecl2Sym(para))
            else:
                raise Redeclared(Paramenter(),para.variable.name)
        
        for varDecl in ast.body[0]:
            if self.lookup(varDecl.variable.name, c.localEnvi, lambda x: x.name) is None:
                c.localEnvi.append(self.varDecl2Sym(varDecl))

                temp = self.lookup(varDecl.variable.name, c.refEnvi, lambda x: x.name)
                if temp is not None:
                    c.refEnvi.remove(temp)
                c.refEnvi.append(self.varDecl2Sym(varDecl))
            else:
                raise Redeclared(Variable(), varDecl.variable.name)

        for stmt in ast.body[1]:
            self.visitStmt(stmt, c)
    
    def visitBinaryOp(self, ast, c):
        inferredType = c.inferredType
        typeRequired = c.typeRequired

        c.typeRequired = True

        if ast.op in ["==", "!=", ">", "<", ">=", "<="]:
            c.inferredType = NumberType()
            leftType = self.visitExpr(ast.left, c)
            rightType = self.visitExpr(ast.right, c)
            if not isinstance(leftType, NumberType) or not isinstance(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            retType = BoolType()
        elif ast.op in ["==."]:
            c.inferredType = StringType()
            leftType = self.visitExpr(ast.left, c)
            rightType = self.visitExpr(ast.right, c)
            if not isinstance(leftType, StringType) or not isinstance(rightType, StringType):
                raise TypeMismatchInExpression(ast)
            retType = BoolType()
        elif ast.op in ["+."]:
            c.inferredType = StringType()
            leftType = self.visitExpr(ast.left, c)
            rightType = self.visitExpr(ast.right, c)
            if not isinstance(leftType, StringType) or not isinstance(rightType, StringType):
                raise TypeMismatchInExpression(ast)
            retType = StringType()
        elif ast.op in ["&&", "||"]:
            c.inferredType = BoolType()
            leftType = self.visitExpr(ast.left, c)
            rightType = self.visitExpr(ast.right, c)
            if not isinstance(leftType, BoolType) or not isinstance(rightType, BoolType):
                raise TypeMismatchInExpression(ast)
            retType = BoolType()
        elif ast.op in ["+", "-", "*", "\\", "%"]:
            c.inferredType = NumberType()
            leftType = self.visitExpr(ast.left, c)
            rightType = self.visitExpr(ast.right, c)
            if not isinstance(leftType, NumberType) or not isinstance(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            retType = NumberType()

        c.inferredType = inferredType
        c.typeRequired = typeRequired
        return retType
    
    def visitUnaryOp(self, ast, c):
        inferredType = c.inferredType
        typeRequired = c.typeRequired

        c.typeRequired = True
        if ast.op == "!":
            c.inferredType = BoolType()
            exprType = self.visitExpr(ast.body, c)
            if not isinstance(exprType, BoolType):
                raise TypeMismatchInExpression(ast)
            retType = BoolType()
        elif ast.op == "-":
            c.inferredType = NumberType()
            exprType = self.visitExpr(ast.body, c)
            if not isinstance(exprType, NumberType):
                raise TypeMismatchInExpression(ast)
            retType = NumberType()
        
        c.inferredType = inferredType
        c.typeRequired = typeRequired
        return retType

    def visitCallExpr(self, ast, c):
        #print(c)
        symbol = self.lookup(ast.method.name, c.refEnvi, lambda x: x.name)
        if symbol is None or not isinstance(symbol.mtype, MType):
            raise Undeclared(Function(), ast.method.name)

        if len(symbol.mtype.intype) != len(ast.param):
            raise TypeMismatchInExpression(ast)

        if c.typeRequired and c.inferredType is None and symbol.mtype.restype is None:
            raise TypeCannotBeInferred(c.innerStmt)

        if symbol.mtype.restype is None:
            symbol.mtype.restype = c.inferredType

        typeRequired = c.typeRequired
        inferredType = c.inferredType
        c.typeRequired = True
        c.inferredType = None
        for i, expr in enumerate(ast.param):
            exprType = self.visitExpr(expr, c)
            if exprType is None:
                raise TypeCannotBeInferred(c.innerStmt)
            elif symbol.mtype.intype[i] is None:
                symbol.mtype.intype[i] = exprType
            elif not self.sameType(symbol.mtype.intype[i], exprType):
                raise TypeMismatchInExpression(ast)
        c.typeRequired = typeRequired
        c.inferredType = inferredType

        
        return symbol.mtype.restype

    def visitId(self, ast, c):
        symbol = self.lookup(ast.name, c.refEnvi, lambda x: x.name)
        if symbol is None:
            raise Undeclared(Identifier(), ast.name)

        if c.typeRequired:
            if symbol.mtype is None and c.inferredType is None:
                raise TypeCannotBeInferred(c.innerStmt)

        if symbol.mtype is None:
            if c.inferredType is not None and not isinstance(c.inferredType, ArrayType):
                symbol.mtype = c.inferredType
        elif isinstance(symbol.mtype, ArrayType) and symbol.mtype.eletype is None:
            if c.inferredType is not None and isinstance(c.inferredType, ArrayType) and len(symbol.mtype.dimen) == len(c.inferredType.dimen):
                symbol.mtype.eletype = c.inferredType.eletype

        return symbol.mtype

    def visitArrayAccess(self, ast, c):
        typeRequired = c.typeRequired
        inferredType = c.inferredType
        c.typeRequired = True;
        c.inferredType = ArrayType([0 for i in ast.idx], c.inferredType)
        
        arrType = self.visitExpr(ast.arr, c)
        if not (isinstance(arrType, ArrayType) and len(arrType.dimen) == len(c.inferredType.dimen)):
            raise TypeMismatchInExpression(ast)

        c.inferredType = IntType()
        for expr in ast.idx:
            idxType = self.visitExpr(expr, c)
            if not isinstance(idxType, NumberType):
                raise TypeMismatchInExpression(ast)
        
        c.typeRequired = typeRequired
        c.inferredType = inferredType
        return arrType.eletype

    def visitAssign(self, ast, c):
        c.typeRequired = False
        leftType = self.visitExpr(ast.lhs, c)
        if leftType is not None and isinstance(leftType, MType):
            raise TypeMismatchInStatement(ast)

        c.typeRequired = True
        c.inferredType = leftType
        rightType = self.visitExpr(ast.rhs, c)
        if leftType is None:
            if isinstance(ast.lhs, Id):
                self.lookup(ast.lhs.name, c.refEnvi, lambda x: x.name).mtype = rightType
            else:
                self.lookup(ast.lhs.arr.name, c.refEnvi, lambda x: x.name).mtype.eletype = rightType
        elif not self.sameType(leftType, rightType):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, c):
        for ifClause in ast.ifthenStmt:
            refEnvi = c.refEnvi[:]
            localEnvi = c.localEnvi
            c.inferredType = BoolType()
            condType = self.visitExpr(ifClause[0], c)
            if not isinstance(condType, BoolType):
                raise TypeMismatchInStatement(ast)

            for varDecl in ifClause[1]:
                if self.lookup(varDecl.variable.name, localEnvi, lambda x: x.name) is None:
                    localEnvi.append(self.varDecl2Sym(varDecl))

                    temp = self.lookup(varDecl.variable.name, refEnvi, lambda x: x.name)
                    if temp is not None:
                        refEnvi.remove(temp)
                    refEnvi.append(self.varDecl2Sym(varDecl))
                else:
                    raise Redeclared(Variable(), varDecl.variable.name)

            for stmt in ifClause[2]:
                self.visitStmt(stmt, RefInfo(refEnvi, localEnvi))

        if len(ast.elseStmt[0] + ast.elseStmt[1]) > 0:
            for varDecl in ast.elseStmt[0]:
                if self.lookup(varDecl.variable.name, c.localEnvi, lambda x: x.name) is None:
                    c.localEnvi.append(self.varDecl2Sym(varDecl))

                    temp = self.lookup(varDecl.variable.name, c.refEnvi, lambda x: x.name)
                    if temp is not None:
                        c.refEnvi.remove(temp)
                    c.refEnvi.append(self.varDecl2Sym(varDecl))
                else:
                    raise Redeclared(Variable(), varDecl.variable.name)
            
            for stmt in ast.elseStmt[1]:
                self.visitStmt(stmt, c)

    def visitFor(self, ast, p):
        c.inferredType = IntType()
        
        idxType = self.visitExpr(ast.idx1, p)
        if not isinstance(idxType, IntType):
            raise TypeMismatchInStatement(ast)

        exprType1 = self.visitExpr(ast.expr1, p)
        exprType3 = self.visitExpr(ast.expr3, p)
        if not isinstance(exprType1, IntType) or not isinstance(exprType3, IntType):
            raise TypeMismatchInStatement(ast)

        c.inferredType = BoolType()
        exprType2 = self.visitExpr(ast.expr2, p)
        if not isinstance(exprType2, BoolType):
            raise TypeMismatchInStatement(ast)

        for varDecl in ast.loop[0]:
            if self.lookup(varDecl.variable.name, c.localEnvi, lambda x: x.name) is None:
                c.localEnvi.append(self.varDecl2Sym(varDecl))

                temp = self.lookup(varDecl.variable.name, c.refEnvi, lambda x: x.name)
                if temp is not None:
                    c.refEnvi.remove(temp)
                c.refEnvi.append(self.varDecl2Sym(varDecl))
            else:
                raise Redeclared(Variable(), varDecl.variable.name)
            
        for stmt in ast.loop[1]:
            self.visitStmt(stmt, p)

    def visitReturn(self, ast, c):
        restype = self.lookup(c.funcName, self.global_envi, lambda x: x.name).mtype.restype
        if restype is not None:
            if isinstance(restype, VoidType) and ast.expr is not None:
                raise TypeMismatchInStatement(ast)

            if not isinstance(restype, VoidType) and ast.expr is None:
                raise TypeMismatchInStatement(ast)

            if ast.expr is not None:
                c.inferredType = restype
                c.typeRequired = False
                exprType = self.visitExpr(ast.expr, c)
                if not self.sameType(restype, exprType):
                    raise TypeMismatchInStatement(ast)

    def visitWhile(self, ast, c):
        c.inferredType = BoolType()
        exprType = self.visitExpr(ast.exp, c)
        if not isinstance(exprType, BoolType):
            raise TypeMismatchInStatement(ast)

        for varDecl in ast.sl[0]:
            if self.lookup(varDecl.variable.name, c.localEnvi, lambda x: x.name) is None:
                c.localEnvi.append(self.varDecl2Sym(varDecl))

                temp = self.lookup(varDecl.variable.name, c.refEnvi, lambda x: x.name)
                if temp is not None:
                    c.refEnvi.remove(temp)
                c.refEnvi.append(self.varDecl2Sym(varDecl))
            else:
                raise Redeclared(Variable(), varDecl.variable.name)
            
        for stmt in ast.sl[1]:
            self.visitStmt(stmt, c)

    def visitCallStmt(self, ast, c):
        symbol = self.lookup(ast.method.name, c.refEnvi, lambda x: x.name)
        if symbol is None or not isinstance(symbol.mtype, MType):
            raise Undeclared(Function(), ast.method.name)

        if len(symbol.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)

        if symbol.mtype.restype is None:
            symbol.mtype.restype = VoidType()
        elif not isinstance(symbol.mtype.restype, VoidType):
            raise TypeMismatchInStatement(ast)

        for i, expr in enumerate(ast.param):
            exprType = self.visitExpr(expr, c)
            if exprType is None:
                raise TypeCannotBeInferred(c.innerStmt)
            elif symbol.mtype.intype[i] is None:
                symbol.mtype.intype[i] = exprType
            elif not self.sameType(symbol.mtype.intype[i], exprType):
                raise TypeMismatchInStatement(ast)


    def visitIntLiteral(self, ast, param):
        pass
    
    def visitNumberLiteral(self, ast, c):
        return NumberType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()
