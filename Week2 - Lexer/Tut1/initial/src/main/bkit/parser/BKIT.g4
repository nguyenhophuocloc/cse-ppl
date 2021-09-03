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

program  : VAR COLON ID SEMI EOF ;

fragment TEXT: [a-z];
fragment DIGIT: [0-9];
ID: TEXT (TEXT|DIGIT)*;

fragment SCENTIST: 'e-';
REAL: [-]? DIGIT+ SCENTIST DIGIT+ | [-]? DIGIT+ '.' DIGIT+ (SCENTIST DIGIT+)*;
/*/
fragment Sign : '-' ;
fragment FractionalPart
:
DIGIT+ '.' DIGIT*
| DIGIT* '.' DIGIT+
;
fragment ExponentPart : 'e' Sign? DIGIT+;
FLOATLIT
:
FractionalPart ExponentPart?
DIGIT+ ExponentPart
;
*/
fragment Quote : '\'';
fragment DoubleQuote : '\'\'' ;
STRLIT : Quote (DoubleQuote|~('\'')*) Quote ;
//STRING: '\'' .* '\'';
SEMI: ';' ;

COLON: ':' ;

VAR: 'Var' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;