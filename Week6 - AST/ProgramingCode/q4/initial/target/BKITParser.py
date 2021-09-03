# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\62\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\5\3\25\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\34\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5$\n\5\f\5\16\5")
        buf.write("\'\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\60\n\6\3\6\2\3")
        buf.write("\b\7\2\4\6\b\n\2\2\2\62\2\f\3\2\2\2\4\24\3\2\2\2\6\33")
        buf.write("\3\2\2\2\b\35\3\2\2\2\n/\3\2\2\2\f\r\5\4\3\2\r\16\7\2")
        buf.write("\2\3\16\3\3\2\2\2\17\20\5\6\4\2\20\21\7\b\2\2\21\22\5")
        buf.write("\4\3\2\22\25\3\2\2\2\23\25\5\6\4\2\24\17\3\2\2\2\24\23")
        buf.write("\3\2\2\2\25\5\3\2\2\2\26\27\5\b\5\2\27\30\7\t\2\2\30\31")
        buf.write("\5\b\5\2\31\34\3\2\2\2\32\34\5\b\5\2\33\26\3\2\2\2\33")
        buf.write("\32\3\2\2\2\34\7\3\2\2\2\35\36\b\5\1\2\36\37\5\n\6\2\37")
        buf.write("%\3\2\2\2 !\f\4\2\2!\"\7\7\2\2\"$\5\n\6\2# \3\2\2\2$\'")
        buf.write("\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\t\3\2\2\2\'%\3\2\2\2(\60")
        buf.write("\7\n\2\2)\60\7\5\2\2*\60\7\6\2\2+,\7\3\2\2,-\5\4\3\2-")
        buf.write(".\7\4\2\2.\60\3\2\2\2/(\3\2\2\2/)\3\2\2\2/*\3\2\2\2/+")
        buf.write("\3\2\2\2\60\13\3\2\2\2\6\24\33%/")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "INTLIT", "BOOLIT", 
                      "ANDOR", "ASSIGN", "COMPARE", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_operand = 4

    ruleNames =  [ "program", "exp", "term", "factor", "operand" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    INTLIT=3
    BOOLIT=4
    ANDOR=5
    ASSIGN=6
    COMPARE=7
    ID=8
    WS=9
    ERROR_CHAR=10
    UNCLOSE_STRING=11
    ILLEGAL_ESCAPE=12
    UNTERMINATED_COMMENT=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.exp()
            self.state = 11
            self.match(BKITParser.EOF)
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

        def term(self):
            return self.getTypedRuleContext(BKITParser.TermContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

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
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.term()
                self.state = 14
                self.match(BKITParser.ASSIGN)
                self.state = 15
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.FactorContext)
            else:
                return self.getTypedRuleContext(BKITParser.FactorContext,i)


        def COMPARE(self):
            return self.getToken(BKITParser.COMPARE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BKITParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.factor(0)
                self.state = 21
                self.match(BKITParser.COMPARE)
                self.state = 22
                self.factor(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.factor(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def factor(self):
            return self.getTypedRuleContext(BKITParser.FactorContext,0)


        def ANDOR(self):
            return self.getToken(BKITParser.ANDOR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_factor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.operand()
            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.FactorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                    self.state = 30
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 31
                    self.match(BKITParser.ANDOR)
                    self.state = 32
                    self.operand() 
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def BOOLIT(self):
            return self.getToken(BKITParser.BOOLIT, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operand)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(BKITParser.ID)
                pass
            elif token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.BOOLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(BKITParser.BOOLIT)
                pass
            elif token in [BKITParser.T__0]:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.match(BKITParser.T__0)
                self.state = 42
                self.exp()
                self.state = 43
                self.match(BKITParser.T__1)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.factor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




