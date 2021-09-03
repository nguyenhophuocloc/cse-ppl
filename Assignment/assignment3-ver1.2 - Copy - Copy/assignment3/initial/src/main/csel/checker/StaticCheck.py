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


class BooleanType(Prim):
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
        if (isinstance(typeA, NumberType) and isinstance(typeB, NumberType)) or (isinstance(typeA, BooleanType) and isinstance(typeB, BooleanType)) or (isinstance(typeA, StringType) and isinstance(typeB, StringType)) or (isinstance(typeA, ArrayType) and isinstance(typeB, ArrayType) and len(typeA.dimen) == len(typeB.dimen) and self.sameType(typeA.eletype, typeB.eletype)):
            return True
        return False

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
        if isinstance(literal, NumberLiteral):
            return NumberType()        
        elif isinstance(literal, BooleanLiteral):
            return BooleanType()
        elif isinstance(literal, StringLiteral):
            return StringType()
        else:
            return self.arrayLiteral2Type(literal, literal)

    def varDecl2Sym(self, varDecl):
        varType = None
        
        if not isinstance(varDecl.typ,NoneType):
           varType=varDecl.typ
        if varDecl.varInit is not None:
            varType = self.literal2Type(varDecl.varInit)
        if len(varDecl.varDimen) > 0:
            varType = ArrayType(varDecl.varDimen, varType)
        return Symbol(varDecl.variable.name, varType)

    def constDecl2Sym(self, constDecl):
        constType = None

        if not isinstance(constDecl.typ,NoneType):
            constType=constDecl.typ
        if constDecl.constInit is not None:
            constType = self.literal2Type(constDecl.constInit)
        if len(constDecl.constDimen) >0:
           constType = ArrayType(constDecl.constDimen, constType)
        return Symbol(constDecl.constant.name, constType)
   
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
            
           
        ]                           
   
    def check(self):
        return self.visit(self.ast, None)

    def visitProgram(self, ast, p):
        
        
        hasMain = True      #for testting
        for decl in ast.decl:
            if isinstance(decl, VarDecl):                
                if self.lookup(decl.variable.name, self.global_envi, lambda x: x.name) is None:
                    self.global_envi.append(self.varDecl2Sym(decl))
                else:
                    raise Redeclared(Variable(), decl.variable.name)
            
            elif isinstance(decl,ConstDecl):
                if self.lookup(decl.constant.name, self.global_envi, lambda x: x.name) is None:
                    self.global_envi.append(self.constDecl2Sym(decl))
                else:
                    raise Redeclared(Constant(), decl.constant.name)

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
                self.visit(decl, RefInfo(refEnvi=self.global_envi[:], localEnvi=[], funcName=decl.name.name))   #môi trường của func
    
    def visitFuncDecl(self, ast, p):        
        for para in ast.param:
            if self.lookup(para.variable.name, p.localEnvi, lambda x: x.name) is None:
                p.localEnvi.append(self.varDecl2Sym(para))

                temp = self.lookup(para.variable.name, p.refEnvi, lambda x: x.name)
                #hủy biến nếu trùng tên global, dùng local thôi bro
                if temp is not None:
                    p.refEnvi.remove(temp)
                p.refEnvi.append(self.varDecl2Sym(para))
            else:
                raise Redeclared(Paramenter(), para.variable.name)
        
        for inst in ast.body:
            if isinstance(inst, VarDecl):
                if self.lookup(inst.variable.name, p.localEnvi, lambda x: x.name) is None:
                    p.localEnvi.append(self.varDecl2Sym(inst))

                    temp = self.lookup(inst.variable.name, p.refEnvi, lambda x: x.name)
                    if temp is not None:
                        p.refEnvi.remove(temp)
                    p.refEnvi.append(self.varDecl2Sym(inst))
                else:
                    raise Redeclared(Variable(), inst.variable.name)                

            elif isinstance(inst, ConstDecl):
                if self.lookup(inst.constant.name, p.localEnvi, lambda x: x.name) is None:
                    p.localEnvi.append(self.constDecl2Sym(inst))

                    temp = self.lookup(inst.constant.name, p.refEnvi, lambda x: x.name)
                    if temp is not None:
                        p.refEnvi.remove(temp)
                    p.refEnvi.append(self.constDecl2Sym(inst))
                else:
                    raise Redeclared(Constant(), inst.constant.name)
            else:
                self.visitStmt(inst, p)
            
        print(p.refEnvi)


    def visitAssign(self, ast, p):        
        
        p.typeRequired = False
        leftType = self.visitExpr(ast.lhs, p)
        
        if leftType is not None and isinstance(leftType, MType):
            raise TypeMismatchInStatement(ast)
        
        p.typeRequired = True
        p.inferredType = leftType
        rightType = self.visitExpr(ast.rhs, p)
        #testing      
        
        if leftType is None:
            if isinstance(ast.lhs, Id):
                self.lookup(ast.lhs.name, p.refEnvi, lambda x: x.name).mtype = rightType
            else:
                self.lookup(ast.lhs.arr.name, p.refEnvi, lambda x: x.name).mtype.eletype = rightType
        elif not self.sameType(leftType, rightType):
            raise TypeMismatchInStatement(ast)

    def visitBinaryOp(self, ast, p):
        inferredType = p.inferredType
        typeRequired = p.typeRequired

        p.typeRequired = True

        if ast.op in ["==", "!=", ">", "<", ">=", "<="]:
            p.inferredType = NumberType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, NumberType) or not isinstance(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            retType = BooleanType()
        elif ast.op in ["==."]:
            p.inferredType = StringType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, StringType) or not isinstance(rightType, StringType):
                raise TypeMismatchInExpression(ast)
            retType = BooleanType()
        elif ast.op in ["==."]:
            p.inferredType = StringType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, StringType) or not isinstance(rightType, StringType):
                raise TypeMismatchInExpression(ast)
            retType = StringType()
        elif ast.op in ["&&", "||"]:
            p.inferredType = BooleanType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, BooleanType) or not isinstance(rightType, BooleanType):
                raise TypeMismatchInExpression(ast)
            retType = BooleanType()
        elif ast.op in ["+", "-", "*", "\\", "%"]:
            p.inferredType = NumberType()
            leftType = self.visitExpr(ast.left, p)
            rightType = self.visitExpr(ast.right, p)
            if not isinstance(leftType, NumberType) or not isinstance(rightType, NumberType):
                raise TypeMismatchInExpression(ast)
            retType = NumberType()
        

        p.inferredType = inferredType
        p.typeRequired = typeRequired
        return retType

    def visitUnaryOp(self, ast, p):
        inferredType = p.inferredType
        typeRequired = p.typeRequired

        p.typeRequired = True
        if ast.op == "!":
            p.inferredType = BooleanType()
            exprType = self.visitExpr(ast.body, p)
            if not isinstance(exprType, BooleanType):
                raise TypeMismatchInExpression(ast)
            retType = BooleanType()
        elif ast.op == "-":
            p.inferredType = NumberType()
            exprType = self.visitExpr(ast.body, p)
            if not isinstance(exprType, NumberType):
                raise TypeMismatchInExpression(ast)
            retType = NumberType()
        
        p.inferredType = inferredType
        p.typeRequired = typeRequired
        return retType

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

    def visitIf(self, ast, p):
        for ifClause in ast.ifthenStmt:
            refEnvi = p.refEnvi[:]
            localEnvi = p.localEnvi
            p.inferredType = BooleanType()
            condType = self.visitExpr(ifClause[0], p)
            if not isinstance(condType, BooleanType):
                raise TypeMismatchInStatement(ast)

            for inst in ifClause[1]:
                if isinstance(inst, VarDecl):            
                    if self.lookup(inst.variable.name, localEnvi, lambda x: x.name) is None:
                        localEnvi.append(self.varDecl2Sym(inst))

                        temp = self.lookup(inst.variable.name, refEnvi, lambda x: x.name)
                        if temp is not None:
                            refEnvi.remove(temp)
                        refEnvi.append(self.varDecl2Sym(inst))
                    else:
                        raise Redeclared(Variable(), inst.variable.name)
                elif isinstance(inst, ConstDecl):
                    if self.lookup(inst.constant.name, p.localEnvi, lambda x: x.name) is None:
                        p.localEnvi.append(self.constDecl2Sym(inst))

                        temp = self.lookup(inst.constant.name, p.refEnvi, lambda x: x.name)
                        if temp is not None:
                            p.refEnvi.remove(temp)
                        p.refEnvi.append(self.constDecl2Sym(inst))
                    else:
                        raise Redeclared(Constant(), inst.constant.name)
                else:
                    self.visitStmt(inst, RefInfo(refEnvi, localEnvi))

            #for stmt in ifClause[2]:
            #    self.visitStmt(stmt, RefInfo(refEnvi, localEnvi))

        if len(ast.elseStmt) > 0:
            for inst in ast.elseStmt:
                if isinstance(inst, VarDecl):
                    if self.lookup(inst.variable.name, p.localEnvi, lambda x: x.name) is None:
                        p.localEnvi.append(self.varDecl2Sym(inst))

                        temp = self.lookup(inst.variable.name, p.refEnvi, lambda x: x.name)
                        if temp is not None:
                            p.refEnvi.remove(temp)
                        p.refEnvi.append(self.varDecl2Sym(inst))
                    else:
                        raise Redeclared(Variable(), inst.variable.name)
                elif isinstance(inst, ConstDecl):
                    if self.lookup(inst.constant.name, p.localEnvi, lambda x: x.name) is None:
                        p.localEnvi.append(self.constDecl2Sym(inst))

                        temp = self.lookup(inst.constant.name, p.refEnvi, lambda x: x.name)
                        if temp is not None:
                            p.refEnvi.remove(temp)
                        p.refEnvi.append(self.constDecl2Sym(inst))
                    else:
                        raise Redeclared(Constant(), inst.constant.name)
                else:
                    self.visitStmt(stmt, p)
            #for stmt in ast.elseStmt[1]:
                
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

    def visitWhile(self, ast, p):
        p.inferredType = BooleanType()
        exprType = self.visitExpr(ast.exp, p)
        if not isinstance(exprType, BooleanType):
            raise TypeMismatchInStatement(ast)

        for inst in ast.sl:
            if isinstance(inst, VarDecl):
                if self.lookup(inst.variable.name, p.localEnvi, lambda x: x.name) is None:
                    p.localEnvi.append(self.varDecl2Sym(inst))

                    temp = self.lookup(inst.variable.name, p.refEnvi, lambda x: x.name)
                    if temp is not None:
                        p.refEnvi.remove(temp)
                    p.refEnvi.append(self.varDecl2Sym(inst))
                else:
                    raise Redeclared(Variable(), inst.variable.name)
            elif isinstance(inst, ConstDecl):
                    if self.lookup(inst.constant.name, p.localEnvi, lambda x: x.name) is None:
                        p.localEnvi.append(self.constDecl2Sym(inst))

                        temp = self.lookup(inst.constant.name, p.refEnvi, lambda x: x.name)
                        if temp is not None:
                            p.refEnvi.remove(temp)
                        p.refEnvi.append(self.constDecl2Sym(inst))
                    else:
                        raise Redeclared(Constant(), inst.constant.name)
            else:
                self.visitStmt(stmt, p)        

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

    def  visitIntLiteral(self, ast,p):
        return NumberType()

    def visitNumberLiteral(self, ast, p):
        return NumberType()

    def visitBooleanLiteral(self, ast, p):
        return BooleanType()

    def visitStringLiteral(self, ast, p):
        return StringType()