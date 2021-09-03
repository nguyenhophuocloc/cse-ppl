import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("ab","",101))

    def test_identifier2(self):
        self.assertTrue(TestLexer.checkLexeme("1","",102))

    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("88v","",103))

    def test_identifier4(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("a99","",104))

    def test_real1(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("0.000000001","",201))
   
    def test_real2(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("1.0","",202))

    def test_real3(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("1e-12","",203))

    def test_real4(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("1.0e-12","",204))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme("'dads\n'","'dads\n',<EOF>",301));

    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme("'isn\"t'","",302));
