import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input="""
           Function foo(x,y){   
                x=5;
                y=6;
                If(x>y){
                    Let z;
                    z=7;
                }
                Elif(True){
                    x=7;
                }
                
                
            }
        """
        expect=str()
        self.assertTrue(TestChecker.test(input,expect,403))

    