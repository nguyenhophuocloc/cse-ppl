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


class StaticChecker(BaseVisitor):

    def getSymbolByName(self, symName, o):
        for lstSymbol in o:
            for symbol in lstSymbol:
                if(symName == symbol.name):
                    return symbol
        raise Undeclared(Identifier(),symName)

    def getSymbolFunctionByName(self, symName, o):
        for lstSymbol in o:
            for symbol in lstSymbol:
                if(symName == symbol.name):
                    return symbol
        raise Undeclared(Function(),symName)

    def inferType(self, symbol, type):
        if(isinstance(symbol.mtype,Unknown)):
            symbol.mtype = type
    
    def literal2Type(self, literal):
        if isinstance(literal, NumberLiteral):
            return NumberType()        
        elif isinstance(literal, BooleanLiteral):
            return BoolType()
        elif isinstance(literal, StringLiteral):
            return StringType()
        else:
            return self.arrayLiteral2Type(literal, literal)

    def varDecl2Sym(self, varDecl):
        varType = Unknown()
        if not isinstance(varDecl.typ,NoneType):
            varType=varDecl.typ
        if varDecl.varInit is not None:
            varType = self.literal2Type(varDecl.varInit)
        if varDecl.varDimen is not None and len(varDecl.varDimen)>0:
           varType = ArrayType(varDecl.varDimen, varType)
        return Symbol(varDecl.variable.name, varType)

    def constDecl2Sym(self, constDecl):
        constType = Unknown()
        if constDecl.typ is not NoneType():
            constType=constDecl.typ
        if constDecl.constInit is not None:
            constType = self.literal2Type(constDecl.constInit)
        if constDecl.constDimen is not None:
           constType = ArrayType(constDecl.constDimen, constType)
        return Symbol(constDecl.constant.name, constType)
    
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("str2num",MType([StringType()],NumberType())),
            Symbol("num2str",MType([NumberType()],StringType())),
            Symbol("str2bool",MType([StringType()],BoolType())),
            Symbol("bool2str",MType([BoolType()],StringType())),

            Symbol("read", MType([], StringType())),
            Symbol("print", MType([StringType()], VoidType())),
            Symbol("printSLn", MType([StringType()], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        #print(ast)
        """
        hasMain=False
        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                if decl.name.name=="main":
                    hasMain=True
        if hasMain==False:
            raise NoEntryPoint()
        """
        c=[[]]
        for x in ast.decl:
            self.visit(x,c)

        #print(c)

    def visitVarDecl(self, ast, c):        
        for symbol in c[0]:
            if symbol.name==ast.variable.name:
                raise Redeclared(Variable(),ast.variable.name)
        c[0].append(self.varDecl2Sym(ast))
        return c

    def visitConstDecl(self, ast, c):        
        for symbol in c[0]:
            if symbol.name==ast.constant.name:
                raise Redeclared(Constant(),ast.constant.name)
        c[0].append(self.constDecl2Sym(ast))
        return c
        

    def visitFuncDecl(self, ast,c):
        
        for symbol in c[0]:
            if(symbol.name == ast.name.name):
                raise Redeclared(Function(),ast.name.name)
        new_env=[[]]+c
        for para in ast.param:
            for x in new_env[0]:
                if x.name==para.variable.name:
                    raise Redeclared(Parameter(),para.variable.name)
            new_env[0].append(self.varDecl2Sym(para))
        params=new_env[0].copy()
        func = Symbol(ast.name.name,MType([param for param in params],None))
        new_env[1].append(func)
        #new_env[0][0].mtype=NumberType()
        #inside_env = reduce(lambda x,y: self.visit(y,x),ast.body,new_env)        

        #print(inside_env)
        #test=Symbol('x',Unknown())
        #print(test.mtype)
        #if type(test.mtype) in [Unknown]:
        #    print("GAI DIT BU")   
        #    self.inferType(test,StringType()) 
        #print(test.mtype)
        #if isinstance(test.mtype,NumberType):
            #print("Ga dit bu")
       
        for x in ast.body:
            if isinstance(x,list):
                for decl in x:
                    self.visit(decl,new_env)
            else:
                self.visit(x,new_env)
        #print(new_env)
        return new_env[1:]


    def visitBinaryOp(self, ast, c):
        typ1 = self.visit(ast.left, c)
        typ2 = self.visit(ast.right, c)
        op = ast.op
        if op in ['==.']:
            if type(typ1.mtype) in [NumberType,BoolType] or type(typ2.mtype) in [NumberType,BoolType]:
                raise TypeMismatchInExpression(ast)
            if isinstance(typ1.mtype,Unknown):
                self.inferType(typ1,StringType())
            if isinstance(typ2.mtype,Unknown):
                self.inferType(typ2,StringType())
            return Symbol(None,BoolType())
        
        if op in ['+.']:
            if type(typ1.mtype) in [NumberType,BoolType] or type(typ2.mtype) in [NumberType,BoolType]:
                raise TypeMismatchInExpression(ast)
            if isinstance(typ1.mtype,Unknown):
                self.inferType(typ1,StringType())
            if isinstance(typ2.mtype,Unknown):
                self.inferType(typ2,StringType())
            return Symbol(None,StringType())
        
        if op in ['==','!=','>','<','>=','<=']:
            if type(typ1.mtype) in [StringType,BoolType] or type(typ2.mtype) in [StringType,BoolType]:
                raise TypeMismatchInExpression(ast)
            if isinstance(typ1.mtype,Unknown):
                self.inferType(typ1,NumberType())
            if isinstance(typ2.mtype,Unknown):
                self.inferType(typ2,NumberType())
            return Symbol(None,BoolType())

        if op in ['&&','||']:
            if type(typ1.mtype) in [StringType,NumberType] or type(typ2.mtype) in [StringType,NumberType]:
                raise TypeMismatchInExpression(ast)
            if isinstance(typ1.mtype,Unknown):
                self.inferType(typ1,BoolType())
            if isinstance(typ2.mtype,Unknown):
                self.inferType(typ2,BoolType())
            return Symbol(None,BoolType())
        
        if op in ['+','-','*','/','%']:
            if type(typ1.mtype) in [StringType,BoolType] or type(typ2.mtype) in [StringType,BoolType]:
                raise TypeMismatchInExpression(ast)
            if isinstance(typ1.mtype,Unknown):
                self.inferType(typ1,NumberType())
            if isinstance(typ2.mtype,Unknown):
                self.inferType(typ2,NumberType())
            return Symbol(None,NumberType())

        

    def visitUnaryOp(self, ast, c):
        op=ast.op
        typ=self.visit(ast.body, c)

        if op in ['!']:
            if type(typ.mtype) in [StringType,NumberType]:
                raise TypeMismatchInExpression(ast)
            if isinstance(typ.mtype,Unknown):
                self.inferType(typ,BoolType())            
            return Symbol(None,BoolType())

        if op in ['-']:
            if type(typ.mtype) in [StringType,BoolType]:
                raise TypeMismatchInExpression(ast)
            if isinstance(typ.mtype,Unknown):
                self.inferType(typ,NumberType())            
            return Symbol(None,NumberType())


    def visitAssign(self, ast, c):
        typ2=self.visit(ast.rhs,c)
        typ1=self.visit(ast.lhs,c)
        if isinstance(typ1.mtype,Unknown) and isinstance(typ2.mtype,Unknown):
            raise TypeCannotBeInferred(ast)

        elif isinstance(typ1.mtype,Unknown) and not isinstance(typ2.mtype,Unknown):
            self.inferType(typ1,typ2.mtype)      

        elif isinstance(typ2.mtype,Unknown) and not isinstance(typ1.mtype,Unknown):
            self.inferType(typ2,typ1.mtype)      

        elif type(typ1.mtype) != type(typ2.mtype):
            raise TypeMismatchInStatement(ast)

        return c

    
    def visitCallStmt(self, ast, c): 
        
        funcSymbol=self.getSymbolFunctionByName(ast.method.name,c)

        if not isinstance(funcSymbol.mtype,MType):
            raise Undeclared(Function(),ast.method.name)

        #tìm kiếm coi có tên trong env chưa
        #if not isinstance(funcSymbol.mtype,MType):  #kiểu của func
            #raise UndeclaredIdentifier(funcSymbol.name)

        lstParam=funcSymbol.mtype.intype

        if len(lstParam)!=len(ast.param):
            raise TypeMismatchInStatement(ast)
        
        if funcSymbol.mtype.restype is None:
            funcSymbol.mtype.restype = VoidType()
        elif not isinstance(funcSymbol.mtype.restype, VoidType):
            raise TypeMismatchInStatement(ast)
        
        for i in range(len(lstParam)):
            argSym=self.visit(ast.param[i],c)
            if isinstance(argSym.mtype,Unknown) and isinstance(lstParam[i].mtype,Unknown):
                raise TypeCannotBeInferred(ast)
            elif isinstance(argSym.mtype,Unknown) and not isinstance(lstParam[i].mtype,Unknown):
                self.inferType(argSym,lstParam[i].mtype)
            elif not isinstance(argSym.mtype,Unknown) and isinstance(lstParam[i].mtype,Unknown):
                self.inferType(lstParam[i],argSym.mtype)
            elif type(lstParam[i].mtype) != type(argSym.mtype):
                raise TypeMismatchInStatement(ast)
            
        return c

    def visitCallExpr(self, ast, c):
        funcSymbol=self.getSymbolFunctionByName(ast.method.name,c)
        #tìm kiếm coi có tên trong env chưa
        if not isinstance(funcSymbol.mtype,MType):  #kiểu của func
            raise Undeclared(Function(),funcSymbol.method.name)

        lstParam=funcSymbol.mtype.intype

        if len(lstParam)!=len(ast.param):
            raise TypeMismatchInExpression(ast)
        
        if funcSymbol.mtype.restype is None:
            raise TypeCannotBeInferred(ast)
        
        
        
        for i in range(len(lstParam)):
            argSym=self.visit(ast.param[i],c)
            if isinstance(argSym.mtype,Unknown) and isinstance(lstParam[i].mtype,Unknown):
                raise TypeCannotBeInferred(ast)
            elif isinstance(argSym.mtype,Unknown) and not isinstance(lstParam[i].mtype,Unknown):
                self.inferType(argSym,lstParam[i].mtype)
            elif not isinstance(argSym.mtype,Unknown) and isinstance(lstParam[i].mtype,Unknown):
                self.inferType(lstParam[i],argSym.mtype)
            elif type(lstParam[i].mtype) != type(argSym.mtype):
                raise TypeMismatchInExpression(ast)
            
        return Symbol(None,funcSymbol.mtype.restype)

    def visitIf(self, ast, c):
        #print(ast.ifthenStmt)
        for x in ast.ifthenStmt:
            if isinstance(x,list):
                for sym in x:
                    if isinstance(sym,list):
                        for s in sym:
                            print(type(s))
                    else:
                        print(type(sym))
            
        
        """
        for ifClause in ast.ifthenStmt:
            condType=self.visit(ast.ifthenStmt[0],c)
            if not isinstance(condType.mtype, BoolType):
                raise TypeMismatchInStatement(ast)
            
        """



    def visitId(self, ast, c):
        return self.getSymbolByName(ast.name,c)


    def visitIntLiteral(self, ast, c):
        return Symbol(None,NumberType())

    def visitNumberLiteral(self, ast, c):
        return Symbol(None,NumberType())

    def visitBooleanLiteral(self, ast, c):
        return Symbol(None,BoolType())

    def visitStringLiteral(self, ast, c):
        return Symbol(None,StringType())

    def visitArrayLiteral(self, ast, c):
        return None

    def visitJSONLiteral(self, ast, c):
        return None

