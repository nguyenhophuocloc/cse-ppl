from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):

    def visitProgram(self,ctx:BKITParser.ProgramContext):

        return ctx.exp().accept(self)

    def visitExp(self,ctx:BKITParser.ExpContext):

        if ctx.getChildCount()==1:
            return ctx.term().accept(self)
        else:
            return Binary(ctx.ASSIGN().getText(),ctx.term().accept(self),ctx.exp().accept(self))

    def visitTerm(self,ctx:BKITParser.TermContext): 

        if ctx.getChildCount()==1:
            return ctx.factor(0).accept(self)
        else:
            return Binary(ctx.COMPARE().getText(),ctx.factor(0).accept(self),ctx.factor(1).accept(self))

    def visitFactor(self,ctx:BKITParser.FactorContext):

        if ctx.getChildCount()==1:
            return ctx.operand().accept(self)
        else:
            return Binary(ctx.ANDOR().getText(),ctx.factor().accept(self),ctx.operand().accept(self))

    def visitOperand(self,ctx:BKITParser.OperandContext):

        if ctx.getChildCount()==1:
            if ctx.INTLIT():
                return IntLiteral(ctx.INTLIT().getText())
            elif ctx.ID():
                return Id(ctx.ID().getText())
            elif ctx.BOOLIT():
                return BooleanLiteral(ctx.BOOLIT().getText())
        else:
            return ctx.exp().accept(self)