import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
    def test_simple_program(self):
        """Simple program: int main() {} """
        input="""Let x;"""
        expect= "Program([VarDecl(Id(x),NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,200))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Let z[3];"""
        expect = "Program([VarDecl(Id(z),[NumberLiteral(3.0)],NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,201))

    def test_vardecl_scalar_with_init(self):
        input = """Let x = 10, y = "abc";"""
        expect = "Program([VarDecl(Id(x),NoneType,NumberLiteral(10.0)),VarDecl(Id(y),NoneType,StringLiteral(abc))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,202))

    def test_vardecl_composite(self):
        input = """Let z[123][10];"""
        expect = "Program([VarDecl(Id(z),[NumberLiteral(123.0)],NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,203))

    def test_vardecl_composite_with_init(self):
        input = """Let t[76] = [89, True, 1.2];"""
        expect = "Program([VarDecl(Id(t),[NumberLiteral(76.0)],NoneType,ArrayLiteral(NumberLiteral(89.0),BooleanLiteral(true),NumberLiteral(1.2)))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,204))
    
    def test_vardecl_array_literal_simple(self):
        input = """
            Let a = [1.2, 3e-7, 0.00];
            Let b[10][0] = [["abc", "def"], ["tnc\\n", "nttk"], ["'"'"", "\\t\\f\\r"]];
        """
        expect = "Program([VarDecl(Id(a),NoneType,ArrayLiteral(NumberLiteral(1.2),NumberLiteral(3e-07),NumberLiteral(0.0))),VarDecl(Id(b),[NumberLiteral(10.0)],NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,205))

    def test_vardecl_array_literal_empty(self):
        input = """
            Let c = [];
        """
        expect = "Program([VarDecl(Id(c),NoneType,ArrayLiteral())])"
        self.assertTrue(TestAST.checkASTGen(input,expect,206))
    
    def test_vardecl_array_literal_different_type(self):
        input = """
            Let d = [[], "x\\nt", True, [False, 3.e+89, 666]];
        """
        expect = "Program([VarDecl(Id(d),NoneType,ArrayLiteral(ArrayLiteral(),StringLiteral(x\nt),BooleanLiteral(true),ArrayLiteral(BooleanLiteral(false),NumberLiteral(3e+89),NumberLiteral(666.0))))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,207))

    def test_vardecl_array_literal_multilevel(self):
        input = """
            Let e = [[[[[[[]]]]]]];
        """
        expect = "Program([VarDecl(Id(e),NoneType,ArrayLiteral(ArrayLiteral(ArrayLiteral(ArrayLiteral(ArrayLiteral(ArrayLiteral(ArrayLiteral())))))))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,208))

    def test_vardecl_empty(self):
        input = """
            Let x:Number;
        """
        expect = "Program([VarDecl(Id(x),NumberType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,209))

    def test_vardecl_redeclare(self):
        input = """
            Let x = False, x = 123;
        """
        expect = "Program([VarDecl(Id(x),NoneType,BooleanLiteral(false)),VarDecl(Id(x),NoneType,NumberLiteral(123.0))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,210))
    #test variable declaration

    #test function declaration
    def test_funcdecl_empty(self):
        input = """
            Function foo()
            {

            }           
            
        """
        expect = "Program([FuncDecl(Id(foo)[],[])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,211))

    def test_funcdecl_nobody(self):
        input = """
            Function foo(a,x){}
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(a),NoneType),VarDecl(Id(x),NoneType)],[])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,212))
    
    def test_funcdecl_empty_parameter(self):
        input = """
            Function foo()
            {
                Let x:Number=10;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='x'), varDimen=None, typ=NumberType(), varInit=NumberLiteral(value=10.0))]])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,213))

    def test_funcdecl_simple_parameter(self):
        input = """
            Function foo(x, y[3,4,67])
            {
            }
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(x),NoneType),VarDecl(Id(y),[NumberLiteral(3.0),NumberLiteral(4.0),NumberLiteral(67.0)],NoneType)],[])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,214))

    def test_funcdecl_parameter_with_init(self):
        input = """
            Function foo(x[4])
            {
            }
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(x),[NumberLiteral(4.0)],NoneType)],[])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,215))

    def test_funcdecl_redeclare_parameter(self):
        input = """
            Function foo(x,x,x,x,x[123,456])
            {
            }
        """
        expect = "Program([FuncDecl(Id(foo)[VarDecl(Id(x),NoneType),VarDecl(Id(x),NoneType),VarDecl(Id(x),NoneType),VarDecl(Id(x),NoneType),VarDecl(Id(x),[NumberLiteral(123.0),NumberLiteral(456.0)],NoneType)],[])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,216))

    def test_funcdecl_redeclare_with_vardecl(self):
        input = """
            Let foo = True;

            Function foo()
            {
            }
        """
        expect = "Program([VarDecl(Id(foo),NoneType,BooleanLiteral(true)),FuncDecl(Id(foo)[],[])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[]),FuncDecl(Id(foo)[],[])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,218))

    def test_funcdecl_vardecl_wrong_order(self):
        input = """
            Function foo()
            {
            }

            Let x, y;
        """
        expect = "Program([FuncDecl(Id(foo)[],[]),VarDecl(Id(x),NoneType),VarDecl(Id(y),NoneType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,219))
    
    def test_funcdecl_body_with_vardecl(self):
        input = """
            Function foo()
            {
                Let x, y;
                Let z[123][456] = 1.234e-789;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='x'), varDimen=None, typ=NoneType(), varInit=None), VarDecl(variable=Id(name='y'), varDimen=None, typ=NoneType(), varInit=None)],[VarDecl(variable=Id(name='z'), varDimen=[NumberLiteral(value=123.0)], typ=NoneType(), varInit=None)]])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),NumberLiteral(10.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,221))

    def test_stmt_assign_array(self):
        input = """
            Function foo()
            {
                Let x= [12, True, "abc"];
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='x'), varDimen=None, typ=NoneType(), varInit=ArrayLiteral(value=[NumberLiteral(value=12.0), BooleanLiteral(value=True), StringLiteral(value='abc')]))]])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,222))

    def test_stmt_assign_arraycell(self):
        input = """
            Function foo()
            {
                x[3108] = 323.e-3;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(ArrayAccess(Id(x),[NumberLiteral(3108.0)]),NumberLiteral(0.323))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,223))

    def test_stmt_assign_expression(self):
        input = """
            Function foo()
            {
                x = 123 + "string";
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),BinaryOp(+,NumberLiteral(123.0),StringLiteral(string)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,224))
    #test assign stmt

    #test if stmt
    def test_stmt_if_only_if(self):
        input = """
            Function foo(){
                Let a = {
                    name: "Yanxi Place",
                    address: "Chinese Forbidden City"
                    };
                For key In a {
                    Call(printLn, ["Value of " + key + ": " + a{key}]);
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='a'), varDimen=None, typ=NoneType(), varInit=JSONLiteral(value=[(Id(name='name'), StringLiteral(value='Yanxi Place')), (Id(name='address'), StringLiteral(value='Chinese Forbidden City'))]))],ForIn(Id(key),Id(a),[CallStmt(Id(printLn),[BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLiteral(Value of ),Id(key)),StringLiteral(: )),JSONAccess(Id(a),[Id(key)]))])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,225))
    
    def test_stmt_if_only_if_empty_then(self):
        input = """
            Function foo()
            {
                If (True){
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(true),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,226))

    def test_stmt_if_only_if_no_then(self):
        input = """
            Function foo()
            {
                If (False){}                
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(false),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,227))

    def test_stmt_if_only_if_no_endif(self):
        input = """
            Function foo()
            {
                If (False) {
                Call(str_to_float,["abc"]);
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(false),[CallStmt(Id(str_to_float),[StringLiteral(abc)])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(false),[CallStmt(Id(str_to_float),[StringLiteral(abc)])])Else([Assign(Id(y),StringLiteral(0x23CD))])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(false),[CallStmt(Id(str_to_float),[StringLiteral(abc)])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(false),[CallStmt(Id(str_to_float),[StringLiteral(abc)])])ElseIf(BooleanLiteral(true),[Assign(Id(z),StringLiteral(xyz))])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(false),[])ElseIf(BinaryOp(!=,Id(m),Id(n)),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,232))

    def test_stmt_if_full(self):
        input = """
            Function foo()
            {
                If (False){x = 1; }
                Elif (m != n){x = 3;}
                Elif ("abc" + def){x = 123;}
                Else {x = 1.2e-3;
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(false),[Assign(Id(x),NumberLiteral(1.0))])ElseIf(BinaryOp(!=,Id(m),Id(n)),[Assign(Id(x),NumberLiteral(3.0))])ElseIf(BinaryOp(+,StringLiteral(abc),Id(def)),[Assign(Id(x),NumberLiteral(123.0))])Else([Assign(Id(x),NumberLiteral(0.0012))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,233))
    #test if stmt

    #test for stmt
    def test_stmt_for_empty(self):
        input = """
            Function foo()
            {
                For x In a {
                    x = x + 1;
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[ForIn(Id(x),Id(a),[Assign(Id(x),BinaryOp(+,Id(x),NumberLiteral(1.0)))])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[ForIn(Id(i),ArrayLiteral(NumberLiteral(0.0),NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0)),[Assign(Id(x),BinaryOp(+,Id(x),NumberLiteral(1.0)))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,235))

    def test_stmt_for_empty_body(self):
        input = """
            Function foo()
            {
                For i In [0,1,2,3,4]{
                   
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[ForIn(Id(i),ArrayLiteral(NumberLiteral(0.0),NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0),NumberLiteral(4.0)),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,236))

    def test_stmt_for_wrong_type_condition(self):
        input = """
            Function foo()
            {
                For i Of a{
                    x = x + 1;
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[ForOf(Id(i),Id(a),[Assign(Id(x),BinaryOp(+,Id(x),NumberLiteral(1.0)))])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[ForIn(Id(i),Id(a),[ForIn(Id(j),Id(a),[ForOf(Id(k),Id(b),[])])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Break()])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,239))

    def test_stmt_break_multiple(self):
        input = """
            Function foo()
            {
                Break;Break;Break;Break;Break;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Break(),Break(),Break(),Break(),Break()])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,240))

    def test_stmt_break_in_loop(self):
        input = """
            Function foo()
            {
                For j In a{
                    Break;
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[ForIn(Id(j),Id(a),[Break()])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(true),[Break()])Else([Break()])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Continue()])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Continue(),Continue(),Continue(),Continue()])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[ForIn(Id(j),Id(a),[Continue()])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(true),[Continue()])Else([Continue()])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[CallStmt(Id(println),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,247))

    def test_stmt_call_with_para(self):
        input = """
            Function foo()
            {
                Call(println,[True, x + y, 12 - 7, "anc"]);
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[CallStmt(Id(println),[BooleanLiteral(true),BinaryOp(+,Id(x),Id(y)),BinaryOp(-,NumberLiteral(12.0),NumberLiteral(7.0)),StringLiteral(anc)])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,248))

    def test_stmt_call_recursive(self):
        input = """
            Function foo()
            {
                Call(println,[Call(println,[Call(println,[zyasdad])])]);
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[CallStmt(Id(println),[CallExpr(Id(println),[CallExpr(Id(println),[Id(zyasdad)])])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,249))

    def test_stmt_call_unclosed(self):
        input = """
            Function foo()
            {
                Call(do_something,[123, 1.23e5, y * d]);
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[CallStmt(Id(do_something),[NumberLiteral(123.0),NumberLiteral(123000.0),BinaryOp(*,Id(y),Id(d))])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Return()])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Return(),Return(),Return(),Return()])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,252))

    def test_stmt_return_call_func(self):
        input = """
            Function foo()
            {
                Return Call(foo,[]);
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Return(CallExpr(Id(foo),[]))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,253))

    def test_stmt_return_valid(self):
        input = """
            Function foo()
            {
                Return True;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Return(BooleanLiteral(true))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,254))
    
    def test_stmt_return_array(self):
        input = """
            Function foo()
            {
                Let a[12] = [];
                Return a;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='a'), varDimen=[NumberLiteral(value=12.0)], typ=NoneType(), varInit=ArrayLiteral(value=[]))],Return(Id(a))])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[If(BooleanLiteral(true),[Return()])Else([Return()])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,257))

    def test_stmt_while_empty_condition(self):
        input = """
            Function foo()
            {
                While (a[5]>1){}
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[While(BinaryOp(>,ArrayAccess(Id(a),[NumberLiteral(5.0)]),NumberLiteral(1.0)),[])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[Assign(Id(x),BooleanLiteral(false))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,259))

    def test_stmt_while_with_break(self):
        input = """
            Function foo()
            {
                While (a>=b) {
                    Break;
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[While(BinaryOp(>=,Id(a),Id(b)),[Break()])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,260))

    def test_stmt_while_with_continue(self):
        input = """
            Function foo()
            {
                While (a==c) {
                    Continue;
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[While(BinaryOp(==,Id(a),Id(c)),[Continue()])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[While(BooleanLiteral(false),[While(Id(xyz),[CallStmt(Id(func),[])])])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[ForIn(Id(i),ArrayLiteral(NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)),[While(BooleanLiteral(false),[])])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[If(BinaryOp(&&,BooleanLiteral(true),StringLiteral(abc)),[Return()])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,264))

    def test_stmt_while_no_end_while(self):
        input = """
            Function foo()
            {
                While (True) {
                    If (True && "abc") { Return;
                    }
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[If(BinaryOp(&&,BooleanLiteral(true),StringLiteral(abc)),[Return()])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,266))

    def test_stmt_dowhile_empty_condition(self):
        input = """
            Function foo()
            {
                While (1){}
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[While(NumberLiteral(1.0),[])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,267))

    def test_stmt_dowhile_no_end_do(self):
        input = """
            Function foo()
            {
                While (True){
                    Call(do_something,[]);
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[CallStmt(Id(do_something),[])])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,268))

    def test_stmt_dowhile_simple_body(self):
        input = """
            Function foo()
            {
                Call(khongthetinnoi,[213, 232 - "abc", 3232]);
                While (True) {}
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[CallStmt(Id(khongthetinnoi),[NumberLiteral(213.0),BinaryOp(-,NumberLiteral(232.0),StringLiteral(abc)),NumberLiteral(3232.0)]),While(BooleanLiteral(true),[])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(NumberLiteral(1.0),[Break()])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(NumberLiteral(1.0),[Continue()])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[If(BinaryOp(<,Id(a),NumberLiteral(5.0)),[While(NumberLiteral(0.0),[While(Id(nothing),[])])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[ForIn(Id(i),ArrayLiteral(NumberLiteral(3.0),NumberLiteral(2.0),NumberLiteral(1.0)),[[VarDecl(variable=Id(name='x'), varDimen=None, typ=NoneType(), varInit=ArrayLiteral(value=[ArrayLiteral(value=[])]))]])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(true),[If(BooleanLiteral(true),[Return(CallExpr(Id(something),[]))])Else([Return()])])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[While(BooleanLiteral(false),[]),While(BooleanLiteral(true),[])])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),BinaryOp(>=,StringLiteral(abc),NumberLiteral(1.2))),Assign(Id(y),BinaryOp(<,BooleanLiteral(true),BooleanLiteral(true))),Assign(ArrayAccess(Id(z),[NumberLiteral(12.0)]),BinaryOp(/,Id(x),NumberLiteral(100.0)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,276))

    def test_binary_compare_invalid(self):
        input = """
            Function foo()
            {
                x = "abc" >= 1.2;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),BinaryOp(>=,StringLiteral(abc),NumberLiteral(1.2)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,277))

    def test_binary_logic_valid(self):
        input = """
            Function foo()
            {
                x = 123 && "abc";
                y = True || False && 1.2;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),BinaryOp(&&,NumberLiteral(123.0),StringLiteral(abc))),Assign(Id(y),BinaryOp(&&,BinaryOp(||,BooleanLiteral(true),BooleanLiteral(false)),NumberLiteral(1.2)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,278))

    def test_binary_locgic_invalid(self):
        input = """
            Function foo()
            {
                x = 123 &&"abc";
                y = True || False && 1.2;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),BinaryOp(&&,NumberLiteral(123.0),StringLiteral(abc))),Assign(Id(y),BinaryOp(&&,BinaryOp(||,BooleanLiteral(true),BooleanLiteral(false)),NumberLiteral(1.2)))])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='x'), varDimen=None, typ=NoneType(), varInit=None), VarDecl(variable=Id(name='y'), varDimen=None, typ=NoneType(), varInit=None)],Assign(Id(x),BinaryOp(*,BinaryOp(/,NumberLiteral(1.0),NumberLiteral(0.0)),NumberLiteral(56.0))),Assign(Id(y),BinaryOp(-,BinaryOp(*,NumberLiteral(1.2),NumberLiteral(0.0)),NumberLiteral(0.0089)))])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='x'), varDimen=None, typ=NoneType(), varInit=None), VarDecl(variable=Id(name='y'), varDimen=None, typ=NoneType(), varInit=None)],Assign(Id(x),BinaryOp(+.,BinaryOp(/,NumberLiteral(1.0),BooleanLiteral(true)),StringLiteral(123))),Assign(Id(y),BinaryOp(%,NumberLiteral(7.8),NumberLiteral(0.0)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,281))
    
    def test_binary_all(self):
        input = """
            Function foo()
            {
                Let x, y;
                x = y - x +. "123" - 456 * 056 == True % 2823 && False || 234;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='x'), varDimen=None, typ=NoneType(), varInit=None), VarDecl(variable=Id(name='y'), varDimen=None, typ=NoneType(), varInit=None)],Assign(Id(x),BinaryOp(+.,BinaryOp(-,Id(y),Id(x)),BinaryOp(==,BinaryOp(-,StringLiteral(123),BinaryOp(*,NumberLiteral(456.0),NumberLiteral(56.0))),BinaryOp(||,BinaryOp(&&,BinaryOp(%,BooleanLiteral(true),NumberLiteral(2823.0)),BooleanLiteral(false)),NumberLiteral(234.0)))))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,282))

    def test_binary_with_bracket(self):
        input = """
            Function foo()
            {
                Let x, y;
                x = y * x +. ("123" - 456 * (56 == True) % 2823) && (False || 234) <= "xyz";
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='x'), varDimen=None, typ=NoneType(), varInit=None), VarDecl(variable=Id(name='y'), varDimen=None, typ=NoneType(), varInit=None)],Assign(Id(x),BinaryOp(+.,BinaryOp(*,Id(y),Id(x)),BinaryOp(<=,BinaryOp(&&,BinaryOp(-,StringLiteral(123),BinaryOp(%,BinaryOp(*,NumberLiteral(456.0),BinaryOp(==,NumberLiteral(56.0),BooleanLiteral(true))),NumberLiteral(2823.0))),BinaryOp(||,BooleanLiteral(false),NumberLiteral(234.0))),StringLiteral(xyz))))])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),UnaryOp(-,Id(x)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,284))

    def test_unary_multiple(self):
        input = """
            Function foo()
            {
                x = !!!!!!!--------x;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(x)))))))))))))))))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,285))

    def test_unary_multiple_wrong_order(self):
        input = """
            Function foo()
            {
                x = !!!!!-------x;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(x))))))))))))))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,286))

    def test_unary_multiple_with_bracket(self):
        input = """
            Function foo()
            {
                x = !!!!-(!!-------x);
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(x))))))))))))))))])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),BinaryOp(+,ArrayAccess(Id(a),[NumberLiteral(123.0)]),StringLiteral(sdsd)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,288))

    def test_index_complex(self):
        input = """
            Function foo()
            {
                x[23] = a[123 - a[67] * "abc" || 1.e45] + "sdsd";
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(ArrayAccess(Id(x),[NumberLiteral(23.0)]),BinaryOp(+,ArrayAccess(Id(a),[BinaryOp(||,BinaryOp(-,NumberLiteral(123.0),BinaryOp(*,ArrayAccess(Id(a),[NumberLiteral(67.0)]),StringLiteral(abc))),NumberLiteral(1e+45))]),StringLiteral(sdsd)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,289))
    
    def test_index_recursive(self):
        input = """
            Function foo()
            {
                x = a[b[c[d[e[f[g[h[0]]]]]]]];
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),ArrayAccess(Id(a),[ArrayAccess(Id(b),[ArrayAccess(Id(c),[ArrayAccess(Id(d),[ArrayAccess(Id(e),[ArrayAccess(Id(f),[ArrayAccess(Id(g),[ArrayAccess(Id(h),[NumberLiteral(0.0)])])])])])])])]))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,290))

    def test_index_left_hand(self):
        input = """
            Function foo()
            {
                x[1 + 2] = 0;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(ArrayAccess(Id(x),[BinaryOp(+,NumberLiteral(1.0),NumberLiteral(2.0))]),NumberLiteral(0.0))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,291))

    def test_index_empty(self):
        input = """
            Function foo()
            {
                x[5] = 0;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(ArrayAccess(Id(x),[NumberLiteral(5.0)]),NumberLiteral(0.0))])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),CallExpr(Id(func),[]))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,293))

    def test_funcall_missing_para(self):
        input = """
            Function foo()
            {
                x = Call(func,[239, "abc"]);
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),CallExpr(Id(func),[NumberLiteral(239.0),StringLiteral(abc)]))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,294))

    def test_funcall_full_para(self):
        input = """
            Function foo()
            {
                x = Call(func,[6 + Call(func,[])]);
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),CallExpr(Id(func),[BinaryOp(+,NumberLiteral(6.0),CallExpr(Id(func),[]))]))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,295))
    
    def test_funcall_left_hand(self):
        input = """
            Function foo()
            {
                x=Call(func,[]);
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(x),CallExpr(Id(func),[]))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,296))
    #test funcall

    #test custom
    def test_expr_left_hand(self):
        input = """
            Function foo()
            {
                y = y + x;
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[Assign(Id(y),BinaryOp(+,Id(y),Id(x)))])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,297))

    def test_comment_0(self):
        input = """           	
                Function main() {
                    a{"name"}{"id"} = 5;
                }
        """
        expect = "Program([FuncDecl(Id(main)[],[Assign(JSONAccess(Id(a),[StringLiteral(name),StringLiteral(id)]),NumberLiteral(5.0))])])"
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
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='a'), varDimen=None, typ=NoneType(), varInit=None)]])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,299))
    #test custom 

    def test_final(self):
        input = """
            Function foo()
            {
                Let a:Number=0;
                For a In [1,2,3]{
                    x=a;
                }
            }
        """
        expect = "Program([FuncDecl(Id(foo)[],[[VarDecl(variable=Id(name='a'), varDimen=None, typ=NumberType(), varInit=NumberLiteral(value=0.0))],ForIn(Id(a),ArrayLiteral(NumberLiteral(1.0),NumberLiteral(2.0),NumberLiteral(3.0)),[Assign(Id(x),Id(a))])])])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    #test custom 
    def test_final1(self):
        input = """
           	Function main() {
                a{"name"}{"id"} = 5;
            }
        """
        expect = ""
        self.assertTrue(TestAST.checkASTGen(input,expect,400))