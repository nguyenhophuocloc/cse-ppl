    def visitFloatLiteral(self,ctx,o):
        return self.emit.emitPUSHFCONST(ctx.value,o.frame), FloatType()