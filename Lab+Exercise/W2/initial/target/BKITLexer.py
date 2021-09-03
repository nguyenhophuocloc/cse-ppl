# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("\61\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\7\4")
        buf.write("\34\n\4\f\4\16\4\37\13\4\3\4\3\4\3\5\6\5$\n\5\r\5\16\5")
        buf.write("%\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\2\2\n\3\2\5")
        buf.write("\2\7\3\t\4\13\5\r\6\17\7\21\b\3\2\4\3\2))\5\2\13\f\17")
        buf.write("\17\"\"\2\61\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\25\3")
        buf.write("\2\2\2\7\30\3\2\2\2\t#\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2")
        buf.write("\17-\3\2\2\2\21/\3\2\2\2\23\24\7)\2\2\24\4\3\2\2\2\25")
        buf.write("\26\7)\2\2\26\27\7)\2\2\27\6\3\2\2\2\30\35\5\3\2\2\31")
        buf.write("\34\n\2\2\2\32\34\5\5\3\2\33\31\3\2\2\2\33\32\3\2\2\2")
        buf.write("\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2")
        buf.write("\37\35\3\2\2\2 !\5\3\2\2!\b\3\2\2\2\"$\t\3\2\2#\"\3\2")
        buf.write("\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\b\5\2")
        buf.write("\2(\n\3\2\2\2)*\13\2\2\2*\f\3\2\2\2+,\13\2\2\2,\16\3\2")
        buf.write("\2\2-.\13\2\2\2.\20\3\2\2\2/\60\13\2\2\2\60\22\3\2\2\2")
        buf.write("\6\2\33\35%\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRLIT = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5
    UNTERMINATED_COMMENT = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "STRLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Quote", "DoubleQuote", "STRLIT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


