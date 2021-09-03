class Program: #decl:List[Decl]

class Decl(ABC): #abstract class

class VarDecl(Decl): #name:str,typ:Type

class ConstDecl(Decl): #name:str,val:Lit

class FuncDecl(Decl): #name:str,param:List[VarDecl],body:List[Decl]

class Type(ABC): #abstract class

class IntType(Type)

class FloatType(Type)

class Lit(ABC): #abstract class

class IntLit(Lit): #val:int

and exceptions:

class RedeclaredVariable(Exception): #name:str

class RedeclaredConstant(Exception): #name:str

class RedeclaredFunction(Exception): #name:str

#------------------------------------
from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        reduce(lambda x,y:self.visit(y,x),ctx.decl,[])

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return o+[ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return o+[ctx.name]
    #name:str,param:List[VarDecl],body:List[Decl]
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        reduce(lambda x,y: self.visit(y,x),ctx.param+ctx.body,[])
        #List Decl con trong Decl
        return o+[ctx.name]

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass
#Lưu ý thứ tự param, body