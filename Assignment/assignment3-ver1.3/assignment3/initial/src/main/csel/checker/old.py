
"""
 * @author nhphung
"""
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
class IntType(Prim):
    pass
class FloatType(Prim):
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
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

@dataclass
class RefInfo:
    refEnvi:List[Symbol]
    localEnvi:List[Symbol]
    innerStmt:Stmt = None
    funcName:str = None
    inferredType:Type = None
    typeRequired:bool = True

@dataclass
class ExprRes:
    retType:Type = None

class StaticChecker(BaseVisitor):
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def visitStmt(self, ast, p):
        self.visit(ast, RefInfo(refEnvi=p.refEnvi[:], localEnvi=[], innerStmt=ast, funcName=p.funcName, inferredType=None, typeRequired=True))

    def visitExpr(self, ast, p):
        return self.visit(ast, RefInfo(refEnvi=p.refEnvi[:], localEnvi=[], innerStmt=p.innerStmt, funcName=p.funcName, inferredType=p.inferredType, typeRequired=p.typeRequired))

    def sameType(self, typeA, typeB):
        return (isinstance(typeA, IntType) and isinstance(typeB, IntType))      \
            or (isinstance(typeA, FloatType) and isinstance(typeB, FloatType))  \
            or (isinstance(typeA, StringType) and isinstance(typeB, StringType))\
            or (isinstance(typeA, BoolType) and isinstance(typeB, BoolType))    \
            or (isinstance(typeA, ArrayType) and isinstance(typeB, ArrayType) and len(typeA.dimen) == len(typeB.dimen) and self.sameType(typeA.eletype, typeB.eletype))

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
            if mtype is None:
                mtype = temp
            elif temp is not None:
                if not self.sameType(mtype, temp):
                    raise InvalidArrayLiteral(arrayLiteral)
        return mType

    def literal2Type(self, literal):
        if isinstance(literal, IntLiteral):
            return IntType()
        elif isinstance(literal, FloatLiteral):
            return FloatType()
        elif isinstance(literal, BooleanLiteral):
            return BoolType()
        elif isinstance(literal, StringLiteral):
            return StringType()
        else:
            return self.arrayLiteral2Type(literal, literal)

    def varDecl2Sym(self, varDecl):
        varType = None
        if varDecl.varInit is not None:
            varType = self.literal2Type(varDecl.varInit)
        if len(varDecl.varDimen) > 0:
            varType = ArrayType(varDecl.varDimen, varType)
        return Symbol(varDecl.variable.name, varType)

    def funcDecl2Sym(self, funcDecl):
        paraTypes = []
        for varDecl in funcDecl.param:
            if len(varDecl.varDimen) > 0:
                paraTypes.append(ArrayType(varDecl.varDimen, None))
            else:
                paraTypes.append(None)
        return Symbol(funcDecl.name.name, MType(paraTypes, None))

    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float",MType([FloatType()],IntType())),
            Symbol("float_of_int",MType([IntType()],FloatType())),
            Symbol("int_of_string",MType([StringType()],IntType())),
            Symbol("string_of_int",MType([IntType()],StringType())),
            Symbol("float_of_string",MType([StringType()],FloatType())),
            Symbol("string_of_float",MType([FloatType()],StringType())),
            Symbol("bool_of_string",MType([StringType()],BoolType())),
            Symbol("string_of_bool",MType([BoolType()],StringType())),
            Symbol("read",MType([],StringType())),
            Symbol("printLn",MType([],VoidType())),
            Symbol("printStr",MType([StringType()],VoidType())),
            Symbol("printStrLn",MType([StringType()],VoidType()))
        ]                           
   
    def check(self):
        return self.visit(self.ast, None)

    def visitProgram(self, ast, p):
        hasMain = False
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                if self.lookup(decl.variable.name, self.global_envi, lambda x: x.name) is None:
                    self.global_envi.append(self.varDecl2Sym(decl))
                else:
                    raise Redeclared(Variable(), decl.variable.name)
            else:
                if self.lookup(decl.name.name, self.global_envi, lambda x: x.name) is None:
                    self.global_envi.append(self.funcDecl2Sym(decl))
                    if decl.name.name == "main":
                        hasMain = True 
                else:
                    raise Redeclared(Function(), decl.name.name)
        
        if not hasMain:
            raise NoEntryPoint()

        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                self.visit(decl, RefInfo(refEnvi=self.global_envi[:], localEnvi=[], funcName=decl.name.name))

    def visitFuncDecl(self, ast, p):
        for para in ast.param:
            if self.lookup(para.variable.name, p.localEnvi, lambda x: x.name) is None:
                p.localEnvi.append(self.varDecl2Sym(para))

                temp = self.lookup(para.variable.name, p.refEnvi, lambda x: x.name)
                if temp is not None:
                    p.refEnvi.remove(temp)
                p.refEnvi.append(self.varDecl2Sym(para))
            else:
                raise Redeclared(Paramenter(), para.variable.name)
    
        for varDecl in ast.body[0]:
            if self.lookup(varDecl.variable.name, p.localEnvi, lambda x: x.name) is None:
                p.localEnvi.append(self.varDecl2Sym(varDecl))

                temp = self.lookup(varDecl.variable.name, p.refEnvi, lambda x: x.name)
                if temp is not None:
                    p.refEnvi.remove(temp)
                p.refEnvi.append(self.varDecl2Sym(varDecl))
            else:
                raise Redeclared(Variable(), varDecl.variable.name)

        for stmt in ast.body[1]:
            self.visitStmt(stmt, p)

    def visitBinaryOp(self, ast, p):
        inferredType = p.inferredType
        typeRequired = p.typeRequired

        p.typeRequired = True

        if ast.op in ["==", "!=", ">", "<", ">=", "<="]:
            p.inferredType = IntType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, IntType) or not isinstance(rightType, IntType):
                raise TypeMismatchInExpression(ast)
            retType = BoolType()
        elif ast.op in ["=/=", "<.", ">.", "<=.", ">=."]:
            p.inferredType = FloatType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, FloatType) or not isinstance(rightType, FloatType):
                raise TypeMismatchInExpression(ast)
            retType = BoolType()
        elif ast.op in ["&&", "||"]:
            p.inferredType = BoolType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, BoolType) or not isinstance(rightType, BoolType):
                raise TypeMismatchInExpression(ast)
            retType = BoolType()
        elif ast.op in ["+", "-", "*", "\\", "%"]:
            p.inferredType = IntType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, IntType) or not isinstance(rightType, IntType):
                raise TypeMismatchInExpression(ast)
            retType = IntType()
        else:
            p.inferredType = FloatType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, FloatType) or not isinstance(rightType, FloatType):
                raise TypeMismatchInExpression(ast)
            retType = FloatType()

        p.inferredType = inferredType
        p.typeRequired = typeRequired
        return retType

    def visitUnaryOp(self, ast, p):
        inferredType = p.inferredType
        typeRequired = p.typeRequired

        p.typeRequired = True
        if ast.op == "!":
            p.inferredType = BoolType()
            exprType = self.visitExpr(ast.body, p)
            if not isinstance(exprType, BoolType):
                raise TypeMismatchInExpression(ast)
            retType = BoolType()
        elif ast.op == "-":
            p.inferredType = IntType()
            exprType = self.visitExpr(ast.body, p)
            if not isinstance(exprType, IntType):
                raise TypeMismatchInExpression(ast)
            retType = IntType()
        else:
            p.inferredType = FloatType()
            exprType = self.visitExpr(ast.body, p)
            if not isinstance(exprType, FloatType):
                raise TypeMismatchInExpression(ast)
            retType = FloatType()

        p.inferredType = inferredType
        p.typeRequired = typeRequired
        return retType

    def visitCallExpr(self, ast, p):
        symbol = self.lookup(ast.method.name, p.refEnvi, lambda x: x.name)
        if symbol is None or not isinstance(symbol.mtype, MType):
            raise Undeclared(Function(), ast.method.name)

        if len(symbol.mtype.intype) != len(ast.param):
            raise TypeMismatchInExpression(ast)

        if p.typeRequired and p.inferredType is None and symbol.mtype.restype is None:
            raise TypeCannotBeInferred(p.innerStmt)

        if symbol.mtype.restype is None:
            symbol.mtype.restype = p.inferredType

        typeRequired = p.typeRequired
        inferredType = p.inferredType
        p.typeRequired = True
        p.inferredType = None
        for i, expr in enumerate(ast.param):
            exprType = self.visitExpr(expr, p)
            if exprType is None:
                raise TypeCannotBeInferred(p.innerStmt)
            elif symbol.mtype.intype[i] is None:
                symbol.mtype.intype[i] = exprType
            elif not self.sameType(symbol.mtype.intype[i], exprType):
                raise TypeMismatchInExpression(ast)
        p.typeRequired = typeRequired
        p.inferredType = inferredType

        return symbol.mtype.restype

    def visitId(self, ast, p):
        symbol = self.lookup(ast.name, p.refEnvi, lambda x: x.name)
        if symbol is None:
            raise Undeclared(Identifier(), ast.name)

        if p.typeRequired:
            if symbol.mtype is None and p.inferredType is None:
                raise TypeCannotBeInferred(p.innerStmt)

        if symbol.mtype is None:
            if p.inferredType is not None and not isinstance(p.inferredType, ArrayType):
                symbol.mtype = p.inferredType
        elif isinstance(symbol.mtype, ArrayType) and symbol.mtype.eletype is None:
            if p.inferredType is not None and isinstance(p.inferredType, ArrayType) and len(symbol.mtype.dimen) == len(p.inferredType.dimen):
                symbol.mtype.eletype = p.inferredType.eletype

        return symbol.mtype

    def visitArrayCell(self, ast, p):
        typeRequired = p.typeRequired
        inferredType = p.inferredType
        p.typeRequired = True;
        p.inferredType = ArrayType([0 for i in ast.idx], p.inferredType)
        
        arrType = self.visitExpr(ast.arr, p)
        if not (isinstance(arrType, ArrayType) and len(arrType.dimen) == len(p.inferredType.dimen)):
            raise TypeMismatchInExpression(ast)

        p.inferredType = IntType()
        for expr in ast.idx:
            idxType = self.visitExpr(expr, p)
            if not isinstance(idxType, IntType):
                raise TypeMismatchInExpression(ast)
        
        p.typeRequired = typeRequired
        p.inferredType = inferredType
        return arrType.eletype

    def visitAssign(self, ast, p):
        p.typeRequired = False
        leftType = self.visitExpr(ast.lhs, p)
        if leftType is not None and isinstance(leftType, MType):
            raise TypeMismatchInStatement(ast)

        p.typeRequired = True
        p.inferredType = leftType
        rightType = self.visitExpr(ast.rhs, p)
        if leftType is None:
            if isinstance(ast.lhs, Id):
                self.lookup(ast.lhs.name, p.refEnvi, lambda x: x.name).mtype = rightType
            else:
                self.lookup(ast.lhs.arr.name, p.refEnvi, lambda x: x.name).mtype.eletype = righttype
        elif not self.sameType(leftType, rightType):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, p):
        for ifClause in ast.ifthenStmt:
            refEnvi = p.refEnvi[:]
            localEnvi = p.localEnvi
            p.inferredType = BoolType()
            condType = self.visitExpr(ifClause[0], p)
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
                if self.lookup(varDecl.variable.name, p.localEnvi, lambda x: x.name) is None:
                    p.localEnvi.append(self.varDecl2Sym(varDecl))

                    temp = self.lookup(varDecl.variable.name, p.refEnvi, lambda x: x.name)
                    if temp is not None:
                        p.refEnvi.remove(temp)
                    p.refEnvi.append(self.varDecl2Sym(varDecl))
                else:
                    raise Redeclared(Variable(), varDecl.variable.name)
            
            for stmt in ast.elseStmt[1]:
                self.visitStmt(stmt, p)

    def visitFor(self, ast, p):
        p.inferredType = IntType()
        
        idxType = self.visitExpr(ast.idx1, p)
        if not isinstance(idxType, IntType):
            raise TypeMismatchInStatement(ast)

        exprType1 = self.visitExpr(ast.expr1, p)
        exprType3 = self.visitExpr(ast.expr3, p)
        if not isinstance(exprType1, IntType) or not isinstance(exprType3, IntType):
            raise TypeMismatchInStatement(ast)

        p.inferredType = BoolType()
        exprType2 = self.visitExpr(ast.expr2, p)
        if not isinstance(exprType2, BoolType):
            raise TypeMismatchInStatement(ast)

        for varDecl in ast.loop[0]:
            if self.lookup(varDecl.variable.name, p.localEnvi, lambda x: x.name) is None:
                p.localEnvi.append(self.varDecl2Sym(varDecl))

                temp = self.lookup(varDecl.variable.name, p.refEnvi, lambda x: x.name)
                if temp is not None:
                    p.refEnvi.remove(temp)
                p.refEnvi.append(self.varDecl2Sym(varDecl))
            else:
                raise Redeclared(Variable(), varDecl.variable.name)
            
        for stmt in ast.loop[1]:
            self.visitStmt(stmt, p)

    def visitReturn(self, ast, p):
        restype = self.lookup(p.funcName, self.global_envi, lambda x: x.name).mtype.restype
        if restype is not None:
            if isinstance(restype, VoidType) and ast.expr is not None:
                raise TypeMismatchInStatement(ast)

            if not isinstance(restype, VoidType) and ast.expr is None:
                raise TypeMismatchInStatement(ast)

            if ast.expr is not None:
                p.inferredType = restype
                p.typeRequired = False
                exprType = self.visitExpr(ast.expr, p)
                if not self.sameType(restype, exprType):
                    raise TypeMismatchInStatement(ast)

    def visitDowhile(self, ast, p):
        p.inferredType = BoolType()
        exprType = self.visitExpr(ast.exp, p)
        if not isinstance(exprType, BoolType):
            raise TypeMismatchInStatement(ast)

        for varDecl in ast.sl[0]:
            if self.lookup(varDecl.variable.name, p.localEnvi, lambda x: x.name) is None:
                p.localEnvi.append(self.varDecl2Sym(varDecl))

                temp = self.lookup(varDecl.variable.name, p.refEnvi, lambda x: x.name)
                if temp is not None:
                    p.refEnvi.remove(temp)
                p.refEnvi.append(self.varDecl2Sym(varDecl))
            else:
                raise Redeclared(Variable(), varDecl.variable.name)
            
        for stmt in ast.sl[1]:
            self.visitStmt(stmt, p)

    def visitWhile(self, ast, p):
        p.inferredType = BoolType()
        exprType = self.visitExpr(ast.exp, p)
        if not isinstance(exprType, BoolType):
            raise TypeMismatchInStatement(ast)

        for varDecl in ast.sl[0]:
            if self.lookup(varDecl.variable.name, p.localEnvi, lambda x: x.name) is None:
                p.localEnvi.append(self.varDecl2Sym(varDecl))

                temp = self.lookup(varDecl.variable.name, p.refEnvi, lambda x: x.name)
                if temp is not None:
                    p.refEnvi.remove(temp)
                p.refEnvi.append(self.varDecl2Sym(varDecl))
            else:
                raise Redeclared(Variable(), varDecl.variable.name)
            
        for stmt in ast.sl[1]:
            self.visitStmt(stmt, p)

    def visitCallStmt(self, ast, p):
        symbol = self.lookup(ast.method.name, p.refEnvi, lambda x: x.name)
        if symbol is None or not isinstance(symbol.mtype, MType):
            raise Undeclared(Function(), ast.method.name)

        if len(symbol.mtype.intype) != len(ast.param):
            raise TypeMismatchInStatement(ast)

        if symbol.mtype.restype is None:
            symbol.mtype.restype = VoidType()
        elif not isinstance(symbol.mtype.restype, VoidType):
            raise TypeMismatchInStatement(ast)

        for i, expr in enumerate(ast.param):
            exprType = self.visitExpr(expr, p)
            if exprType is None:
                raise TypeCannotBeInferred(p.innerStmt)
            elif symbol.mtype.intype[i] is None:
                symbol.mtype.intype[i] = exprType
            elif not self.sameType(symbol.mtype.intype[i], exprType):
                raise TypeMismatchInStatement(ast)

    def visitIntLiteral(self, ast, p):
        return IntType()

    def visitFloatLiteral(self, ast, p):
        return FloatType()

    def visitBooleanLiteral(self, ast, p):
        return BoolType()

    def visitStringLiteral(self, ast, p):
        return StringType()