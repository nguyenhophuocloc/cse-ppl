class Program: #decl:List[VarDecl],stmts:List[Assign]

class VarDecl: #name:str

class Assign: #lhs:Id,rhs:Exp

class Exp(ABC): #abstract class

class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b

class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor

class IntLit(Exp): #val:int

class FloatLit(Exp): #val:float

class BoolLit(Exp): #val:bool

class Id(Exp): #name:str

and the Visitor class is declared as follows:

class StaticCheck(Visitor):
    #decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self,ctx:Program,o):
        


    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitAssign(self,ctx:Assign,o): pass

     #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o):
        typ1=self.visit(ctx.e1,o)
        typ2=self.visit(ctx.e2,o)
        op=ctx.op
        if op in ['+' , '-' , '*', '/']:
            if typ1==1 and typ2==1:
                return 1
            raise TypeMismatchInExpression(o)
        elif op in ['+.' , '-.' , '*.', '/.']:
            if typ1==2 and typ2==2:
                return 1
            raise TypeMismatchInExpression(o)
        elif op in ['&&','||','>b','=b']:
            if typ1==3 and typ2==3:
                return 3
            raise TypeMismatchInExpression(o)
        elif op in['>','=']:
            if typ1==1 and typ2==1:
                return 3
            raise TypeMismatchInExpression(o)
        elif op in ['>.','=.']:
            if typ1==2 and typ2==2:
                return 3
            raise TypeMismatchInExpression(o)

    #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o):
        typ=self.visit(ctx.e,o)
        op=ctx.op
        if op =='-':
            if typ==1:
                return 1
            raise TypeMismatchInExpression(o)
        elif op=='-.':
            if typ==2:
                return 2
            raise TypeMismatchInExpression(o)
        

    def visitIntLit(self,ctx:IntLit,o):
        return 1 

    def visitFloatLit(self,ctx,o):
        return 2

    def visitBoolLit(self,ctx,o):
        return 3

    def visitId(self,ctx,o): pass