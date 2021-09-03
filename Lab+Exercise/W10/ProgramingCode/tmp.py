class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o):
        op=ctx.op
        typ1=self.visit(ctx.e1,o)
        typ2=self.visit(ctx.e2,o)
        if op in ['+','-','*']:
            if typ1=="bool" or typ2=="bool":
                raise TypeMismatchInExpression(ctx)
            else:
                if typ1=="float" or typ2=='float':
                    return "float"
                return "int"
        elif op =='/':
            if typ1=="bool" or typ2=="bool":
                raise TypeMismatchInExpression(ctx)
            return "float"
        elif op in ['&&','||']:
            if typ1=="bool" and typ2=="bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)
        elif op in ['>','<','==','!=']:
            if typ1==typ2:
                return "bool"
            raise TypeMismatchInExpression(ctx)

    def visitUnOp(self,ctx:UnOp,o):
        op=ctx.op
        typ=self.visit(ctx.e,o)
        if op =='-':
            if typ=="bool":
                raise TypeMismatchInExpression(ctx)
            else:
                if typ=="float":
                    return "float"
                return "int"
        elif op =='!':
            if typ=="bool":
                return "bool"
            raise TypeMismatchInExpression(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return "int" 

    def visitFloatLit(self,ctx,o):
        return "float"

    def visitBoolLit(self,ctx,o):
        return "bool"
