def visitId(self,ctx,o):
    sym = [x for x in o.sym if x.name == ctx.name][0]
    if type(sym.value) is Index:
        return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
    else:
        return self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, sym.mtype, o.frame), sym.mtype