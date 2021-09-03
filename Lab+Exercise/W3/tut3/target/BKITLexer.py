# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("~\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\6\20\\\n\20\r\20\16\20]\3\21\6\21a")
        buf.write("\n\21\r\21\16\21b\3\22\5\22f\n\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\6\25q\n\25\r\25\16\25r\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\2\2\32\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\2%\2\'\23)\24+\25-\26/\27\61\30")
        buf.write("\3\2\6\4\2C\\c|\3\2\62;\3\2))\5\2\13\f\17\17\"\"\2\177")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\3\63\3\2\2\2\5\65\3\2\2\2\7\67\3\2\2\2\t9\3\2\2\2")
        buf.write("\13;\3\2\2\2\rB\3\2\2\2\17D\3\2\2\2\21F\3\2\2\2\23H\3")
        buf.write("\2\2\2\25J\3\2\2\2\27L\3\2\2\2\31N\3\2\2\2\33P\3\2\2\2")
        buf.write("\35T\3\2\2\2\37[\3\2\2\2!`\3\2\2\2#e\3\2\2\2%i\3\2\2\2")
        buf.write("\'l\3\2\2\2)p\3\2\2\2+v\3\2\2\2-x\3\2\2\2/z\3\2\2\2\61")
        buf.write("|\3\2\2\2\63\64\7,\2\2\64\4\3\2\2\2\65\66\7\61\2\2\66")
        buf.write("\6\3\2\2\2\678\7-\2\28\b\3\2\2\29:\7/\2\2:\n\3\2\2\2;")
        buf.write("<\7t\2\2<=\7g\2\2=>\7v\2\2>?\7w\2\2?@\7t\2\2@A\7p\2\2")
        buf.write("A\f\3\2\2\2BC\7?\2\2C\16\3\2\2\2DE\7*\2\2E\20\3\2\2\2")
        buf.write("FG\7+\2\2G\22\3\2\2\2HI\7}\2\2I\24\3\2\2\2JK\7\177\2\2")
        buf.write("K\26\3\2\2\2LM\7.\2\2M\30\3\2\2\2NO\7=\2\2O\32\3\2\2\2")
        buf.write("PQ\7k\2\2QR\7p\2\2RS\7v\2\2S\34\3\2\2\2TU\7h\2\2UV\7n")
        buf.write("\2\2VW\7q\2\2WX\7c\2\2XY\7v\2\2Y\36\3\2\2\2Z\\\t\2\2\2")
        buf.write("[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^ \3\2\2\2_a")
        buf.write("\t\3\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\"\3")
        buf.write("\2\2\2df\t\4\2\2ed\3\2\2\2ef\3\2\2\2fg\3\2\2\2gh\t\3\2")
        buf.write("\2h$\3\2\2\2ij\7\60\2\2jk\t\3\2\2k&\3\2\2\2lm\5#\22\2")
        buf.write("mn\5%\23\2n(\3\2\2\2oq\t\5\2\2po\3\2\2\2qr\3\2\2\2rp\3")
        buf.write("\2\2\2rs\3\2\2\2st\3\2\2\2tu\b\25\2\2u*\3\2\2\2vw\13\2")
        buf.write("\2\2w,\3\2\2\2xy\13\2\2\2y.\3\2\2\2z{\13\2\2\2{\60\3\2")
        buf.write("\2\2|}\13\2\2\2}\62\3\2\2\2\7\2]ber\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MUL = 1
    DIV = 2
    ADD = 3
    SUB = 4
    RETURN = 5
    EQUAL = 6
    LP = 7
    RP = 8
    LB = 9
    RB = 10
    COMMA = 11
    SEMI = 12
    INT = 13
    FLOAT = 14
    ID = 15
    INTLIT = 16
    FLOATLIT = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21
    UNTERMINATED_COMMENT = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'return'", "'='", "'('", "')'", 
            "'{'", "'}'", "','", "';'", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "RETURN", "EQUAL", "LP", "RP", "LB", 
            "RB", "COMMA", "SEMI", "INT", "FLOAT", "ID", "INTLIT", "FLOATLIT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "MUL", "DIV", "ADD", "SUB", "RETURN", "EQUAL", "LP", "RP", 
                  "LB", "RB", "COMMA", "SEMI", "INT", "FLOAT", "ID", "INTLIT", 
                  "INTPART", "FRACPART", "FLOATLIT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.(INT|FLOAT)
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


