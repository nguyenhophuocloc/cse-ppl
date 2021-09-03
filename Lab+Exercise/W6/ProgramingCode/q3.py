class ASTGeneration(MPVisitor):

    # program: vardecls EOF;
    def visitProgram(self, ctx: MPParser.ProgramContext):

        return Program(self.visit(ctx.vardecls()))

    # vardecls: vardecl vardecltail;
    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self, ctx: MPParser.VardecltailContext):

        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    # vardecl: mptype ids ';' ;
    def visitVardecl(self, ctx: MPParser.VardeclContext):
        typ=self.visit(ctx.mptype())        #IntType
        idlist=self.visit(ctx.ids())        #[Id(x),Id(y)]
        #[VarDecl(Id(x),IntType,Id(y),IntType)]
        #dist -> FP
        return [VarDecl(id,typ) for id in idlist]

    #mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self, ctx: MPParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    # ids: ID ',' ids | ID;
    def visitIds(self, ctx: MPParser.IdsContext):   #ids trả về list
        #sẽ bỏ []
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.ids())     #đối tượng + list
