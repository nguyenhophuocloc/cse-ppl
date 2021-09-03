import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = """
        """
        expect= str()
        self.assertTrue(TestChecker.test(input,expect,403))
    