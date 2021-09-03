from abc import ABC


class Exp(ABC):
    pass


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinExp(self)


class UnExp(Exp):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def accept(self, visitor):
        return visitor.visitUnExp(self)


class IntLit(Exp):
    def __init__(self, num):
        self.num = num

    def accept(self, visitor):
        return visitor.visitIntLit(self)


class FloatLit(Exp):
    def __init__(self, num):
        self.num = num

    def accept(self, visitor):
        return visitor.visitFloatLit(self)


class Visitor(ABC):
    def visitBinExp(self, binexp): pass
    def visitUnExp(self, unexp): pass
    def visitIntLit(self, intlit): pass
    def visitFloatLit(self, floatlit): pass


class Eval(Visitor):
    def visitBinExp(self, binexp):
        if binexp.op == '+':
            return binexp.left.accept(Eval()) + binexp.right.accept(Eval())
        elif binexp.op == '-':
            return binexp.left.accept(Eval()) - binexp.right.accept(Eval())
        elif binexp.op == '*':
            return binexp.left.accept(Eval()) * binexp.right.accept(Eval())
        elif binexp.op == '/':
            return binexp.left.accept(Eval()) / binexp.right.accept(Eval())

    def visitUnExp(self, unexp):
        if unexp.op == '+':
            return unexp.operand.accept(Eval())
        elif unexp.op == '-':
            return unexp.operand.accept(Eval())*-1
    def visitIntLit(self, intlit):
        return intlit.num
    def visitFloatLit(self, floatlit):
        return floatlit.num


class PrintPrefix(Visitor):
    def visitBinExp(self, binexp):
        return binexp.op + " " + binexp.left.accept(PrintPrefix())+" " + binexp.right.accept(PrintPrefix())
    def visitUnExp(self, unexp):
        if unexp.op == '+':
            return "+. " + unexp.operand.accept(PrintPrefix())
        elif unexp.op == '-':
            return "-. " + unexp.operand.accept(PrintPrefix())
    def visitIntLit(self, intlit):
        return str(intlit.num)
    def visitFloatLit(self, floatlit):
        return str(floatlit.num)


class PrintPostfix(Visitor):
    def visitBinExp(self, binexp):
        return  binexp.left.accept(PrintPostfix())+" " + binexp.right.accept(PrintPostfix()) + " " + binexp.op
    def visitUnExp(self, unexp):
        if unexp.op == '+':
            return unexp.operand.accept(PrintPostfix()) + " +."
        elif unexp.op == '-':
            return unexp.operand.accept(PrintPostfix()) + " -."
    def visitIntLit(self, intlit):
        return str(intlit.num)
    def visitFloatLit(self, floatlit):
        return str(floatlit.num)


