# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete generic visitor for a parse tree produced by CSELParser.

class CSELVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#manyDecl.
    def visitManyDecl(self, ctx:CSELParser.ManyDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#varDecl.
    def visitVarDecl(self, ctx:CSELParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#typ.
    def visitTyp(self, ctx:CSELParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#variable.
    def visitVariable(self, ctx:CSELParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#vartail.
    def visitVartail(self, ctx:CSELParser.VartailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var.
    def visitVar(self, ctx:CSELParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#varlist.
    def visitVarlist(self, ctx:CSELParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#literal.
    def visitLiteral(self, ctx:CSELParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:CSELParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#jsonLiteral.
    def visitJsonLiteral(self, ctx:CSELParser.JsonLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#funcDecl.
    def visitFuncDecl(self, ctx:CSELParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#paraList.
    def visitParaList(self, ctx:CSELParser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#param.
    def visitParam(self, ctx:CSELParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#body.
    def visitBody(self, ctx:CSELParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stmtList.
    def visitStmtList(self, ctx:CSELParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#manyStmt.
    def visitManyStmt(self, ctx:CSELParser.ManyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#otherStmt.
    def visitOtherStmt(self, ctx:CSELParser.OtherStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assignStmt.
    def visitAssignStmt(self, ctx:CSELParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#arrList.
    def visitArrList(self, ctx:CSELParser.ArrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#jsonList.
    def visitJsonList(self, ctx:CSELParser.JsonListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#ifStmt.
    def visitIfStmt(self, ctx:CSELParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forStmt.
    def visitForStmt(self, ctx:CSELParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forIn.
    def visitForIn(self, ctx:CSELParser.ForInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forOf.
    def visitForOf(self, ctx:CSELParser.ForOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#whileStmt.
    def visitWhileStmt(self, ctx:CSELParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#breakStmt.
    def visitBreakStmt(self, ctx:CSELParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#continueStmt.
    def visitContinueStmt(self, ctx:CSELParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#callStmt.
    def visitCallStmt(self, ctx:CSELParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#funcall.
    def visitFuncall(self, ctx:CSELParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#returnStmt.
    def visitReturnStmt(self, ctx:CSELParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#expr.
    def visitExpr(self, ctx:CSELParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stringExpr.
    def visitStringExpr(self, ctx:CSELParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#logicExpr.
    def visitLogicExpr(self, ctx:CSELParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:CSELParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#multiplicateExpr.
    def visitMultiplicateExpr(self, ctx:CSELParser.MultiplicateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#unaryLogicExpr.
    def visitUnaryLogicExpr(self, ctx:CSELParser.UnaryLogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#unarySignExpr.
    def visitUnarySignExpr(self, ctx:CSELParser.UnarySignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#indexExpr.
    def visitIndexExpr(self, ctx:CSELParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#indexOperator.
    def visitIndexOperator(self, ctx:CSELParser.IndexOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#keyExpr.
    def visitKeyExpr(self, ctx:CSELParser.KeyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#keyOperator.
    def visitKeyOperator(self, ctx:CSELParser.KeyOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#finalExpr.
    def visitFinalExpr(self, ctx:CSELParser.FinalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#callList.
    def visitCallList(self, ctx:CSELParser.CallListContext):
        return self.visitChildren(ctx)



del CSELParser