# Generated from d:\Python\Principles of Programming Languages\cse-ppl-master-pre\Trainning\Week6 - AST\ProgramingCode\q6\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\6\4#\n\4\r\4\16\4$\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\60\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6\67\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7C\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bM\n\b\3")
        buf.write("\t\6\tP\n\t\r\t\16\tQ\3\n\6\nU\n\n\r\n\16\nV\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\2\2\17\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3")
        buf.write("\2\6\3\2\62;\4\2>>@@\3\2c|\5\2\13\f\17\17\"\"\2n\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3")
        buf.write("\35\3\2\2\2\5\37\3\2\2\2\7\"\3\2\2\2\t/\3\2\2\2\13\66")
        buf.write("\3\2\2\2\rB\3\2\2\2\17L\3\2\2\2\21O\3\2\2\2\23T\3\2\2")
        buf.write("\2\25Z\3\2\2\2\27\\\3\2\2\2\31^\3\2\2\2\33`\3\2\2\2\35")
        buf.write("\36\7*\2\2\36\4\3\2\2\2\37 \7+\2\2 \6\3\2\2\2!#\t\2\2")
        buf.write("\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\b\3\2\2")
        buf.write("\2&\'\7V\2\2\'(\7t\2\2()\7w\2\2)\60\7g\2\2*+\7H\2\2+,")
        buf.write("\7c\2\2,-\7n\2\2-.\7u\2\2.\60\7g\2\2/&\3\2\2\2/*\3\2\2")
        buf.write("\2\60\n\3\2\2\2\61\62\7c\2\2\62\63\7p\2\2\63\67\7f\2\2")
        buf.write("\64\65\7q\2\2\65\67\7t\2\2\66\61\3\2\2\2\66\64\3\2\2\2")
        buf.write("\67\f\3\2\2\289\7-\2\29C\7?\2\2:;\7/\2\2;C\7?\2\2<=\7")
        buf.write("(\2\2=C\7?\2\2>?\7~\2\2?C\7?\2\2@A\7<\2\2AC\7?\2\2B8\3")
        buf.write("\2\2\2B:\3\2\2\2B<\3\2\2\2B>\3\2\2\2B@\3\2\2\2C\16\3\2")
        buf.write("\2\2DM\7?\2\2EF\7>\2\2FM\7@\2\2GH\7@\2\2HM\7?\2\2IJ\7")
        buf.write(">\2\2JM\7?\2\2KM\t\3\2\2LD\3\2\2\2LE\3\2\2\2LG\3\2\2\2")
        buf.write("LI\3\2\2\2LK\3\2\2\2M\20\3\2\2\2NP\t\4\2\2ON\3\2\2\2P")
        buf.write("Q\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\22\3\2\2\2SU\t\5\2\2TS")
        buf.write("\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2WX\3\2\2\2XY\b\n")
        buf.write("\2\2Y\24\3\2\2\2Z[\13\2\2\2[\26\3\2\2\2\\]\13\2\2\2]\30")
        buf.write("\3\2\2\2^_\13\2\2\2_\32\3\2\2\2`a\13\2\2\2a\34\3\2\2\2")
        buf.write("\n\2$/\66BLQV\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INTLIT = 3
    BOOLIT = 4
    ANDOR = 5
    ASSIGN = 6
    COMPARE = 7
    ID = 8
    WS = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12
    UNTERMINATED_COMMENT = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "BOOLIT", "ANDOR", "ASSIGN", "COMPARE", "ID", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "INTLIT", "BOOLIT", "ANDOR", "ASSIGN", 
                  "COMPARE", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


