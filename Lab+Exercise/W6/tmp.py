class ASTGeneration(MPVisitor):
    # program: vardecls EOF;
    def visitProgram(self, ctx: MPParser.ProgramContext):

        return Program(self.visit(ctx.vardecls()))

    # vardecls: vardecl vardecltail;
    def visitVardecls(self, ctx: MPParser.VardeclsContext):

        return self.visit(ctx.vardecl())+self.visit(ctx.vardecltail())

    # vardecltail: vardecl vardecltail | ;
    def visitVardecltail(self, ctx: MPParser.VardecltailContext):

        if ctx.getChildCount() > 1:
            return self.visit(ctx.vardecl())+self.visit(ctx.vardecltail())
        return []

    # vardecl: mptype ids ';' ;
    def visitVardecl(self, ctx: MPParser.VardeclContext):

        typ = self.visit(ctx.mptype())
        list_id = self.visit(ctx.ids())
        return [VarDecl(id, typ) for id in list_id]

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self, ctx: MPParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        return FloatType()
    # ids: ID ',' ids | ID;

    def visitIds(self, ctx: MPParser.IdsContext):

        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())]+self.visit(ctx.ids())
######################################################################


class ASTGeneration(MPVisitor):

    # program: vardecl+ EOF;
    def visitProgram(self, ctx: MPParser.ProgramContext):

        list_vardecl = ctx.vardecl()
        res = []
        for vardecl in list_vardecl:
            res += self.visit(vardecl)
        return Program(res)

    # vardecl: mptype ids ';' ;
    def visitVardecl(self, ctx: MPParser.VardeclContext):
        typ = self.visit(ctx.mptype())
        list_id = self.visit(ctx.ids())
        return [VarDecl(id, typ) for id in list_id]

    # mptype: INTTYPE | FLOATTYPE;
    def visitMptype(self, ctx: MPParser.MptypeContext):

        if ctx.INTTYPE():
            return IntType()
        return FloatType()

    # ids: ID (',' ID)*;
    def visitIds(self, ctx: MPParser.IdsContext):

        list_id = ctx.ID()
        return [Id(id.getText()) for id in list_id]
############################################################################


class ASTGeneration(MPVisitor):

    # program: exp EOF;
    def visitProgram(self, ctx: MPParser.ProgramContext):

        return Program(self.visit(ctx.exp()))

    # exp: term ASSIGN exp | term;
    def visitExp(self, ctx: MPParser.ExpContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.term())
        return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp()))

    # term: factor COMPARE factor | factor;
    def visitTerm(self, ctx: MPParser.TermContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor(0))
        return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))

    # factor: factor ANDOR operand | operand;
    def visitFactor(self, ctx: MPParser.FactorContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand()))

    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self, ctx: MPParser.OperandContext):

        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            if ctx.INTLIT():
                return IntLiteral(ctx.INTLIT().getText())
            if ctx.BOOLIT():
                return BooleanLiteral(ctx.BOOLIT().getText())
        return self.visit(ctx.exp())
###############################################################################
class ASTGeneration(MPVisitor):
    
    #program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.exp())

    #exp: (term ASSIGN)* term;
    def visitExp(self,ctx:MPParser.ExpContext):

        if ctx.getChildCount()==1:
            return self.visit(ctx.term(0))
        else:
            lstTermDecs=ctx.term()[::-1]
            lastTerm=self.visit(ctx.term(len(lstTermDecs)-1))
            lstOpDecs=ctx.ASSIGN()[::-1]
            lstZip=list(zip(lstOpDecs,lstTermDecs[1:]))
            return reduce(lambda acc,zipItem: Binary(zipItem[0].getText(),self.visit(zipItem[1]),acc),lstZip,lastTerm)

    #term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 

        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor(0))
        return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))

    #factor: operand (ANDOR operand)*; 
    def visitFactor(self,ctx:MPParser.FactorContext):

        if ctx.getChildCount()==1:
            return ctx.operand(0).accept(self)
        else:
            lstOperand=ctx.operand()
            firstOperand=self.visit(ctx.operand(0))
            lstOpDecs=ctx.ANDOR()
            lstZip=list(zip(lstOpDecs,lstOperand[1:]))
            return reduce(lambda acc,zipItem: Binary(zipItem[0].getText(),acc,self.visit(zipItem[1])),lstZip,firstOperand)

    #operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):

        if ctx.getChildCount() == 1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            if ctx.INTLIT():
                return IntLiteral(ctx.INTLIT().getText())
            if ctx.BOOLIT():
                return BooleanLiteral(ctx.BOOLIT().getText())
        return self.visit(ctx.exp())