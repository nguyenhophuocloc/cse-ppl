from functools import reduce

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):

        return ctx.exp().accept(self)
    
    #exp: (term ASSIGN)* term; right-ass
    def visitExp(self,ctx:MPParser.ExpContext):

        if ctx.getChildCount()==1:
            return ctx.term(0).accept(self)
        else:
            lstTermDecs=ctx.term()[::-1] #phai dao vi ket hop phải
            lastTerm=ctx.term(len(lstTermDecs)-1).accept(self)
            lstOpDecs=ctx.ASSIGN()[::-1]
            lstZip=list(zip(lstOpDecs,lstTermDecs[1:]))
            return reduce(lambda acc,zipItem: Binary(zipItem[0].getText(),zipItem[1].accept(self),acc),lstZip,lastTerm)

    #term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 

        if ctx.getChildCount()==1:
            return ctx.factor(0).accept(self)
        else:
            return Binary(ctx.COMPARE().getText(),ctx.factor(0).accept(self),ctx.factor(1).accept(self))

    #factor: operand (ANDOR operand)*; 
    def visitFactor(self,ctx:MPParser.FactorContext):

        if ctx.getChildCount()==1:
            return ctx.operand(0).accept(self)
        else:
            lstOperand=ctx.operand()
            firstOperand=ctx.operand(0).accept(self)
            lstOpDecs=ctx.ANDOR()
            lstZip=list(zip(lstOpDecs,lstOperand[1:]))
            return reduce(lambda acc,zipItem: Binary(zipItem[0].getText(),acc,zipItem[1].accept(self)),lstZip,firstOperand)

    #operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):

        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        else:
            return ctx.exp().accept(self)