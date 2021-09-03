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

options {
	language = Python3;
}
FLOAT: 'float';
INT: 'int';
RETURN: 'return';
program: manydcl* EOF;
manydcl: vardcl | funcdcl;

vardcl: mc_type idlist SM;
mc_type: INT|FLOAT;
idlist: ID (CM idlist)*;

funcdcl: mc_type ID paramdecl body;

paramdecl: LP paralist? RP;
paralist: mc_type ID (CM ID)* (SM paralist)*;

body: LB bodylist* RB;
bodylist: vardcl | stmt;
stmt: stmt_assign | stmt_call | stmt_return;
stmt_assign: ID EQ exp SM;
stmt_call: ID LP (exp(CM exp)*)* RP;
stmt_return: RETURN exp SM;

exp: operands
	| <assoc = left> exp (MUL | DIV) exp
	| operands SUB operands
	| <assoc = right> exp ADD exp;
operands: INTLIT | FLOATLIT | stmt_call | ID | subexp;
subexp: LP exp RP;


fragment NonDigit: [a-zA-Z_];
fragment Digit: [0-9];
fragment Sign: '-';
fragment Dot: '.';
fragment NonZero: [1-9];
fragment Quote: '\'';

ID: NonDigit (NonDigit | Digit)*;

INTLIT: '0' | NonZero Digit*;
FLOATLIT: INTLIT ([.][0-9]+)? ([eE][+-]? [0-9]+)?;

LB: '{';
RB: '}';
SM: ';';
CM: ',';
EQ: '=';
LP: '(';
RP: ')';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;

