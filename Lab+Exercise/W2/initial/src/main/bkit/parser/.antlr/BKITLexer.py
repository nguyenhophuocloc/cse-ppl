# Generated from d:\Python\Principles of Programming Languages v2\initial\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("g\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\5\5#\n\5\3\5\6\5&\n\5\r\5\16")
        buf.write("\5\'\3\5\5\5+\n\5\3\5\6\5.\n\5\r\5\16\5/\3\5\3\5\3\5\6")
        buf.write("\5\65\n\5\r\5\16\5\66\5\59\n\5\3\5\5\5<\n\5\3\5\3\5\3")
        buf.write("\5\5\5A\n\5\3\5\6\5D\n\5\r\5\16\5E\5\5H\n\5\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\7\bR\n\b\f\b\16\bU\13\b\3\b\3\b")
        buf.write("\3\t\6\tZ\n\t\r\t\16\t[\3\t\3\t\3\n\3\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\2\2\16\3\2\5\2\7\2\t\3\13\2\r\2\17\4\21\5")
        buf.write("\23\6\25\7\27\b\31\t\3\2\7\3\2//\3\2\62;\5\2GGgg~~\3\2")
        buf.write("))\5\2\13\f\17\17\"\"\2n\2\t\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\tG\3\2\2")
        buf.write("\2\13I\3\2\2\2\rK\3\2\2\2\17N\3\2\2\2\21Y\3\2\2\2\23_")
        buf.write("\3\2\2\2\25a\3\2\2\2\27c\3\2\2\2\31e\3\2\2\2\33\34\t\2")
        buf.write("\2\2\34\4\3\2\2\2\35\36\t\3\2\2\36\6\3\2\2\2\37 \7\60")
        buf.write("\2\2 \b\3\2\2\2!#\5\3\2\2\"!\3\2\2\2\"#\3\2\2\2#%\3\2")
        buf.write("\2\2$&\5\5\3\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2")
        buf.write("\2\2(*\3\2\2\2)+\5\7\4\2*)\3\2\2\2*+\3\2\2\2+-\3\2\2\2")
        buf.write(",.\5\5\3\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write("8\3\2\2\2\61\62\t\4\2\2\62\64\5\3\2\2\63\65\5\5\3\2\64")
        buf.write("\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2")
        buf.write("\679\3\2\2\28\61\3\2\2\289\3\2\2\29H\3\2\2\2:<\5\3\2\2")
        buf.write(";:\3\2\2\2;<\3\2\2\2<=\3\2\2\2=>\5\5\3\2>@\t\4\2\2?A\5")
        buf.write("\3\2\2@?\3\2\2\2@A\3\2\2\2AC\3\2\2\2BD\5\5\3\2CB\3\2\2")
        buf.write("\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2G\"\3\2\2\2")
        buf.write("G;\3\2\2\2H\n\3\2\2\2IJ\7)\2\2J\f\3\2\2\2KL\7)\2\2LM\7")
        buf.write(")\2\2M\16\3\2\2\2NS\5\13\6\2OR\n\5\2\2PR\5\r\7\2QO\3\2")
        buf.write("\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2")
        buf.write("US\3\2\2\2VW\5\13\6\2W\20\3\2\2\2XZ\t\6\2\2YX\3\2\2\2")
        buf.write("Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\b\t\2\2^")
        buf.write("\22\3\2\2\2_`\13\2\2\2`\24\3\2\2\2ab\13\2\2\2b\26\3\2")
        buf.write("\2\2cd\13\2\2\2d\30\3\2\2\2ef\13\2\2\2f\32\3\2\2\2\20")
        buf.write("\2\"\'*/\668;@EGQS[\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    REAL = 1
    STRLIT = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6
    UNTERMINATED_COMMENT = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "REAL", "STRLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "SIGN", "DIGIT", "POINT", "REAL", "Quote", "DoubleQuote", 
                  "STRLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

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


