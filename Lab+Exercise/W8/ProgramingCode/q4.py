class Program: #decl:List[Decl]

class Decl(ABC): #abstract class

class VarDecl(Decl): #name:str,typ:Type

class ConstDecl(Decl): #name:str,val:Lit

class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])

class Type(ABC): #abstract class

class IntType(Type)

class FloatType(Type)

class Expr(ABC): #abstract class

class Lit(Expr): #abstract class

class IntLit(Lit): #val:int

class Id(Expr): #name:str

and exceptions:

class RedeclaredVariable(Exception): #name:str

class RedeclaredConstant(Exception): #name:str

class RedeclaredFunction(Exception): #name:str

class UndeclaredIdentifier(Exception): #name:str

#-------------------------------------
#2 tầng
from functools import reduce
class StaticCheck(Visitor):
    #decl:List[Decl]
    def visitProgram(self,ctx:Program,o:object):
        #reduce(lambda x,y: self.visit(y,x),ctx.decl,[])
        o=[[]]
        reduce(lambda x,y:self.visit(y,x),ctx.decl,o)
    #name:str,typ:Type
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        o[0].append(ctx.name)
        return o

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        o[0].append(ctx.name)
        return o
    #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        o[0].append(ctx.name)
        reduce(lambda x,y:self.visit(y,x),ctx.param+ctx.body[0]+ctx.body[1],[[]]+o)
        return o

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):
        return o
     #name:str
    def visitId(self,ctx:Id,o:object):
        for lstSymbol in o:
            for symbol in lstSymbol:
                if symbol == ctx.name:
                    return o
        raise UndeclaredIdentifier(ctx.name)