"""
	
Program([VarDecl("x")],[Assign(Id("x"),BinOp("+",IntLit(3),BoolLit(True)))])
"""


def infer(id, o, typ):
    for x in o:
        if id.name == x[0]:
            x[1] = typ
# hàm suy diễn kiểu, nếu tìm được id name trong o, thì kiểu
# của nó tức id[1] chính là tham số typ


class StaticCheck(Visitor):
    # decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self, ctx: Program, o):
        o = []
        for x in ctx.decl:
            o += [self.visit(x, o)]
        for x in ctx.stmts:
            self.visit(x, o)
    # tổ chức o thành [[x,None]] thực ra là [[ , ]]
    # tổ chức xong thì duyệt stmts, 2 chữ x ko liên quan nhau

    # name:str
    def visitVarDecl(self, ctx: VarDecl, o):
        return [ctx.name, 0]  # số 0 điền cái gì cũng được, éo có kiểu

    # lhs:Id,rhs:Exp
    def visitAssign(self, ctx: Assign, o):
        typ1 = self.visit(ctx.lhs, o)
        typ2 = self.visit(ctx.rhs, o)
        if typ1 == 0 and typ2 == 0:
            raise TypeCannotBeInferred(ctx)
        if typ1 == 0:
            infer(ctx.lhs, o, typ2)
            return
        if typ2 == 0 and type(ctx.rhs) is Id:
            infer(ctx.rhs, o, typ1)
            return
        if typ1 != typ2:
            raise TypeMismatchInStatement(ctx)

    # op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self, ctx: BinOp, o):
        typ1 = self.visit(ctx.e1, o)
        typ2 = self.visit(ctx.e2, o)
        op = ctx.op
        if ctx.op in ['+', '-', '*', '/']:  # suy diễn rồi mới làm
            if typ1 == 0:
                infer(ctx.e1, o, 1)  # tác động trong o
                typ1 = 1  # tác động biến typ1
            if typ2 == 0:
                infer(ctx.e2, o, 1)
                typ2 = 1
            if typ1 == 1 and typ2 == 1:
                return 1
            else:
                raise TypeMismatchInExpression(ctx)
        if ctx.op in ['+.', '-.', '*.', '/.']:  # suy diễn rồi mới làm
            if typ1 == 0:
                infer(ctx.e1, o, 2)  # tác động trong o
                typ1 = 2  # tác động biến typ1
            if typ2 == 0:
                infer(ctx.e2, o, 2)
                typ2 = 2
            if typ1 == 2 and typ2 == 2:
                return 2
            else:
                raise TypeMismatchInExpression(ctx)
        if ctx.op in ['&&', '||', '>b', '=b']:
            if typ1 == 0:
                infer(ctx.e1, o, 3)  # tác động trong o
                typ1 = 3  # tác động biến typ1
            if typ2 == 0:
                infer(ctx.e2, o, 3)
                typ2 = 3
            if typ1 == 3 and typ2 == 3:
                return 3
            else:
                raise TypeMismatchInExpression(ctx)
        if ctx.op in ['>', '=']:
            if typ1 == 0:
                infer(ctx.e1, o, 1)  # tác động trong o
                typ1 = 1  # tác động biến typ1
            if typ2 == 0:
                infer(ctx.e2, o, 1)
                typ2 = 1
            if typ1 == 1 and typ2 == 1:
                return 3
            else:
                raise TypeMismatchInExpression(ctx)
        if ctx.op in ['>.', '=.']:
            if typ1 == 0:
                infer(ctx.e1, o, 2)  # tác động trong o
                typ1 = 2  # tác động biến typ1
            if typ2 == 0:
                infer(ctx.e2, o, 2)
                typ2 = 2
            if typ1 == 2 and typ2 == 2:
                return 3
            else:
                raise TypeMismatchInExpression(ctx)

    # op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self, ctx: UnOp, o):
        typ = self.visit(ctx.e, o)
        op = ctx.op
        if op == '-':
            if typ == 0:
                infer(ctx.e, o, 1)
                typ = 1
            if typ == 1:
                return 1
            else:
                raise TypeMismatchInExpression(ctx)
        
        if op == '-.':
            if typ == 0:
                infer(ctx.e, o, 2)
                typ = 2
            if typ == 2:
                return 2
            else:
                raise TypeMismatchInExpression(ctx)

        if op == '!':
            if typ == 0:
                infer(ctx.e, o, 3)
                typ = 3
            if typ == 3:
                return 3
            else:
                raise TypeMismatchInExpression(ctx)

        if op == 'i2f':
            if typ == 0:
                infer(ctx.e, o, 1)
                typ = 1
            if typ == 1:
                return 2
            else:
                raise TypeMismatchInExpression(ctx)

        if op == 'floor':
            if typ == 0:
                infer(ctx.e, o, 2)
                typ = 2
            if typ == 2:
                return 1
            else:
                raise TypeMismatchInExpression(ctx)

    # val:int
    def visitIntLit(self, ctx: IntLit, o):
        return 1

    # val:float
    def visitFloatLit(self, ctx, o):
        return 2

    # val:bool
    def visitBoolLit(self, ctx, o):
        return 3

    # name:str
    def visitId(self, ctx, o):
        for x in o:
            if ctx.name==x[0]:
                return x[1]
        raise UndeclaredIdentifier(ctx.name)
