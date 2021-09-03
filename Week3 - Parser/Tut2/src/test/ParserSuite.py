import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """

        input = """
                    int a,b,c;
                    float foo(int a;float c,d) {
                        int e; 
                        e=a+4; 
                        c=a*d/2.0; 
                        return c + 1;
                    }
                    float goo(float a,b) {
                        return foo(1,a,b);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_2(self):
        """Miss variable"""
        input = """
                    int ;
                    int Test(int a,b) {
                        int sum; 
                        sum=a+b;  
                        return sum;
                    }
                """
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_3(self):
        """Miss function name"""
        input = """
                    int n;
                    int (int a,b) {
                        int sum; 
                        sum=a+b;  
                        return sum;
                    }
                """
        expect = "Error on line 2 col 4: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 203))
    def test_4(self):
        """Miss semiconlon in body"""
        input = """
                    int n;
                    int Sum(int a,b) {
                        int sum; 
                        sum=a+b  
                        return sum;
                    }
                """
        expect = "Error on line 5 col 4: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 204))
    def test_5(self):
        """Mistake in param"""
        input = """
                    int a,b;
                    int Sum(float n, int a,b) {
                        int sum; 
                        sum=a+b;  
                        return sum;
                    }
                """
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 205))
    def test_6(self):
        """Ambigous type declare"""
        input = """
                    float int x;
                    int Sum(float n; int a,b) {
                        int sum; 
                        sum=a+b  
                        return sum;
                    }
                """
        expect = "Error on line 1 col 6: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 206))
    def test_7(self):
        """Missing brace"""
        input = """
                    int x;
                    int Sum(float n; int a,b) {
                        int sum; 
                        sum=a+b;  
                        return sum;
                    
                """
        expect = "Error on line 6 col 0: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_8(self):
        """Missing keyword or type declaration"""
        input = """
                    int x;
                    int Sum(int a,b) {
                        sum; 
                        sum=a+b;
                        return sum;
                    }
                """
        expect = "Error on line 3 col 7: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_9(self):
        """Semicolon in param declaration"""
        input = """
                    int x;
                    int Sum(;int a,b) {
                        int sum;
                        sum=a+b;  
                        return sum;
                    }
                    int main(){
                        Sum(1,2);
                    }
                """
        expect = "Error on line 2 col 8: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_10(self):
        """Ambiguous return"""
        input = """
                    int x;
                    int Sum(int a,b) {
                        int sum;
                        sum=a+b;  
                        return;
                    }
                """
        expect = "Error on line 5 col 11: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 210))