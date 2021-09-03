class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):

        expr = self.visit(ctx.term(len(ctx.term())-1))
        for i in reversed(range(len(ctx.term()) - 1)):
            expr = Binary(ctx.getChild(i * 2 + 1).getText(), self.visit(ctx.term(i)),expr)
        return expr

    def visitTerm(self,ctx:MPParser.TermContext): 

        if ctx.getChildCount()==1:
            return self.visit(ctx.factor(0))
        else:
            return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))

    def visitFactor(self,ctx:MPParser.FactorContext):

        expr = self.visit(ctx.operand(0))
        for i in range(len(ctx.operand()) - 1):
            expr = Binary(ctx.getChild(i * 2 + 1).getText(), expr, self.visit(ctx.operand(i + 1)))
        return expr
    def visitOperand(self,ctx:MPParser.OperandContext):

        if ctx.getChildCount()==1:
            if ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.INTLIT():
                return IntLiteral(ctx.INTLIT().getText())
            elif ctx.BOOLIT():
                return BooleanLiteral(ctx.BOOLIT().getText())
        else:
            return self.visit(ctx.exp())