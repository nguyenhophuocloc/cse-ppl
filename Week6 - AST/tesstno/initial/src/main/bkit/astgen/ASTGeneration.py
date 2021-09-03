from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):

        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self,ctx:BKITParser.VardeclsContext):

        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecltail(self,ctx:BKITParser.VardecltailContext): 

        if ctx.getChildCount()==0:
            return []
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    def visitVardecl(self,ctx:BKITParser.VardeclContext): 
        
        type=ctx.mptype().accept(self)
        ids=ctx.ids().accept(self)
        return [VarDecl(id,type) for id in ids]

    def visitMptype(self,ctx:BKITParser.MptypeContext):

        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self,ctx:BKITParser.IdsContext):

        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())]+ctx.ids().accept(self)
