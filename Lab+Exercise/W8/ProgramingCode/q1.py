class Program: #decl:List[Decl]

class Decl(ABC): #abstract class

class VarDecl(Decl): #name:str,typ:Type

class ConstDecl(Decl): #name:str,val:Lit

class Type(ABC): #abstract class

class IntType(Type)

class FloatType(Type)

class Lit(ABC): #abstract class

class IntLit(Lit): #val:int
#------------------------------------------
#Tìm kiếm phần tử đã khai báo
from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        """
        o=[]
        for decl in ctx.decl:
            self.visit(decl,o)
        """
        reduce(lambda x,y:self.visit(y,x),ctx.decl,[])
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return o+[ctx.name]
    #nếu phần tử dã có trong o thì raise, ngược lại thì thêm vào
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return o+[ctx.name]


    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

#Sol: 