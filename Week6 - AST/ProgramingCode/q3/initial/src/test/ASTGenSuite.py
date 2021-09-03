import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int a;"""
        expect = "bb"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """int c,b;"""
        expect = "bbb"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """int c;float b;"""
        expect = "bbb"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

 
   
 
   
 
   
 
   