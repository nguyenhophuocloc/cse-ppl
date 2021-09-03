#Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))
from functools import reduce
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


    def visitTerm(self,ctx:MPParser.TermContext): 

        if ctx.getChildCount()==1:
            return self.visit(ctx.factor(0))
        return Binary(ctx.COMPARE().getText(),self.visit(ctx.factor(0)),self.visit(ctx.factor(1)))

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