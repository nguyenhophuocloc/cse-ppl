class ASTGeneration(MPVisitor):
    #program: vardecl+ EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        vardecls=ctx.vardecl()  #list các vardecl
        result=[]               #Program(Var[],Var[])
        for vardecl in vardecls:
            result+=self.visit(vardecl)     #flatten
        return Program(result)
    #vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        typ=self.visit(ctx.mptype())
        idslist=self.visit(ctx.ids())
        return [VarDecl(id,typ) for id in idslist]
    #mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        return FloatType()
    #ids: ID (',' ID)*;         #trả về 1 list
    def visitIds(self,ctx:MPParser.IdsContext):
        ids=ctx.ID()    #List id thuoc kieu MPParser.ID() -> Id()
        result=[]
        #for id in ids:
        #    result+=[Id(id.getText())]
        #return result
        return [Id(id.getText()) for id in ids]