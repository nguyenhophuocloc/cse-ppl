class Exp:
    pass


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def eval(self):
        if self.op == '+':
            return self.left.eval()+self.right.eval()
        elif self.op == '-':
            return self.left.eval()-self.right.eval()
        elif self.op == '*':
            return self.left.eval()*self.right.eval()
        elif self.op == '/':
            return self.left.eval()/self.right.eval()


class UnExp(Exp):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def eval(self):
        if self.op == '+':
            return self.operand.eval()
        elif self.op == '-':
            return self.operand.eval()*-1


class IntLit(Exp):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num


class FloatLit(Exp):
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num

x=BinExp(IntLit(4),'-',IntLit(3))
print(x.eval())