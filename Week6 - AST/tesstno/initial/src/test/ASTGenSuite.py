import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple(self):
        input = """
            int b;
        """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

 
   