# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#manydecl.
    def visitManydecl(self, ctx:BKITParser.ManydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardecl.
    def visitVardecl(self, ctx:BKITParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#idlist.
    def visitIdlist(self, ctx:BKITParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdecl.
    def visitFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramlist.
    def visitParamlist(self, ctx:BKITParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignstmt.
    def visitAssignstmt(self, ctx:BKITParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callstmt.
    def visitCallstmt(self, ctx:BKITParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#explist.
    def visitExplist(self, ctx:BKITParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnstmt.
    def visitReturnstmt(self, ctx:BKITParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)



del BKITParser