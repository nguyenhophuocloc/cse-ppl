# Generated from d:\Python\Principles of Programming Languages v2\Assignment\assignment2-ver1.3\assignment2\initial\src\main\csel\parser\CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01ac\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\7\2\u0082\n\2\f")
        buf.write("\2\16\2\u0085\13\2\3\3\6\3\u0088\n\3\r\3\16\3\u0089\3")
        buf.write("\4\3\4\7\4\u008e\n\4\f\4\16\4\u0091\13\4\3\5\3\5\5\5\u0095")
        buf.write("\n\5\3\5\6\5\u0098\n\5\r\5\16\5\u0099\3\6\5\6\u009d\n")
        buf.write("\6\3\6\3\6\5\6\u00a1\n\6\3\6\5\6\u00a4\n\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u00b0\n\t\f\t\16\t\u00b3")
        buf.write("\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3:\7:\u0175")
        buf.write("\n:\f:\16:\u0178\13:\3:\3:\3:\3:\3:\3;\6;\u0180\n;\r;")
        buf.write("\16;\u0181\3;\3;\3<\3<\3<\3<\7<\u018a\n<\f<\16<\u018d")
        buf.write("\13<\3<\3<\3=\3=\3=\3=\7=\u0195\n=\f=\16=\u0198\13=\3")
        buf.write("=\3=\5=\u019c\n=\3=\3=\3>\3>\3>\3>\3>\3>\7>\u01a6\n>\f")
        buf.write(">\16>\u01a9\13>\3?\3?\3\u0176\2@\3\3\5\2\7\2\t\2\13\4")
        buf.write("\r\2\17\2\21\5\23\6\25\7\27\b\31\t\33\n\35\13\37\f!\r")
        buf.write("#\16%\17\'\20)\21+\22-\23/\24\61\25\63\26\65\27\67\30")
        buf.write("9\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[*]")
        buf.write("+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8y9{:};\3\2")
        buf.write("\f\5\2&&``c|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\t")
        buf.write("\2))^^ddhhppttvv\5\2\f\f$$^^\5\2\13\f\16\17\"\"\t\2$$")
        buf.write("^^ddhhppttvv\3\2%%\2\u01bc\2\3\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2")
        buf.write("\5\u0087\3\2\2\2\7\u008b\3\2\2\2\t\u0092\3\2\2\2\13\u009c")
        buf.write("\3\2\2\2\r\u00a5\3\2\2\2\17\u00a8\3\2\2\2\21\u00ab\3\2")
        buf.write("\2\2\23\u00b7\3\2\2\2\25\u00bd\3\2\2\2\27\u00c6\3\2\2")
        buf.write("\2\31\u00c9\3\2\2\2\33\u00ce\3\2\2\2\35\u00d3\3\2\2\2")
        buf.write("\37\u00d9\3\2\2\2!\u00dd\3\2\2\2#\u00e0\3\2\2\2%\u00e3")
        buf.write("\3\2\2\2\'\u00ec\3\2\2\2)\u00f0\3\2\2\2+\u00f5\3\2\2\2")
        buf.write("-\u00fb\3\2\2\2/\u0100\3\2\2\2\61\u0107\3\2\2\2\63\u010e")
        buf.write("\3\2\2\2\65\u0116\3\2\2\2\67\u011d\3\2\2\29\u0122\3\2")
        buf.write("\2\2;\u0128\3\2\2\2=\u0131\3\2\2\2?\u0133\3\2\2\2A\u0135")
        buf.write("\3\2\2\2C\u0137\3\2\2\2E\u0139\3\2\2\2G\u013b\3\2\2\2")
        buf.write("I\u013e\3\2\2\2K\u0141\3\2\2\2M\u0143\3\2\2\2O\u0146\3")
        buf.write("\2\2\2Q\u0148\3\2\2\2S\u014b\3\2\2\2U\u014d\3\2\2\2W\u0150")
        buf.write("\3\2\2\2Y\u0153\3\2\2\2[\u0156\3\2\2\2]\u015a\3\2\2\2")
        buf.write("_\u015c\3\2\2\2a\u015e\3\2\2\2c\u0160\3\2\2\2e\u0162\3")
        buf.write("\2\2\2g\u0164\3\2\2\2i\u0166\3\2\2\2k\u0168\3\2\2\2m\u016a")
        buf.write("\3\2\2\2o\u016c\3\2\2\2q\u016e\3\2\2\2s\u0170\3\2\2\2")
        buf.write("u\u017f\3\2\2\2w\u0185\3\2\2\2y\u0190\3\2\2\2{\u019f\3")
        buf.write("\2\2\2}\u01aa\3\2\2\2\177\u0083\t\2\2\2\u0080\u0082\t")
        buf.write("\3\2\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\4\3\2\2\2\u0085\u0083")
        buf.write("\3\2\2\2\u0086\u0088\t\4\2\2\u0087\u0086\3\2\2\2\u0088")
        buf.write("\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2")
        buf.write("\u008a\6\3\2\2\2\u008b\u008f\5m\67\2\u008c\u008e\t\4\2")
        buf.write("\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u008f\u0090\3\2\2\2\u0090\b\3\2\2\2\u0091\u008f")
        buf.write("\3\2\2\2\u0092\u0094\t\5\2\2\u0093\u0095\t\6\2\2\u0094")
        buf.write("\u0093\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2")
        buf.write("\u0096\u0098\t\4\2\2\u0097\u0096\3\2\2\2\u0098\u0099\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\n")
        buf.write("\3\2\2\2\u009b\u009d\7/\2\2\u009c\u009b\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\5\5\3\2")
        buf.write("\u009f\u00a1\5\7\4\2\u00a0\u009f\3\2\2\2\u00a0\u00a1\3")
        buf.write("\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u00a4\5\t\5\2\u00a3\u00a2")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\f\3\2\2\2\u00a5\u00a6")
        buf.write("\7^\2\2\u00a6\u00a7\t\7\2\2\u00a7\16\3\2\2\2\u00a8\u00a9")
        buf.write("\7)\2\2\u00a9\u00aa\7$\2\2\u00aa\20\3\2\2\2\u00ab\u00b1")
        buf.write("\7$\2\2\u00ac\u00b0\5\r\7\2\u00ad\u00b0\5\17\b\2\u00ae")
        buf.write("\u00b0\n\b\2\2\u00af\u00ac\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b4\u00b5\7$\2\2\u00b5\u00b6\b\t\2\2\u00b6")
        buf.write("\22\3\2\2\2\u00b7\u00b8\7D\2\2\u00b8\u00b9\7t\2\2\u00b9")
        buf.write("\u00ba\7g\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7m\2\2\u00bc")
        buf.write("\24\3\2\2\2\u00bd\u00be\7E\2\2\u00be\u00bf\7q\2\2\u00bf")
        buf.write("\u00c0\7p\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7k\2\2\u00c2")
        buf.write("\u00c3\7p\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5\7g\2\2\u00c5")
        buf.write("\26\3\2\2\2\u00c6\u00c7\7K\2\2\u00c7\u00c8\7h\2\2\u00c8")
        buf.write("\30\3\2\2\2\u00c9\u00ca\7G\2\2\u00ca\u00cb\7n\2\2\u00cb")
        buf.write("\u00cc\7k\2\2\u00cc\u00cd\7h\2\2\u00cd\32\3\2\2\2\u00ce")
        buf.write("\u00cf\7G\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7u\2\2\u00d1")
        buf.write("\u00d2\7g\2\2\u00d2\34\3\2\2\2\u00d3\u00d4\7Y\2\2\u00d4")
        buf.write("\u00d5\7j\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7n\2\2\u00d7")
        buf.write("\u00d8\7g\2\2\u00d8\36\3\2\2\2\u00d9\u00da\7H\2\2\u00da")
        buf.write("\u00db\7q\2\2\u00db\u00dc\7t\2\2\u00dc \3\2\2\2\u00dd")
        buf.write("\u00de\7Q\2\2\u00de\u00df\7h\2\2\u00df\"\3\2\2\2\u00e0")
        buf.write("\u00e1\7K\2\2\u00e1\u00e2\7p\2\2\u00e2$\3\2\2\2\u00e3")
        buf.write("\u00e4\7H\2\2\u00e4\u00e5\7w\2\2\u00e5\u00e6\7p\2\2\u00e6")
        buf.write("\u00e7\7e\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7k\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7p\2\2\u00eb&\3\2\2\2\u00ec")
        buf.write("\u00ed\7N\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7v\2\2\u00ef")
        buf.write("(\3\2\2\2\u00f0\u00f1\7V\2\2\u00f1\u00f2\7t\2\2\u00f2")
        buf.write("\u00f3\7w\2\2\u00f3\u00f4\7g\2\2\u00f4*\3\2\2\2\u00f5")
        buf.write("\u00f6\7H\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7n\2\2\u00f8")
        buf.write("\u00f9\7u\2\2\u00f9\u00fa\7g\2\2\u00fa,\3\2\2\2\u00fb")
        buf.write("\u00fc\7E\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7n\2\2\u00fe")
        buf.write("\u00ff\7n\2\2\u00ff.\3\2\2\2\u0100\u0101\7T\2\2\u0101")
        buf.write("\u0102\7g\2\2\u0102\u0103\7v\2\2\u0103\u0104\7w\2\2\u0104")
        buf.write("\u0105\7t\2\2\u0105\u0106\7p\2\2\u0106\60\3\2\2\2\u0107")
        buf.write("\u0108\7P\2\2\u0108\u0109\7w\2\2\u0109\u010a\7o\2\2\u010a")
        buf.write("\u010b\7d\2\2\u010b\u010c\7g\2\2\u010c\u010d\7t\2\2\u010d")
        buf.write("\62\3\2\2\2\u010e\u010f\7D\2\2\u010f\u0110\7q\2\2\u0110")
        buf.write("\u0111\7q\2\2\u0111\u0112\7n\2\2\u0112\u0113\7g\2\2\u0113")
        buf.write("\u0114\7c\2\2\u0114\u0115\7p\2\2\u0115\64\3\2\2\2\u0116")
        buf.write("\u0117\7U\2\2\u0117\u0118\7v\2\2\u0118\u0119\7t\2\2\u0119")
        buf.write("\u011a\7k\2\2\u011a\u011b\7p\2\2\u011b\u011c\7i\2\2\u011c")
        buf.write("\66\3\2\2\2\u011d\u011e\7L\2\2\u011e\u011f\7U\2\2\u011f")
        buf.write("\u0120\7Q\2\2\u0120\u0121\7P\2\2\u01218\3\2\2\2\u0122")
        buf.write("\u0123\7C\2\2\u0123\u0124\7t\2\2\u0124\u0125\7t\2\2\u0125")
        buf.write("\u0126\7c\2\2\u0126\u0127\7{\2\2\u0127:\3\2\2\2\u0128")
        buf.write("\u0129\7E\2\2\u0129\u012a\7q\2\2\u012a\u012b\7p\2\2\u012b")
        buf.write("\u012c\7u\2\2\u012c\u012d\7v\2\2\u012d\u012e\7c\2\2\u012e")
        buf.write("\u012f\7p\2\2\u012f\u0130\7v\2\2\u0130<\3\2\2\2\u0131")
        buf.write("\u0132\7-\2\2\u0132>\3\2\2\2\u0133\u0134\7/\2\2\u0134")
        buf.write("@\3\2\2\2\u0135\u0136\7,\2\2\u0136B\3\2\2\2\u0137\u0138")
        buf.write("\7\61\2\2\u0138D\3\2\2\2\u0139\u013a\7\'\2\2\u013aF\3")
        buf.write("\2\2\2\u013b\u013c\7?\2\2\u013c\u013d\7?\2\2\u013dH\3")
        buf.write("\2\2\2\u013e\u013f\7#\2\2\u013f\u0140\7?\2\2\u0140J\3")
        buf.write("\2\2\2\u0141\u0142\7@\2\2\u0142L\3\2\2\2\u0143\u0144\7")
        buf.write("@\2\2\u0144\u0145\7?\2\2\u0145N\3\2\2\2\u0146\u0147\7")
        buf.write(">\2\2\u0147P\3\2\2\2\u0148\u0149\7>\2\2\u0149\u014a\7")
        buf.write("?\2\2\u014aR\3\2\2\2\u014b\u014c\7#\2\2\u014cT\3\2\2\2")
        buf.write("\u014d\u014e\7(\2\2\u014e\u014f\7(\2\2\u014fV\3\2\2\2")
        buf.write("\u0150\u0151\7~\2\2\u0151\u0152\7~\2\2\u0152X\3\2\2\2")
        buf.write("\u0153\u0154\7-\2\2\u0154\u0155\7\60\2\2\u0155Z\3\2\2")
        buf.write("\2\u0156\u0157\7?\2\2\u0157\u0158\7?\2\2\u0158\u0159\7")
        buf.write("\60\2\2\u0159\\\3\2\2\2\u015a\u015b\7?\2\2\u015b^\3\2")
        buf.write("\2\2\u015c\u015d\7*\2\2\u015d`\3\2\2\2\u015e\u015f\7+")
        buf.write("\2\2\u015fb\3\2\2\2\u0160\u0161\7]\2\2\u0161d\3\2\2\2")
        buf.write("\u0162\u0163\7_\2\2\u0163f\3\2\2\2\u0164\u0165\7}\2\2")
        buf.write("\u0165h\3\2\2\2\u0166\u0167\7\177\2\2\u0167j\3\2\2\2\u0168")
        buf.write("\u0169\7<\2\2\u0169l\3\2\2\2\u016a\u016b\7\60\2\2\u016b")
        buf.write("n\3\2\2\2\u016c\u016d\7.\2\2\u016dp\3\2\2\2\u016e\u016f")
        buf.write("\7=\2\2\u016fr\3\2\2\2\u0170\u0171\7%\2\2\u0171\u0172")
        buf.write("\7%\2\2\u0172\u0176\3\2\2\2\u0173\u0175\13\2\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0177\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0177\u0179\3\2\2\2\u0178\u0176\3")
        buf.write("\2\2\2\u0179\u017a\7%\2\2\u017a\u017b\7%\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017c\u017d\b:\3\2\u017dt\3\2\2\2\u017e\u0180")
        buf.write("\t\t\2\2\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0184\b;\3\2\u0184v\3\2\2\2\u0185\u018b\7$\2\2")
        buf.write("\u0186\u018a\5\r\7\2\u0187\u018a\5\17\b\2\u0188\u018a")
        buf.write("\n\b\2\2\u0189\u0186\3\2\2\2\u0189\u0187\3\2\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018c\u018e\3\2\2\2\u018d\u018b\3")
        buf.write("\2\2\2\u018e\u018f\b<\4\2\u018fx\3\2\2\2\u0190\u0196\7")
        buf.write("$\2\2\u0191\u0195\5\r\7\2\u0192\u0195\5\17\b\2\u0193\u0195")
        buf.write("\n\b\2\2\u0194\u0191\3\2\2\2\u0194\u0192\3\2\2\2\u0194")
        buf.write("\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0199\3\2\2\2\u0198\u0196\3")
        buf.write("\2\2\2\u0199\u019b\7^\2\2\u019a\u019c\n\n\2\2\u019b\u019a")
        buf.write("\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019e\b=\5\2\u019ez\3\2\2\2\u019f\u01a0\7%\2\2\u01a0")
        buf.write("\u01a1\7%\2\2\u01a1\u01a7\3\2\2\2\u01a2\u01a6\n\13\2\2")
        buf.write("\u01a3\u01a4\7%\2\2\u01a4\u01a6\n\13\2\2\u01a5\u01a2\3")
        buf.write("\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8|\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01aa\u01ab\13\2\2\2\u01ab~\3\2\2\2\26\2\u0083")
        buf.write("\u0089\u008f\u0094\u0099\u009c\u00a0\u00a3\u00af\u00b1")
        buf.write("\u0176\u0181\u0189\u018b\u0194\u0196\u019b\u01a5\u01a7")
        buf.write("\6\3\t\2\b\2\2\3<\3\3=\4")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    NUMLIT = 2
    STRINGLIT = 3
    BREAK = 4
    CONTINUE = 5
    IF = 6
    ELIF = 7
    ELSE = 8
    WHILE = 9
    FOR = 10
    OF = 11
    IN = 12
    FUNCTION = 13
    LET = 14
    TRUE = 15
    FALSE = 16
    CALL = 17
    RETURN = 18
    NUMBER = 19
    BOOLEAN = 20
    STRING = 21
    JSON = 22
    ARRAY = 23
    CONSTANT = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    MOD = 29
    EQ = 30
    NEQ = 31
    GT = 32
    GTE = 33
    LT = 34
    LTE = 35
    NOT = 36
    AND = 37
    OR = 38
    SADD = 39
    SEQ = 40
    ASSIGN = 41
    LP = 42
    RP = 43
    LQP = 44
    RQP = 45
    LB = 46
    RB = 47
    COLON = 48
    DOT = 49
    CM = 50
    SM = 51
    COMMENT = 52
    WS = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55
    UNTERMINATED_COMMENT = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elif'", "'Else'", "'While'", 
            "'For'", "'Of'", "'In'", "'Function'", "'Let'", "'True'", "'False'", 
            "'Call'", "'Return'", "'Number'", "'Boolean'", "'String'", "'JSON'", 
            "'Array'", "'Constant'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'!'", "'&&'", 
            "'||'", "'+.'", "'==.'", "'='", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "':'", "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMLIT", "STRINGLIT", "BREAK", "CONTINUE", "IF", "ELIF", 
            "ELSE", "WHILE", "FOR", "OF", "IN", "FUNCTION", "LET", "TRUE", 
            "FALSE", "CALL", "RETURN", "NUMBER", "BOOLEAN", "STRING", "JSON", 
            "ARRAY", "CONSTANT", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
            "NEQ", "GT", "GTE", "LT", "LTE", "NOT", "AND", "OR", "SADD", 
            "SEQ", "ASSIGN", "LP", "RP", "LQP", "RQP", "LB", "RB", "COLON", 
            "DOT", "CM", "SM", "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "ID", "IPART", "DPART", "EPART", "NUMLIT", "ES", "DQ", 
                  "STRINGLIT", "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", 
                  "WHILE", "FOR", "OF", "IN", "FUNCTION", "LET", "TRUE", 
                  "FALSE", "CALL", "RETURN", "NUMBER", "BOOLEAN", "STRING", 
                  "JSON", "ARRAY", "CONSTANT", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "EQ", "NEQ", "GT", "GTE", "LT", "LTE", "NOT", "AND", 
                  "OR", "SADD", "SEQ", "ASSIGN", "LP", "RP", "LQP", "RQP", 
                  "LB", "RB", "COLON", "DOT", "CM", "SM", "COMMENT", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "CSEL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.STRINGLIT_action 
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = self.text[1:];

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:];

     


