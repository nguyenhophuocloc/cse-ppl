class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        list_vardecl=ctx.vardecl()
        return Program([x for vardecl in list_vardecl for x in vardecl.accept(self)])
        #lay list,  x la 1 vardecl

    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        
        ids=ctx.ids().accept(self)
        typ=ctx.mptype().accept(self)
        return [VarDecl(id,typ) for id in ids]

    def visitMptype(self,ctx:MPParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()

    def visitIds(self,ctx:MPParser.IdsContext):

        return [Id(id.getText()) for id in ctx.ID()]
