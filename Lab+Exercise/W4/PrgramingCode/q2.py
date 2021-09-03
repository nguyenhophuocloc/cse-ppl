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

    def printPrefix(self):
        return self.op +" " + self.left.printPrefix()+" " + self.right.printPrefix()

class UnExp(Exp):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def eval(self):
        if self.op == '+':
            return self.operand.eval()
        elif self.op == '-':
            return self.operand.eval()*-1

    def printPrefix(self):
        if self.op=='+':
            return "+. " + self.operand.printPrefix() 
        elif self.op=='-':
            return "-. " + self.operand.printPrefix()



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


