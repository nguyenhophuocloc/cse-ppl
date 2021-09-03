from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *


class ASTGeneration(CSELVisitor):
    def visitProgram(self, ctx: CSELParser.ProgramContext):
        #program: manyDecl+ EOF;
        listdecls = ctx.manyDecl()  # list các vardecl
        result = []  # Program(Var[],Var[])
        for decl in listdecls:
            result += self.visit(decl)  # flatten
        return Program(result)

    def visitManyDecl(self, ctx: CSELParser.ManyDeclContext):
        #manyDecl: varDecl|funcDecl;
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        return self.visit(ctx.funcDecl())

    def visitVarDecl(self, ctx: CSELParser.VarDeclContext):
        # varDecl: (LET|CONSTANT) variable (CM variable)* SM;
        # variable: var (COLON typ)? (ASSIGN (vartail))?;
        #vartail: literal|expr;
        #typ: 'Number'|'String'|'Boolean'|'Array'|'JSON';
        # var: ID (LQP varlist RQP)?;
        # varlist: NUMLIT CM varlist | NUMLIT;
        if ctx.LET():
            # return [VarDecl(Id(variable.var().ID().getText()), [], NoneType(), None) for variable in ctx.variable()]
            return [VarDecl(Id(variable.var().ID().getText()),  self.visit(variable.var().varlist()) if variable.var().varlist() else [], self.visit(variable.typ()) if variable.typ() else NoneType(), self.visit(variable.vartail()) if variable.vartail() else None) for variable in ctx.variable()]
        elif ctx.CONSTANT():
            return [ConstDecl(Id(variable.var().ID().getText()), self.visit(variable.var().varlist()) if variable.var().varlist() else [], self.visit(variable.typ()) if variable.typ() else NoneType(), self.visit(variable.vartail()) if variable.vartail() else None) for variable in ctx.variable()]

    def visitVarlist(self, ctx: CSELParser.VarlistContext):
        # varlist: NUMLIT CM varlist | NUMLIT;
        if ctx.getChildCount() == 1:
            return [ctx.NUMLIT().getText()]
        else:
            return [ctx.NUMLIT().getText()] + self.visit(ctx.varlist())

    def visitTyp(self, ctx: CSELParser.TypContext):
        #typ: 'Number'|'String'|'Boolean'|'Array'|'JSON';
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.BOOLEAN():
            return ctx.BOOLEAN().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.JSON():
            return ctx.JSON().getText()
        elif ctx.ARRAY():
            return ctx.ARRAY().getText()

    def visitVartail(self, ctx: CSELParser.VartailContext):
        #vartail: literal|expr;
        if ctx.literal():
            return self.visit(ctx.literal())
        return self.visit(ctx.expr())

    def visitLiteral(self, ctx: CSELParser.LiteralContext):
        #literal: TRUE | FALSE | NUMLIT| STRINGLIT | arrayLiteral|jsonLiteral;
        if ctx.TRUE() or ctx.FALSE():
            return BooleanLiteral(True if ctx.TRUE() else False)
        elif ctx.NUMLIT():
            return NumberLiteral(ctx.NUMLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.arrayLiteral():
            return self.visit(ctx.arrayLiteral())
        else:
            return self.visit(ctx.jsonLiteral())

    def visitArrayLiteral(self, ctx: CSELParser.ArrayLiteralContext):
        # arrayLiteral: LQP (literal (CM literal)*)? RQP;
        return ArrayLiteral([self.visit(lit) for lit in ctx.literal()])

    def visitJsonLiteral(self, ctx: CSELParser.JsonLiteralContext):
        # jsonLiteral: LB ID COLON literal (CM ID COLON literal)* RB;
        return JSONLiteral([self.visit(lit) for lit in ctx.literal()])

    def visitFuncDecl(self, ctx: CSELParser.FuncDeclContext):
        # funcDecl: FUNCTION ID LP paraList? RP LB body RB;
        return [FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paraList()) if ctx.paraList() else [], self.visit(ctx.body()))]

    def visitParaList(self, ctx: CSELParser.ParaListContext):
        # paraList: var (CM var)*;
        # var: ID (LQP varlist RQP)?;
        # varlist: NUMLIT CM varlist | NUMLIT;
        return [VarDecl(Id(var.ID().getText()), self.visit(var.varlist()) if var.varlist() else [], NoneType(), None) for var in ctx.var()]

    def visitBody(self, ctx: CSELParser.BodyContext):
        #body: stmtList;
        return self.visit(ctx.stmtList())

    def visitStmtList(self, ctx: CSELParser.StmtListContext):
        # stmtList: manyStmt*;
        liststmt = ctx.manyStmt()
        res = []
        for stmt in liststmt:
            res += self.visit(stmt)
        return res

    def visitManyStmt(self, ctx: CSELParser.ManyStmtContext):
        # manyStmt:varDecl|otherStmt;
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        return self.visit(ctx.otherStmt())

    def visitOtherStmt(self, ctx: CSELParser.OtherStmtContext):
        #otherStmt: assignStmt | ifStmt | forStmt | whileStmt  | breakStmt | continueStmt | callStmt | returnStmt;
        return self.visit(ctx.getChild(0))

    def visitAssignStmt(self, ctx: CSELParser.AssignStmtContext):
        # assignStmt: ID (LQP expr RQP)* ASSIGN expr SM;
        return Assign(Id(ctx.ID().getText()) if len(ctx.expr()) == 1 else ArrayCell(Id(ctx.ID().getText()), [self.visit(e) for e in ctx.expr()[:-1]]), self.visit(ctx.expr()[-1]))
    
    def visitIfStmt(self, ctx:CSELParser.IfStmtContext):
        #ifStmt: IF LP expr RP LB stmtList RB (ELIF LP expr RP LB stmtList RB)* (ELSE LB stmtList RB)?;
        #ifStmt: IF expr THEN stmtList (ELSEIF expr THEN stmtList)* (ELSE stmtList)? EIF DOT;
        return If([(self.visit(ctx.expr(i)), *self.visit(ctx.stmtList(i))) for i in range(len(ctx.expr()))], self.visit(ctx.stmtList()[-1]) if ctx.ELSE() else ([],[]))

    def visitForStmt(self, ctx:CSELParser.ForStmtContext):
        #forStmt: FOR ID IN arrayLiteral LB stmtList RB
        #         | FOR ID OF jsonLiteral LB stmtList RB
        #         | FOR ID IN ID LB stmtList RB
        #         | FOR ID OF ID LB stmtList RB;
        if ctx.IN():
            if ctx.arrayLiteral():
                ForIn(Id(ctx.ID().getText()),self.visit(ctx.arrayLiteral()),self.visit(ctx.stmtList()))
            else:
                ForIn(Id(ctx.ID(0).getText()), ctx.ID(1).getText(), self.visit(ctx.stmtList()))
        elif ctx.OF():
            if ctx.jsonLiteral():
                ForOf(Id(ctx.ID().getText()),self.visit(ctx.jsonLiteral()),self.visit(ctx.stmtList()))
            else:
                ForOf(Id(ctx.ID(0).getText()), ctx.ID(1).getText(), self.visit(ctx.stmtList()))

    def visitWhileStmt(self, ctx:CSELParser.WhileStmtContext):
        #whileStmt: WHILE LP expr RP LB stmtList RB;
        return While(self.visit(ctx.expr()), self.visit(ctx.stmtList()))

    def visitBreakStmt(self, ctx:CSELParser.BreakStmtContext):
        #breakStmt: BREAK SM;
        return Break()
        
    def visitContinueStmt(self, ctx:CSELParser.ContinueStmtContext):
        #continueStmt: CONTINUE SM;
        return Continue()

    def visitReturnStmt(self, ctx:CSELParser.ReturnStmtContext):
        #returnStmt: RETURN expr? SM;
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)

    def visitCallStmt(self, ctx:CSELParser.CallStmtContext):
        #callStmt: funcall SM;
        #funcall: CALL LP callList RP;
        #callList: ID CM LQP ((expr CM)* expr)? RQP;
        return CallExpr(Id(ctx.funcall().callList().ID().getText()), [self.visit(e) for e in ctx.funcall().callList().expr()])

    
    def visitExpr(self, ctx:CSELParser.ExprContext):
        #expr: logicExpr ((EQ|INE|ILT|IGT|ILTE|IGTE|FNE|FLT|FGT|FLTE|FGTE) logicExpr)?;
        expr = self.visit(ctx.logicExpr(0))
        if ctx.getChildCount() > 1:
            expr = BinaryOp(ctx.getChild(1).getText(), expr, self.visit(ctx.logicExpr(1)))
        return expr
    
    def visitLogicExpr(self, ctx:CSELParser.LogicExprContext):
        #logicExpr: additiveExpr ((AND|OR) additiveExpr)*;
        expr = self.visit(ctx.additiveExpr(0))
        for i in range(len(ctx.additiveExpr()) - 1):
            expr = BinaryOp(ctx.getChild(i * 2 + 1).getText(), expr, self.visit(ctx.additiveExpr(i + 1)))
        return expr

    def visitAdditiveExpr(self, ctx:CSELParser.AdditiveExprContext):
        #additiveExpr: multiplicateExpr ((IADD|ISUB|FADD|FSUB) multiplicateExpr)*;
        expr = self.visit(ctx.multiplicateExpr(0))
        for i in range(len(ctx.multiplicateExpr()) - 1):
            expr = BinaryOp(ctx.getChild(i * 2 + 1).getText(), expr, self.visit(ctx.multiplicateExpr(i + 1)))
        return expr

    def visitMultiplicateExpr(self, ctx:CSELParser.MultiplicateExprContext):
        #multiplicateExpr: unaryLogicExpr ((IMUL|IDIV|FMUL|FDIV|MOD) unaryLogicExpr)*;
        expr = self.visit(ctx.unaryLogicExpr()[0])
        for i in range(len(ctx.unaryLogicExpr()) - 1):
            expr = BinaryOp(ctx.getChild(i * 2 + 1).getText(), expr, self.visit(ctx.unaryLogicExpr(i + 1)))
        return expr

    def visitUnaryLogicExpr(self, ctx:CSELParser.UnaryLogicExprContext):
        #unaryLogicExpr: NOT* unarySignExpr;
        expr = self.visit(ctx.unarySignExpr())
        for i in range(len(ctx.NOT())):
            expr = UnaryOp(ctx.NOT(i).getText(), expr)
        return expr

    def visitUnarySignExpr(self, ctx:CSELParser.UnarySignExprContext):
        #unarySignExpr: (ISUB|FSUB)* indexExpr;
        expr = self.visit(ctx.indexExpr())
        for i in list(range(ctx.getChildCount() - 1))[-1::-1]:
            expr = UnaryOp(ctx.getChild(i).getText(), expr)
        return expr
    
    def visitIndexExpr(self, ctx: CSELParser.IndexExprContext):
        #indexExpr: ID (LQP expr (CM expr)* RQP)* | finalExpr;
        if ctx.getChildCount()==1:
            return self.visit(ctx.finalExpr())
        else:
            return ArrayCell(Id(ctx.ID().getText()), [self.visit(e) for e in ctx.expr()])

    def visitFinalExpr(self, ctx: CSELParser.FinalExprContext):
        #finalExpr: NUMLIT| TRUE | FALSE | STRINGLIT | funcall | LP expr RP;
        #funcall: CALL LP callList RP;
        #callList: ID CM LQP ((expr CM)* expr)? RQP;
        if ctx.TRUE() or ctx.FALSE():
            return BooleanLiteral(True if ctx.TRUE() else False)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.NUMLIT():
            return NumberLiteral(ctx.NUMLIT().getText())        
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.funcall():
            return CallExpr(Id(ctx.funcall().callList().ID().getText()), [self.visit(e) for e in ctx.funcall().callList().expr()])
        else:
            return self.visit(ctx.expr())