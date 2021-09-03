from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):

    def visitProgram(self, ctx: BKITParser.ProgramContext):

        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self, ctx: BKITParser.VardeclsContext):

        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self, ctx: BKITParser.VardecltailContext):

        if ctx.getChildCount() > 0:
            return ctx.vardecl().accept(self)+ctx.vardecltail().accept(self)
        else:
            return []
    def visitVardecl(self, ctx: BKITParser.VardeclContext):
        ids=ctx.ids().accept(self)
        typ=ctx.mptype().accept(self)
        return [VarDecl(id,typ) for id in ids]

    def visitMptype(self, ctx: BKITParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()
    def visitIds(self, ctx: BKITParser.IdsContext):
        if ctx.getChildCount()>1:
            return [Id(ctx.ID().getText())] + ctx.ids().accept(self)
        else:
            return [Id(ctx.ID().getText())]
