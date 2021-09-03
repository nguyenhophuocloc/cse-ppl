# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01a9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n\5\3\5\6\5\u0098\n\5\r\5\16\5\u0099\3\6\3\6\5\6\u009e")
        buf.write("\n\6\3\6\5\6\u00a1\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\7\t\u00ad\n\t\f\t\16\t\u00b0\13\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3:\3:\7:\u0172\n:\f:\16:\u0175\13:\3:")
        buf.write("\3:\3:\3:\3:\3;\6;\u017d\n;\r;\16;\u017e\3;\3;\3<\3<\3")
        buf.write("<\3<\7<\u0187\n<\f<\16<\u018a\13<\3<\3<\3=\3=\3=\3=\7")
        buf.write("=\u0192\n=\f=\16=\u0195\13=\3=\3=\5=\u0199\n=\3=\3=\3")
        buf.write(">\3>\3>\3>\3>\3>\7>\u01a3\n>\f>\16>\u01a6\13>\3?\3?\3")
        buf.write("\u0173\2@\3\3\5\2\7\2\t\2\13\4\r\2\17\2\21\5\23\6\25\7")
        buf.write("\27\b\31\t\33\n\35\13\37\f!\r#\16%\17\'\20)\21+\22-\23")
        buf.write("/\24\61\25\63\26\65\27\67\309\31;\32=\33?\34A\35C\36E")
        buf.write("\37G I!K\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63")
        buf.write("o\64q\65s\66u\67w8y9{:};\3\2\f\5\2&&``c|\6\2\62;C\\aa")
        buf.write("c|\3\2\62;\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\5\2\f\f$")
        buf.write("$^^\5\2\13\f\16\17\"\"\t\2$$^^ddhhppttvv\3\2%%\2\u01b8")
        buf.write("\2\3\3\2\2\2\2\13\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\3\177\3\2\2\2\5\u0087\3\2\2\2\7\u008b\3")
        buf.write("\2\2\2\t\u0092\3\2\2\2\13\u009b\3\2\2\2\r\u00a2\3\2\2")
        buf.write("\2\17\u00a5\3\2\2\2\21\u00a8\3\2\2\2\23\u00b4\3\2\2\2")
        buf.write("\25\u00ba\3\2\2\2\27\u00c3\3\2\2\2\31\u00c6\3\2\2\2\33")
        buf.write("\u00cb\3\2\2\2\35\u00d0\3\2\2\2\37\u00d6\3\2\2\2!\u00da")
        buf.write("\3\2\2\2#\u00dd\3\2\2\2%\u00e0\3\2\2\2\'\u00e9\3\2\2\2")
        buf.write(")\u00ed\3\2\2\2+\u00f2\3\2\2\2-\u00f8\3\2\2\2/\u00fd\3")
        buf.write("\2\2\2\61\u0104\3\2\2\2\63\u010b\3\2\2\2\65\u0113\3\2")
        buf.write("\2\2\67\u011a\3\2\2\29\u011f\3\2\2\2;\u0125\3\2\2\2=\u012e")
        buf.write("\3\2\2\2?\u0130\3\2\2\2A\u0132\3\2\2\2C\u0134\3\2\2\2")
        buf.write("E\u0136\3\2\2\2G\u0138\3\2\2\2I\u013b\3\2\2\2K\u013e\3")
        buf.write("\2\2\2M\u0140\3\2\2\2O\u0143\3\2\2\2Q\u0145\3\2\2\2S\u0148")
        buf.write("\3\2\2\2U\u014a\3\2\2\2W\u014d\3\2\2\2Y\u0150\3\2\2\2")
        buf.write("[\u0153\3\2\2\2]\u0157\3\2\2\2_\u0159\3\2\2\2a\u015b\3")
        buf.write("\2\2\2c\u015d\3\2\2\2e\u015f\3\2\2\2g\u0161\3\2\2\2i\u0163")
        buf.write("\3\2\2\2k\u0165\3\2\2\2m\u0167\3\2\2\2o\u0169\3\2\2\2")
        buf.write("q\u016b\3\2\2\2s\u016d\3\2\2\2u\u017c\3\2\2\2w\u0182\3")
        buf.write("\2\2\2y\u018d\3\2\2\2{\u019c\3\2\2\2}\u01a7\3\2\2\2\177")
        buf.write("\u0083\t\2\2\2\u0080\u0082\t\3\2\2\u0081\u0080\3\2\2\2")
        buf.write("\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3")
        buf.write("\2\2\2\u0084\4\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0088")
        buf.write("\t\4\2\2\u0087\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\6\3\2\2\2\u008b")
        buf.write("\u008f\5m\67\2\u008c\u008e\t\4\2\2\u008d\u008c\3\2\2\2")
        buf.write("\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3")
        buf.write("\2\2\2\u0090\b\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0094")
        buf.write("\t\5\2\2\u0093\u0095\t\6\2\2\u0094\u0093\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0097\3\2\2\2\u0096\u0098\t\4\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u0097\3")
        buf.write("\2\2\2\u0099\u009a\3\2\2\2\u009a\n\3\2\2\2\u009b\u009d")
        buf.write("\5\5\3\2\u009c\u009e\5\7\4\2\u009d\u009c\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u00a0\3\2\2\2\u009f\u00a1\5\t\5\2")
        buf.write("\u00a0\u009f\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\f\3\2\2")
        buf.write("\2\u00a2\u00a3\7^\2\2\u00a3\u00a4\t\7\2\2\u00a4\16\3\2")
        buf.write("\2\2\u00a5\u00a6\7)\2\2\u00a6\u00a7\7$\2\2\u00a7\20\3")
        buf.write("\2\2\2\u00a8\u00ae\7$\2\2\u00a9\u00ad\5\r\7\2\u00aa\u00ad")
        buf.write("\5\17\b\2\u00ab\u00ad\n\b\2\2\u00ac\u00a9\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3")
        buf.write("\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7$\2\2\u00b2\u00b3")
        buf.write("\b\t\2\2\u00b3\22\3\2\2\2\u00b4\u00b5\7D\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9")
        buf.write("\7m\2\2\u00b9\24\3\2\2\2\u00ba\u00bb\7E\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7w\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\26\3\2\2\2\u00c3\u00c4\7K\2\2\u00c4\u00c5")
        buf.write("\7h\2\2\u00c5\30\3\2\2\2\u00c6\u00c7\7G\2\2\u00c7\u00c8")
        buf.write("\7n\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7h\2\2\u00ca\32")
        buf.write("\3\2\2\2\u00cb\u00cc\7G\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce")
        buf.write("\7u\2\2\u00ce\u00cf\7g\2\2\u00cf\34\3\2\2\2\u00d0\u00d1")
        buf.write("\7Y\2\2\u00d1\u00d2\7j\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\u00d5\7g\2\2\u00d5\36\3\2\2\2\u00d6\u00d7")
        buf.write("\7H\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7t\2\2\u00d9 \3")
        buf.write("\2\2\2\u00da\u00db\7Q\2\2\u00db\u00dc\7h\2\2\u00dc\"\3")
        buf.write("\2\2\2\u00dd\u00de\7K\2\2\u00de\u00df\7p\2\2\u00df$\3")
        buf.write("\2\2\2\u00e0\u00e1\7H\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3\u00e4\7e\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7p\2\2\u00e8&\3")
        buf.write("\2\2\2\u00e9\u00ea\7N\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec")
        buf.write("\7v\2\2\u00ec(\3\2\2\2\u00ed\u00ee\7V\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7w\2\2\u00f0\u00f1\7g\2\2\u00f1*\3")
        buf.write("\2\2\2\u00f2\u00f3\7H\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5")
        buf.write("\7n\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7\7g\2\2\u00f7,\3")
        buf.write("\2\2\2\u00f8\u00f9\7E\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb")
        buf.write("\7n\2\2\u00fb\u00fc\7n\2\2\u00fc.\3\2\2\2\u00fd\u00fe")
        buf.write("\7T\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7t\2\2\u0102\u0103\7p\2\2\u0103\60")
        buf.write("\3\2\2\2\u0104\u0105\7P\2\2\u0105\u0106\7w\2\2\u0106\u0107")
        buf.write("\7o\2\2\u0107\u0108\7d\2\2\u0108\u0109\7g\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\62\3\2\2\2\u010b\u010c\7D\2\2\u010c\u010d")
        buf.write("\7q\2\2\u010d\u010e\7q\2\2\u010e\u010f\7n\2\2\u010f\u0110")
        buf.write("\7g\2\2\u0110\u0111\7c\2\2\u0111\u0112\7p\2\2\u0112\64")
        buf.write("\3\2\2\2\u0113\u0114\7U\2\2\u0114\u0115\7v\2\2\u0115\u0116")
        buf.write("\7t\2\2\u0116\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118\u0119")
        buf.write("\7i\2\2\u0119\66\3\2\2\2\u011a\u011b\7L\2\2\u011b\u011c")
        buf.write("\7U\2\2\u011c\u011d\7Q\2\2\u011d\u011e\7P\2\2\u011e8\3")
        buf.write("\2\2\2\u011f\u0120\7C\2\2\u0120\u0121\7t\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7c\2\2\u0123\u0124\7{\2\2\u0124:\3")
        buf.write("\2\2\2\u0125\u0126\7E\2\2\u0126\u0127\7q\2\2\u0127\u0128")
        buf.write("\7p\2\2\u0128\u0129\7u\2\2\u0129\u012a\7v\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7p\2\2\u012c\u012d\7v\2\2\u012d<\3")
        buf.write("\2\2\2\u012e\u012f\7-\2\2\u012f>\3\2\2\2\u0130\u0131\7")
        buf.write("/\2\2\u0131@\3\2\2\2\u0132\u0133\7,\2\2\u0133B\3\2\2\2")
        buf.write("\u0134\u0135\7\61\2\2\u0135D\3\2\2\2\u0136\u0137\7\'\2")
        buf.write("\2\u0137F\3\2\2\2\u0138\u0139\7?\2\2\u0139\u013a\7?\2")
        buf.write("\2\u013aH\3\2\2\2\u013b\u013c\7#\2\2\u013c\u013d\7?\2")
        buf.write("\2\u013dJ\3\2\2\2\u013e\u013f\7@\2\2\u013fL\3\2\2\2\u0140")
        buf.write("\u0141\7@\2\2\u0141\u0142\7?\2\2\u0142N\3\2\2\2\u0143")
        buf.write("\u0144\7>\2\2\u0144P\3\2\2\2\u0145\u0146\7>\2\2\u0146")
        buf.write("\u0147\7?\2\2\u0147R\3\2\2\2\u0148\u0149\7#\2\2\u0149")
        buf.write("T\3\2\2\2\u014a\u014b\7(\2\2\u014b\u014c\7(\2\2\u014c")
        buf.write("V\3\2\2\2\u014d\u014e\7~\2\2\u014e\u014f\7~\2\2\u014f")
        buf.write("X\3\2\2\2\u0150\u0151\7-\2\2\u0151\u0152\7\60\2\2\u0152")
        buf.write("Z\3\2\2\2\u0153\u0154\7?\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("\u0156\7\60\2\2\u0156\\\3\2\2\2\u0157\u0158\7?\2\2\u0158")
        buf.write("^\3\2\2\2\u0159\u015a\7*\2\2\u015a`\3\2\2\2\u015b\u015c")
        buf.write("\7+\2\2\u015cb\3\2\2\2\u015d\u015e\7]\2\2\u015ed\3\2\2")
        buf.write("\2\u015f\u0160\7_\2\2\u0160f\3\2\2\2\u0161\u0162\7}\2")
        buf.write("\2\u0162h\3\2\2\2\u0163\u0164\7\177\2\2\u0164j\3\2\2\2")
        buf.write("\u0165\u0166\7<\2\2\u0166l\3\2\2\2\u0167\u0168\7\60\2")
        buf.write("\2\u0168n\3\2\2\2\u0169\u016a\7.\2\2\u016ap\3\2\2\2\u016b")
        buf.write("\u016c\7=\2\2\u016cr\3\2\2\2\u016d\u016e\7%\2\2\u016e")
        buf.write("\u016f\7%\2\2\u016f\u0173\3\2\2\2\u0170\u0172\13\2\2\2")
        buf.write("\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0174\3")
        buf.write("\2\2\2\u0173\u0171\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0173")
        buf.write("\3\2\2\2\u0176\u0177\7%\2\2\u0177\u0178\7%\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u017a\b:\3\2\u017at\3\2\2\2\u017b\u017d")
        buf.write("\t\t\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180\u0181\b;\3\2\u0181v\3\2\2\2\u0182\u0188\7$\2\2")
        buf.write("\u0183\u0187\5\r\7\2\u0184\u0187\5\17\b\2\u0185\u0187")
        buf.write("\n\b\2\2\u0186\u0183\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189\u018b\3\2\2\2\u018a\u0188\3")
        buf.write("\2\2\2\u018b\u018c\b<\4\2\u018cx\3\2\2\2\u018d\u0193\7")
        buf.write("$\2\2\u018e\u0192\5\r\7\2\u018f\u0192\5\17\b\2\u0190\u0192")
        buf.write("\n\b\2\2\u0191\u018e\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0193\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0193\3")
        buf.write("\2\2\2\u0196\u0198\7^\2\2\u0197\u0199\n\n\2\2\u0198\u0197")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\3\2\2\2\u019a")
        buf.write("\u019b\b=\5\2\u019bz\3\2\2\2\u019c\u019d\7%\2\2\u019d")
        buf.write("\u019e\7%\2\2\u019e\u01a4\3\2\2\2\u019f\u01a3\n\13\2\2")
        buf.write("\u01a0\u01a1\7%\2\2\u01a1\u01a3\n\13\2\2\u01a2\u019f\3")
        buf.write("\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5|\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a8\13\2\2\2\u01a8~\3\2\2\2\25\2\u0083")
        buf.write("\u0089\u008f\u0094\u0099\u009d\u00a0\u00ac\u00ae\u0173")
        buf.write("\u017e\u0186\u0188\u0191\u0193\u0198\u01a2\u01a4\6\3\t")
        buf.write("\2\b\2\2\3<\3\3=\4")
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

     


