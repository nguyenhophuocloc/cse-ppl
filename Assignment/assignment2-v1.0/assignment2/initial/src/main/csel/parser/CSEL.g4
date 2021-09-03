grammar CSEL;

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

//program
program: manyDecl+ EOF;

manyDecl: varDecl|funcDecl;
//variable declaration
varDecl: (LET|CONSTANT) variable (CM variable)* SM;

//varlist: variable CM varlist |variable ;

typ: NUMBER |BOOLEAN|STRING|JSON|ARRAY;


variable: var (COLON typ)? (ASSIGN (vartail))?;

vartail: literal|expr;

var: ID (LQP varlist RQP)?;

varlist: NUMLIT CM varlist | NUMLIT;

literal: TRUE | FALSE | NUMLIT| STRINGLIT | arrayLiteral|jsonLiteral;

arrayLiteral: LQP (literal (CM literal)*)? RQP;

jsonLiteral: LB ID COLON literal (CM ID COLON literal)* RB;
//variable declararion

//function declaration
funcDecl: FUNCTION ID LP paraList? RP LB body RB;

paraList: var (CM var)*;

body: stmtList;
//function declaration

//statement

stmtList: manyStmt*;  //thứ tự @@

manyStmt:varDecl|otherStmt;

otherStmt: assignStmt | ifStmt | forStmt | whileStmt  | breakStmt | continueStmt | callStmt | returnStmt;

assignStmt: ID (LQP expr RQP)* ASSIGN expr SM;

ifStmt: IF LP expr RP LB stmtList RB (ELIF LP expr RP LB stmtList RB)* (ELSE LB stmtList RB)?;

forStmt: FOR ID IN arrayLiteral LB stmtList RB
                 | FOR ID OF jsonLiteral LB stmtList RB
                 | FOR ID IN ID LB stmtList RB
                 | FOR ID OF ID LB stmtList RB;

whileStmt: WHILE LP expr RP LB stmtList RB;

breakStmt: BREAK SM;

continueStmt: CONTINUE SM;

callStmt: funcall SM;

funcall: CALL LP callList RP;

returnStmt: RETURN expr? SM;
//statement

//expression
expr: logicExpr ((EQ|NEQ|GT|GTE|LT|LTE|SEQ) logicExpr)?;

logicExpr: additiveExpr ((AND|OR) additiveExpr)*;

additiveExpr: multiplicateExpr ((ADD|SUB|SADD) multiplicateExpr)*;

multiplicateExpr: unaryLogicExpr ((MUL|DIV|MOD) unaryLogicExpr)*;

unaryLogicExpr: NOT* unarySignExpr;

unarySignExpr: (SUB)* indexExpr;

indexExpr: ID (LQP expr (CM expr)* RQP)* | finalExpr;

finalExpr: NUMLIT| TRUE | FALSE | STRINGLIT | funcall | LP expr RP;

//funcall: ID CM LQP ((expr CM)* expr)? RQP;
callList: ID CM LQP ((expr CM)* expr)? RQP;
//expression
//program

//TOKEN
//IDENTIFIER

ID: [^a-z$][A-Za-z0-9_]* ;

//IDENTIFIER

//LITERALS
fragment IPART: [0-9]+;
fragment DPART: DOT [0-9]*;
fragment EPART: [eE][+-]?[0-9]+;
NUMLIT: '-'? IPART DPART? EPART?;

//BOOL
//BOOLIT: TRUE|FALSE;

//STRING
fragment ES: '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\');
fragment DQ: '\'''"';
STRINGLIT : '"' (ES | DQ | ~["\\\n])* '"'{self.text = self.text[1:-1]};


//Keywords
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELIF: 'Elif';
ELSE:'Else';
WHILE:'While';
FOR:'For';
OF: 'Of';
IN: 'In';
FUNCTION: 'Function';
LET: 'Let';
TRUE: 'True';
FALSE: 'False';
CALL: 'Call';
RETURN: 'Return';
NUMBER: 'Number';
BOOLEAN: 'Boolean';
STRING: 'String';
JSON: 'JSON';
ARRAY: 'Array';
CONSTANT: 'Constant';

//Operators:
ADD:'+';
SUB:'-';
MUL:'*';
DIV:'/';
MOD:'%';
EQ: '==';
NEQ: '!=';
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';

NOT: '!';
AND: '&&';
OR: '||';

SADD:'+.';
SEQ:'==.';

ASSIGN:'=';

//Seperators
LP: '(';
RP: ')';
LQP: '[';
RQP: ']';
LB: '{';
RB: '}';
COLON: ':';
DOT: '.';
CM: ',';
SM: ';';

//Opening

//CSETYPE: 'String'|'int';


//COMMENT && ERROR
COMMENT: '##' .*? '##' -> skip;
WS : [ \t\f\r\n]+ -> skip ;     // skip spaces, tabs, newlines
//COMMENT & WHITE SPACE

//EXCEPTION
UNCLOSE_STRING: '"' (ES | DQ | ~["\\\n])* {
    self.text = self.text[1:];
};
ILLEGAL_ESCAPE: '"' (ES | DQ | ~["\\\n])* '\\' (~[btnfr"\\])? {
    self.text = self.text[1:];
};
UNTERMINATED_COMMENT: '##' (~'#' | '#'(~'#'))*;
ERROR_CHAR: .;
//EXCEPTION
//TOKEN