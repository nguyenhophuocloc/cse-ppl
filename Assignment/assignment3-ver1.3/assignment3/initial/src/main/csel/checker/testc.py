import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 415))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 417))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 418))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 420))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 426))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 4036))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 466))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 467))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 480))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 484))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 485))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 486))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 487))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 499))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 500))
    def test_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([VarDecl(Id('a'),[NumberLiteral(30.0)],NoneType(),ArrayLiteral([NumberLiteral(3.0)])),
                        FuncDecl(Id('main'),[],[ ForIn(Id('x'),ArrayLiteral([NumberLiteral(3.0)]),[])])
                ])
        expect=str()
        self.assertTrue(TestChecker.test(input, expect, 501))
    