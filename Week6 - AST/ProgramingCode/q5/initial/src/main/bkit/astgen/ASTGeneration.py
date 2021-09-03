from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):

        list_vardecl=ctx.vardecl()
        return Program([x for vardecl in list_vardecl for x in vardecl.accept(self)])


    def visitVardecl(self,ctx:BKITParser.VardeclContext): 
        
        ids=ctx.ids().accept(self)
        typ=ctx.mptype().accept(self)
        return [VarDecl(id,typ) for id in ids]

    def visitMptype(self,ctx:BKITParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()

    def visitIds(self,ctx:BKITParser.IdsContext):

        return [Id(id.getText()) for id in ctx.ID()]
