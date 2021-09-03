class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o):
        typ1=self.visit(ctx.e1,o)
        typ2=self.visit(ctx.e2,o)
        if ctx.op in ['+','-','*']:
            if (typ1==3 or typ2==3):
                raise TypeMismatchInExpression(ctx)
            if(typ1!=typ2):
                return 2
            return typ1
        elif ctx.op=='/':
            if (typ1==3 or typ2==3):
                raise TypeMismatchInExpression(ctx)
            return 2
        elif ctx.op in ['!','&&','||']:
            if(typ1==3 and typ2==3):
                return 3
            raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['>','<','==','!=']:
            if(typ1==typ2):
                return 3
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        typ=self.visit(ctx.e,o)
        if ctx.op=='-':
            if typ==2:
                return 2
            elif typ==1:
                return 1
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op=='!':
            if typ==3:
                return 3
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return 1

    def visitFloatLit(self,ctx,o):
        return 2

    def visitBoolLit(self,ctx,o):
        return 3