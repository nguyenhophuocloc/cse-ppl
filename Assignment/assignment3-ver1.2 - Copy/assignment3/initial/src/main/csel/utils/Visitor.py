from abc import ABC, abstractmethod, ABCMeta


class Visitor(ABC):

    def visit(self, ast, param):
        return ast.accept(self, param)

    @abstractmethod
    def visitProgram(self, ast, param):
        pass

    @abstractmethod
    def visitVarDecl(self, ast, param):
        pass

    @abstractmethod
    def visitConstDecl(self, ast, param):
        pass

    @abstractmethod
    def visitFuncDecl(self, ast, param):
        pass

    @abstractmethod
    def visitBinaryOp(self, ast, param):
        pass

    @abstractmethod
    def visitUnaryOp(self, ast, param):
        pass

    @abstractmethod
    def visitCallExpr(self, ast, param):
        pass

    @abstractmethod
    def visitId(self, ast, param):
        pass

    @abstractmethod
    def visitArrayAccess(self, ast, param):
        pass

    @abstractmethod
    def visitJSONAccess(self, ast, param):
        pass

    @abstractmethod
    def visitAssign(self, ast, param):
        pass

    @abstractmethod
    def visitIf(self, ast, param):
        pass

    @abstractmethod
    def visitFor(self, ast, param):
        pass

    @abstractmethod
    def visitContinue(self, ast, param):
        pass

    @abstractmethod
    def visitBreak(self, ast, param):
        pass

    @abstractmethod
    def visitReturn(self, ast, param):
        pass

    @abstractmethod
    def visitDowhile(self, ast, param):
        pass

    @abstractmethod
    def visitWhile(self, ast, param):
        pass

    @abstractmethod
    def visitCallStmt(self, ast, param):
        pass

    @abstractmethod
    def visitIntLiteral(self, ast, param):
        pass

    @abstractmethod
    def visitNumberLiteral(self, ast, param):
        pass

    @abstractmethod
    def visitStringLiteral(self, ast, param):
        pass

    @abstractmethod
    def visitArrayLiteral(self, ast, param):
        pass
    
    @abstractmethod
    def visitJSONLiteral(self, ast, param):
        return None


class BaseVisitor(Visitor):

    def visitProgram(self, ast, param):
        return None

    def visitVarDecl(self, ast, param):
        return None

    def visitConstDecl(self, ast, param):
        return None

    def visitFuncDecl(self, ast, param):
        return None

    def visitBinaryOp(self, ast, param):
        return None

    def visitUnaryOp(self, ast, param):
        return None

    def visitCallExpr(self, ast, param):
        return None

    def visitId(self, ast, param):
        return None

    def visitArrayAccess(self, ast, param):
        return None

    def visitJSONAccess(self, ast, param):
        return None

    def visitAssign(self, ast, param):
        return None

    def visitIf(self, ast, param):
        return None

    def visitFor(self, ast, param):
        return None

    def visitContinue(self, ast, param):
        return None

    def visitBreak(self, ast, param):
        return None

    def visitReturn(self, ast, param):
        return None

    def visitDowhile(self, ast, param):
        return None

    def visitWhile(self, ast, param):
        return None

    def visitCallStmt(self, ast, param):
        return None

    def visitNumberLiteral(self, ast, param):
        return None

    def visitBooleanLiteral(self, ast, param):
        return None

    def visitStringLiteral(self, ast, param):
        return None

    def visitArrayLiteral(self, ast, param):
        return None

    def visitJSONLiteral(self, ast, param):
        return None
