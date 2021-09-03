from abc import ABC
class IllegalOperandException(Exception):
	def __init__(self,msg):
	# msg:string
		self.s = msg
	def __str__(self):
		return "Illegal Operand: " + self.s +"\n"
class IllegalRuntimeException(Exception):
	def __init__(self,msg):
	# msg:string
		self.s = msg
	def __str__(self):
		return "Illegal Runtime: " + self.s +"\n"
class Program:
    def __init__(self,lst):
        self.decl = lst
    def accept(self, v, param):
        return v.visitProgram(self, param)
class Decl(ABC):pass
class FuncDecl(Decl):
    def __init__(self,i,it,ot,b):
        self.name = i
        self.param = it
        self.returnType = ot
        self.body = b
    def accept(self, v, param):
        return v.visitFuncDecl(self, param)
class Expr(ABC):pass
class Id(Expr):
    def __init__(self,n):
        self.name = n
    def accept(self, v, param):
        return v.visitId(self, param)
class CallExpr(Expr):
    def __init__(self,n,a):
        self.method = n
        self.param = a
    def accept(self, v, param):
        return v.visitCallExpr(self, param)
class BinExpr(Expr):
    def __init__(self,n,a,b):
        self.op = n
        self.e1 = a
        self.e2 = b
    def accept(self, v, param):
        return v.visitBinExpr(self, param)
class FloatLiteral(Expr):
    def __init__(self,v):
        self.value = v
    def accept(self, v, param):
        return v.visitFloatLiteral(self, param)
class IntLiteral(Expr):
    def __init__(self,v):
        self.value = v
    def accept(self, v, param):
        return v.visitIntLiteral(self, param)




class Type(ABC): pass
class IntType(Type):
    def accept(self, v, param):
        return v.visitIntType(self, param)
class FloatType(Type):
    def accept(self, v, param):
        return v.visitFloatType(self, param)
class VoidType(Type):
    def accept(self, v, param):
        return v.visitVoidType(self, param)
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
    def __str__(self):
        return "ClassType"
    def accept(self, v, param):
        return v.visitClassType(self, param)
class StringType(Type):
    def accept(self, v, param):
        return v.visitStringType(self, param)
class BoolType(Type):
    def accept(self, v, param):
        return v.visitBoolType(self, param)
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
    def accept(self, v, param):
        return v.visitMType(self, param)
class ArrayType(Type):
    def __init__(self,et,*s):
        self.eleType = et #Type
        self.dimen = s   #List[int]  
    def accept(self, v, param):
        return v.visitArrayType(self, param) 




class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class BaseVisitor: 
    def visit(self,ast,param):
        return ast.accept(self,param)

    def visitProgram(self,ast,param):
        return None
    def visitVarDecl(self,ast,param):
        return None    
    def visitFuncDecl(self,ast,param):
        return None
    def visitIntType(self,ast,param):
        return None
    def visitFloatType(self,ast,param):
        return None
    def visitBoolType(self,ast,param):
        return None 
    def visitStringType(self,ast,param):
        return None
    def visitVoidType(self,ast,param):
        return None
    def visitArrayType(self,ast,param):
        return None
    def visitBinExpr(self,ast,param):
        return None
    def visitUnaryOp(self,ast,param):
        return None
    def visitCallExpr(self,ast,param):
        return None 
    def visitId(self,ast,param):
        return None
    def visitArrayCell(self,ast,param):
        return None   
    def visitIf(self,ast,param):
        return None    
    def visitFor(self,ast,param):
        return None    
    def visitContinue(self,ast,param):
        return None    
    def visitBreak(self,ast,param):
        return None    
    def visitReturn(self,ast,param):
        return None    
    def visitDowhile(self,ast,param):
        return None    
    def visitIntLiteral(self,ast,param):
        return None   
    def visitFloatLiteral(self,ast,param):
        return None
    def visitBooleanLiteral(self,ast,param):
        return None    
    def visitStringLiteral(self,ast,param):
        return None