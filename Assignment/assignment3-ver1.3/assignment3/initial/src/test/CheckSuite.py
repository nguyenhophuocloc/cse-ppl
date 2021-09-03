import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[],NoneType(),JSONLiteral([(Id('age'),NumberLiteral(10.0)),(Id('b'),JSONLiteral([(Id('name'),StringLiteral('loc'))]))])),
                        FuncDecl(Id('main'),[],[ForOf(Id('x'),Id('a'),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 403))
