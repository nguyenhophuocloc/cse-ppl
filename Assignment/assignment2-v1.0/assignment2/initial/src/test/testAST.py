import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Let x;"""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Let ;"""
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestAST.checkASTGen(input,expect,202))

    def test_vardecl_scalar_with_init(self):
        input = """Let x = 10, y = "abc";"""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,202))

    def test_vardecl_composite(self):
        input = """Let z[123][10];"""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,203))

    def test_vardecl_composite_with_init(self):
        input = """Let t[76] = [89, True, 1.2];"""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,204))
    
    def test_vardecl_array_literal_simple(self):
        input = """
            Let a = [1.2, 3e-7, 0.00];
            Let b[10][0] = [["abc", "def"], ["tnc\\n", "nttk"], ["'"'"", "\\t\\f\\r"]];
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,205))

    def test_vardecl_array_literal_empty(self):
        input = """
            Let c = [];
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,206))
    
    def test_vardecl_array_literal_different_type(self):
        input = """
            Let d = [[], "x\\nt", True, [False, 3.e+89, 666]];
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,207))

    def test_vardecl_array_literal_multilevel(self):
        input = """
            Let e = [[[[[[[]]]]]]];
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,208))

    def test_vardecl_empty(self):
        input = """
            Let ;
        """
        expect = "Error on line 2 col 16: ;"
        self.assertTrue(TestAST.checkASTGen(input,expect,209))

    def test_vardecl_redeclare(self):
        input = """
            Let x = False, x = 123;
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,210))
    #test variable declaration

    #test function declaration
    def test_funcdecl_empty(self):
        input = """
            Function foo()
            {

            }           
            
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,211))

    def test_funcdecl_nobody(self):
        input = """
            Function foo()
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestAST.checkASTGen(input,expect,212))
    
    def test_funcdecl_empty_parameter(self):
        input = """
            Function foo()
            () 
            {
            }
        """
        expect = "Error on line 3 col 12: ("
        self.assertTrue(TestAST.checkASTGen(input,expect,213))

    def test_funcdecl_simple_parameter(self):
        input = """
            Function foo()
            (x, y[3][34][067])
            {
            }
        """
        expect = "Error on line 3 col 12: ("
        self.assertTrue(TestAST.checkASTGen(input,expect,214))

    def test_funcdecl_parameter_with_init(self):
        input = """
            Function foo()
            (x = "abc")
            {
            }
        """
        expect = "Error on line 3 col 12: ("
        self.assertTrue(TestAST.checkASTGen(input,expect,215))

    def test_funcdecl_redeclare_parameter(self):
        input = """
            Function foo()
            (x,x,x,x,x[123][456])
            {
            }
        """
        expect = "Error on line 3 col 12: ("
        self.assertTrue(TestAST.checkASTGen(input,expect,216))

    def test_funcdecl_redeclare_with_vardecl(self):
        input = """
            Let foo = True;

            Function foo()
            {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,217))

    def test_funcdecl_redeclare_with_funcdecl(self):
        input = """
            Function foo()
            {
            }

            Function foo()
            {
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,218))

    def test_funcdecl_vardecl_wrong_order(self):
        input = """
            Function foo()
            {
            }

            Let x, y;
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,219))
    
    def test_funcdecl_body_with_vardecl(self):
        input = """
            Function foo()
            {
                Let x, y;
                Let z[123][456] = 1.234e-789;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,220))
    #test function declaration

    #test assign stmt
    def test_stmt_assign_simple(self):
        input = """
            Function foo()
            {
                x = 10;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,221))

    def test_stmt_assign_array(self):
        input = """
            Function foo()
            {
                x = [12, True, "abc"];
            }
        """
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestAST.checkASTGen(input,expect,222))

    def test_stmt_assign_arraycell(self):
        input = """
            Function foo()
            {
                x[3108] = 323.e-3;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,223))

    def test_stmt_assign_expression(self):
        input = """
            Function foo()
            {
                x = 123 + "string";
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,224))
    #test assign stmt

    #test if stmt
    def test_stmt_if_only_if(self):
        input = """
            Function foo()
            {
                If (True) {x = False;}
                
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,225))

    def test_stmt_if_only_if_empty_then(self):
        input = """
            Function foo()
            {
                If (True){
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,226))

    def test_stmt_if_only_if_no_then(self):
        input = """
            Function foo()
            {
                If (False)
                }
            }
        """
        expect = "Error on line 5 col 16: }"
        self.assertTrue(TestAST.checkASTGen(input,expect,227))

    def test_stmt_if_only_if_no_endif(self):
        input = """
            Function foo()
            {
                If (False) {
                Call(str_to_float,["abc"]);
            }
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestAST.checkASTGen(input,expect,228))

    def test_stmt_if_with_else(self):
        input = """
            Function foo()
            {
                If (False) 
                {
                    Call(str_to_float,["abc"]);
                }
                Else
                { 
                    y = "0x23CD";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,229))
    
    def test_stmt_if_empty_else(self):
        input = """
            Function foo()
            {
                If (False) 
                {
                    Call(str_to_float,["abc"]);
                }
                Else{

                }
                
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,230))

    def test_stmt_if_with_elseif(self):
        input = """
            Function foo()
            {
                If (False) 
                {
                    Call(str_to_float,["abc"]);
                }
                Elif (True) {
                    z = "xyz";
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,231))

    def test_stmt_if_full_empty(self):
        input = """
            Function foo()
            {
                If (False){
                } 
                Elif(m != n)
                {

                }
                Else{

                }
                
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,232))

    def test_stmt_if_full(self):
        input = """
            Function foo()
            {
                If (False){x = 1; }
                Elif (m != n){x = 0xABC;}
                Elif ("abc" + def){x = 123;}
                Else {x = 1.2e-3;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,233))
    #test if stmt

    #test for stmt
    def test_stmt_for_empty(self):
        input = """
            Function foo()
            {
                For () {
                    x = x + 1;
                }
            }
        """
        expect = "Error on line 4 col 20: ("
        self.assertTrue(TestAST.checkASTGen(input,expect,234))

    def test_stmt_for_full_condition(self):
        input = """
            Function foo()
            {
                For i In [0,1,2,3,4]{
                    x = x + 1;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,235))

    def test_stmt_for_empty_body(self):
        input = """
            Function foo()
            {
                For i In [0,1,2,3,4]{
                   
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,236))

    def test_stmt_for_wrong_type_condition(self):
        input = """
            Function foo()
            {
                For i In a{
                    x = x + 1;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,237))

    def test_stmt_for_nested(self):
        input = """
            Function foo()
            {
                For i In a
                {
                    For j In a
                    {
                        For k Of b
                        {

                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,238))
    #test for stmt

    #test break stmt
    def test_stmt_break_simple(self):
        input = """
            Function foo()
            {
                Break;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,239))

    def test_stmt_break_multiple(self):
        input = """
            Function foo()
            {
                Break;Break;Break;Break;Break;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,240))

    def test_stmt_break_in_loop(self):
        input = """
            Function foo()
            {
                For j in a{
                    Break;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,241))

    def test_stmt_break_in_if(self):
        input = """
            Function foo()
            {
                If (True){Break;}
                Else {Break;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,242))
    #test break stmt

    #test continue stmt
    def test_stmt_continue_simple(self):
        input = """
            Function foo()
            {
                Continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,243))

    def test_stmt_continue_multiple(self):
        input = """
            Function foo()
            {
                Continue;
                Continue;
                Continue;
                Continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,244))

    def test_stmt_continue_in_loop(self):
        input = """
            Function foo()
            {
                For j In a{
                    Continue;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,245))

    def test_stmt_continue_in_if(self):
        input = """
            Function foo()
            {
                If (True)
                {Continue;}
                Else {Continue;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,246))
    #test continue stmt

    #test call stmt
    def test_stmt_call_no_para(self):
        input = """
            Function foo()
            {
                Call(println,[]);
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,247))

    def test_stmt_call_with_para(self):
        input = """
            Function foo()
            {
                Call(println,[True, x + y, 12 - 7, "anc"]);
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,248))

    def test_stmt_call_recursive(self):
        input = """
            Function foo()
            {
                Call(println,[Call(println,[Call(println,[zyasdad])])]);
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,249))

    def test_stmt_call_unclosed(self):
        input = """
            Function foo()
            {
                Call(do_something,[123, 1.23e5, y * d];
            }
        """
        expect = "Error on line 4 col 54: ;"
        self.assertTrue(TestAST.checkASTGen(input,expect,250))
    #test call stmt

    #test return stmt
    def test_stmt_return_empty(self):
        input = """
            Function foo()
            {
                Return;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,251))

    def test_stmt_return_multiple(self):
        input = """
            Function foo()
            {
                Return;
                Return;
                Return;
                Return;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,252))

    def test_stmt_return_call_func(self):
        input = """
            Function foo()
            {
                Return Call(foo,[]);
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,253))

    def test_stmt_return_valid(self):
        input = """
            Function foo()
            {
                Return True;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,254))
    
    def test_stmt_return_array(self):
        input = """
            Function foo()
            {
                Let a[12] = [];
                Return a;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,255))
    
    def test_stmt_return_in_if(self):
        input = """
            Function foo()
            {
                If (True){ Return;}
                Else {
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,256))
    #test return stmt

    #test while stmt
    def test_stmt_while_empty_body(self):
        input = """
            Function foo()
            {
                While True {
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,257))

    def test_stmt_while_empty_condition(self):
        input = """
            Function foo()
            {
                While (){}
            }
        """
        expect = "Error on line 4 col 23: )"
        self.assertTrue(TestAST.checkASTGen(input,expect,258))

    def test_stmt_while_simple_body(self):
        input = """
            Function foo()
            {
                While (True){
                    x = False;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,259))

    def test_stmt_while_with_break(self):
        input = """
            Function foo()
            {
                While True {
                    Break;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,260))

    def test_stmt_while_with_continue(self):
        input = """
            Function foo()
            {
                While True {
                    Continue;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,261))

    def test_stmt_while_nested(self):
        input = """
            Function foo()
            {
                While (True) {
                    While (False) {
                        While (xyz) {
                            Call(func,[]);
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,262))

    def test_stmt_while_with_for(self):
        input = """
            Function foo()
            {
                While (True) {
                    For i In [1,2,3] {
                        While (False) {
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,263))

    def test_stmt_while_nested_with_if(self):
        input = """
            Function foo()
            {
                While (True) {
                    If (True && "abc") { Return;}
                
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,264))

    def test_stmt_while_no_end_while(self):
        input = """
            Function foo()
            {
                While (True) {
                    If (True && "abc") { Return;
                    }
            }
        """
        expect = "Error on line 8 col 8: <EOF>"
        self.assertTrue(TestAST.checkASTGen(input,expect,265))
    #test while stmt

    #test dowhile stmt
    def test_stmt_dowhile_empty_body(self):
        input = """
            Function foo()
            {
                While (True) {}
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,266))

    def test_stmt_dowhile_empty_condition(self):
        input = """
            Function foo()
            {
                While (1){
            }
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestAST.checkASTGen(input,expect,267))

    def test_stmt_dowhile_no_end_do(self):
        input = """
            Function foo()
            {
                While (True)
                    Call(do_something,[]);
                }
            }
        """
        expect = "Error on line 5 col 20: Call"
        self.assertTrue(TestAST.checkASTGen(input,expect,268))

    def test_stmt_dowhile_simple_body(self):
        input = """
            Function foo()
            {
                Call(khongthetinnoi,[213, 232 - "abc", 3232]);
                While (True) {}
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,269))

    def test_stmt_dowhile_with_break(self):
        input = """
            Function foo()
            {
                While(1){
                    Break;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,270))

    def test_stmt_dowhile_with_continue(self):
        input = """
            Function foo()
            {
                While(1){
                    Continue;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,271))

    def test_stmt_dowhile_nested(self):
        input = """
            Function foo()
            {
                If(a<5)
                {
                    While(0)
                    {                    
                        While (nothing) 
                        {

                        }                    
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,272))

    def test_stmt_dowhile_with_for(self):
        input = """
            Function foo()
            {
                While(True)
                {
                    For i In [3,2,1]
                    {
                        Let x=[[]];
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,273))

    def test_stmt_dowhile_with_if(self):
        input = """
            Function foo()
            {
                While(True){
                If (True) { 
                    Return Call(something,[]);
                }
                Else{
                    Return;
                }
                }   
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,274))

    def test_stmt_dowhile_with_while(self):
        input = """
            Function foo()
            {
               
                    While (False) 
                    {
                    }
                While (True) {}
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,275))
    #test dowhile stmt

    #test binary expression
    def test_binary_compare_valid(self):
        input = """
            Function foo()
            {
                x = "abc" >= 1.2;
                y = True < True;
                z[12] = x / 1e2;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,276))

    def test_binary_compare_invalid(self):
        input = """
            Function foo()
            {
                x = "abc" >= 1.2 < True;
            }
        """
        expect = "Error on line 4 col 33: <"
        self.assertTrue(TestAST.checkASTGen(input,expect,277))

    def test_binary_logic_valid(self):
        input = """
            Function foo()
            {
                x = 123 && "abc";
                y = True || False && 1.2;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,278))

    def test_binary_locgic_invalid(self):
        input = """
            Function foo()
            {
                x = 123 & "abc";
                y = True || False && 1.2;
            }
        """
        expect = "&"
        self.assertTrue(TestAST.checkASTGen(input,expect,279))

    def test_binary_arithmetic_right_type(self):
        input = """
            Function foo()
            {
                Let x, y;
                x = 1 / 0 * 56;
                y = 1.2 * 0. - 89e-4; 
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,280))

    def test_binary_arithmetic_wrong_type(self):
        input = """
            Function foo()
            {
                Let x, y;
                x = 1 / True +. "123";
                y = 7.8 % 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,281))
    
    def test_binary_all(self):
        input = """
            Function foo()
            {
                Let x, y;
                x = y - x +. "123" - 456 * 056 == True % 2823 && False || 234;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,282))

    def test_binary_with_bracket(self):
        input = """
            Function foo()
            {
                Let x, y;
                x = y * x +. ("123" - 456 * (56 == True) % 2823) && (False || 234) <= "xyz";
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,283))
    #test binary expression

    #test unary exresion
    def test_unary_simple(self):
        input = """
            Function foo()
            {
                x = -x;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,284))

    def test_unary_multiple(self):
        input = """
            Function foo()
            {
                x = !!!!!!!--------x;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,285))

    def test_unary_multiple_wrong_order(self):
        input = """
            Function foo()
            {
                x = !!!-!!-------x;
            }
        """
        expect = "Error on line 4 col 24: !"
        self.assertTrue(TestAST.checkASTGen(input,expect,286))

    def test_unary_multiple_with_bracket(self):
        input = """
            Function foo()
            {
                x = !!!!-(!!-------x);
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,287))
    #test unary exresion

    #test index expression
    def test_index_simple(self):
        input = """
            Function foo()
            {
                x = a[123] + "sdsd";
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,288))

    def test_index_complex(self):
        input = """
            Function foo()
            {
                x[23] = a[123 - a[67] * "abc" || 1.e45] + "sdsd";
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,289))
    
    def test_index_recursive(self):
        input = """
            Function foo()
            {
                x = a[b[c[d[e[f[g[h[0]]]]]]]];
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,290))

    def test_index_left_hand(self):
        input = """
            Function foo()
            {
                x[1 + 2] = 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,291))

    def test_index_empty(self):
        input = """
            Function foo()
            {
                x[] = 0;
            }
        """
        expect = "Error on line 4 col 18: ]"
        self.assertTrue(TestAST.checkASTGen(input,expect,292))
    #test index expression

    #test funcall
    def test_funcall_empty(self):
        input = """
            Function foo()
            {
                x = Call(func,[]);
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,293))

    def test_funcall_missing_para(self):
        input = """
            Function foo()
            {
                x = Call(func,[239, "abc",);
            }
        """
        expect = "Error on line 4 col 42: )"
        self.assertTrue(TestAST.checkASTGen(input,expect,294))

    def test_funcall_full_para(self):
        input = """
            Function foo()
            {
                x = Call(func,[6 + Call(func,[])]);
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,295))
    
    def test_funcall_left_hand(self):
        input = """
            Function foo()
            {
                Call(func,[]) = x;
            }
        """
        expect = "Error on line 4 col 30: ="
        self.assertTrue(TestAST.checkASTGen(input,expect,296))
    #test funcall

    #test custom
    def test_expr_left_hand(self):
        input = """
            Function foo()
            {
                x + y = y + x;
            }
        """
        expect = "Error on line 4 col 18: +"
        self.assertTrue(TestAST.checkASTGen(input,expect,297))

    def test_comment_0(self):
        input = """
            Function foo()
            {
                x = ##0## 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,298))

    def test_comment_1(self):
        input = """
            Function foo()
            {
                Let ##This 
                is 
                a 
                line 
                comment## a;
            }
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input,expect,299))
    #test custom 