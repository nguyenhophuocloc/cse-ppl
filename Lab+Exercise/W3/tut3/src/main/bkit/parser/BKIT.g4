grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options {
	language = Python3;
}

program: manydecl* EOF;
manydecl: vardecl | funcdecl;
vardecl: (INT | FLOAT) idlist SEMI;
idlist: ID COMMA idlist | ID;
//id: ID;

funcdecl: (INT | FLOAT) ID LP paramlist* RP LB body* RB;
paramlist: param SEMI paramlist | param;
param: (INT | FLOAT) idlist;
body: vardecl | stmt SEMI;
stmt: assignstmt | callstmt | returnstmt;
assignstmt: ID EQUAL exp;
callstmt: ID LP explist RP;
explist: exp COMMA explist | exp;
returnstmt: RETURN exp;
//exp: operands | <assoc = left> exp (MUL|DIV) exp | operands SUB operands | <assoc = right> exp ADD
// exp; subexp: LP exp RP; operands: subexp | INTLIT|FLOATLIT|ID |callstmt ;
exp: exp1 ADD exp | exp1;
exp1: exp2 SUB exp2 | exp2;
exp2: exp2 MUL exp3 | exp2 DIV exp3| exp3;
exp3: LP exp RP | literal | ID | callstmt;
literal: FLOATLIT | INTLIT;

MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';
RETURN: 'return';
EQUAL: '=';
LP: '(';
RP: ')';
LB: '{';
RB: '}';
COMMA: ',';
SEMI: ';';
INT: 'int';
FLOAT: 'float';
ID: [A-Za-z]+;
INTLIT: [0-9]+;
//SIGN: ['+'|'-'];
fragment INTPART: ['-']? [0-9];
fragment FRACPART: '.' [0-9];
FLOATLIT: INTPART FRACPART;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;