import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Let x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Let ;"""
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_vardecl_scalar_with_init(self):
        input = """Var: x = 10, y = "abc";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_vardecl_composite(self):
        input = """Var: z[123][0xABC];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_vardecl_composite_with_init(self):
        input = """Var: t[0o76] = {89, True, 1.2};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def test_vardecl_array_literal_simple(self):
        input = """
            Var: a = {1.2, 3e-7, 0.00};
            Var: b[0xDEF][0] = {{"abc", "def"}, {"tnc\\n", "nttk"}, {"'"'"", "\\t\\f\\r"}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_vardecl_array_literal_empty(self):
        input = """
            Var: c = {};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    
    def test_vardecl_array_literal_different_type(self):
        input = """
            Var: d = {{}, "x\\nt", True, {False, 3.e+89, 0o666}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_vardecl_array_literal_multilevel(self):
        input = """
            Var: e = {{{{{{{}}}}}}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_vardecl_empty(self):
        input = """
            Var: ;
        """
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_vardecl_redeclare(self):
        input = """
            Var: x = False, x = 123;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    #test variable declaration

    #test function declaration
    def test_funcdecl_empty(self):
        input = """
            Function: foo
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_funcdecl_nobody(self):
        input = """
            Function: foo
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    
    def test_funcdecl_empty_parameter(self):
        input = """
            Function: foo
            Parameter: 
            Body:
            EndBody.
        """
        expect = "Error on line 4 col 12: Body"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_funcdecl_simple_parameter(self):
        input = """
            Function: foo
            Parameter: x, y[0x1A][34][0O67]
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_funcdecl_parameter_with_init(self):
        input = """
            Function: foo
            Parameter: x = "abc"
            Body:
            EndBody.
        """
        expect = "Error on line 3 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_funcdecl_redeclare_parameter(self):
        input = """
            Function: foo
            Parameter: x,x,x,x,x[123][0x456]
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_funcdecl_redeclare_with_vardecl(self):
        input = """
            Var: foo = True;

            Function: foo
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_funcdecl_redeclare_with_funcdecl(self):
        input = """
            Function: foo
            Body:
            EndBody.

            Function: foo
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_funcdecl_vardecl_wrong_order(self):
        input = """
            Function: foo
            Body:
            EndBody.

            Var: x, y;
        """
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    
    def test_funcdecl_body_with_vardecl(self):
        input = """
            Function: foo
            Body:
                Var: x, y;
                Var: z[123][456] = 1.234e-789;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    #test function declaration

    #test assign stmt
    def test_stmt_assign_simple(self):
        input = """
            Function: foo
            Body:
                x = 10;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_stmt_assign_array(self):
        input = """
            Function: foo
            Body:
                x = {12, True, "abc"};
            EndBody.
        """
        expect = "Error on line 4 col 20: {"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_stmt_assign_arraycell(self):
        input = """
            Function: foo
            Body:
                x[3108] = 323.e-3;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_stmt_assign_expression(self):
        input = """
            Function: foo
            Body:
                x = 123 + "string";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    #test assign stmt

    #test if stmt
    def test_stmt_if_only_if(self):
        input = """
            Function: foo
            Body:
                If True Then x = False;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_stmt_if_only_if_empty_then(self):
        input = """
            Function: foo
            Body:
                If True Then
                EndIf. 
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_stmt_if_only_if_no_then(self):
        input = """
            Function: foo
            Body:
                If False
                EndIf.
            EndBody.
        """
        expect = "Error on line 5 col 16: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_stmt_if_only_if_no_endif(self):
        input = """
            Function: foo
            Body:
                If False Then str_to_float("abc");
            EndBody.
        """
        expect = "Error on line 5 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_stmt_if_with_else(self):
        input = """
            Function: foo
            Body:
                If False Then str_to_float("abc");
                Else y = 0x23CD;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test_stmt_if_empty_else(self):
        input = """
            Function: foo
            Body:
                If False Then str_to_float("abc");
                Else
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_stmt_if_with_elseif(self):
        input = """
            Function: foo
            Body:
                If False Then str_to_float("abc");
                ElseIf True Then z = "xyz";
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_stmt_if_full_empty(self):
        input = """
            Function: foo
            Body:
                If False Then 
                ElseIf m != n Then
                Else
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_stmt_if_full(self):
        input = """
            Function: foo
            Body:
                If False Then x = 1; 
                ElseIf m != n Then x = 0xABC;
                ElseIf "abc" + def Then x = 0o123;
                Else x = 1.2e-3;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    #test if stmt

    #test for stmt
    def test_stmt_for_empty(self):
        input = """
            Function: foo
            Body:
                For () Do
                    x = x + 1;
                EndFor.
            EndBody.
        """
        expect = "Error on line 4 col 21: )"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_stmt_for_full_condition(self):
        input = """
            Function: foo
            Body:
                For (i = 0, i < 10, 1) Do
                    x = x + 1;
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_stmt_for_empty_body(self):
        input = """
            Function: foo
            Body:
                For (i = 0, i < 10, 1) Do
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_stmt_for_wrong_type_condition(self):
        input = """
            Function: foo
            Body:
                For (i = 1.97e5, i < True, "123") Do
                    x = x + 1;
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_stmt_for_nested(self):
        input = """
            Function: foo
            Body:
                For (i = 1.97e5, i < True, "123") Do
                    For (j = 2321, j < "abc", True) Do
                        For (k = 0, k < 0, 0) Do EndFor.
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    #test for stmt

    #test break stmt
    def test_stmt_break_simple(self):
        input = """
            Function: foo
            Body:
                Break;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_stmt_break_multiple(self):
        input = """
            Function: foo
            Body:
                Break;Break;Break;Break;Break;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_stmt_break_in_loop(self):
        input = """
            Function: foo
            Body:
                For (j = 0, j < "abc", -2321) Do
                    Break;
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_stmt_break_in_if(self):
        input = """
            Function: foo
            Body:
                If True Then Break;
                Else Break;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    #test break stmt

    #test continue stmt
    def test_stmt_continue_simple(self):
        input = """
            Function: foo
            Body:
                Continue;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_stmt_continue_multiple(self):
        input = """
            Function: foo
            Body:
                Continue;
                Continue;
                Continue;
                Continue;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_stmt_continue_in_loop(self):
        input = """
            Function: foo
            Body:
                For (j = 0, j < "abc", -2321) Do
                    Continue;
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_stmt_continue_in_if(self):
        input = """
            Function: foo
            Body:
                If True Then Continue;
                Else Continue;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    #test continue stmt

    #test call stmt
    def test_stmt_call_no_para(self):
        input = """
            Function: foo
            Body:
                println();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_stmt_call_with_para(self):
        input = """
            Function: foo
            Body:
                println(True, x + y, 12 -. 7, "anc");
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_stmt_call_recursive(self):
        input = """
            Function: foo
            Body:
                println(println(println(zyasdad)));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_stmt_call_unclosed(self):
        input = """
            Function: foo
            Body:
                do_something(123, 1.23e5, y * d;
            EndBody.
        """
        expect = "Error on line 4 col 47: ;"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    #test call stmt

    #test return stmt
    def test_stmt_return_empty(self):
        input = """
            Function: foo
            Body:
                Return;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_stmt_return_multiple(self):
        input = """
            Function: foo
            Body:
                Return;
                Return;
                Return;
                Return;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_stmt_return_call_func(self):
        input = """
            Function: foo
            Body:
                Return foo();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_stmt_return_valid(self):
        input = """
            Function: foo
            Body:
                Return True;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    def test_stmt_return_array(self):
        input = """
            Function: foo
            Body:
                Var: a[12] = {};
                Return a;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    
    def test_stmt_return_in_if(self):
        input = """
            Function: foo
            Body:
                If True Then Return;
                Else Return;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    #test return stmt

    #test while stmt
    def test_stmt_while_empty_body(self):
        input = """
            Function: foo
            Body:
                While True Do
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_stmt_while_empty_condition(self):
        input = """
            Function: foo
            Body:
                While Do
                EndWhile.
            EndBody.
        """
        expect = "Error on line 4 col 16: While"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_stmt_while_simple_body(self):
        input = """
            Function: foo
            Body:
                While True Do
                    x = False;
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_stmt_while_with_break(self):
        input = """
            Function: foo
            Body:
                While True Do
                    Break;
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_stmt_while_with_continue(self):
        input = """
            Function: foo
            Body:
                While True Do
                    Continue;
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_stmt_while_nested(self):
        input = """
            Function: foo
            Body:
                While True Do
                    While False Do
                        While xyz Do
                            func();
                        EndWhile.
                    EndWhile.
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_stmt_while_with_for(self):
        input = """
            Function: foo
            Body:
                While True Do
                    For (i = 1, i < 1.3, 0.1) Do
                        While False Do
                        EndWhile.
                    EndFor.
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_stmt_while_nested_with_if(self):
        input = """
            Function: foo
            Body:
                While True Do
                    If (True && "abc") Then Return;
                    EndIf. 
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_stmt_while_no_end_while(self):
        input = """
            Function: foo
            Body:
                While True Do
                    If (True && "abc") Then Return;
                    EndIf.
            EndBody.
        """
        expect = "Error on line 7 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    #test while stmt

    #test dowhile stmt
    def test_stmt_dowhile_empty_body(self):
        input = """
            Function: foo
            Body:
                Do
                While True EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_stmt_dowhile_empty_condition(self):
        input = """
            Function: foo
            Body:
                Do
                    do_something();
                While EndDo.
            EndBody.
        """
        expect = "Error on line 6 col 22: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_stmt_dowhile_no_end_do(self):
        input = """
            Function: foo
            Body:
                Do
                    do_something();
                While True
            EndBody.
        """
        expect = "Error on line 7 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_stmt_dowhile_simple_body(self):
        input = """
            Function: foo
            Body:
                Do
                    khongthetinnoi(213, 0x232 -. "abc", 0o23232);
                While True EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_stmt_dowhile_with_break(self):
        input = """
            Function: foo
            Body:
                Do
                    Break;
                While True EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_stmt_dowhile_with_continue(self):
        input = """
            Function: foo
            Body:
                Do
                    Continue;
                While True EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_stmt_dowhile_nested(self):
        input = """
            Function: foo
            Body:
                Do
                    Do
                        Do
                        While nothing EndDo.
                    While False EndDo.
                While True EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_stmt_dowhile_with_for(self):
        input = """
            Function: foo
            Body:
                Do
                    For (i = 232-1.3, i > 0.9 + "abc", False) Do
                        Var: x = {{}};
                    EndFor.
                While True EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_stmt_dowhile_with_if(self):
        input = """
            Function: foo
            Body:
                Do
                    If (True) Then Return something;
                    Else Return something + else;
                    EndIf.
                While True EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_stmt_dowhile_with_while(self):
        input = """
            Function: foo
            Body:
                Do
                    While (False) Do
                    EndWhile.
                While True EndDo.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    #test dowhile stmt

    #test binary expression
    def test_binary_compare_valid(self):
        input = """
            Function: foo
            Body:
                x = "abc" >= 1.2;
                y = True <. True;
                z[0x12] = x =/= 1e2;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_binary_compare_invalid(self):
        input = """
            Function: foo
            Body:
                x = "abc" >= 1.2 < True;
            EndBody.
        """
        expect = "Error on line 4 col 33: <"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_binary_logic_valid(self):
        input = """
            Function: foo
            Body:
                x = 123 && "abc";
                y = True || False && 1.2;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_binary_locgic_invalid(self):
        input = """
            Function: foo
            Body:
                x = 123 & "abc";
                y = True || False && 1.2;
            EndBody.
        """
        expect = "&"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_binary_arithmetic_right_type(self):
        input = """
            Function: foo
            Body:
                Var: x, y;
                x = 1 \\ 0 * 0x56;
                y = 1.2 *. 0. -. 89e-4; 
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_binary_arithmetic_wrong_type(self):
        input = """
            Function: foo
            Body:
                Var: x, y;
                x = 1 \\. True +. "123";
                y = 7.8 % 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test_binary_all(self):
        input = """
            Function: foo
            Body:
                Var: x, y;
                x = y *. x +. "123" - 456 * 0o56 == True % 2823 && False || 234;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_binary_with_bracket(self):
        input = """
            Function: foo
            Body:
                Var: x, y;
                x = y *. x +. ("123" - 456 * (0o56 == True) % 2823) && (False || 234) <=. "xyz";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    #test binary expression

    #test unary exresion
    def test_unary_simple(self):
        input = """
            Function: foo
            Body:
                x = -x;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_unary_multiple(self):
        input = """
            Function: foo
            Body:
                x = !!!!!!!-.-.---.-.--.x;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_unary_multiple_wrong_order(self):
        input = """
            Function: foo
            Body:
                x = !!!!-.!!-.---.-.--.x;
            EndBody.
        """
        expect = "Error on line 4 col 26: !"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_unary_multiple_with_bracket(self):
        input = """
            Function: foo
            Body:
                x = !!!!-.(!!-.---.-.--.x);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    #test unary exresion

    #test index expression
    def test_index_simple(self):
        input = """
            Function: foo
            Body:
                x = a[123] + "sdsd";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_index_complex(self):
        input = """
            Function: foo
            Body:
                x[0x23A] = a[123 -. a[0o67] *. "abc" || 1.e45] + "sdsd";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    
    def test_index_recursive(self):
        input = """
            Function: foo
            Body:
                x = a[b[c[d[e[f[g[h[0]]]]]]]];
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_index_left_hand(self):
        input = """
            Function: foo
            Body:
                x[1 + 2] = 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_index_empty(self):
        input = """
            Function: foo
            Body:
                x[] = 0;
            EndBody.
        """
        expect = "Error on line 4 col 18: ]"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    #test index expression

    #test funcall
    def test_funcall_empty(self):
        input = """
            Function: foo
            Body:
                x = func();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_funcall_missing_para(self):
        input = """
            Function: foo
            Body:
                x = func(239, "abc", );
            EndBody.
        """
        expect = "Error on line 4 col 37: )"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_funcall_full_para(self):
        input = """
            Function: foo
            Body:
                x = func(6 + func() -. "anc", True || False);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    
    def test_funcall_left_hand(self):
        input = """
            Function: foo
            Body:
                func() = x;
            EndBody.
        """
        expect = "Error on line 4 col 23: ="
        self.assertTrue(TestParser.checkParser(input,expect,296))
    #test funcall

    #test custom
    def test_expr_left_hand(self):
        input = """
            Function: foo
            Body:
                x + y = y + x;
            EndBody.
        """
        expect = "Error on line 4 col 18: +"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_comment_0(self):
        input = """
            Function: foo
            Body:
                x = **0** 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_comment_1(self):
        input = """
            Function: foo
            Body:
                Var: **This 
                is 
                a 
                line 
                comment** a;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    #test custom 