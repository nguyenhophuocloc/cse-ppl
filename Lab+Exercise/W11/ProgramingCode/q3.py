def visitBinExpr(self,ctx,o):   #op,e1,e2
    op=ctx.op
    e1c, e1t=self.visit(ctx.e1,o)
    e2c, e2t=self.visit(ctx.e2,o)
    if op in ['+','-']:
        op=self.emit.emitADDOP(op,IntType(),o.frame)
        rt=IntType()
        return e1c+e2c+op, IntType()
    elif op in ['*','/']:
        op=self.emit.emitMULOP(op,IntType(),o.frame)
        rt=IntType()
        return e1c+e2c+op, IntType()
    elif op in ['+.','-.']:
        if op=='+.':
            op='+'           
            return e1c+e2c+self.emit.emitADDOP(op,FloatType(),o.frame), FloatType()
        elif op=='-.':
            op='-'           
            return e1c+e2c+self.emit.emitADDOP(op,FloatType(),o.frame), FloatType()
    elif op in ['*.','/.']:
        if op=='*.':
            op='*'           
            return e1c+e2c+self.emit.emitMULOP(op,FloatType(),o.frame), FloatType()
    
