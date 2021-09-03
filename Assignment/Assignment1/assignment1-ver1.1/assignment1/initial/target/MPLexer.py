# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01b3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\7\3\u0089\n\3\f\3\16\3\u008c\13\3\3\4\5\4\u008f")
        buf.write("\n\4\3\4\6\4\u0092\n\4\r\4\16\4\u0093\3\5\3\5\7\5\u0098")
        buf.write("\n\5\f\5\16\5\u009b\13\5\3\6\3\6\5\6\u009f\n\6\3\6\6\6")
        buf.write("\u00a2\n\6\r\6\16\6\u00a3\3\7\3\7\5\7\u00a8\n\7\3\7\5")
        buf.write("\7\u00ab\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7")
        buf.write("\n\u00b7\n\n\f\n\16\n\u00ba\13\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(")
        buf.write("\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3")
        buf.write(";\3;\3;\3;\7;\u017c\n;\f;\16;\u017f\13;\3;\3;\3;\3;\3")
        buf.write(";\3<\6<\u0187\n<\r<\16<\u0188\3<\3<\3=\3=\3=\3=\7=\u0191")
        buf.write("\n=\f=\16=\u0194\13=\3=\3=\3>\3>\3>\3>\7>\u019c\n>\f>")
        buf.write("\16>\u019f\13>\3>\3>\5>\u01a3\n>\3>\3>\3?\3?\3?\3?\3?")
        buf.write("\3?\7?\u01ad\n?\f?\16?\u01b0\13?\3@\3@\3\u017d\2A\3\3")
        buf.write("\5\4\7\2\t\2\13\2\r\5\17\2\21\2\23\6\25\7\27\b\31\t\33")
        buf.write("\n\35\13\37\f!\r#\16%\17\'\20)\21+\22-\23/\24\61\25\63")
        buf.write("\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O")
        buf.write("$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u")
        buf.write("\67w8y9{:};\177<\3\2\r\5\2&&``c|\6\2\62;C\\aac|\3\2//")
        buf.write("\3\2\62;\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\5\2\f\f$$^")
        buf.write("^\5\2\13\f\16\17\"\"\t\2$$^^ddhhppttvv\3\2,,\2\u01c3\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u0086\3\2\2")
        buf.write("\2\7\u008e\3\2\2\2\t\u0095\3\2\2\2\13\u009c\3\2\2\2\r")
        buf.write("\u00a5\3\2\2\2\17\u00ac\3\2\2\2\21\u00af\3\2\2\2\23\u00b2")
        buf.write("\3\2\2\2\25\u00be\3\2\2\2\27\u00c4\3\2\2\2\31\u00cd\3")
        buf.write("\2\2\2\33\u00d0\3\2\2\2\35\u00d5\3\2\2\2\37\u00da\3\2")
        buf.write("\2\2!\u00e0\3\2\2\2#\u00e4\3\2\2\2%\u00e7\3\2\2\2\'\u00ea")
        buf.write("\3\2\2\2)\u00f3\3\2\2\2+\u00f7\3\2\2\2-\u00fc\3\2\2\2")
        buf.write("/\u0102\3\2\2\2\61\u0107\3\2\2\2\63\u010e\3\2\2\2\65\u0115")
        buf.write("\3\2\2\2\67\u011d\3\2\2\29\u0124\3\2\2\2;\u0129\3\2\2")
        buf.write("\2=\u012f\3\2\2\2?\u0138\3\2\2\2A\u013a\3\2\2\2C\u013c")
        buf.write("\3\2\2\2E\u013e\3\2\2\2G\u0140\3\2\2\2I\u0142\3\2\2\2")
        buf.write("K\u0145\3\2\2\2M\u0148\3\2\2\2O\u014a\3\2\2\2Q\u014d\3")
        buf.write("\2\2\2S\u014f\3\2\2\2U\u0152\3\2\2\2W\u0154\3\2\2\2Y\u0157")
        buf.write("\3\2\2\2[\u015a\3\2\2\2]\u015d\3\2\2\2_\u0161\3\2\2\2")
        buf.write("a\u0163\3\2\2\2c\u0165\3\2\2\2e\u0167\3\2\2\2g\u0169\3")
        buf.write("\2\2\2i\u016b\3\2\2\2k\u016d\3\2\2\2m\u016f\3\2\2\2o\u0171")
        buf.write("\3\2\2\2q\u0173\3\2\2\2s\u0175\3\2\2\2u\u0177\3\2\2\2")
        buf.write("w\u0186\3\2\2\2y\u018c\3\2\2\2{\u0197\3\2\2\2}\u01a6\3")
        buf.write("\2\2\2\177\u01b1\3\2\2\2\u0081\u0082\7L\2\2\u0082\u0083")
        buf.write("\7u\2\2\u0083\u0084\7q\2\2\u0084\u0085\7p\2\2\u0085\4")
        buf.write("\3\2\2\2\u0086\u008a\t\2\2\2\u0087\u0089\t\3\2\2\u0088")
        buf.write("\u0087\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2")
        buf.write("\u008a\u008b\3\2\2\2\u008b\6\3\2\2\2\u008c\u008a\3\2\2")
        buf.write("\2\u008d\u008f\t\4\2\2\u008e\u008d\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u0092\t\5\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0093\u0094\3\2\2\2\u0094\b\3\2\2\2\u0095\u0099\5o8\2")
        buf.write("\u0096\u0098\t\5\2\2\u0097\u0096\3\2\2\2\u0098\u009b\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\n")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e\t\6\2\2\u009d")
        buf.write("\u009f\t\7\2\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a1\3\2\2\2\u00a0\u00a2\t\5\2\2\u00a1\u00a0\3")
        buf.write("\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\f\3\2\2\2\u00a5\u00a7\5\7\4\2\u00a6\u00a8")
        buf.write("\5\t\5\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00ab\5\13\6\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00ab\16\3\2\2\2\u00ac\u00ad\7")
        buf.write("^\2\2\u00ad\u00ae\t\b\2\2\u00ae\20\3\2\2\2\u00af\u00b0")
        buf.write("\7)\2\2\u00b0\u00b1\7$\2\2\u00b1\22\3\2\2\2\u00b2\u00b8")
        buf.write("\7$\2\2\u00b3\u00b7\5\17\b\2\u00b4\u00b7\5\21\t\2\u00b5")
        buf.write("\u00b7\n\t\2\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3")
        buf.write("\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00bb\u00bc\7$\2\2\u00bc\u00bd\b\n\2\2\u00bd")
        buf.write("\24\3\2\2\2\u00be\u00bf\7D\2\2\u00bf\u00c0\7t\2\2\u00c0")
        buf.write("\u00c1\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3\7m\2\2\u00c3")
        buf.write("\26\3\2\2\2\u00c4\u00c5\7E\2\2\u00c5\u00c6\7q\2\2\u00c6")
        buf.write("\u00c7\7p\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9\7k\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\u00cb\7w\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\30\3\2\2\2\u00cd\u00ce\7K\2\2\u00ce\u00cf\7h\2\2\u00cf")
        buf.write("\32\3\2\2\2\u00d0\u00d1\7G\2\2\u00d1\u00d2\7n\2\2\u00d2")
        buf.write("\u00d3\7k\2\2\u00d3\u00d4\7h\2\2\u00d4\34\3\2\2\2\u00d5")
        buf.write("\u00d6\7G\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7u\2\2\u00d8")
        buf.write("\u00d9\7g\2\2\u00d9\36\3\2\2\2\u00da\u00db\7Y\2\2\u00db")
        buf.write("\u00dc\7j\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7n\2\2\u00de")
        buf.write("\u00df\7g\2\2\u00df \3\2\2\2\u00e0\u00e1\7H\2\2\u00e1")
        buf.write("\u00e2\7q\2\2\u00e2\u00e3\7t\2\2\u00e3\"\3\2\2\2\u00e4")
        buf.write("\u00e5\7Q\2\2\u00e5\u00e6\7h\2\2\u00e6$\3\2\2\2\u00e7")
        buf.write("\u00e8\7K\2\2\u00e8\u00e9\7p\2\2\u00e9&\3\2\2\2\u00ea")
        buf.write("\u00eb\7H\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\u00ee\7e\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7k\2\2\u00f0")
        buf.write("\u00f1\7q\2\2\u00f1\u00f2\7p\2\2\u00f2(\3\2\2\2\u00f3")
        buf.write("\u00f4\7N\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7v\2\2\u00f6")
        buf.write("*\3\2\2\2\u00f7\u00f8\7V\2\2\u00f8\u00f9\7t\2\2\u00f9")
        buf.write("\u00fa\7w\2\2\u00fa\u00fb\7g\2\2\u00fb,\3\2\2\2\u00fc")
        buf.write("\u00fd\7H\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7n\2\2\u00ff")
        buf.write("\u0100\7u\2\2\u0100\u0101\7g\2\2\u0101.\3\2\2\2\u0102")
        buf.write("\u0103\7E\2\2\u0103\u0104\7c\2\2\u0104\u0105\7n\2\2\u0105")
        buf.write("\u0106\7n\2\2\u0106\60\3\2\2\2\u0107\u0108\7T\2\2\u0108")
        buf.write("\u0109\7g\2\2\u0109\u010a\7v\2\2\u010a\u010b\7w\2\2\u010b")
        buf.write("\u010c\7t\2\2\u010c\u010d\7p\2\2\u010d\62\3\2\2\2\u010e")
        buf.write("\u010f\7P\2\2\u010f\u0110\7w\2\2\u0110\u0111\7o\2\2\u0111")
        buf.write("\u0112\7d\2\2\u0112\u0113\7g\2\2\u0113\u0114\7t\2\2\u0114")
        buf.write("\64\3\2\2\2\u0115\u0116\7D\2\2\u0116\u0117\7q\2\2\u0117")
        buf.write("\u0118\7q\2\2\u0118\u0119\7n\2\2\u0119\u011a\7g\2\2\u011a")
        buf.write("\u011b\7c\2\2\u011b\u011c\7p\2\2\u011c\66\3\2\2\2\u011d")
        buf.write("\u011e\7U\2\2\u011e\u011f\7v\2\2\u011f\u0120\7t\2\2\u0120")
        buf.write("\u0121\7k\2\2\u0121\u0122\7p\2\2\u0122\u0123\7i\2\2\u0123")
        buf.write("8\3\2\2\2\u0124\u0125\7L\2\2\u0125\u0126\7U\2\2\u0126")
        buf.write("\u0127\7Q\2\2\u0127\u0128\7P\2\2\u0128:\3\2\2\2\u0129")
        buf.write("\u012a\7C\2\2\u012a\u012b\7t\2\2\u012b\u012c\7t\2\2\u012c")
        buf.write("\u012d\7c\2\2\u012d\u012e\7{\2\2\u012e<\3\2\2\2\u012f")
        buf.write("\u0130\7E\2\2\u0130\u0131\7q\2\2\u0131\u0132\7p\2\2\u0132")
        buf.write("\u0133\7u\2\2\u0133\u0134\7v\2\2\u0134\u0135\7c\2\2\u0135")
        buf.write("\u0136\7p\2\2\u0136\u0137\7v\2\2\u0137>\3\2\2\2\u0138")
        buf.write("\u0139\7-\2\2\u0139@\3\2\2\2\u013a\u013b\7/\2\2\u013b")
        buf.write("B\3\2\2\2\u013c\u013d\7,\2\2\u013dD\3\2\2\2\u013e\u013f")
        buf.write("\7\61\2\2\u013fF\3\2\2\2\u0140\u0141\7\'\2\2\u0141H\3")
        buf.write("\2\2\2\u0142\u0143\7?\2\2\u0143\u0144\7?\2\2\u0144J\3")
        buf.write("\2\2\2\u0145\u0146\7#\2\2\u0146\u0147\7?\2\2\u0147L\3")
        buf.write("\2\2\2\u0148\u0149\7@\2\2\u0149N\3\2\2\2\u014a\u014b\7")
        buf.write("@\2\2\u014b\u014c\7?\2\2\u014cP\3\2\2\2\u014d\u014e\7")
        buf.write(">\2\2\u014eR\3\2\2\2\u014f\u0150\7>\2\2\u0150\u0151\7")
        buf.write("?\2\2\u0151T\3\2\2\2\u0152\u0153\7#\2\2\u0153V\3\2\2\2")
        buf.write("\u0154\u0155\7(\2\2\u0155\u0156\7(\2\2\u0156X\3\2\2\2")
        buf.write("\u0157\u0158\7~\2\2\u0158\u0159\7~\2\2\u0159Z\3\2\2\2")
        buf.write("\u015a\u015b\7-\2\2\u015b\u015c\7\60\2\2\u015c\\\3\2\2")
        buf.write("\2\u015d\u015e\7?\2\2\u015e\u015f\7?\2\2\u015f\u0160\7")
        buf.write("\60\2\2\u0160^\3\2\2\2\u0161\u0162\7?\2\2\u0162`\3\2\2")
        buf.write("\2\u0163\u0164\7*\2\2\u0164b\3\2\2\2\u0165\u0166\7+\2")
        buf.write("\2\u0166d\3\2\2\2\u0167\u0168\7]\2\2\u0168f\3\2\2\2\u0169")
        buf.write("\u016a\7_\2\2\u016ah\3\2\2\2\u016b\u016c\7}\2\2\u016c")
        buf.write("j\3\2\2\2\u016d\u016e\7\177\2\2\u016el\3\2\2\2\u016f\u0170")
        buf.write("\7<\2\2\u0170n\3\2\2\2\u0171\u0172\7\60\2\2\u0172p\3\2")
        buf.write("\2\2\u0173\u0174\7.\2\2\u0174r\3\2\2\2\u0175\u0176\7=")
        buf.write("\2\2\u0176t\3\2\2\2\u0177\u0178\7%\2\2\u0178\u0179\7%")
        buf.write("\2\2\u0179\u017d\3\2\2\2\u017a\u017c\13\2\2\2\u017b\u017a")
        buf.write("\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017e\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017e\u0180\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u0180\u0181\7%\2\2\u0181\u0182\7%\2\2\u0182\u0183\3\2")
        buf.write("\2\2\u0183\u0184\b;\3\2\u0184v\3\2\2\2\u0185\u0187\t\n")
        buf.write("\2\2\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0186")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018b\b<\3\2\u018bx\3\2\2\2\u018c\u0192\7$\2\2\u018d")
        buf.write("\u0191\5\17\b\2\u018e\u0191\5\21\t\2\u018f\u0191\n\t\2")
        buf.write("\2\u0190\u018d\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0195\u0196\b=\4\2\u0196z\3\2\2\2\u0197\u019d\7$\2\2")
        buf.write("\u0198\u019c\5\17\b\2\u0199\u019c\5\21\t\2\u019a\u019c")
        buf.write("\n\t\2\2\u019b\u0198\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019a\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019d\3")
        buf.write("\2\2\2\u01a0\u01a2\7^\2\2\u01a1\u01a3\n\13\2\2\u01a2\u01a1")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("\u01a5\b>\5\2\u01a5|\3\2\2\2\u01a6\u01a7\7,\2\2\u01a7")
        buf.write("\u01a8\7,\2\2\u01a8\u01ae\3\2\2\2\u01a9\u01ad\n\f\2\2")
        buf.write("\u01aa\u01ab\7,\2\2\u01ab\u01ad\n\f\2\2\u01ac\u01a9\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af~\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b1\u01b2\13\2\2\2\u01b2\u0080\3\2\2\2\26\2")
        buf.write("\u008a\u008e\u0093\u0099\u009e\u00a3\u00a7\u00aa\u00b6")
        buf.write("\u00b8\u017d\u0188\u0190\u0192\u019b\u019d\u01a2\u01ac")
        buf.write("\u01ae\6\3\n\2\b\2\2\3=\3\3>\4")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ID = 2
    NUMLIT = 3
    STRINGLIT = 4
    BREAK = 5
    CONTINUE = 6
    IF = 7
    ELIF = 8
    ELSE = 9
    WHILE = 10
    FOR = 11
    OF = 12
    IN = 13
    FUNCTION = 14
    LET = 15
    TRUE = 16
    FALSE = 17
    CALL = 18
    RETURN = 19
    NUMBER = 20
    BOOLEAN = 21
    STRING = 22
    JSON = 23
    ARRAY = 24
    CONSTANT = 25
    ADD = 26
    SUB = 27
    MUL = 28
    DIV = 29
    MOD = 30
    EQ = 31
    NEQ = 32
    GT = 33
    GTE = 34
    LT = 35
    LTE = 36
    NOT = 37
    AND = 38
    OR = 39
    SADD = 40
    SEQ = 41
    ASSIGN = 42
    LP = 43
    RP = 44
    LQP = 45
    RQP = 46
    LB = 47
    RB = 48
    COLON = 49
    DOT = 50
    CM = 51
    SM = 52
    COMMENT = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    UNTERMINATED_COMMENT = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Json'", "'Break'", "'Continue'", "'If'", "'Elif'", "'Else'", 
            "'While'", "'For'", "'Of'", "'In'", "'Function'", "'Let'", "'True'", 
            "'False'", "'Call'", "'Return'", "'Number'", "'Boolean'", "'String'", 
            "'JSON'", "'Array'", "'Constant'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'!'", 
            "'&&'", "'||'", "'+.'", "'==.'", "'='", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "':'", "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMLIT", "STRINGLIT", "BREAK", "CONTINUE", "IF", "ELIF", 
            "ELSE", "WHILE", "FOR", "OF", "IN", "FUNCTION", "LET", "TRUE", 
            "FALSE", "CALL", "RETURN", "NUMBER", "BOOLEAN", "STRING", "JSON", 
            "ARRAY", "CONSTANT", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
            "NEQ", "GT", "GTE", "LT", "LTE", "NOT", "AND", "OR", "SADD", 
            "SEQ", "ASSIGN", "LP", "RP", "LQP", "RQP", "LB", "RB", "COLON", 
            "DOT", "CM", "SM", "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "ID", "IPART", "DPART", "EPART", "NUMLIT", "ES", 
                  "DQ", "STRINGLIT", "BREAK", "CONTINUE", "IF", "ELIF", 
                  "ELSE", "WHILE", "FOR", "OF", "IN", "FUNCTION", "LET", 
                  "TRUE", "FALSE", "CALL", "RETURN", "NUMBER", "BOOLEAN", 
                  "STRING", "JSON", "ARRAY", "CONSTANT", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "EQ", "NEQ", "GT", "GTE", "LT", "LTE", "NOT", 
                  "AND", "OR", "SADD", "SEQ", "ASSIGN", "LP", "RP", "LQP", 
                  "RQP", "LB", "RB", "COLON", "DOT", "CM", "SM", "COMMENT", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
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
            actions[8] = self.STRINGLIT_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
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

     


