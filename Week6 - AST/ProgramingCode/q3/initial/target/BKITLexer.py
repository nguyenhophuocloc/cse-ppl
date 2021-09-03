# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\6\6\'\n\6\r\6")
        buf.write("\16\6(\3\7\6\7,\n\7\r\7\16\7-\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\3\2\4\3\2c|\5\2\13\f\17\17\"\"\2:\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3\2\2\2\7\33\3\2\2\2")
        buf.write("\t\37\3\2\2\2\13&\3\2\2\2\r+\3\2\2\2\17\61\3\2\2\2\21")
        buf.write("\63\3\2\2\2\23\65\3\2\2\2\25\67\3\2\2\2\27\30\7=\2\2\30")
        buf.write("\4\3\2\2\2\31\32\7.\2\2\32\6\3\2\2\2\33\34\7k\2\2\34\35")
        buf.write("\7p\2\2\35\36\7v\2\2\36\b\3\2\2\2\37 \7h\2\2 !\7n\2\2")
        buf.write("!\"\7q\2\2\"#\7c\2\2#$\7v\2\2$\n\3\2\2\2%\'\t\2\2\2&%")
        buf.write("\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)\f\3\2\2\2*,\t")
        buf.write("\3\2\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2./\3\2\2")
        buf.write("\2/\60\b\7\2\2\60\16\3\2\2\2\61\62\13\2\2\2\62\20\3\2")
        buf.write("\2\2\63\64\13\2\2\2\64\22\3\2\2\2\65\66\13\2\2\2\66\24")
        buf.write("\3\2\2\2\678\13\2\2\28\26\3\2\2\2\5\2(-\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTTYPE = 3
    FLOATTYPE = 4
    ID = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9
    UNTERMINATED_COMMENT = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "FLOATTYPE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "INTTYPE", "FLOATTYPE", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
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


