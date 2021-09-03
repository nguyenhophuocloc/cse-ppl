from abc import ABC


class Expr(ABC):
    pass


class Var(Expr):
    def __init__(self, name):
        self.name = str(name)


class Number(Expr):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return int(self.num)

    def print(self):
        print(self.num)


class UnOp(Expr):  # Nhu la -1 (1 bien, 1 toan tu)
    def __init__(self, operator, arg):
        self.operator = operator
        self.arg = arg


class BinOp(Expr):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        if self.operator == "+":
            return Number(self.left+self.right)
        if self.operator == "-":
            return Number(self.left-self.right)
        if self.operator == "*":
            return Number(self.left*self.right)
        if self.operator == "/":
            return Number(self.left/self.right)


x = 1
o = BinOp("+", 2, 2)
t = o.eval().print()
