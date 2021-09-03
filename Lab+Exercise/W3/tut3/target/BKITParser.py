# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("\u009f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\7\2(\n\2\f\2\16\2+\13\2\3\2\3\2\3\3\3\3\5\3\61\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5;\n\5\3\6\3\6\3")
        buf.write("\6\3\6\7\6A\n\6\f\6\16\6D\13\6\3\6\3\6\3\6\7\6I\n\6\f")
        buf.write("\6\16\6L\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7U\n\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\5\t^\n\t\3\n\3\n\3\n\5\nc\n\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\5\rs\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17}\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u0084\n\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u008f")
        buf.write("\n\21\f\21\16\21\u0092\13\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u009b\n\22\3\23\3\23\3\23\2\3 \24\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\4\3\2\17\20")
        buf.write("\3\2\22\23\2\u009d\2)\3\2\2\2\4\60\3\2\2\2\6\62\3\2\2")
        buf.write("\2\b:\3\2\2\2\n<\3\2\2\2\fT\3\2\2\2\16V\3\2\2\2\20]\3")
        buf.write("\2\2\2\22b\3\2\2\2\24d\3\2\2\2\26h\3\2\2\2\30r\3\2\2\2")
        buf.write("\32t\3\2\2\2\34|\3\2\2\2\36\u0083\3\2\2\2 \u0085\3\2\2")
        buf.write("\2\"\u009a\3\2\2\2$\u009c\3\2\2\2&(\5\4\3\2\'&\3\2\2\2")
        buf.write("(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2\2+)\3\2\2\2,-")
        buf.write("\7\2\2\3-\3\3\2\2\2.\61\5\6\4\2/\61\5\n\6\2\60.\3\2\2")
        buf.write("\2\60/\3\2\2\2\61\5\3\2\2\2\62\63\t\2\2\2\63\64\5\b\5")
        buf.write("\2\64\65\7\16\2\2\65\7\3\2\2\2\66\67\7\21\2\2\678\7\r")
        buf.write("\2\28;\5\b\5\29;\7\21\2\2:\66\3\2\2\2:9\3\2\2\2;\t\3\2")
        buf.write("\2\2<=\t\2\2\2=>\7\21\2\2>B\7\t\2\2?A\5\f\7\2@?\3\2\2")
        buf.write("\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CE\3\2\2\2DB\3\2\2\2E")
        buf.write("F\7\n\2\2FJ\7\13\2\2GI\5\20\t\2HG\3\2\2\2IL\3\2\2\2JH")
        buf.write("\3\2\2\2JK\3\2\2\2KM\3\2\2\2LJ\3\2\2\2MN\7\f\2\2N\13\3")
        buf.write("\2\2\2OP\5\16\b\2PQ\7\16\2\2QR\5\f\7\2RU\3\2\2\2SU\5\16")
        buf.write("\b\2TO\3\2\2\2TS\3\2\2\2U\r\3\2\2\2VW\t\2\2\2WX\5\b\5")
        buf.write("\2X\17\3\2\2\2Y^\5\6\4\2Z[\5\22\n\2[\\\7\16\2\2\\^\3\2")
        buf.write("\2\2]Y\3\2\2\2]Z\3\2\2\2^\21\3\2\2\2_c\5\24\13\2`c\5\26")
        buf.write("\f\2ac\5\32\16\2b_\3\2\2\2b`\3\2\2\2ba\3\2\2\2c\23\3\2")
        buf.write("\2\2de\7\21\2\2ef\7\b\2\2fg\5\34\17\2g\25\3\2\2\2hi\7")
        buf.write("\21\2\2ij\7\t\2\2jk\5\30\r\2kl\7\n\2\2l\27\3\2\2\2mn\5")
        buf.write("\34\17\2no\7\r\2\2op\5\30\r\2ps\3\2\2\2qs\5\34\17\2rm")
        buf.write("\3\2\2\2rq\3\2\2\2s\31\3\2\2\2tu\7\7\2\2uv\5\34\17\2v")
        buf.write("\33\3\2\2\2wx\5\36\20\2xy\7\5\2\2yz\5\34\17\2z}\3\2\2")
        buf.write("\2{}\5\36\20\2|w\3\2\2\2|{\3\2\2\2}\35\3\2\2\2~\177\5")
        buf.write(" \21\2\177\u0080\7\6\2\2\u0080\u0081\5 \21\2\u0081\u0084")
        buf.write("\3\2\2\2\u0082\u0084\5 \21\2\u0083~\3\2\2\2\u0083\u0082")
        buf.write("\3\2\2\2\u0084\37\3\2\2\2\u0085\u0086\b\21\1\2\u0086\u0087")
        buf.write("\5\"\22\2\u0087\u0090\3\2\2\2\u0088\u0089\f\5\2\2\u0089")
        buf.write("\u008a\7\3\2\2\u008a\u008f\5\"\22\2\u008b\u008c\f\4\2")
        buf.write("\2\u008c\u008d\7\4\2\2\u008d\u008f\5\"\22\2\u008e\u0088")
        buf.write("\3\2\2\2\u008e\u008b\3\2\2\2\u008f\u0092\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091!\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0093\u0094\7\t\2\2\u0094\u0095\5\34\17")
        buf.write("\2\u0095\u0096\7\n\2\2\u0096\u009b\3\2\2\2\u0097\u009b")
        buf.write("\5$\23\2\u0098\u009b\7\21\2\2\u0099\u009b\5\26\f\2\u009a")
        buf.write("\u0093\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u0099\3\2\2\2\u009b#\3\2\2\2\u009c\u009d\t\3\2")
        buf.write("\2\u009d%\3\2\2\2\20)\60:BJT]br|\u0083\u008e\u0090\u009a")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'return'", 
                     "'='", "'('", "')'", "'{'", "'}'", "','", "';'", "'int'", 
                     "'float'" ]

    symbolicNames = [ "<INVALID>", "MUL", "DIV", "ADD", "SUB", "RETURN", 
                      "EQUAL", "LP", "RP", "LB", "RB", "COMMA", "SEMI", 
                      "INT", "FLOAT", "ID", "INTLIT", "FLOATLIT", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_manydecl = 1
    RULE_vardecl = 2
    RULE_idlist = 3
    RULE_funcdecl = 4
    RULE_paramlist = 5
    RULE_param = 6
    RULE_body = 7
    RULE_stmt = 8
    RULE_assignstmt = 9
    RULE_callstmt = 10
    RULE_explist = 11
    RULE_returnstmt = 12
    RULE_exp = 13
    RULE_exp1 = 14
    RULE_exp2 = 15
    RULE_exp3 = 16
    RULE_literal = 17

    ruleNames =  [ "program", "manydecl", "vardecl", "idlist", "funcdecl", 
                   "paramlist", "param", "body", "stmt", "assignstmt", "callstmt", 
                   "explist", "returnstmt", "exp", "exp1", "exp2", "exp3", 
                   "literal" ]

    EOF = Token.EOF
    MUL=1
    DIV=2
    ADD=3
    SUB=4
    RETURN=5
    EQUAL=6
    LP=7
    RP=8
    LB=9
    RB=10
    COMMA=11
    SEMI=12
    INT=13
    FLOAT=14
    ID=15
    INTLIT=16
    FLOATLIT=17
    WS=18
    ERROR_CHAR=19
    UNCLOSE_STRING=20
    ILLEGAL_ESCAPE=21
    UNTERMINATED_COMMENT=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def manydecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ManydeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.ManydeclContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.INT or _la==BKITParser.FLOAT:
                self.state = 36
                self.manydecl()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManydeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKITParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKITParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_manydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManydecl" ):
                return visitor.visitManydecl(self)
            else:
                return visitor.visitChildren(self)




    def manydecl(self):

        localctx = BKITParser.ManydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydecl)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKITParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKITParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 49
            self.idlist()
            self.state = 50
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKITParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKITParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idlist)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(BKITParser.ID)
                self.state = 53
                self.match(BKITParser.COMMA)
                self.state = 54
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(BKITParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def paramlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ParamlistContext)
            else:
                return self.getTypedRuleContext(BKITParser.ParamlistContext,i)


        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.BodyContext)
            else:
                return self.getTypedRuleContext(BKITParser.BodyContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = BKITParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 59
            self.match(BKITParser.ID)
            self.state = 60
            self.match(BKITParser.LP)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.INT or _la==BKITParser.FLOAT:
                self.state = 61
                self.paramlist()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(BKITParser.RP)
            self.state = 68
            self.match(BKITParser.LB)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.RETURN) | (1 << BKITParser.INT) | (1 << BKITParser.FLOAT) | (1 << BKITParser.ID))) != 0):
                self.state = 69
                self.body()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKITParser.ParamContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKITParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKITParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramlist)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.param()
                self.state = 78
                self.match(BKITParser.SEMI)
                self.state = 79
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(BKITParser.IdlistContext,0)


        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKITParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 85
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKITParser.VardeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(BKITParser.StmtContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_body)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INT, BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.vardecl()
                pass
            elif token in [BKITParser.RETURN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.stmt()
                self.state = 89
                self.match(BKITParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(BKITParser.AssignstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(BKITParser.CallstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(BKITParser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_stmt)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.callstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.returnstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = BKITParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(BKITParser.ID)
            self.state = 99
            self.match(BKITParser.EQUAL)
            self.state = 100
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def explist(self):
            return self.getTypedRuleContext(BKITParser.ExplistContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = BKITParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BKITParser.ID)
            self.state = 103
            self.match(BKITParser.LP)
            self.state = 104
            self.explist()
            self.state = 105
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def explist(self):
            return self.getTypedRuleContext(BKITParser.ExplistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = BKITParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_explist)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.exp()
                self.state = 108
                self.match(BKITParser.COMMA)
                self.state = 109
                self.explist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = BKITParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(BKITParser.RETURN)
            self.state = 115
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.exp1()
                self.state = 118
                self.match(BKITParser.ADD)
                self.state = 119
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp2Context,i)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKITParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp1)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.exp2(0)
                self.state = 125
                self.match(BKITParser.SUB)
                self.state = 126
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 140
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 134
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 135
                        self.match(BKITParser.MUL)
                        self.state = 136
                        self.exp3()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 137
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 138
                        self.match(BKITParser.DIV)
                        self.state = 139
                        self.exp3()
                        pass

             
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def callstmt(self):
            return self.getTypedRuleContext(BKITParser.CallstmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = BKITParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp3)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(BKITParser.LP)
                self.state = 146
                self.exp()
                self.state = 147
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(BKITParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 151
                self.callstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not(_la==BKITParser.INTLIT or _la==BKITParser.FLOATLIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.exp2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




