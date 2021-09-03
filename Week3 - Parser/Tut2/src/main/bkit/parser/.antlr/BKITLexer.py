# Generated from d:\Python\Principles of Programming Languages\Tmp\Trainning\Week3 - Parser\Tut2\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u00a3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\13\7\13\\\n\13\f\13\16\13_\13\13\3\f")
        buf.write("\3\f\3\f\7\fd\n\f\f\f\16\fg\13\f\5\fi\n\f\3\r\3\r\3\r")
        buf.write("\6\rn\n\r\r\r\16\ro\5\rr\n\r\3\r\3\r\5\rv\n\r\3\r\6\r")
        buf.write("y\n\r\r\r\16\rz\5\r}\n\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\6\31\u0096\n\31\r\31\16")
        buf.write("\31\u0097\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\2\2\36\3\3\5\4\7\5\t\2\13\2\r\2\17\2\21\2\23\2\25")
        buf.write("\6\27\7\31\b\33\t\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22")
        buf.write("/\23\61\24\63\25\65\26\67\279\30\3\2\t\5\2C\\aac|\3\2")
        buf.write("\62;\3\2\63;\3\2\60\60\4\2GGgg\4\2--//\5\2\13\f\17\17")
        buf.write("\"\"\2\u00a6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\3;\3\2\2\2\5A\3\2\2\2\7E\3\2\2\2\tL\3\2\2\2")
        buf.write("\13N\3\2\2\2\rP\3\2\2\2\17R\3\2\2\2\21T\3\2\2\2\23V\3")
        buf.write("\2\2\2\25X\3\2\2\2\27h\3\2\2\2\31j\3\2\2\2\33~\3\2\2\2")
        buf.write("\35\u0080\3\2\2\2\37\u0082\3\2\2\2!\u0084\3\2\2\2#\u0086")
        buf.write("\3\2\2\2%\u0088\3\2\2\2\'\u008a\3\2\2\2)\u008c\3\2\2\2")
        buf.write("+\u008e\3\2\2\2-\u0090\3\2\2\2/\u0092\3\2\2\2\61\u0095")
        buf.write("\3\2\2\2\63\u009b\3\2\2\2\65\u009d\3\2\2\2\67\u009f\3")
        buf.write("\2\2\29\u00a1\3\2\2\2;<\7h\2\2<=\7n\2\2=>\7q\2\2>?\7c")
        buf.write("\2\2?@\7v\2\2@\4\3\2\2\2AB\7k\2\2BC\7p\2\2CD\7v\2\2D\6")
        buf.write("\3\2\2\2EF\7t\2\2FG\7g\2\2GH\7v\2\2HI\7w\2\2IJ\7t\2\2")
        buf.write("JK\7p\2\2K\b\3\2\2\2LM\t\2\2\2M\n\3\2\2\2NO\t\3\2\2O\f")
        buf.write("\3\2\2\2PQ\7/\2\2Q\16\3\2\2\2RS\7\60\2\2S\20\3\2\2\2T")
        buf.write("U\t\4\2\2U\22\3\2\2\2VW\7)\2\2W\24\3\2\2\2X]\5\t\5\2Y")
        buf.write("\\\5\t\5\2Z\\\5\13\6\2[Y\3\2\2\2[Z\3\2\2\2\\_\3\2\2\2")
        buf.write("][\3\2\2\2]^\3\2\2\2^\26\3\2\2\2_]\3\2\2\2`i\7\62\2\2")
        buf.write("ae\5\21\t\2bd\5\13\6\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2e")
        buf.write("f\3\2\2\2fi\3\2\2\2ge\3\2\2\2h`\3\2\2\2ha\3\2\2\2i\30")
        buf.write("\3\2\2\2jq\5\27\f\2km\t\5\2\2ln\t\3\2\2ml\3\2\2\2no\3")
        buf.write("\2\2\2om\3\2\2\2op\3\2\2\2pr\3\2\2\2qk\3\2\2\2qr\3\2\2")
        buf.write("\2r|\3\2\2\2su\t\6\2\2tv\t\7\2\2ut\3\2\2\2uv\3\2\2\2v")
        buf.write("x\3\2\2\2wy\t\3\2\2xw\3\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3")
        buf.write("\2\2\2{}\3\2\2\2|s\3\2\2\2|}\3\2\2\2}\32\3\2\2\2~\177")
        buf.write("\7}\2\2\177\34\3\2\2\2\u0080\u0081\7\177\2\2\u0081\36")
        buf.write("\3\2\2\2\u0082\u0083\7=\2\2\u0083 \3\2\2\2\u0084\u0085")
        buf.write("\7.\2\2\u0085\"\3\2\2\2\u0086\u0087\7?\2\2\u0087$\3\2")
        buf.write("\2\2\u0088\u0089\7*\2\2\u0089&\3\2\2\2\u008a\u008b\7+")
        buf.write("\2\2\u008b(\3\2\2\2\u008c\u008d\7-\2\2\u008d*\3\2\2\2")
        buf.write("\u008e\u008f\7/\2\2\u008f,\3\2\2\2\u0090\u0091\7,\2\2")
        buf.write("\u0091.\3\2\2\2\u0092\u0093\7\61\2\2\u0093\60\3\2\2\2")
        buf.write("\u0094\u0096\t\b\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\b\31\2\2\u009a\62\3\2\2\2\u009b\u009c")
        buf.write("\13\2\2\2\u009c\64\3\2\2\2\u009d\u009e\13\2\2\2\u009e")
        buf.write("\66\3\2\2\2\u009f\u00a0\13\2\2\2\u00a08\3\2\2\2\u00a1")
        buf.write("\u00a2\13\2\2\2\u00a2:\3\2\2\2\r\2[]ehoquz|\u0097\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    FLOAT = 1
    INT = 2
    RETURN = 3
    ID = 4
    INTLIT = 5
    FLOATLIT = 6
    LB = 7
    RB = 8
    SM = 9
    CM = 10
    EQ = 11
    LP = 12
    RP = 13
    ADD = 14
    SUB = 15
    MUL = 16
    DIV = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21
    UNTERMINATED_COMMENT = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'float'", "'int'", "'return'", "'{'", "'}'", "';'", "','", 
            "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "FLOAT", "INT", "RETURN", "ID", "INTLIT", "FLOATLIT", "LB", 
            "RB", "SM", "CM", "EQ", "LP", "RP", "ADD", "SUB", "MUL", "DIV", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "FLOAT", "INT", "RETURN", "NonDigit", "Digit", "Sign", 
                  "Dot", "NonZero", "Quote", "ID", "INTLIT", "FLOATLIT", 
                  "LB", "RB", "SM", "CM", "EQ", "LP", "RP", "ADD", "SUB", 
                  "MUL", "DIV", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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


