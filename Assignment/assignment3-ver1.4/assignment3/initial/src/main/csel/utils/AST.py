from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from Visitor import Visitor


def printlist(lst, f=str, start="[", sepa=",", ending="]"):
    return start + sepa.join(f(i) for i in lst) + ending


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)


class Inst(AST):
    __metaclass__ = ABCMeta
    pass


class Stmt(Inst):
    __metaclass__ = ABCMeta
    pass


class Decl(Inst):
    __metaclass__ = ABCMeta
    pass


class Expr(Inst):
    __metaclass__ = ABCMeta
    pass


class Literal(Expr):
    __metaclass__ = ABCMeta
    pass


class LHS(Expr):
    __metaclass__ = ABCMeta
    pass


class Type(AST):
    __metaclass__ = ABCMeta
    pass


@dataclass
class NumberType(Type):
    def __str__(self):
        return "NumberType"

    def accept(self, v, param):
        return v.visitNumberType(self, param)


@dataclass
class StringType(Type):
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return v.visitStringType(self, param)


@dataclass
class BooleanType(Type):
    def __str__(self):
        return "BooleanType"

    def accept(self, v, param):
        return v.visitBooleanType(self, param)


@dataclass
class ArrayType(Type):
    def __str__(self):
        return "ArrayType"

    def accept(self, v, param):
        return v.visitArrayType(self, param)


@dataclass
class JSONType(Type):
    def __str__(self):
        return "JSONType"

    def accept(self, v, param):
        return v.visitJSONType(self, param)


@dataclass
class NoneType(Type):
    def __str__(self):
        return "NoneType"

    def accept(self, v, param):
        return v.visitNoneType(self, param)


@dataclass
class Id(LHS):
    name: str

    def __str__(self):
        return "Id(" + self.name + ")"

    def accept(self, v, param):
        return v.visitId(self, param)


@dataclass
class Program(AST):
    decl: List[Decl]

    def __str__(self):
        return "Program("+printlist(self.decl)+")"

    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)


@dataclass
class VarDecl(Decl):
    variable: Id
    varDimen: List[Expr]     # empty list for scalar variable
    typ: Type               # NoneType if empty
    varInit: Expr           # None if no initial

    def __str__(self):
        initial = (","+str(self.varInit)) if self.varInit else ""
        typ = ","+str(self.typ)
        dimen = (","+printlist(self.varDimen)) if self.varDimen else ""
        return "VarDecl(" + str(self.variable) + dimen + typ + initial + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)


@dataclass
class ConstDecl(Decl):
    constant: Id
    constDimen: List[Expr]       # empty list for scalar variable
    typ: Type                   # NoneType if empty
    constInit: Expr             

    def __str__(self):
        initial = ("," + str(self.constInit)) if self.constInit else ""
        typ = ","+str(self.typ)
        dimen = ("," + printlist(self.constDimen)) if self.constDimen else ""
        return "ConstDecl(" + str(self.constant) + dimen + typ + initial + ")"

    def accept(self, v, param):
        return v.visitConstDecl(self, param)


@dataclass
class FuncDecl(Decl):
    name: Id
    param: List[VarDecl]
    body: List[Inst]

    def __str__(self):
        return "FuncDecl(" + str(self.name) + \
            printlist(self.param) + "," + printlist(self.body) + ")"

    def accept(self, v, param):
        return v.visitFuncDecl(self, param)


@dataclass
class ArrayAccess(LHS):  # For access in Array
    arr: Expr
    idx: List[Expr]

    def __str__(self):
        return "ArrayAccess(" + str(self.arr) + "," + printlist(self.idx) + ")"

    def accept(self, v, param):
        return v.visitArrayAccess(self, param)


@dataclass
class JSONAccess(LHS):  # For access in JSON
    json: Expr
    idx: List[Expr]

    def __str__(self):
        return "JSONAccess(" + str(self.json) + "," + printlist(self.idx) + ")"

    def accept(self, v, param):
        return v.visitJSONAccess(self, param)


@dataclass
class BinaryOp(Expr):
    op: str
    left: Expr
    right: Expr

    def __str__(self):
        return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)


@dataclass
class UnaryOp(Expr):
    op: str
    body: Expr

    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

    def accept(self, v, param):
        return v.visitUnaryOp(self, param)


@dataclass
class CallExpr(Expr):
    method: Id
    param: List[Expr]

    def __str__(self):
        return "CallExpr(" + str(self.method) + "," + printlist(self.param) + ")"

    def accept(self, v, param):
        return v.visitCallExpr(self, param)


@dataclass
class NumberLiteral(Literal):
    value: float

    def __str__(self):
        return "NumberLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitNumberLiteral(self, param)


@dataclass
class StringLiteral(Literal):
    value: str

    def __str__(self):
        return "StringLiteral(" + self.value + ")"

    def accept(self, v, param):
        return v.visitStringLiteral(self, param)


@dataclass
class BooleanLiteral(Literal):
    value: bool

    def __str__(self):
        return "BooleanLiteral(" + str(self.value).lower() + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)


@dataclass
class JSONLiteral(Literal):
    value: List[tuple]

    def __str__(self):
        return "JSONLiteral(" + ','.join(["(Key=" + str(x[0]) + ",Value=" + str(x[1]) + ")" for x in self.value])

    def accept(self, v, param):
        return v.visitJSONLiteral(self, param)


@dataclass
class ArrayLiteral(Literal):
    value: List[Literal]

    def __str__(self):
        return printlist(self.value, start="ArrayLiteral(", ending=")")

    def accept(self, v, param):
        return v.visitArrayLiteral(self, param)


@dataclass
class Assign(Stmt):
    lhs: LHS
    rhs: Expr

    def __str__(self):
        return "Assign(" + str(self.lhs) + "," + str(self.rhs) + ")"

    def accept(self, v, param):
        return v.visitAssign(self, param)


def printListStmt(stmt):
    return printlist(stmt)


def printIfThenStmt(stmt):
    return str(stmt[0])+","+printlist(stmt[1])


@dataclass
class If(Stmt):
    """Expr is the condition, 
        List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
        List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
    """
    ifthenStmt: List[Tuple[Expr, List[Inst]]]
    elseStmt: List[Inst]  # for Else branch, empty list if no Else

    def __str__(self):
        ifstmt = printlist(self.ifthenStmt, printIfThenStmt,
                           "If(", ")ElseIf(", ")")
        elsestmt = ("Else("+printListStmt(self.elseStmt) +
                    ")") if self.elseStmt else ""
        return ifstmt + elsestmt

    def accept(self, v, param):
        return v.visitIf(self, param)


@dataclass
class ForIn(Stmt):
    idx1: Id
    expr: Expr
    body: List[Inst]

    def __str__(self):
        return "ForIn(" + \
            str(self.idx1)+"," + \
            str(self.expr) + "," + \
            printlist(self.body) + ")"

    def accept(self, v, param):
        return v.visitForIn(self, param)


@dataclass
class ForOf(Stmt):
    idx1: Id
    expr: Expr
    body: List[Inst]

    def __str__(self):
        return "ForOf(" + \
            str(self.idx1)+"," + \
            str(self.expr) + "," + \
            printlist(self.body) + ")"

    def accept(self, v, param):
        return v.visitForOf(self, param)


class Break(Stmt):
    def __str__(self):
        return "Break()"

    def accept(self, v, param):
        return v.visitBreak(self, param)


class Continue(Stmt):
    def __str__(self):
        return "Continue()"

    def accept(self, v, param):
        return v.visitContinue(self, param)


@dataclass
class Return(Stmt):
    expr: Expr  # None if no expression

    def __str__(self):
        return "Return(" + ("" if (self.expr is None) else str(self.expr)) + ")"

    def accept(self, v, param):
        return v.visitReturn(self, param)


@dataclass
class While(Stmt):
    exp: Expr
    sl: List[Inst]

    def __str__(self):
        return "While(" + str(self.exp) + "," + printListStmt(self.sl) + ")"

    def accept(self, v, param):
        return v.visitWhile(self, param)


@dataclass
class CallStmt(Stmt):
    method: Id
    param: List[Expr]

    def __str__(self):
        return "CallStmt(" + str(self.method) + "," + printlist(self.param) + ")"

    def accept(self, v, param):
        return v.visitCallStmt(self, param)
