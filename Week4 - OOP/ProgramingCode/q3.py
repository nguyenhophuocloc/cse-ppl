from abc import ABC, abstractmethod


class Exp(ABC):
    @abstractmethod
    def accept(self): pass


class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinExp(self)


class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def accept(self, visitor):
        return visitor.visitUnExp(self)


class IntLit(Exp):
    def __init__(self, num):
        self.num = num

    def accept(self, visitor):
        return visitor.visitIntLit(self)


class FloatLit(Exp):        #Eletement
    def __init__(self, num):
        self.num = num

    def accept(self, visitor):
        return visitor.visitFloatLit(self)


class Visitor(ABC):                         #interface
    def visitBinExp(self, binexp): pass
    def visitUnExp(self, unexp): pass
    def visitFloatLit(self, floatlit): pass
    def visitIntLit(self, intlit): pass


class Eval(Visitor):                        #ConcreteElement
    def visitBinExp(self, binexp):
        if(binexp.operator == '+'):
            return binexp.left.accept(Eval()) + binexp.right.accept(Eval())
        elif (binexp.operator == '-'):
            return binexp.left.accept(Eval()) - binexp.right.accept(Eval())
        elif (binexp.operator == '*'):
            return binexp.left.accept(Eval()) * binexp.right.accept(Eval())
        elif (binexp.operator == '/'):
            return binexp.left.accept(Eval()) / binexp.right.accept(Eval())

    def visitUnExp(self, unexp):
        if(unexp.operator == '+'):
            return unexp.operand.accept(Eval())
        elif (unexp.operator == '-'):
            return unexp.operand.accept(Eval())*-1

    def visitIntLit(self, intlit):
        return intlit.num.accept(Eval())

    def visitFloatLit(self, floatlit):
        return floatlit.num.accept(Eval())


class printPrefix(Visitor):
    def visitBinExp(self, binexp):
        return binexp.operator + " " + binexp.left.accept(printPrefix()) + " "+binexp.right.accept(printPrefix())

    def visitUnExp(self, unexp):
        if(unexp.operator == '+'):
            return "+. " + unexp.operand.accept(printPrefix())
        elif (unexp.operator == '-'):
            return "-. " + unexp.operand.accept(printPrefix())

    def visitIntLit(self, intlit):
        return str(intlit.num.accept(printPrefix()))

    def visitFloatLit(self, floatlit):
        return str(floatlit.num.accept(printPrefix()))


class pritPostfix(Visitor):
    def visitBinExp(self, binexp):
        return binexp.left.accept(pritPostfix()) + " "+binexp.right.accept(pritPostfix()) + " " + binexp.operator

    def visitUnExp(self, unexp):
        if(unexp.operator == '+'):
            return unexp.operand.accept(pritPostfix()) + " +."
        elif (unexp.operator == '-'):
            return unexp.operand.accept(pritPostfix()) + " -."

    def visitIntLit(self, intlit):
        return str(intlit.num.accept(pritPostfix()))

    def visitFloatLit(self, floatlit):
        return str(floatlit.num.accept(pritPostfix()))


# trung to
# -4 + 3 * 2
