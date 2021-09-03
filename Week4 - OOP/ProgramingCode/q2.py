from abc import ABC, abstractmethod

class Exp:
    @abstractmethod
    def eval(self):pass
    @abstractmethod
    def printPrefix(self):pass


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

    def printPrefix(self):
        return self.operator + " " + self.left.printPrefix() + " " + self.right.printPrefix()


class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def eval(self):
        if self.operator == '+':
            return self.operand.eval()
        elif self.operator == '-':
            return self.operand.eval()*-1

    def printPrefix(self):
        if self.operator == '+':
            return "+." + " "+self.operand.printPrefix()
        elif self.operator == '-':
            return "-." + " " + self.operand.printPrefix()


class IntLit(Exp):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def printPrefix(self):
        return str(self.num)


class FloatLit(Exp):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

    def printPrefix(self):
        return str(self.num)


x = BinExp(UnExp('-',IntLit(4)),'+',BinExp(IntLit(3),'*',IntLit(2)))
print(x.printPrefix())
# trung to
# -4 + 3 * 2