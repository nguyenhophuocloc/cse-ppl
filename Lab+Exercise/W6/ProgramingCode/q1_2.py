class ASTGeneration(MPVisitor):

    #program: vardecls EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.vardecls())+1
    #vardecls: vardecl vardecltail;
    def visitVardecls(self,ctx:MPParser.VardeclsContext):

        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
    #vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self,ctx:MPParser.VardecltailContext): 

        if ctx.getChildCount()==0:
            return 0
        return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)
    #vardecl: mptype ids ';' ;
    def visitVardecl(self,ctx:MPParser.VardeclContext): 
        return self.visit(ctx.mptype()) + self.visit(ctx.ids()) +1

    #mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self,ctx:MPParser.MptypeContext):

        return 1

    #ids: ID ',' ids | ID;
    def visitIds(self,ctx:MPParser.IdsContext):

        if ctx.getChildCount()==1:
            return 1
        return 2 + self.visit(ctx.ids())