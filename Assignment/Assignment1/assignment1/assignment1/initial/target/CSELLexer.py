# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01b0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\7\2\u0084")
        buf.write("\n\2\f\2\16\2\u0087\13\2\3\3\5\3\u008a\n\3\3\3\6\3\u008d")
        buf.write("\n\3\r\3\16\3\u008e\3\4\3\4\7\4\u0093\n\4\f\4\16\4\u0096")
        buf.write("\13\4\3\5\3\5\5\5\u009a\n\5\3\5\6\5\u009d\n\5\r\5\16\5")
        buf.write("\u009e\3\6\3\6\5\6\u00a3\n\6\3\6\5\6\u00a6\n\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u00b2\n\t\f\t\16")
        buf.write("\t\u00b5\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3")
        buf.write(";\7;\u0179\n;\f;\16;\u017c\13;\3;\3;\3;\3;\3;\3<\6<\u0184")
        buf.write("\n<\r<\16<\u0185\3<\3<\3=\3=\3=\3=\7=\u018e\n=\f=\16=")
        buf.write("\u0191\13=\3=\3=\3>\3>\3>\3>\7>\u0199\n>\f>\16>\u019c")
        buf.write("\13>\3>\3>\5>\u01a0\n>\3>\3>\3?\3?\3?\3?\3?\3?\7?\u01aa")
        buf.write("\n?\f?\16?\u01ad\13?\3@\3@\3\u017a\2A\3\3\5\2\7\2\t\2")
        buf.write("\13\4\r\2\17\2\21\5\23\6\25\7\27\b\31\t\33\n\35\13\37")
        buf.write("\f!\r#\16%\17\'\20)\21+\22-\23/\24\61\25\63\26\65\27\67")
        buf.write("\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)")
        buf.write("[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8y9{:};\177")
        buf.write("<\3\2\r\5\2&&``c|\6\2\62;C\\aac|\3\2//\3\2\62;\4\2GGg")
        buf.write("g\4\2--//\t\2))^^ddhhppttvv\5\2\f\f$$^^\5\2\13\f\16\17")
        buf.write("\"\"\t\2$$^^ddhhppttvv\3\2,,\2\u01c0\2\3\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\3\u0081\3\2\2\2\5\u0089\3\2\2\2\7\u0090\3\2\2")
        buf.write("\2\t\u0097\3\2\2\2\13\u00a0\3\2\2\2\r\u00a7\3\2\2\2\17")
        buf.write("\u00aa\3\2\2\2\21\u00ad\3\2\2\2\23\u00b9\3\2\2\2\25\u00bf")
        buf.write("\3\2\2\2\27\u00c8\3\2\2\2\31\u00cb\3\2\2\2\33\u00d0\3")
        buf.write("\2\2\2\35\u00d5\3\2\2\2\37\u00db\3\2\2\2!\u00df\3\2\2")
        buf.write("\2#\u00e2\3\2\2\2%\u00e5\3\2\2\2\'\u00ee\3\2\2\2)\u00f2")
        buf.write("\3\2\2\2+\u00f7\3\2\2\2-\u00fd\3\2\2\2/\u0102\3\2\2\2")
        buf.write("\61\u0109\3\2\2\2\63\u0110\3\2\2\2\65\u0118\3\2\2\2\67")
        buf.write("\u011f\3\2\2\29\u0124\3\2\2\2;\u012a\3\2\2\2=\u0133\3")
        buf.write("\2\2\2?\u0135\3\2\2\2A\u0137\3\2\2\2C\u0139\3\2\2\2E\u013b")
        buf.write("\3\2\2\2G\u013d\3\2\2\2I\u0140\3\2\2\2K\u0143\3\2\2\2")
        buf.write("M\u0145\3\2\2\2O\u0148\3\2\2\2Q\u014a\3\2\2\2S\u014d\3")
        buf.write("\2\2\2U\u014f\3\2\2\2W\u0152\3\2\2\2Y\u0155\3\2\2\2[\u0158")
        buf.write("\3\2\2\2]\u015c\3\2\2\2_\u015e\3\2\2\2a\u0160\3\2\2\2")
        buf.write("c\u0162\3\2\2\2e\u0164\3\2\2\2g\u0166\3\2\2\2i\u0168\3")
        buf.write("\2\2\2k\u016a\3\2\2\2m\u016c\3\2\2\2o\u016e\3\2\2\2q\u0170")
        buf.write("\3\2\2\2s\u0172\3\2\2\2u\u0174\3\2\2\2w\u0183\3\2\2\2")
        buf.write("y\u0189\3\2\2\2{\u0194\3\2\2\2}\u01a3\3\2\2\2\177\u01ae")
        buf.write("\3\2\2\2\u0081\u0085\t\2\2\2\u0082\u0084\t\3\2\2\u0083")
        buf.write("\u0082\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2")
        buf.write("\u0085\u0086\3\2\2\2\u0086\4\3\2\2\2\u0087\u0085\3\2\2")
        buf.write("\2\u0088\u008a\t\4\2\2\u0089\u0088\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u008c\3\2\2\2\u008b\u008d\t\5\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\6\3\2\2\2\u0090\u0094\5o8\2")
        buf.write("\u0091\u0093\t\5\2\2\u0092\u0091\3\2\2\2\u0093\u0096\3")
        buf.write("\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\b")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0099\t\6\2\2\u0098")
        buf.write("\u009a\t\7\2\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009c\3\2\2\2\u009b\u009d\t\5\2\2\u009c\u009b\3")
        buf.write("\2\2\2\u009d\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f")
        buf.write("\3\2\2\2\u009f\n\3\2\2\2\u00a0\u00a2\5\5\3\2\u00a1\u00a3")
        buf.write("\5\7\4\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a5\3\2\2\2\u00a4\u00a6\5\t\5\2\u00a5\u00a4\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\f\3\2\2\2\u00a7\u00a8\7^\2")
        buf.write("\2\u00a8\u00a9\t\b\2\2\u00a9\16\3\2\2\2\u00aa\u00ab\7")
        buf.write(")\2\2\u00ab\u00ac\7$\2\2\u00ac\20\3\2\2\2\u00ad\u00b3")
        buf.write("\7$\2\2\u00ae\u00b2\5\r\7\2\u00af\u00b2\5\17\b\2\u00b0")
        buf.write("\u00b2\n\t\2\2\u00b1\u00ae\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3")
        buf.write("\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3")
        buf.write("\3\2\2\2\u00b6\u00b7\7$\2\2\u00b7\u00b8\b\t\2\2\u00b8")
        buf.write("\22\3\2\2\2\u00b9\u00ba\7D\2\2\u00ba\u00bb\7t\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7m\2\2\u00be")
        buf.write("\24\3\2\2\2\u00bf\u00c0\7E\2\2\u00c0\u00c1\7q\2\2\u00c1")
        buf.write("\u00c2\7p\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7k\2\2\u00c4")
        buf.write("\u00c5\7p\2\2\u00c5\u00c6\7w\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write("\26\3\2\2\2\u00c8\u00c9\7K\2\2\u00c9\u00ca\7h\2\2\u00ca")
        buf.write("\30\3\2\2\2\u00cb\u00cc\7G\2\2\u00cc\u00cd\7n\2\2\u00cd")
        buf.write("\u00ce\7k\2\2\u00ce\u00cf\7h\2\2\u00cf\32\3\2\2\2\u00d0")
        buf.write("\u00d1\7G\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3")
        buf.write("\u00d4\7g\2\2\u00d4\34\3\2\2\2\u00d5\u00d6\7Y\2\2\u00d6")
        buf.write("\u00d7\7j\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7n\2\2\u00d9")
        buf.write("\u00da\7g\2\2\u00da\36\3\2\2\2\u00db\u00dc\7H\2\2\u00dc")
        buf.write("\u00dd\7q\2\2\u00dd\u00de\7t\2\2\u00de \3\2\2\2\u00df")
        buf.write("\u00e0\7Q\2\2\u00e0\u00e1\7h\2\2\u00e1\"\3\2\2\2\u00e2")
        buf.write("\u00e3\7K\2\2\u00e3\u00e4\7p\2\2\u00e4$\3\2\2\2\u00e5")
        buf.write("\u00e6\7H\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8\7p\2\2\u00e8")
        buf.write("\u00e9\7e\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb")
        buf.write("\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed&\3\2\2\2\u00ee")
        buf.write("\u00ef\7N\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7v\2\2\u00f1")
        buf.write("(\3\2\2\2\u00f2\u00f3\7V\2\2\u00f3\u00f4\7t\2\2\u00f4")
        buf.write("\u00f5\7w\2\2\u00f5\u00f6\7g\2\2\u00f6*\3\2\2\2\u00f7")
        buf.write("\u00f8\7H\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7n\2\2\u00fa")
        buf.write("\u00fb\7u\2\2\u00fb\u00fc\7g\2\2\u00fc,\3\2\2\2\u00fd")
        buf.write("\u00fe\7E\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7n\2\2\u0100")
        buf.write("\u0101\7n\2\2\u0101.\3\2\2\2\u0102\u0103\7T\2\2\u0103")
        buf.write("\u0104\7g\2\2\u0104\u0105\7v\2\2\u0105\u0106\7w\2\2\u0106")
        buf.write("\u0107\7t\2\2\u0107\u0108\7p\2\2\u0108\60\3\2\2\2\u0109")
        buf.write("\u010a\7P\2\2\u010a\u010b\7w\2\2\u010b\u010c\7o\2\2\u010c")
        buf.write("\u010d\7d\2\2\u010d\u010e\7g\2\2\u010e\u010f\7t\2\2\u010f")
        buf.write("\62\3\2\2\2\u0110\u0111\7D\2\2\u0111\u0112\7q\2\2\u0112")
        buf.write("\u0113\7q\2\2\u0113\u0114\7n\2\2\u0114\u0115\7g\2\2\u0115")
        buf.write("\u0116\7c\2\2\u0116\u0117\7p\2\2\u0117\64\3\2\2\2\u0118")
        buf.write("\u0119\7U\2\2\u0119\u011a\7v\2\2\u011a\u011b\7t\2\2\u011b")
        buf.write("\u011c\7k\2\2\u011c\u011d\7p\2\2\u011d\u011e\7i\2\2\u011e")
        buf.write("\66\3\2\2\2\u011f\u0120\7L\2\2\u0120\u0121\7U\2\2\u0121")
        buf.write("\u0122\7Q\2\2\u0122\u0123\7P\2\2\u01238\3\2\2\2\u0124")
        buf.write("\u0125\7C\2\2\u0125\u0126\7t\2\2\u0126\u0127\7t\2\2\u0127")
        buf.write("\u0128\7c\2\2\u0128\u0129\7{\2\2\u0129:\3\2\2\2\u012a")
        buf.write("\u012b\7E\2\2\u012b\u012c\7q\2\2\u012c\u012d\7p\2\2\u012d")
        buf.write("\u012e\7u\2\2\u012e\u012f\7v\2\2\u012f\u0130\7c\2\2\u0130")
        buf.write("\u0131\7p\2\2\u0131\u0132\7v\2\2\u0132<\3\2\2\2\u0133")
        buf.write("\u0134\7-\2\2\u0134>\3\2\2\2\u0135\u0136\7/\2\2\u0136")
        buf.write("@\3\2\2\2\u0137\u0138\7,\2\2\u0138B\3\2\2\2\u0139\u013a")
        buf.write("\7\61\2\2\u013aD\3\2\2\2\u013b\u013c\7\'\2\2\u013cF\3")
        buf.write("\2\2\2\u013d\u013e\7?\2\2\u013e\u013f\7?\2\2\u013fH\3")
        buf.write("\2\2\2\u0140\u0141\7#\2\2\u0141\u0142\7?\2\2\u0142J\3")
        buf.write("\2\2\2\u0143\u0144\7@\2\2\u0144L\3\2\2\2\u0145\u0146\7")
        buf.write("@\2\2\u0146\u0147\7?\2\2\u0147N\3\2\2\2\u0148\u0149\7")
        buf.write(">\2\2\u0149P\3\2\2\2\u014a\u014b\7>\2\2\u014b\u014c\7")
        buf.write("?\2\2\u014cR\3\2\2\2\u014d\u014e\7#\2\2\u014eT\3\2\2\2")
        buf.write("\u014f\u0150\7(\2\2\u0150\u0151\7(\2\2\u0151V\3\2\2\2")
        buf.write("\u0152\u0153\7~\2\2\u0153\u0154\7~\2\2\u0154X\3\2\2\2")
        buf.write("\u0155\u0156\7-\2\2\u0156\u0157\7\60\2\2\u0157Z\3\2\2")
        buf.write("\2\u0158\u0159\7?\2\2\u0159\u015a\7?\2\2\u015a\u015b\7")
        buf.write("\60\2\2\u015b\\\3\2\2\2\u015c\u015d\7?\2\2\u015d^\3\2")
        buf.write("\2\2\u015e\u015f\7(\2\2\u015f`\3\2\2\2\u0160\u0161\7*")
        buf.write("\2\2\u0161b\3\2\2\2\u0162\u0163\7+\2\2\u0163d\3\2\2\2")
        buf.write("\u0164\u0165\7]\2\2\u0165f\3\2\2\2\u0166\u0167\7_\2\2")
        buf.write("\u0167h\3\2\2\2\u0168\u0169\7}\2\2\u0169j\3\2\2\2\u016a")
        buf.write("\u016b\7\177\2\2\u016bl\3\2\2\2\u016c\u016d\7<\2\2\u016d")
        buf.write("n\3\2\2\2\u016e\u016f\7\60\2\2\u016fp\3\2\2\2\u0170\u0171")
        buf.write("\7.\2\2\u0171r\3\2\2\2\u0172\u0173\7=\2\2\u0173t\3\2\2")
        buf.write("\2\u0174\u0175\7%\2\2\u0175\u0176\7%\2\2\u0176\u017a\3")
        buf.write("\2\2\2\u0177\u0179\13\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("\u017c\3\2\2\2\u017a\u017b\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017b\u017d\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e\7")
        buf.write("%\2\2\u017e\u017f\7%\2\2\u017f\u0180\3\2\2\2\u0180\u0181")
        buf.write("\b;\3\2\u0181v\3\2\2\2\u0182\u0184\t\n\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\b<\3\2")
        buf.write("\u0188x\3\2\2\2\u0189\u018f\7$\2\2\u018a\u018e\5\r\7\2")
        buf.write("\u018b\u018e\5\17\b\2\u018c\u018e\n\t\2\2\u018d\u018a")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e")
        buf.write("\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190\u0192\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193\b")
        buf.write("=\4\2\u0193z\3\2\2\2\u0194\u019a\7$\2\2\u0195\u0199\5")
        buf.write("\r\7\2\u0196\u0199\5\17\b\2\u0197\u0199\n\t\2\2\u0198")
        buf.write("\u0195\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0197\3\2\2\2")
        buf.write("\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019f")
        buf.write("\7^\2\2\u019e\u01a0\n\13\2\2\u019f\u019e\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\b>\5\2")
        buf.write("\u01a2|\3\2\2\2\u01a3\u01a4\7,\2\2\u01a4\u01a5\7,\2\2")
        buf.write("\u01a5\u01ab\3\2\2\2\u01a6\u01aa\n\f\2\2\u01a7\u01a8\7")
        buf.write(",\2\2\u01a8\u01aa\n\f\2\2\u01a9\u01a6\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac~\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae")
        buf.write("\u01af\13\2\2\2\u01af\u0080\3\2\2\2\26\2\u0085\u0089\u008e")
        buf.write("\u0094\u0099\u009e\u00a2\u00a5\u00b1\u00b3\u017a\u0185")
        buf.write("\u018d\u018f\u0198\u019a\u019f\u01a9\u01ab\6\3\t\2\b\2")
        buf.write("\2\3=\3\3>\4")
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
    REF = 42
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
            "'Break'", "'Continue'", "'If'", "'Elif'", "'Else'", "'While'", 
            "'For'", "'Of'", "'In'", "'Function'", "'Let'", "'True'", "'False'", 
            "'Call'", "'Return'", "'Number'", "'Boolean'", "'String'", "'JSON'", 
            "'Array'", "'Constant'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'!'", "'&&'", 
            "'||'", "'+.'", "'==.'", "'='", "'&'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "':'", "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUMLIT", "STRINGLIT", "BREAK", "CONTINUE", "IF", "ELIF", 
            "ELSE", "WHILE", "FOR", "OF", "IN", "FUNCTION", "LET", "TRUE", 
            "FALSE", "CALL", "RETURN", "NUMBER", "BOOLEAN", "STRING", "JSON", 
            "ARRAY", "CONSTANT", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
            "NEQ", "GT", "GTE", "LT", "LTE", "NOT", "AND", "OR", "SADD", 
            "SEQ", "ASSIGN", "REF", "LP", "RP", "LQP", "RQP", "LB", "RB", 
            "COLON", "DOT", "CM", "SM", "COMMENT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "ID", "IPART", "DPART", "EPART", "NUMLIT", "ES", "DQ", 
                  "STRINGLIT", "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", 
                  "WHILE", "FOR", "OF", "IN", "FUNCTION", "LET", "TRUE", 
                  "FALSE", "CALL", "RETURN", "NUMBER", "BOOLEAN", "STRING", 
                  "JSON", "ARRAY", "CONSTANT", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "EQ", "NEQ", "GT", "GTE", "LT", "LTE", "NOT", "AND", 
                  "OR", "SADD", "SEQ", "ASSIGN", "REF", "LP", "RP", "LQP", 
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
            actions[7] = self.STRINGLIT_action 
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

     


