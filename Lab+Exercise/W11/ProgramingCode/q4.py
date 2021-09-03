    def visitBinExpr(self,ctx,o):
        op=ctx.op
        e1c, e1t = self.visit(ctx.e1, o)
        e2c,e2t= self.visit(ctx.e2, o)        
        if isinstance(e1t,FloatType) or isinstance(e2t,FloatType):
            mType=FloatType()
        else:
            mType=IntType()
        if op == '/': mType = FloatType()
        if type(e1t) is IntType and type(mType) != type(e1t): e1c = e1c + self.emit.emitI2F(o.frame)
        if type(e2t) is IntType and type(mType) != type(e2t): e2c = e2c + self.emit.emitI2F(o.frame)
        
    
        if op in ['>','<','>=','<=','!=','==']:
            return e1c + e2c + self.emit.emitREOP(op, mType, o.frame), BoolType()
        if op in ['+', '-']:
            return e1c + e2c + self.emit.emitADDOP(op, mType, o.frame), mType
        if op in ['*']:
            return e1c + e2c + self.emit.emitMULOP(op, mType, o.frame), mType
        if op in ['/']:
            return e1c + e2c + self.emit.emitMULOP(op, mType, o.frame), mType