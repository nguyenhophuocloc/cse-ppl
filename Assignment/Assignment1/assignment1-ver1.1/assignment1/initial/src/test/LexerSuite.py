import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Let","Let,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Let x;","Let,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
    
    def test_keyword_all(self):
        self.assertTrue(TestLexer.checkLexeme("BreakContinueIfElifElseWhileForOfInFunctionLetTrueFalseCallReturnNumberBooleanStringJSONArrayConstant","Break,Continue,If,Elif,Else,While,For,Of,In,Function,Let,True,False,Call,Return,Number,Boolean,String,JSON,Array,Constant,<EOF>",108))
    #test keywords

    #test operators
    def test_operator_all(self):
        self.assertTrue(TestLexer.checkLexeme("+-*/%!&&||==!=><=>>=","+,-,*,/,%,!,&&,||,==,!=,>,<=,>,>=,<EOF>",109))

    def test_operator_invalid(self):
        self.assertTrue(TestLexer.checkLexeme("&|","Error Token &",110))
    #test operators

    #test literals
    def test_literal_int_decimal_valid(self):
        self.assertTrue(TestLexer.checkLexeme("-1234 0 9000","1234,0,9000,<EOF>",111))

    def test_literal_int_decimal_invalid_zero_first(self):
        self.assertTrue(TestLexer.checkLexeme("09","09,<EOF>",112))

    def test_literal_int_decimal_invalid_multiple_zero(self):
        self.assertTrue(TestLexer.checkLexeme("0000","0000,<EOF>",113))

    def test_literal_json_int_valid(self):
        self.assertTrue(TestLexer.checkLexeme("{number: 785}","{,number,:,785,},<EOF>",114))

    def test_literal_int_hexa_invalid_zero(self):
        self.assertTrue(TestLexer.checkLexeme("{Number: 785}","{,Number,:,785,},<EOF>",115))

    def test_literal_int_octa_valid(self):
        self.assertTrue(TestLexer.checkLexeme("0o1234567 0O76543210","0,o1234567,0,Error Token O",116))
    
    def test_literal_int_octa_invalid_zero(self):
        self.assertTrue(TestLexer.checkLexeme("0o0123","0,o0123,<EOF>",117))

    def test_literal_int_octa_invalid_digit(self):
        self.assertTrue(TestLexer.checkLexeme("0o89","0,o89,<EOF>",118))

    def test_literal_float_valid(self):
        self.assertTrue(TestLexer.checkLexeme("-1.3e-12 78. 00. 0e+12 02.03","1.3e-12,78.,00.,0e+12,02.03,<EOF>",119))

    def test_literal_float_invalid(self):
        self.assertTrue(TestLexer.checkLexeme(".09e-1",".,09e-1,<EOF>",120))

    def test_literal_bool_valid(self):
        self.assertTrue(TestLexer.checkLexeme("True False","True,False,<EOF>",121))

    def test_literal_bool_invalid(self):
        self.assertTrue(TestLexer.checkLexeme("true false TRUE FALSE","true,false,Error Token T",122))

    def test_literal_string_valid_simple(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string" ""","This is a string,<EOF>",123))

    def test_literal_string_valid_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is \\n\\f\\r\\b\\t\\\\ a string" ""","This is \\n\\f\\r\\b\\t\\\\ a string,<EOF>",124))

    def test_literal_string_valid_nested_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"This is a string'"" ""","'\"This is a string'\",<EOF>",125))

    def test_literal_string_invalid_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a \\a string" ""","Illegal Escape In String: This is a \\a",126))

    def test_literal_string_invalid_unclosed(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string ""","Unclosed String: This is a string ",127))

    def test_literal_string_valid_unclosed_nested_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"This is a string" ""","'\"This is a string,<EOF>",128))
    
    def test_literal_string_valid_unclosed_with_nested_quote(self):
        self.assertTrue(TestLexer.checkLexeme(""" "'"This is a string'" ""","Unclosed String: '\"This is a string'\" ",129))
    #test literals

    #test comments
    def test_comment_valid_simple(self):
        self.assertTrue(TestLexer.checkLexeme("##This is a comment##","<EOF>",130))

    def test_comment_valid_multiline(self):
        self.assertTrue(TestLexer.checkLexeme("##This \n is \n a \n multiline \n comment##","<EOF>",131))

    def test_comment_valid_empty(self):
        self.assertTrue(TestLexer.checkLexeme("####","<EOF>",132))

    def test_comment_valid_multiple(self):
        self.assertTrue(TestLexer.checkLexeme("##This is a comment####This is another comment##","<EOF>",133))

    def test_comment_valid_complex(self):
        self.assertTrue(TestLexer.checkLexeme("##!&#&@*#&!@!#^@!&!@$*^$&^!&@##","<EOF>",134))

    def test_comment_valid_escape(self):
        self.assertTrue(TestLexer.checkLexeme("""## \\\n\b\r\t\f\ ##""","<EOF>",135))

    def test_comment_invalid_unclosed(self):
        self.assertTrue(TestLexer.checkLexeme("##This is a comment","Unterminated Comment",136))

    def test_comment_invalid_half_unclosed(self):
        self.assertTrue(TestLexer.checkLexeme("##This is a comment#","Unterminated Comment",137))

    def test_comment_invalid_empty_unclosed(self):
        self.assertTrue(TestLexer.checkLexeme("##","Unterminated Comment",138))
    #test comments

    #test separators
    def test_separtor_valid_0(self):
        self.assertTrue(TestLexer.checkLexeme("[[]]()))():.,;[[]","[,[,],],(,),),),(,),:,.,,,;,[,[,],<EOF>",139))

    def test_separtor_valid_1(self):
        self.assertTrue(TestLexer.checkLexeme("Let ad,cd;","Let,ad,,,cd,;,<EOF>",140))

    def test_separtor_valid_2(self):
        self.assertTrue(TestLexer.checkLexeme("Let ad,cd;","Let,ad,,,cd,;,<EOF>",141))

    def test_separtor_valid_3(self):
        self.assertTrue(TestLexer.checkLexeme("[gg](123][,.:]()[.]","[,gg,],(,123,],[,,,.,:,],(,),[,.,],<EOF>",142))

    def test_separtor_valid_4(self):
        self.assertTrue(TestLexer.checkLexeme("(Let a = 45;)[Body EndBody.]","(,Let,a,=,45,;,),[,Error Token B",143))
    
    def test_separator_invalid_0(self):
        self.assertTrue(TestLexer.checkLexeme("[[]]()))():.,;[[]{","[,[,],],(,),),),(,),:,.,,,;,[,[,],{,<EOF>",144))

    def test_separator_invalid_1(self):
        self.assertTrue(TestLexer.checkLexeme("foo(a[789]) } Let ad,cd;","foo,(,a,[,789,],),},Let,ad,,,cd,;,<EOF>",145))

    def test_separator_invalid_2(self):
        self.assertTrue(TestLexer.checkLexeme("[[[]]]([])_:,.,","[,[,[,],],],(,[,],),Error Token _",146))

    def test_separator_invalid_3(self):
        self.assertTrue(TestLexer.checkLexeme("[gg](123][,.:]{}()[.]","[,gg,],(,123,],[,,,.,:,],{,},(,),[,.,],<EOF>",147))

    def test_separator_invalid_4(self):
        self.assertTrue(TestLexer.checkLexeme("(Let a = 45_;)[Body EndBody.]","(,Let,a,=,45,Error Token _",148))
    #test separators

    #test white space
    def test_ws_only(self):
        self.assertTrue(TestLexer.checkLexeme(" \n\f\r\t","<EOF>",149))

    def test_ws_with_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("a\nb\fc\rd\te","a,b,c,d,e,<EOF>",150))

    def test_ws_complex(self):
        self.assertTrue(TestLexer.checkLexeme("abc\n\"789.12\"\f12.e-13\r33\ttrue","abc,789.12,12.e-13,0x33,true,<EOF>",151))
    #test while space

    #test int literal
    def test_intlit_0(self):
        self.assertTrue(TestLexer.checkLexeme("-8909 09878+3287","-,8909,0,9878,+,3287,<EOF>",152))
        
    def test_intlit_1(self):
        self.assertTrue(TestLexer.checkLexeme("89 - 76 != 98-042","89,-,76,!=,98,-042,<EOF>",153))
    
    def test_intlit_2(self):
        self.assertTrue(TestLexer.checkLexeme("7 !=88 - 00 + 7","7,!=,88,-,00,+,7,<EOF>",154))
        
    def test_intlit_3(self):
        self.assertTrue(TestLexer.checkLexeme("98 + 6 - 77 != 97","98,+,6,-,77,!=,97,<EOF>",155))
        
    def test_intlit_4(self):
        self.assertTrue(TestLexer.checkLexeme("7 - 5 -18 == 23 && 76","7,-,5,-18,==,23,&&,76,<EOF>",156))

    def test_intlit_5(self):
        self.assertTrue(TestLexer.checkLexeme("-98 78 2 8","-98,78,2,8,<EOF>",157))
        
    def test_intlit_6(self):
        self.assertTrue(TestLexer.checkLexeme("45 542","45,542,<EOF>",158))
        
    def test_intlit_7(self):
        self.assertTrue(TestLexer.checkLexeme("98 987 678 A","98,987,678,Error Token A",159))
        
    def test_intlit_8(self):
        self.assertTrue(TestLexer.checkLexeme("56 76","56,76,<EOF>",160))
        
    def test_intlit_9(self):
        self.assertTrue(TestLexer.checkLexeme("955846 - 54848 + 878 - 56","955846,-,54848,+,878,-,56,<EOF>",161))
    #test int literal

    #test float literal
    def test_floatlit_0(self):
        self.assertTrue(TestLexer.checkLexeme("0.0e-4 45E23 254e-56","0.0e-4,45E23,254e-56,<EOF>",162))
        
    def test_floatlit_1(self):
        self.assertTrue(TestLexer.checkLexeme("0E-89 2356e89 0E0 ","0E-89,2356e89,0E0,<EOF>",163))
        
    def test_floatlit_2(self):
        self.assertTrue(TestLexer.checkLexeme("000E-000 9867. 5674.e-0","000E-000,9867.,5674.e-0,<EOF>",164))
        
    def test_floatlit_3(self):
        self.assertTrue(TestLexer.checkLexeme("4587.E00000 6754.e-00000 4530.0000e3","4587.E00000,6754.e-00000,4530.0000e3,<EOF>",165))
        
    def test_floatlit_4(self):
        self.assertTrue(TestLexer.checkLexeme("456789.0e0 0.0e0 12345.E-0","456789.0e0,0.0e0,12345.E-0,<EOF>",166))

    def test_floatlit_5(self):
        self.assertTrue(TestLexer.checkLexeme("0.0e-4 45E23 254e-56","0.0e-4,45E23,254e-56,<EOF>",167))
        
    def test_floatlit_6(self):
        self.assertTrue(TestLexer.checkLexeme("0E-89 2356e89 0E0 ","0E-89,2356e89,0E0,<EOF>",168))
        
    def test_floatlit_7(self): 
        self.assertTrue(TestLexer.checkLexeme("000E-000 9867. 5674.e-0","000E-000,9867.,5674.e-0,<EOF>",169))
        
    def test_floatlit_8(self):
        self.assertTrue(TestLexer.checkLexeme("4587.E00000 6754.e-00000 4530.0000e3","4587.E00000,6754.e-00000,4530.0000e3,<EOF>",170))
        
    def test_floatlit_9(self):
        self.assertTrue(TestLexer.checkLexeme("456789.0e0 0.0e0 12345.E-0","456789.0e0,0.0e0,12345.E-0,<EOF>",171))
    #test float literal

    #test string literal
    def test_stringlit_0(self):
        self.assertTrue(TestLexer.checkLexeme(""" "nguyen ly" ""","nguyen ly,<EOF>",172))
        
    def test_stringlit_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """,",<EOF>",173))
        
    def test_stringlit_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string<0x08>adwd" ""","""This is a string<0x08>adwd,<EOF>""",174))
        
    def test_stringlit_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab " ""","This is a string containing tab ,<EOF>",175))
        
    def test_stringlit_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is unclose string ""","Unclosed String: This is unclose string ",176))
    #test string literal

    #test more operators
    def test_operator_0(self):
        self.assertTrue(TestLexer.checkLexeme("""+-*/""","+,-,*,/,<EOF>",177))

    def test_operator_1(self):
        self.assertTrue(TestLexer.checkLexeme("a+b-c+d+.f!a","a,+,b,-,c,+,d,+.,f,!,a,<EOF>",178))
        
    def test_operator_2(self):
        self.assertTrue(TestLexer.checkLexeme("%!&&||==!=<><=>==/","%,!,&&,||,==,!=,<,>,<=,>=,=,/,<EOF>",179))
        
    def test_operator_3(self):
        self.assertTrue(TestLexer.checkLexeme("+%!==||","+,%,!=,=,||,<EOF>",180))
        
    def test_operator_4(self):
        self.assertTrue(TestLexer.checkLexeme("++++----<=>===","+,+,+,+,-,-,-,-,<=,>=,==,<EOF>",181))
        
    def test_operator_5(self):
        self.assertTrue(TestLexer.checkLexeme("!!====/=++-<>","!,!=,==,=,/,=,+,+,-,<,>,<EOF>",182))
        
    def test_operator_6(self):
        self.assertTrue(TestLexer.checkLexeme(">=<=<>+++-&&||%",">=,<=,<,>,+,+,+,-,&&,||,%,<EOF>",183))
    #test more operators

    #test custom
    def test_custom_0(self):
        self.assertTrue(TestLexer.checkLexeme("""##No function name##{Let r = 10., $v;v = (4. / 3.) *. 3.14 *. r *. r *. r;}""","{,Let,r,=,10.,,,$v,;,v,=,(,4.,/,3.,),*,.,3.14,*,.,r,*,.,r,*,.,r,;,},<EOF>",184))
        
    def test_custom_1(self):
        self.assertTrue(TestLexer.checkLexeme("""Call(foo,[2 + x, 4. /. y]);**foo call** goo ();""","Call,(,foo,,,[,2,+,x,,,4.,/,.,y,],),;,*,*,foo,call,*,*,goo,(,),;,<EOF>",185))
        
    def test_custom_2(self):
        self.assertTrue(TestLexer.checkLexeme("""For @(i = 0, i < 10, i = i + 2) Do writeln(i)**write i in new line**; EndFor.""","For,Error Token @",186))
        
    def test_custom_3(self):
        self.assertTrue(TestLexer.checkLexeme("""For (i = 0, i < 10, i = i + 2) DO writeln(i); EndFor.""","For,(,i,=,0,,,i,<,10,,,i,=,i,+,2,),Error Token D",187))
        
    def test_custom_4(self):
        self.assertTrue(TestLexer.checkLexeme("""Function foo(a[5], b)##this is parameter##{Let i= 0;While (i < 5){a[i] = b + 1.0;i = i + 1;}}""","Function,foo,(,a,[,5,],,,b,),{,Let,i,=,0,;,While,(,i,<,5,),{,a,[,i,],=,b,+,1.0,;,i,=,i,+,1,;,},},<EOF>",188))
        
    def test_custom_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" Var: day,month,year; Function main& Body: If(day == 22) Return True EndBody.""","Error Token V",189))
        
    def test_custom_6(self):
        self.assertTrue(TestLexer.checkLexeme("""Body:Var: r = 10.,  v;v = (4. / 3.) *. 3.14 *. r *. r *. r;EnDBody.""","Error Token B",190))
        
    def test_custom_7(self):
        self.assertTrue(TestLexer.checkLexeme("""Let: day,month,year; Function main Body: If(day == 22`) Return True EndBody.""","Let,:,day,,,month,,,year,;,Function,main,Error Token B",191))
        
    def test_custom_8(self):
        self.assertTrue(TestLexer.checkLexeme("""LeT: a[5];Var: b`[2][3];""","Error Token L",192))
        
    def test_custom_9(self):
        self.assertTrue(TestLexer.checkLexeme("""Function split(){sring.split();}""","Function,split,(,),{,sring,.,split,(,),;,},<EOF>",193))
        
    def test_custom_10(self):
        self.assertTrue(TestLexer.checkLexeme("""Function split (string){string.split()}""","Function,split,(,string,),{,string,.,split,(,),},<EOF>",194))
        
    def test_custom_11(self):
        self.assertTrue(TestLexer.checkLexeme("""Let day,month,year; Function main(){If(day == 22){Return True} }""","Let,day,,,month,,,year,;,Function,main,(,),{,If,(,day,==,22,),{,Return,True,},},<EOF>",195))
        
    def test_custom_12(self):
        self.assertTrue(TestLexer.checkLexeme("""FunCTion foo(a[5], b)##this is parameter##{Let i= 0;While (i < 5){a[i] = b + 1.0;i = i + 1;}}""","Error Token F",196))
        
    def test_custom_13(self):
        self.assertTrue(TestLexer.checkLexeme("a[3 + Call(foo,[2])] = a[b[2][3]] + 4;","a,[,3,+,Call,(,foo,,,[,2,],),],=,a,[,b,[,2,],[,3,],],+,4,;,<EOF>",197))
        
    def test_custom_14(self):
        self.assertTrue(TestLexer.checkLexeme("a[3 + Call(foo,[2])] = a[b[2][3]] + 4;##asign statement##","a,[,3,+,Call,(,foo,,,[,2,],),],=,a,[,b,[,2,],[,3,],],+,4,;,<EOF>",198))
    
    def test_custom_15(self):
        self.assertTrue(TestLexer.checkLexeme("""Call(foo,[2 + x, 4. /y]); Goo ?();""","Call,(,foo,,,[,2,+,x,,,4.,/,y,],),;,Error Token G",199))
    
    def test_json(self):
        self.assertTrue(TestLexer.checkLexeme("""{name:"Yanxi",surface:6}""","{,name,:,Yanxi,,,surface,:,6,},<EOF>",200))
    #test custom
