def visitIntLiteral(self,ctx,o):
    return self.emit.emitPUSHICONST(ctx.value,o.frame), IntType()
    #visit trả về 1 cặp, o chứa frame, ctx chứa value