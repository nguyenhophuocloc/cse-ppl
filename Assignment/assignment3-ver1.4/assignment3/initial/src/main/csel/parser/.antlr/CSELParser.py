# Generated from /Users/duytran/Desktop/202/PPL/assignment/assignment3/initial/src/main/csel/parser/CSEL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2")
        buf.write("\t\2\4\3\2\2\2\4\5\7\6\2\2\5\6\7\5\2\2\6\7\7\3\2\2\7\b")
        buf.write("\7\4\2\2\b\t\7\2\2\3\t\3\3\2\2\2\2")
        return buf.getvalue()


class CSELParser ( Parser ):

    grammarFileName = "CSEL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>", "ID", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    SEMI=2
    COLON=3
    VAR=4
    WS=5
    ERROR_CHAR=6
    UNCLOSE_STRING=7
    ILLEGAL_ESCAPE=8
    UNTERMINATED_COMMENT=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSELParser.VAR, 0)

        def COLON(self):
            return self.getToken(CSELParser.COLON, 0)

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def SEMI(self):
            return self.getToken(CSELParser.SEMI, 0)

        def EOF(self):
            return self.getToken(CSELParser.EOF, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_program




    def program(self):

        localctx = CSELParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(CSELParser.VAR)
            self.state = 3
            self.match(CSELParser.COLON)
            self.state = 4
            self.match(CSELParser.ID)
            self.state = 5
            self.match(CSELParser.SEMI)
            self.state = 6
            self.match(CSELParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





