from abc import ABC,abstractclassmethod


class Exp:
    @abstractclassmethod
    def eval(self):pass


class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self):
        if self.operator == '+':
            return self.left.eval()+self.right.eval()
        elif self.operator == '-':
            return self.left.eval()-self.right.eval()
        elif self.operator == '*':
            return self.left.eval() * self.right.eval()
        elif self.operator == '/':
            return self.left.eval()/self.right.eval()


class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self):
        if self.operator == '+':
            return self.operand.eval()
        elif self.operator == '-':
            return self.operand.eval()*-1


class IntLit(Exp):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return int(self.num)


class FloatLit(Exp):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return float(self.num)


x = BinExp(UnExp('-', IntLit(4)), '+', BinExp(IntLit(3), '*', IntLit(2)))
print(x.eval())
#trung to