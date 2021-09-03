import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input=Program([VarDecl(Id("x"),[],NumberType(),NumberLiteral(10.0)),VarDecl(Id("y"),[],NumberType(),None),
                FuncDecl(Id("foo"),[VarDecl(Id("x"),[],NoneType(),None)],[Assign(Id('x'),BooleanLiteral(True)),
                If([[Id('x'),[Assign(Id('x'),NumberLiteral(10.0))]]],[])])])
        expect=str()
        self.assertTrue(TestChecker.test(input,expect,403))

    