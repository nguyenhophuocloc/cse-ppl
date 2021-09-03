grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

program  :  EOF ;


fragment SIGN:[-];
fragment DIGIT:[0-9];
fragment POINT: '.';

REAL:  SIGN? DIGIT+ POINT? DIGIT+ ([E|e] SIGN DIGIT+)?| SIGN? DIGIT [e|E] SIGN? DIGIT+  ;

fragment Quote : '\'';
fragment DoubleQuote : '\'\'' ;
STRLIT: Quote (~('\'')| DoubleQuote )* Quote;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;