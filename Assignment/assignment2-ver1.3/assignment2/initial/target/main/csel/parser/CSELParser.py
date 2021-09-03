# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("\n\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\b\2\4")
        buf.write("\3\2\2\2\4\5\7\5\2\2\5\6\7\3\2\2\6\7\7\4\2\2\7\b\7\2\2")
        buf.write("\3\b\3\3\2\2\2\2")
        return buf.getvalue()


class CSELParser ( Parser ):

    grammarFileName = "CSEL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "';'", "'Let'" ]

    symbolicNames = [ "<INVALID>", "ID", "SEMI", "LET", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    SEMI=2
    LET=3
    WS=4
    ERROR_CHAR=5
    UNCLOSE_STRING=6
    ILLEGAL_ESCAPE=7
    UNTERMINATED_COMMENT=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CSELParser.LET, 0)

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def SEMI(self):
            return self.getToken(CSELParser.SEMI, 0)

        def EOF(self):
            return self.getToken(CSELParser.EOF, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSELParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(CSELParser.LET)
            self.state = 3
            self.match(CSELParser.ID)
            self.state = 4
            self.match(CSELParser.SEMI)
            self.state = 5
            self.match(CSELParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





