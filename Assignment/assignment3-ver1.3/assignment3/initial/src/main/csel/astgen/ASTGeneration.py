from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *

class ASTGeneration(CSELVisitor):
    def visitProgram(self,ctx:CSELParser.ProgramContext):
        return Program([VarDecl(Id(ctx.ID().getText()),[],None)])

    

