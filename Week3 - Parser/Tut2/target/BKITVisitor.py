# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9
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


    # Visit a parse tree produced by BKITParser#manydcl.
    def visitManydcl(self, ctx:BKITParser.ManydclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardcl.
    def visitVardcl(self, ctx:BKITParser.VardclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mc_type.
    def visitMc_type(self, ctx:BKITParser.Mc_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#idlist.
    def visitIdlist(self, ctx:BKITParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcdcl.
    def visitFuncdcl(self, ctx:BKITParser.FuncdclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paramdecl.
    def visitParamdecl(self, ctx:BKITParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#paralist.
    def visitParalist(self, ctx:BKITParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#body.
    def visitBody(self, ctx:BKITParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bodylist.
    def visitBodylist(self, ctx:BKITParser.BodylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt.
    def visitStmt(self, ctx:BKITParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_assign.
    def visitStmt_assign(self, ctx:BKITParser.Stmt_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_call.
    def visitStmt_call(self, ctx:BKITParser.Stmt_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#stmt_return.
    def visitStmt_return(self, ctx:BKITParser.Stmt_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operands.
    def visitOperands(self, ctx:BKITParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#subexp.
    def visitSubexp(self, ctx:BKITParser.SubexpContext):
        return self.visitChildren(ctx)



del BKITParser