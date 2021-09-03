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


def infer(id,o,typ):
    for x in o:
        if id.name==x[0]:
            x[1]=typ

class StaticCheck(Visitor):
    #decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self,ctx:Program,o):
        o=[]
        for x in ctx.decl:
            o+=[self.visit(x,o)]
        for x in ctx.stmts:
            self.visit(x,o)


    def visitVarDecl(self,ctx:VarDecl,o):
        return [ctx.name,0]

    def visitAssign(self,ctx:Assign,o):
        typ1=self.visit(ctx.lhs,o)
        typ2=self.visit(ctx.rhs,o)
        if typ1==0 and typ2==0:
            raise TypeCannotBeInferred(ctx)
        elif typ1==0 and typ2!=0:
            infer(ctx.lhs,o,typ2)
        elif typ1!=0 and typ2==0:
            infer(ctx.rhs,o,typ1)
        elif typ1!=typ2:
            raise TypeMismatchInExpression(ctx)

     #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o):
        typ1=self.visit(ctx.e1,o)
        typ2=self.visit(ctx.e2,o)
        op=ctx.op
        if ctx.op in ['+','-','*','/']:
            if typ1==0:
                infer(ctx.e1,o,1)
                typ1=1
            if typ2==0:
                infer(ctx.e2,o,1)
                typ2=1
            if typ1!=1 or typ2!=1:
                raise TypeMismatchInExpression(ctx)
            return 1
        if ctx.op in ['+.','-.','*.','/.']:
            if typ1==0:
                infer(ctx.e1,o,2)
                typ1=2
            if typ2==0:
                infer(ctx.e2,o,2)
                typ2=2
            if typ1!=2 or typ2!=2:
                raise TypeMismatchInExpression(ctx)
            return 2
        if ctx.op in ['&&','||','>b','=b']:
            if typ1==0:
                infer(ctx.e1,o,3)
                typ1=3
            if typ2==0:
                infer(ctx.e2,o,3)
                typ2=3
            if typ1!=3 or typ2!=3:
                raise TypeMismatchInExpression(ctx)
            return 3
        if ctx.op in ['>','=']:
            if typ1==0:
                infer(ctx.e1,o,1)
                typ1=1
            if typ2==0:
                infer(ctx.e2,o,1)
                typ2=1
            if typ1!=1 or typ2!=1:
                raise TypeMismatchInExpression(ctx)
            return 3
        if ctx.op in ['>.','=.']:
            if typ1==0:
                infer(ctx.e1,o,2)
                typ1=2
            if typ2==0:
                infer(ctx.e2,o,2)
                typ2=2
            if typ1!=2 or typ2!=2:
                raise TypeMismatchInExpression(ctx)
            return 3

    #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o):
        pass

    def visitIntLit(self,ctx:IntLit,o):
        return 1 

    def visitFloatLit(self,ctx,o):
        return 2

    def visitBoolLit(self,ctx,o):
        return 3

    def visitId(self,ctx,o):
        for x in o:
            if x[0]==ctx.name:
                return x[1]
        raise UndeclaredIdentifier(ctx.name)


o=[[x,0],[y,0],[z,0]]
[[x,1],[y,2],[z,0]] ->sau khi suy diễn