class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):

        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self, ctx: MPParser.VardecltailContext):

        if ctx.getChildCount() > 0:
            return ctx.vardecl().accept(self)+ctx.vardecltail().accept(self)
        else:
            return []
    def visitVardecl(self, ctx: MPParser.VardeclContext):
        ids=ctx.ids().accept(self)
        typ=ctx.mptype().accept(self)
        return [VarDecl(id,typ) for id in ids]

    def visitMptype(self, ctx: MPParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()
    def visitIds(self, ctx: MPParser.IdsContext):
        if ctx.getChildCount()>1:
            return [Id(ctx.ID().getText())] + ctx.ids().accept(self)
        else:
            return [Id(ctx.ID().getText())]
