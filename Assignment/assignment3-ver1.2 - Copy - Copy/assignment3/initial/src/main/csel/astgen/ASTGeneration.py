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
            return [VarDecl(Id(variable.var().ID().getText()),  self.visit(variable.var().varlist()) if variable.var().varlist() else None, self.visit(variable.typ()) if variable.typ() else NoneType(), self.visit(variable.vartail()) if variable.vartail() else None) for variable in ctx.variable()]
        elif ctx.CONSTANT():
            return [ConstDecl(Id(variable.var().ID().getText()), self.visit(variable.var().varlist()) if variable.var().varlist() else None, self.visit(variable.typ()) if variable.typ() else NoneType(), self.visit(variable.vartail()) if variable.vartail() else None) for variable in ctx.variable()]

    def visitVarlist(self, ctx: CSELParser.VarlistContext):
        # varlist: NUMLIT CM varlist | NUMLIT;
        if ctx.getChildCount() == 1:
            return [NumberLiteral(float(ctx.NUMLIT().getText()))]
        else:
            return [NumberLiteral(float(ctx.NUMLIT().getText()))] + self.visit(ctx.varlist())

    def visitTyp(self, ctx: CSELParser.TypContext):
        #typ: 'Number'|'String'|'Boolean'|'Array'|'JSON';
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()
        elif ctx.JSON():
            return JSONType()
        elif ctx.ARRAY():
            return ArrayType()

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
            return NumberLiteral(float(ctx.NUMLIT().getText()))
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
        # return JSONLiteral([self.visit(lit) for lit in ctx.ID().getText()+ctx.literal()])
        # return +ctx.literal()]
        list1 = [Id(i.getText()) for i in ctx.ID()]
        list2 = [self.visit(lit) for lit in ctx.literal()]
        x = []
        x = list(zip(list1, list2))
        return JSONLiteral(x)

    def visitFuncDecl(self, ctx: CSELParser.FuncDeclContext):
        # funcDecl: FUNCTION ID LP paraList? RP LB body RB;
        return [FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paraList()) if ctx.paraList() else [], self.visit(ctx.body()))]

    def visitParaList(self, ctx: CSELParser.ParaListContext):
        # paraList: param (CM param)*;
        # param: ID (LQP varlist? RQP)?;
        # varlist: NUMLIT CM varlist | NUMLIT;
        return [VarDecl(Id(param.ID().getText()), self.visit(param.varlist()) if param.varlist() else [], NoneType(), None) for param in ctx.param()]

    def visitBody(self, ctx: CSELParser.BodyContext):
        #body: stmtList;
        return self.visit(ctx.stmtList())

    def visitStmtList(self, ctx: CSELParser.StmtListContext):
        # stmtList: manyStmt*;
        liststmt = ctx.manyStmt()
        res = []
        for stmt in liststmt:
            res += [self.visit(stmt)]
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
        # assignStmt: ID (LQP arrList RQP)? ASSIGN expr SM|ID jsonList? ASSIGN expr SM;
        # arrList: expr|expr CM arrList;
        # jsonList: LB expr RB | LB expr RB jsonList;
        # return Assign(Id(ctx.ID().getText()) if len(ctx.expr()) == 1 else ArrayAccess(Id(ctx.ID().getText()), [self.visit(e) for e in ctx.expr()[:-1]]), self.visit(ctx.expr()[-1]))
        if not ctx.arrList() and not ctx.jsonList():
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.expr()))
        elif ctx.arrList():
            return Assign(ArrayAccess(Id(ctx.ID().getText()), self.visit(ctx.arrList())), self.visit(ctx.expr()))
        elif ctx.jsonList():
            return Assign(JSONAccess(Id(ctx.ID().getText()), self.visit(ctx.jsonList())), self.visit(ctx.expr()))

    def visitArrList(self, ctx: CSELParser.ArrListContext):
        # arrList: expr|expr CM arrList;
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.arrList())

    def visitJsonList(self, ctx: CSELParser.JsonListContext):
        # jsonList: LB expr RB | LB expr RB jsonList;
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.jsonList())

    def visitIfStmt(self, ctx: CSELParser.IfStmtContext):
        # ifStmt: IF LP expr RP LB stmtList RB (ELIF LP expr RP LB stmtList RB)* (ELSE LB stmtList RB)?;
        if not ctx.ELSE():
            return If([[self.visit(ctx.expr(i)), self.visit(ctx.stmtList(i))] for i in range(len(ctx.expr()))], [])
        else:
            return If([[self.visit(ctx.expr(i)), self.visit(ctx.stmtList(i))] for i in range(len(ctx.expr()))], self.visit(ctx.stmtList(len(ctx.stmtList())-1)))

    def visitForStmt(self, ctx: CSELParser.ForStmtContext):
        #forStmt: forIn|forOf;
        if ctx.forIn():
            return self.visit(ctx.forIn())
        else:
            return self.visit(ctx.forOf())

    def visitForIn(self,ctx:CSELParser.ForInContext):
        #forIn: FOR ID IN arrayLiteral LB stmtList RB | FOR ID IN expr LB stmtList RB;
        if ctx.arrayLiteral():
            return ForIn(Id(ctx.ID().getText()), self.visit(ctx.arrayLiteral()), self.visit(ctx.stmtList()))
        else:
            return ForIn(Id(ctx.ID().getText()), self.visit(ctx.expr()), self.visit(ctx.stmtList()))

    def visitForOf(self,ctx:CSELParser.ForOfContext):
        #forOf: FOR ID OF jsonLiteral LB stmtList RB  | FOR ID OF expr LB stmtList RB;
        if ctx.jsonLiteral():
            return ForOf(Id(ctx.ID().getText()), self.visit(ctx.jsonLiteral()), self.visit(ctx.stmtList()))
        else:
            return ForOf(Id(ctx.ID().getText()), self.visit(ctx.expr()), self.visit(ctx.stmtList()))

    def visitWhileStmt(self, ctx: CSELParser.WhileStmtContext):
        # whileStmt: WHILE LP expr RP LB stmtList RB;
        return While(self.visit(ctx.expr()), self.visit(ctx.stmtList()))

    def visitBreakStmt(self, ctx: CSELParser.BreakStmtContext):
        # breakStmt: BREAK SM;
        return Break()

    def visitContinueStmt(self, ctx: CSELParser.ContinueStmtContext):
        # continueStmt: CONTINUE SM;
        return Continue()

    def visitReturnStmt(self, ctx: CSELParser.ReturnStmtContext):
        # returnStmt: RETURN expr? SM;
        return Return(self.visit(ctx.expr()) if ctx.expr() else None)

    def visitCallStmt(self, ctx: CSELParser.CallStmtContext):
        # callStmt: funcall SM;
        # funcall: CALL LP callList RP;
        # callList: ID CM LQP ((expr CM)* expr)? RQP;
        return CallStmt(Id(ctx.funcall().callList().ID().getText()), [self.visit(e) for e in ctx.funcall().callList().expr()])

    def visitExpr(self, ctx: CSELParser.ExprContext):
        # expr: stringExpr| stringExpr (SADD|SEQ) stringExpr;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stringExpr(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.stringExpr(0)), self.visit(ctx.stringExpr(1)))

    def visitStringExpr(self, ctx: CSELParser.StringExprContext):
        # stringExpr: logicExpr | logicExpr (EQ|NEQ|GT|GTE|LT|LTE) logicExpr;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicExpr(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.logicExpr(0)), self.visit(ctx.logicExpr(1)))

    def visitLogicExpr(self, ctx: CSELParser.LogicExprContext):
        # logicExpr: logicExpr (AND|OR) additiveExpr | additiveExpr;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.additiveExpr())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.logicExpr()), self.visit(ctx.additiveExpr()))

    def visitAdditiveExpr(self, ctx: CSELParser.AdditiveExprContext):
        # additiveExpr: additiveExpr (ADD|SUB) multiplicateExpr| multiplicateExpr;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiplicateExpr())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.additiveExpr()), self.visit(ctx.multiplicateExpr()))

    def visitMultiplicateExpr(self, ctx: CSELParser.MultiplicateExprContext):
        # multiplicateExpr: multiplicateExpr (MUL|DIV|MOD) unaryLogicExpr| unaryLogicExpr;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryLogicExpr())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.multiplicateExpr()), self.visit(ctx.unaryLogicExpr()))

    def visitUnaryLogicExpr(self, ctx: CSELParser.UnaryLogicExprContext):
        # unaryLogicExpr: NOT unaryLogicExpr | unarySignExpr;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unarySignExpr())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.unaryLogicExpr()))

    def visitUnarySignExpr(self, ctx: CSELParser.UnarySignExprContext):
        # unarySignExpr: SUB unarySignExpr | keyExpr | indexExpr;
        if ctx.keyExpr():
            return self.visit(ctx.keyExpr())
        elif ctx.indexExpr():
            return self.visit(ctx.indexExpr())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.unarySignExpr()))

    def visitIndexExpr(self, ctx: CSELParser.IndexExprContext):
        # indexExpr: indexExpr LQP indexOperator RQP | finalExpr;
        # indexOperator: expr| expr CM indexOperator;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.finalExpr())
        else:
            return ArrayAccess(self.visit(ctx.indexExpr()), self.visit(ctx.indexOperator()))

    def visitIndexOperator(self, ctx: CSELParser.IndexOperatorContext):

        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.indexOperator())

    def visitKeyExpr(self, ctx: CSELParser.KeyExprContext):
        # keyExpr: keyExpr keyOperator |finalExpr;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.finalExpr())
        else:
            return JSONAccess(self.visit(ctx.keyExpr()), self.visit(ctx.keyOperator()))

    def visitKeyOperator(self, ctx: CSELParser.KeyOperatorContext):
        # keyOperator: LB expr RB | LB expr RB keyOperator;
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())]+self.visit(ctx.keyOperator())

    def visitFinalExpr(self, ctx: CSELParser.FinalExprContext):
        # finalExpr: NUMLIT| TRUE | FALSE | STRINGLIT | funcall | LP expr RP | ID;
        # funcall: CALL LP callList RP;
        # callList: ID CM LQP ((expr CM)* expr)? RQP;
        if ctx.TRUE() or ctx.FALSE():
            return BooleanLiteral(True if ctx.TRUE() else False)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.NUMLIT():
            return NumberLiteral(float(ctx.NUMLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.funcall():
            return CallExpr(Id(ctx.funcall().callList().ID().getText()), [self.visit(e) for e in ctx.funcall().callList().expr()])
        else:
            return self.visit(ctx.expr())
