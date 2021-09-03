# Generated from d:\Python\Principles of Programming Languages v2\Assignment\assignment2-v1.0\assignment2\initial\src\main\csel\parser\CSEL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u018b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\6\2J\n")
        buf.write("\2\r\2\16\2K\3\2\3\2\3\3\3\3\5\3R\n\3\3\4\3\4\3\4\3\4")
        buf.write("\7\4X\n\4\f\4\16\4[\13\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\5")
        buf.write("\6d\n\6\3\6\3\6\5\6h\n\6\3\7\3\7\5\7l\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\bs\n\b\3\t\3\t\3\t\3\t\5\ty\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\n\u0081\n\n\3\13\3\13\3\13\3\13\7\13\u0087")
        buf.write("\n\13\f\13\16\13\u008a\13\13\5\13\u008c\n\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0098\n\f\f\f\16")
        buf.write("\f\u009b\13\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00a3\n\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u00ad\n\16\f\16")
        buf.write("\16\16\u00b0\13\16\3\17\3\17\3\20\7\20\u00b5\n\20\f\20")
        buf.write("\16\20\u00b8\13\20\3\21\3\21\5\21\u00bc\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00c6\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\7\23\u00cd\n\23\f\23\16\23\u00d0\13")
        buf.write("\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00e5")
        buf.write("\n\24\f\24\16\24\u00e8\13\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u00ef\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u0111\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\5\33\u012b")
        buf.write("\n\33\3\33\3\33\3\34\3\34\3\34\5\34\u0132\n\34\3\35\3")
        buf.write("\35\3\35\7\35\u0137\n\35\f\35\16\35\u013a\13\35\3\36\3")
        buf.write("\36\3\36\7\36\u013f\n\36\f\36\16\36\u0142\13\36\3\37\3")
        buf.write("\37\3\37\7\37\u0147\n\37\f\37\16\37\u014a\13\37\3 \7 ")
        buf.write("\u014d\n \f \16 \u0150\13 \3 \3 \3!\7!\u0155\n!\f!\16")
        buf.write("!\u0158\13!\3!\3!\3\"\3\"\3\"\3\"\3\"\7\"\u0161\n\"\f")
        buf.write("\"\16\"\u0164\13\"\3\"\3\"\7\"\u0168\n\"\f\"\16\"\u016b")
        buf.write("\13\"\3\"\5\"\u016e\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#")
        buf.write("\u0179\n#\3$\3$\3$\3$\3$\3$\7$\u0181\n$\f$\16$\u0184\13")
        buf.write("$\3$\5$\u0187\n$\3$\3$\3$\2\2%\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF\2\b\4\2\20")
        buf.write("\20\32\32\3\2\25\31\4\2 %**\3\2\'(\4\2\33\34))\3\2\35")
        buf.write("\37\2\u0199\2I\3\2\2\2\4Q\3\2\2\2\6S\3\2\2\2\b^\3\2\2")
        buf.write("\2\n`\3\2\2\2\fk\3\2\2\2\16m\3\2\2\2\20x\3\2\2\2\22\u0080")
        buf.write("\3\2\2\2\24\u0082\3\2\2\2\26\u008f\3\2\2\2\30\u009e\3")
        buf.write("\2\2\2\32\u00a9\3\2\2\2\34\u00b1\3\2\2\2\36\u00b6\3\2")
        buf.write("\2\2 \u00bb\3\2\2\2\"\u00c5\3\2\2\2$\u00c7\3\2\2\2&\u00d5")
        buf.write("\3\2\2\2(\u0110\3\2\2\2*\u0112\3\2\2\2,\u011a\3\2\2\2")
        buf.write(".\u011d\3\2\2\2\60\u0120\3\2\2\2\62\u0123\3\2\2\2\64\u0128")
        buf.write("\3\2\2\2\66\u012e\3\2\2\28\u0133\3\2\2\2:\u013b\3\2\2")
        buf.write("\2<\u0143\3\2\2\2>\u014e\3\2\2\2@\u0156\3\2\2\2B\u016d")
        buf.write("\3\2\2\2D\u0178\3\2\2\2F\u017a\3\2\2\2HJ\5\4\3\2IH\3\2")
        buf.write("\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7\2\2\3")
        buf.write("N\3\3\2\2\2OR\5\6\4\2PR\5\30\r\2QO\3\2\2\2QP\3\2\2\2R")
        buf.write("\5\3\2\2\2ST\t\2\2\2TY\5\n\6\2UV\7\64\2\2VX\5\n\6\2WU")
        buf.write("\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3")
        buf.write("\2\2\2\\]\7\65\2\2]\7\3\2\2\2^_\t\3\2\2_\t\3\2\2\2`c\5")
        buf.write("\16\b\2ab\7\62\2\2bd\5\b\5\2ca\3\2\2\2cd\3\2\2\2dg\3\2")
        buf.write("\2\2ef\7+\2\2fh\5\f\7\2ge\3\2\2\2gh\3\2\2\2h\13\3\2\2")
        buf.write("\2il\5\22\n\2jl\5\66\34\2ki\3\2\2\2kj\3\2\2\2l\r\3\2\2")
        buf.write("\2mr\7\3\2\2no\7.\2\2op\5\20\t\2pq\7/\2\2qs\3\2\2\2rn")
        buf.write("\3\2\2\2rs\3\2\2\2s\17\3\2\2\2tu\7\4\2\2uv\7\64\2\2vy")
        buf.write("\5\20\t\2wy\7\4\2\2xt\3\2\2\2xw\3\2\2\2y\21\3\2\2\2z\u0081")
        buf.write("\7\21\2\2{\u0081\7\22\2\2|\u0081\7\4\2\2}\u0081\7\5\2")
        buf.write("\2~\u0081\5\24\13\2\177\u0081\5\26\f\2\u0080z\3\2\2\2")
        buf.write("\u0080{\3\2\2\2\u0080|\3\2\2\2\u0080}\3\2\2\2\u0080~\3")
        buf.write("\2\2\2\u0080\177\3\2\2\2\u0081\23\3\2\2\2\u0082\u008b")
        buf.write("\7.\2\2\u0083\u0088\5\22\n\2\u0084\u0085\7\64\2\2\u0085")
        buf.write("\u0087\5\22\n\2\u0086\u0084\3\2\2\2\u0087\u008a\3\2\2")
        buf.write("\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008c")
        buf.write("\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u0083\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e\7/\2\2")
        buf.write("\u008e\25\3\2\2\2\u008f\u0090\7\60\2\2\u0090\u0091\7\3")
        buf.write("\2\2\u0091\u0092\7\62\2\2\u0092\u0099\5\22\n\2\u0093\u0094")
        buf.write("\7\64\2\2\u0094\u0095\7\3\2\2\u0095\u0096\7\62\2\2\u0096")
        buf.write("\u0098\5\22\n\2\u0097\u0093\3\2\2\2\u0098\u009b\3\2\2")
        buf.write("\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c")
        buf.write("\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009d\7\61\2\2\u009d")
        buf.write("\27\3\2\2\2\u009e\u009f\7\17\2\2\u009f\u00a0\7\3\2\2\u00a0")
        buf.write("\u00a2\7,\2\2\u00a1\u00a3\5\32\16\2\u00a2\u00a1\3\2\2")
        buf.write("\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5")
        buf.write("\7-\2\2\u00a5\u00a6\7\60\2\2\u00a6\u00a7\5\34\17\2\u00a7")
        buf.write("\u00a8\7\61\2\2\u00a8\31\3\2\2\2\u00a9\u00ae\5\16\b\2")
        buf.write("\u00aa\u00ab\7\64\2\2\u00ab\u00ad\5\16\b\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\33\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1")
        buf.write("\u00b2\5\36\20\2\u00b2\35\3\2\2\2\u00b3\u00b5\5 \21\2")
        buf.write("\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3")
        buf.write("\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\37\3\2\2\2\u00b8\u00b6")
        buf.write("\3\2\2\2\u00b9\u00bc\5\6\4\2\u00ba\u00bc\5\"\22\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc!\3\2\2\2\u00bd")
        buf.write("\u00c6\5$\23\2\u00be\u00c6\5&\24\2\u00bf\u00c6\5(\25\2")
        buf.write("\u00c0\u00c6\5*\26\2\u00c1\u00c6\5,\27\2\u00c2\u00c6\5")
        buf.write(".\30\2\u00c3\u00c6\5\60\31\2\u00c4\u00c6\5\64\33\2\u00c5")
        buf.write("\u00bd\3\2\2\2\u00c5\u00be\3\2\2\2\u00c5\u00bf\3\2\2\2")
        buf.write("\u00c5\u00c0\3\2\2\2\u00c5\u00c1\3\2\2\2\u00c5\u00c2\3")
        buf.write("\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6#")
        buf.write("\3\2\2\2\u00c7\u00ce\7\3\2\2\u00c8\u00c9\7.\2\2\u00c9")
        buf.write("\u00ca\5\66\34\2\u00ca\u00cb\7/\2\2\u00cb\u00cd\3\2\2")
        buf.write("\2\u00cc\u00c8\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d1\u00d2\7+\2\2\u00d2\u00d3\5\66\34")
        buf.write("\2\u00d3\u00d4\7\65\2\2\u00d4%\3\2\2\2\u00d5\u00d6\7\b")
        buf.write("\2\2\u00d6\u00d7\7,\2\2\u00d7\u00d8\5\66\34\2\u00d8\u00d9")
        buf.write("\7-\2\2\u00d9\u00da\7\60\2\2\u00da\u00db\5\36\20\2\u00db")
        buf.write("\u00e6\7\61\2\2\u00dc\u00dd\7\t\2\2\u00dd\u00de\7,\2\2")
        buf.write("\u00de\u00df\5\66\34\2\u00df\u00e0\7-\2\2\u00e0\u00e1")
        buf.write("\7\60\2\2\u00e1\u00e2\5\36\20\2\u00e2\u00e3\7\61\2\2\u00e3")
        buf.write("\u00e5\3\2\2\2\u00e4\u00dc\3\2\2\2\u00e5\u00e8\3\2\2\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00ee\3")
        buf.write("\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\7\n\2\2\u00ea\u00eb")
        buf.write("\7\60\2\2\u00eb\u00ec\5\36\20\2\u00ec\u00ed\7\61\2\2\u00ed")
        buf.write("\u00ef\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee\u00ef\3\2\2\2")
        buf.write("\u00ef\'\3\2\2\2\u00f0\u00f1\7\f\2\2\u00f1\u00f2\7\3\2")
        buf.write("\2\u00f2\u00f3\7\16\2\2\u00f3\u00f4\5\24\13\2\u00f4\u00f5")
        buf.write("\7\60\2\2\u00f5\u00f6\5\36\20\2\u00f6\u00f7\7\61\2\2\u00f7")
        buf.write("\u0111\3\2\2\2\u00f8\u00f9\7\f\2\2\u00f9\u00fa\7\3\2\2")
        buf.write("\u00fa\u00fb\7\r\2\2\u00fb\u00fc\5\26\f\2\u00fc\u00fd")
        buf.write("\7\60\2\2\u00fd\u00fe\5\36\20\2\u00fe\u00ff\7\61\2\2\u00ff")
        buf.write("\u0111\3\2\2\2\u0100\u0101\7\f\2\2\u0101\u0102\7\3\2\2")
        buf.write("\u0102\u0103\7\16\2\2\u0103\u0104\7\3\2\2\u0104\u0105")
        buf.write("\7\60\2\2\u0105\u0106\5\36\20\2\u0106\u0107\7\61\2\2\u0107")
        buf.write("\u0111\3\2\2\2\u0108\u0109\7\f\2\2\u0109\u010a\7\3\2\2")
        buf.write("\u010a\u010b\7\r\2\2\u010b\u010c\7\3\2\2\u010c\u010d\7")
        buf.write("\60\2\2\u010d\u010e\5\36\20\2\u010e\u010f\7\61\2\2\u010f")
        buf.write("\u0111\3\2\2\2\u0110\u00f0\3\2\2\2\u0110\u00f8\3\2\2\2")
        buf.write("\u0110\u0100\3\2\2\2\u0110\u0108\3\2\2\2\u0111)\3\2\2")
        buf.write("\2\u0112\u0113\7\13\2\2\u0113\u0114\7,\2\2\u0114\u0115")
        buf.write("\5\66\34\2\u0115\u0116\7-\2\2\u0116\u0117\7\60\2\2\u0117")
        buf.write("\u0118\5\36\20\2\u0118\u0119\7\61\2\2\u0119+\3\2\2\2\u011a")
        buf.write("\u011b\7\6\2\2\u011b\u011c\7\65\2\2\u011c-\3\2\2\2\u011d")
        buf.write("\u011e\7\7\2\2\u011e\u011f\7\65\2\2\u011f/\3\2\2\2\u0120")
        buf.write("\u0121\5\62\32\2\u0121\u0122\7\65\2\2\u0122\61\3\2\2\2")
        buf.write("\u0123\u0124\7\23\2\2\u0124\u0125\7,\2\2\u0125\u0126\5")
        buf.write("F$\2\u0126\u0127\7-\2\2\u0127\63\3\2\2\2\u0128\u012a\7")
        buf.write("\24\2\2\u0129\u012b\5\66\34\2\u012a\u0129\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\7\65\2")
        buf.write("\2\u012d\65\3\2\2\2\u012e\u0131\58\35\2\u012f\u0130\t")
        buf.write("\4\2\2\u0130\u0132\58\35\2\u0131\u012f\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\67\3\2\2\2\u0133\u0138\5:\36\2\u0134\u0135")
        buf.write("\t\5\2\2\u0135\u0137\5:\36\2\u0136\u0134\3\2\2\2\u0137")
        buf.write("\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u01399\3\2\2\2\u013a\u0138\3\2\2\2\u013b\u0140\5<\37")
        buf.write("\2\u013c\u013d\t\6\2\2\u013d\u013f\5<\37\2\u013e\u013c")
        buf.write("\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140")
        buf.write("\u0141\3\2\2\2\u0141;\3\2\2\2\u0142\u0140\3\2\2\2\u0143")
        buf.write("\u0148\5> \2\u0144\u0145\t\7\2\2\u0145\u0147\5> \2\u0146")
        buf.write("\u0144\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149=\3\2\2\2\u014a\u0148\3\2\2")
        buf.write("\2\u014b\u014d\7&\2\2\u014c\u014b\3\2\2\2\u014d\u0150")
        buf.write("\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0151\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152\5@!\2\u0152")
        buf.write("?\3\2\2\2\u0153\u0155\7\34\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\5")
        buf.write("B\"\2\u015aA\3\2\2\2\u015b\u0169\7\3\2\2\u015c\u015d\7")
        buf.write(".\2\2\u015d\u0162\5\66\34\2\u015e\u015f\7\64\2\2\u015f")
        buf.write("\u0161\5\66\34\2\u0160\u015e\3\2\2\2\u0161\u0164\3\2\2")
        buf.write("\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\7/\2\2\u0166")
        buf.write("\u0168\3\2\2\2\u0167\u015c\3\2\2\2\u0168\u016b\3\2\2\2")
        buf.write("\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016e\3")
        buf.write("\2\2\2\u016b\u0169\3\2\2\2\u016c\u016e\5D#\2\u016d\u015b")
        buf.write("\3\2\2\2\u016d\u016c\3\2\2\2\u016eC\3\2\2\2\u016f\u0179")
        buf.write("\7\4\2\2\u0170\u0179\7\21\2\2\u0171\u0179\7\22\2\2\u0172")
        buf.write("\u0179\7\5\2\2\u0173\u0179\5\62\32\2\u0174\u0175\7,\2")
        buf.write("\2\u0175\u0176\5\66\34\2\u0176\u0177\7-\2\2\u0177\u0179")
        buf.write("\3\2\2\2\u0178\u016f\3\2\2\2\u0178\u0170\3\2\2\2\u0178")
        buf.write("\u0171\3\2\2\2\u0178\u0172\3\2\2\2\u0178\u0173\3\2\2\2")
        buf.write("\u0178\u0174\3\2\2\2\u0179E\3\2\2\2\u017a\u017b\7\3\2")
        buf.write("\2\u017b\u017c\7\64\2\2\u017c\u0186\7.\2\2\u017d\u017e")
        buf.write("\5\66\34\2\u017e\u017f\7\64\2\2\u017f\u0181\3\2\2\2\u0180")
        buf.write("\u017d\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0182\3")
        buf.write("\2\2\2\u0185\u0187\5\66\34\2\u0186\u0182\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\7/\2\2")
        buf.write("\u0189G\3\2\2\2$KQYcgkrx\u0080\u0088\u008b\u0099\u00a2")
        buf.write("\u00ae\u00b6\u00bb\u00c5\u00ce\u00e6\u00ee\u0110\u012a")
        buf.write("\u0131\u0138\u0140\u0148\u014e\u0156\u0162\u0169\u016d")
        buf.write("\u0178\u0182\u0186")
        return buf.getvalue()


class CSELParser ( Parser ):

    grammarFileName = "CSEL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Break'", "'Continue'", "'If'", "'Elif'", "'Else'", 
                     "'While'", "'For'", "'Of'", "'In'", "'Function'", "'Let'", 
                     "'True'", "'False'", "'Call'", "'Return'", "'Number'", 
                     "'Boolean'", "'String'", "'JSON'", "'Array'", "'Constant'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>'", "'>='", "'<'", "'<='", "'!'", "'&&'", "'||'", 
                     "'+.'", "'==.'", "'='", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "':'", "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "ID", "NUMLIT", "STRINGLIT", "BREAK", 
                      "CONTINUE", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
                      "OF", "IN", "FUNCTION", "LET", "TRUE", "FALSE", "CALL", 
                      "RETURN", "NUMBER", "BOOLEAN", "STRING", "JSON", "ARRAY", 
                      "CONSTANT", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                      "NEQ", "GT", "GTE", "LT", "LTE", "NOT", "AND", "OR", 
                      "SADD", "SEQ", "ASSIGN", "LP", "RP", "LQP", "RQP", 
                      "LB", "RB", "COLON", "DOT", "CM", "SM", "COMMENT", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_manyDecl = 1
    RULE_varDecl = 2
    RULE_typ = 3
    RULE_variable = 4
    RULE_vartail = 5
    RULE_var = 6
    RULE_varlist = 7
    RULE_literal = 8
    RULE_arrayLiteral = 9
    RULE_jsonLiteral = 10
    RULE_funcDecl = 11
    RULE_paraList = 12
    RULE_body = 13
    RULE_stmtList = 14
    RULE_manyStmt = 15
    RULE_otherStmt = 16
    RULE_assignStmt = 17
    RULE_ifStmt = 18
    RULE_forStmt = 19
    RULE_whileStmt = 20
    RULE_breakStmt = 21
    RULE_continueStmt = 22
    RULE_callStmt = 23
    RULE_funcall = 24
    RULE_returnStmt = 25
    RULE_expr = 26
    RULE_logicExpr = 27
    RULE_additiveExpr = 28
    RULE_multiplicateExpr = 29
    RULE_unaryLogicExpr = 30
    RULE_unarySignExpr = 31
    RULE_indexExpr = 32
    RULE_finalExpr = 33
    RULE_callList = 34

    ruleNames =  [ "program", "manyDecl", "varDecl", "typ", "variable", 
                   "vartail", "var", "varlist", "literal", "arrayLiteral", 
                   "jsonLiteral", "funcDecl", "paraList", "body", "stmtList", 
                   "manyStmt", "otherStmt", "assignStmt", "ifStmt", "forStmt", 
                   "whileStmt", "breakStmt", "continueStmt", "callStmt", 
                   "funcall", "returnStmt", "expr", "logicExpr", "additiveExpr", 
                   "multiplicateExpr", "unaryLogicExpr", "unarySignExpr", 
                   "indexExpr", "finalExpr", "callList" ]

    EOF = Token.EOF
    ID=1
    NUMLIT=2
    STRINGLIT=3
    BREAK=4
    CONTINUE=5
    IF=6
    ELIF=7
    ELSE=8
    WHILE=9
    FOR=10
    OF=11
    IN=12
    FUNCTION=13
    LET=14
    TRUE=15
    FALSE=16
    CALL=17
    RETURN=18
    NUMBER=19
    BOOLEAN=20
    STRING=21
    JSON=22
    ARRAY=23
    CONSTANT=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    EQ=30
    NEQ=31
    GT=32
    GTE=33
    LT=34
    LTE=35
    NOT=36
    AND=37
    OR=38
    SADD=39
    SEQ=40
    ASSIGN=41
    LP=42
    RP=43
    LQP=44
    RQP=45
    LB=46
    RB=47
    COLON=48
    DOT=49
    CM=50
    SM=51
    COMMENT=52
    WS=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55
    UNTERMINATED_COMMENT=56
    ERROR_CHAR=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSELParser.EOF, 0)

        def manyDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ManyDeclContext)
            else:
                return self.getTypedRuleContext(CSELParser.ManyDeclContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_program




    def program(self):

        localctx = CSELParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.manyDecl()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.FUNCTION) | (1 << CSELParser.LET) | (1 << CSELParser.CONSTANT))) != 0)):
                    break

            self.state = 75
            self.match(CSELParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(CSELParser.VarDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(CSELParser.FuncDeclContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_manyDecl




    def manyDecl(self):

        localctx = CSELParser.ManyDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manyDecl)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.LET, CSELParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.varDecl()
                pass
            elif token in [CSELParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.funcDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.VariableContext)
            else:
                return self.getTypedRuleContext(CSELParser.VariableContext,i)


        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def LET(self):
            return self.getToken(CSELParser.LET, 0)

        def CONSTANT(self):
            return self.getToken(CSELParser.CONSTANT, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_varDecl




    def varDecl(self):

        localctx = CSELParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==CSELParser.LET or _la==CSELParser.CONSTANT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 82
            self.variable()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.CM:
                self.state = 83
                self.match(CSELParser.CM)
                self.state = 84
                self.variable()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CSELParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(CSELParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(CSELParser.STRING, 0)

        def JSON(self):
            return self.getToken(CSELParser.JSON, 0)

        def ARRAY(self):
            return self.getToken(CSELParser.ARRAY, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_typ




    def typ(self):

        localctx = CSELParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.NUMBER) | (1 << CSELParser.BOOLEAN) | (1 << CSELParser.STRING) | (1 << CSELParser.JSON) | (1 << CSELParser.ARRAY))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(CSELParser.VarContext,0)


        def COLON(self):
            return self.getToken(CSELParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSELParser.TypContext,0)


        def ASSIGN(self):
            return self.getToken(CSELParser.ASSIGN, 0)

        def vartail(self):
            return self.getTypedRuleContext(CSELParser.VartailContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_variable




    def variable(self):

        localctx = CSELParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.var()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.COLON:
                self.state = 95
                self.match(CSELParser.COLON)
                self.state = 96
                self.typ()


            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.ASSIGN:
                self.state = 99
                self.match(CSELParser.ASSIGN)

                self.state = 100
                self.vartail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(CSELParser.LiteralContext,0)


        def expr(self):
            return self.getTypedRuleContext(CSELParser.ExprContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_vartail




    def vartail(self):

        localctx = CSELParser.VartailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vartail)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def LQP(self):
            return self.getToken(CSELParser.LQP, 0)

        def varlist(self):
            return self.getTypedRuleContext(CSELParser.VarlistContext,0)


        def RQP(self):
            return self.getToken(CSELParser.RQP, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_var




    def var(self):

        localctx = CSELParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(CSELParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.LQP:
                self.state = 108
                self.match(CSELParser.LQP)
                self.state = 109
                self.varlist()
                self.state = 110
                self.match(CSELParser.RQP)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(CSELParser.NUMLIT, 0)

        def CM(self):
            return self.getToken(CSELParser.CM, 0)

        def varlist(self):
            return self.getTypedRuleContext(CSELParser.VarlistContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_varlist




    def varlist(self):

        localctx = CSELParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varlist)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.match(CSELParser.NUMLIT)
                self.state = 115
                self.match(CSELParser.CM)
                self.state = 116
                self.varlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(CSELParser.NUMLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSELParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSELParser.FALSE, 0)

        def NUMLIT(self):
            return self.getToken(CSELParser.NUMLIT, 0)

        def STRINGLIT(self):
            return self.getToken(CSELParser.STRINGLIT, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(CSELParser.ArrayLiteralContext,0)


        def jsonLiteral(self):
            return self.getTypedRuleContext(CSELParser.JsonLiteralContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_literal




    def literal(self):

        localctx = CSELParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literal)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.TRUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(CSELParser.TRUE)
                pass
            elif token in [CSELParser.FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(CSELParser.FALSE)
                pass
            elif token in [CSELParser.NUMLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(CSELParser.NUMLIT)
                pass
            elif token in [CSELParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(CSELParser.STRINGLIT)
                pass
            elif token in [CSELParser.LQP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.arrayLiteral()
                pass
            elif token in [CSELParser.LB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.jsonLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LQP(self):
            return self.getToken(CSELParser.LQP, 0)

        def RQP(self):
            return self.getToken(CSELParser.RQP, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.LiteralContext)
            else:
                return self.getTypedRuleContext(CSELParser.LiteralContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_arrayLiteral




    def arrayLiteral(self):

        localctx = CSELParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(CSELParser.LQP)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.NUMLIT) | (1 << CSELParser.STRINGLIT) | (1 << CSELParser.TRUE) | (1 << CSELParser.FALSE) | (1 << CSELParser.LQP) | (1 << CSELParser.LB))) != 0):
                self.state = 129
                self.literal()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSELParser.CM:
                    self.state = 130
                    self.match(CSELParser.CM)
                    self.state = 131
                    self.literal()
                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 139
            self.match(CSELParser.RQP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JsonLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSELParser.LB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.ID)
            else:
                return self.getToken(CSELParser.ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.COLON)
            else:
                return self.getToken(CSELParser.COLON, i)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.LiteralContext)
            else:
                return self.getTypedRuleContext(CSELParser.LiteralContext,i)


        def RB(self):
            return self.getToken(CSELParser.RB, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_jsonLiteral




    def jsonLiteral(self):

        localctx = CSELParser.JsonLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_jsonLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(CSELParser.LB)
            self.state = 142
            self.match(CSELParser.ID)
            self.state = 143
            self.match(CSELParser.COLON)
            self.state = 144
            self.literal()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.CM:
                self.state = 145
                self.match(CSELParser.CM)
                self.state = 146
                self.match(CSELParser.ID)
                self.state = 147
                self.match(CSELParser.COLON)
                self.state = 148
                self.literal()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.match(CSELParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(CSELParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def LP(self):
            return self.getToken(CSELParser.LP, 0)

        def RP(self):
            return self.getToken(CSELParser.RP, 0)

        def LB(self):
            return self.getToken(CSELParser.LB, 0)

        def body(self):
            return self.getTypedRuleContext(CSELParser.BodyContext,0)


        def RB(self):
            return self.getToken(CSELParser.RB, 0)

        def paraList(self):
            return self.getTypedRuleContext(CSELParser.ParaListContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_funcDecl




    def funcDecl(self):

        localctx = CSELParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(CSELParser.FUNCTION)
            self.state = 157
            self.match(CSELParser.ID)
            self.state = 158
            self.match(CSELParser.LP)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.ID:
                self.state = 159
                self.paraList()


            self.state = 162
            self.match(CSELParser.RP)
            self.state = 163
            self.match(CSELParser.LB)
            self.state = 164
            self.body()
            self.state = 165
            self.match(CSELParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.VarContext)
            else:
                return self.getTypedRuleContext(CSELParser.VarContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_paraList




    def paraList(self):

        localctx = CSELParser.ParaListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.var()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.CM:
                self.state = 168
                self.match(CSELParser.CM)
                self.state = 169
                self.var()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtList(self):
            return self.getTypedRuleContext(CSELParser.StmtListContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_body




    def body(self):

        localctx = CSELParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.stmtList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manyStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ManyStmtContext)
            else:
                return self.getTypedRuleContext(CSELParser.ManyStmtContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_stmtList




    def stmtList(self):

        localctx = CSELParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmtList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.ID) | (1 << CSELParser.BREAK) | (1 << CSELParser.CONTINUE) | (1 << CSELParser.IF) | (1 << CSELParser.WHILE) | (1 << CSELParser.FOR) | (1 << CSELParser.LET) | (1 << CSELParser.CALL) | (1 << CSELParser.RETURN) | (1 << CSELParser.CONSTANT))) != 0):
                self.state = 177
                self.manyStmt()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManyStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(CSELParser.VarDeclContext,0)


        def otherStmt(self):
            return self.getTypedRuleContext(CSELParser.OtherStmtContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_manyStmt




    def manyStmt(self):

        localctx = CSELParser.ManyStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_manyStmt)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.LET, CSELParser.CONSTANT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.varDecl()
                pass
            elif token in [CSELParser.ID, CSELParser.BREAK, CSELParser.CONTINUE, CSELParser.IF, CSELParser.WHILE, CSELParser.FOR, CSELParser.CALL, CSELParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.otherStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(CSELParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(CSELParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(CSELParser.ForStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(CSELParser.WhileStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(CSELParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(CSELParser.ContinueStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(CSELParser.CallStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(CSELParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_otherStmt




    def otherStmt(self):

        localctx = CSELParser.OtherStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_otherStmt)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.assignStmt()
                pass
            elif token in [CSELParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.ifStmt()
                pass
            elif token in [CSELParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.forStmt()
                pass
            elif token in [CSELParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.whileStmt()
                pass
            elif token in [CSELParser.BREAK]:
                self.enterOuterAlt(localctx, 5)
                self.state = 191
                self.breakStmt()
                pass
            elif token in [CSELParser.CONTINUE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 192
                self.continueStmt()
                pass
            elif token in [CSELParser.CALL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 193
                self.callStmt()
                pass
            elif token in [CSELParser.RETURN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 194
                self.returnStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CSELParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSELParser.ExprContext,i)


        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def LQP(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.LQP)
            else:
                return self.getToken(CSELParser.LQP, i)

        def RQP(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.RQP)
            else:
                return self.getToken(CSELParser.RQP, i)

        def getRuleIndex(self):
            return CSELParser.RULE_assignStmt




    def assignStmt(self):

        localctx = CSELParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(CSELParser.ID)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.LQP:
                self.state = 198
                self.match(CSELParser.LQP)
                self.state = 199
                self.expr()
                self.state = 200
                self.match(CSELParser.RQP)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(CSELParser.ASSIGN)
            self.state = 208
            self.expr()
            self.state = 209
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSELParser.IF, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.LP)
            else:
                return self.getToken(CSELParser.LP, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSELParser.ExprContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.RP)
            else:
                return self.getToken(CSELParser.RP, i)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.LB)
            else:
                return self.getToken(CSELParser.LB, i)

        def stmtList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.StmtListContext)
            else:
                return self.getTypedRuleContext(CSELParser.StmtListContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.RB)
            else:
                return self.getToken(CSELParser.RB, i)

        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.ELIF)
            else:
                return self.getToken(CSELParser.ELIF, i)

        def ELSE(self):
            return self.getToken(CSELParser.ELSE, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_ifStmt




    def ifStmt(self):

        localctx = CSELParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(CSELParser.IF)
            self.state = 212
            self.match(CSELParser.LP)
            self.state = 213
            self.expr()
            self.state = 214
            self.match(CSELParser.RP)
            self.state = 215
            self.match(CSELParser.LB)
            self.state = 216
            self.stmtList()
            self.state = 217
            self.match(CSELParser.RB)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.ELIF:
                self.state = 218
                self.match(CSELParser.ELIF)
                self.state = 219
                self.match(CSELParser.LP)
                self.state = 220
                self.expr()
                self.state = 221
                self.match(CSELParser.RP)
                self.state = 222
                self.match(CSELParser.LB)
                self.state = 223
                self.stmtList()
                self.state = 224
                self.match(CSELParser.RB)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.ELSE:
                self.state = 231
                self.match(CSELParser.ELSE)
                self.state = 232
                self.match(CSELParser.LB)
                self.state = 233
                self.stmtList()
                self.state = 234
                self.match(CSELParser.RB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSELParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.ID)
            else:
                return self.getToken(CSELParser.ID, i)

        def IN(self):
            return self.getToken(CSELParser.IN, 0)

        def arrayLiteral(self):
            return self.getTypedRuleContext(CSELParser.ArrayLiteralContext,0)


        def LB(self):
            return self.getToken(CSELParser.LB, 0)

        def stmtList(self):
            return self.getTypedRuleContext(CSELParser.StmtListContext,0)


        def RB(self):
            return self.getToken(CSELParser.RB, 0)

        def OF(self):
            return self.getToken(CSELParser.OF, 0)

        def jsonLiteral(self):
            return self.getTypedRuleContext(CSELParser.JsonLiteralContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_forStmt




    def forStmt(self):

        localctx = CSELParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forStmt)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(CSELParser.FOR)
                self.state = 239
                self.match(CSELParser.ID)
                self.state = 240
                self.match(CSELParser.IN)
                self.state = 241
                self.arrayLiteral()
                self.state = 242
                self.match(CSELParser.LB)
                self.state = 243
                self.stmtList()
                self.state = 244
                self.match(CSELParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(CSELParser.FOR)
                self.state = 247
                self.match(CSELParser.ID)
                self.state = 248
                self.match(CSELParser.OF)
                self.state = 249
                self.jsonLiteral()
                self.state = 250
                self.match(CSELParser.LB)
                self.state = 251
                self.stmtList()
                self.state = 252
                self.match(CSELParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.match(CSELParser.FOR)
                self.state = 255
                self.match(CSELParser.ID)
                self.state = 256
                self.match(CSELParser.IN)
                self.state = 257
                self.match(CSELParser.ID)
                self.state = 258
                self.match(CSELParser.LB)
                self.state = 259
                self.stmtList()
                self.state = 260
                self.match(CSELParser.RB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.match(CSELParser.FOR)
                self.state = 263
                self.match(CSELParser.ID)
                self.state = 264
                self.match(CSELParser.OF)
                self.state = 265
                self.match(CSELParser.ID)
                self.state = 266
                self.match(CSELParser.LB)
                self.state = 267
                self.stmtList()
                self.state = 268
                self.match(CSELParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CSELParser.WHILE, 0)

        def LP(self):
            return self.getToken(CSELParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(CSELParser.ExprContext,0)


        def RP(self):
            return self.getToken(CSELParser.RP, 0)

        def LB(self):
            return self.getToken(CSELParser.LB, 0)

        def stmtList(self):
            return self.getTypedRuleContext(CSELParser.StmtListContext,0)


        def RB(self):
            return self.getToken(CSELParser.RB, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_whileStmt




    def whileStmt(self):

        localctx = CSELParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(CSELParser.WHILE)
            self.state = 273
            self.match(CSELParser.LP)
            self.state = 274
            self.expr()
            self.state = 275
            self.match(CSELParser.RP)
            self.state = 276
            self.match(CSELParser.LB)
            self.state = 277
            self.stmtList()
            self.state = 278
            self.match(CSELParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSELParser.BREAK, 0)

        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_breakStmt




    def breakStmt(self):

        localctx = CSELParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(CSELParser.BREAK)
            self.state = 281
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSELParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_continueStmt




    def continueStmt(self):

        localctx = CSELParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(CSELParser.CONTINUE)
            self.state = 284
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(CSELParser.FuncallContext,0)


        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_callStmt




    def callStmt(self):

        localctx = CSELParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_callStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.funcall()
            self.state = 287
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(CSELParser.CALL, 0)

        def LP(self):
            return self.getToken(CSELParser.LP, 0)

        def callList(self):
            return self.getTypedRuleContext(CSELParser.CallListContext,0)


        def RP(self):
            return self.getToken(CSELParser.RP, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_funcall




    def funcall(self):

        localctx = CSELParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_funcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(CSELParser.CALL)
            self.state = 290
            self.match(CSELParser.LP)
            self.state = 291
            self.callList()
            self.state = 292
            self.match(CSELParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSELParser.RETURN, 0)

        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def expr(self):
            return self.getTypedRuleContext(CSELParser.ExprContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_returnStmt




    def returnStmt(self):

        localctx = CSELParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(CSELParser.RETURN)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.ID) | (1 << CSELParser.NUMLIT) | (1 << CSELParser.STRINGLIT) | (1 << CSELParser.TRUE) | (1 << CSELParser.FALSE) | (1 << CSELParser.CALL) | (1 << CSELParser.SUB) | (1 << CSELParser.NOT) | (1 << CSELParser.LP))) != 0):
                self.state = 295
                self.expr()


            self.state = 298
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.LogicExprContext)
            else:
                return self.getTypedRuleContext(CSELParser.LogicExprContext,i)


        def EQ(self):
            return self.getToken(CSELParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CSELParser.NEQ, 0)

        def GT(self):
            return self.getToken(CSELParser.GT, 0)

        def GTE(self):
            return self.getToken(CSELParser.GTE, 0)

        def LT(self):
            return self.getToken(CSELParser.LT, 0)

        def LTE(self):
            return self.getToken(CSELParser.LTE, 0)

        def SEQ(self):
            return self.getToken(CSELParser.SEQ, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_expr




    def expr(self):

        localctx = CSELParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.logicExpr()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.EQ) | (1 << CSELParser.NEQ) | (1 << CSELParser.GT) | (1 << CSELParser.GTE) | (1 << CSELParser.LT) | (1 << CSELParser.LTE) | (1 << CSELParser.SEQ))) != 0):
                self.state = 301
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.EQ) | (1 << CSELParser.NEQ) | (1 << CSELParser.GT) | (1 << CSELParser.GTE) | (1 << CSELParser.LT) | (1 << CSELParser.LTE) | (1 << CSELParser.SEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 302
                self.logicExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(CSELParser.AdditiveExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.AND)
            else:
                return self.getToken(CSELParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.OR)
            else:
                return self.getToken(CSELParser.OR, i)

        def getRuleIndex(self):
            return CSELParser.RULE_logicExpr




    def logicExpr(self):

        localctx = CSELParser.LogicExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_logicExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.additiveExpr()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.AND or _la==CSELParser.OR:
                self.state = 306
                _la = self._input.LA(1)
                if not(_la==CSELParser.AND or _la==CSELParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 307
                self.additiveExpr()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicateExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.MultiplicateExprContext)
            else:
                return self.getTypedRuleContext(CSELParser.MultiplicateExprContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.ADD)
            else:
                return self.getToken(CSELParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.SUB)
            else:
                return self.getToken(CSELParser.SUB, i)

        def SADD(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.SADD)
            else:
                return self.getToken(CSELParser.SADD, i)

        def getRuleIndex(self):
            return CSELParser.RULE_additiveExpr




    def additiveExpr(self):

        localctx = CSELParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.multiplicateExpr()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.ADD) | (1 << CSELParser.SUB) | (1 << CSELParser.SADD))) != 0):
                self.state = 314
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.ADD) | (1 << CSELParser.SUB) | (1 << CSELParser.SADD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 315
                self.multiplicateExpr()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicateExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryLogicExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.UnaryLogicExprContext)
            else:
                return self.getTypedRuleContext(CSELParser.UnaryLogicExprContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.MUL)
            else:
                return self.getToken(CSELParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.DIV)
            else:
                return self.getToken(CSELParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.MOD)
            else:
                return self.getToken(CSELParser.MOD, i)

        def getRuleIndex(self):
            return CSELParser.RULE_multiplicateExpr




    def multiplicateExpr(self):

        localctx = CSELParser.MultiplicateExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_multiplicateExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.unaryLogicExpr()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.MUL) | (1 << CSELParser.DIV) | (1 << CSELParser.MOD))) != 0):
                self.state = 322
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.MUL) | (1 << CSELParser.DIV) | (1 << CSELParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 323
                self.unaryLogicExpr()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryLogicExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unarySignExpr(self):
            return self.getTypedRuleContext(CSELParser.UnarySignExprContext,0)


        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.NOT)
            else:
                return self.getToken(CSELParser.NOT, i)

        def getRuleIndex(self):
            return CSELParser.RULE_unaryLogicExpr




    def unaryLogicExpr(self):

        localctx = CSELParser.UnaryLogicExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_unaryLogicExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.NOT:
                self.state = 329
                self.match(CSELParser.NOT)
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 335
            self.unarySignExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnarySignExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexExpr(self):
            return self.getTypedRuleContext(CSELParser.IndexExprContext,0)


        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.SUB)
            else:
                return self.getToken(CSELParser.SUB, i)

        def getRuleIndex(self):
            return CSELParser.RULE_unarySignExpr




    def unarySignExpr(self):

        localctx = CSELParser.UnarySignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_unarySignExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.SUB:
                self.state = 337
                self.match(CSELParser.SUB)
                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 343
            self.indexExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def LQP(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.LQP)
            else:
                return self.getToken(CSELParser.LQP, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSELParser.ExprContext,i)


        def RQP(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.RQP)
            else:
                return self.getToken(CSELParser.RQP, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def finalExpr(self):
            return self.getTypedRuleContext(CSELParser.FinalExprContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_indexExpr




    def indexExpr(self):

        localctx = CSELParser.IndexExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_indexExpr)
        self._la = 0 # Token type
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(CSELParser.ID)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSELParser.LQP:
                    self.state = 346
                    self.match(CSELParser.LQP)
                    self.state = 347
                    self.expr()
                    self.state = 352
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSELParser.CM:
                        self.state = 348
                        self.match(CSELParser.CM)
                        self.state = 349
                        self.expr()
                        self.state = 354
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 355
                    self.match(CSELParser.RQP)
                    self.state = 361
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [CSELParser.NUMLIT, CSELParser.STRINGLIT, CSELParser.TRUE, CSELParser.FALSE, CSELParser.CALL, CSELParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.finalExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinalExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(CSELParser.NUMLIT, 0)

        def TRUE(self):
            return self.getToken(CSELParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSELParser.FALSE, 0)

        def STRINGLIT(self):
            return self.getToken(CSELParser.STRINGLIT, 0)

        def funcall(self):
            return self.getTypedRuleContext(CSELParser.FuncallContext,0)


        def LP(self):
            return self.getToken(CSELParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(CSELParser.ExprContext,0)


        def RP(self):
            return self.getToken(CSELParser.RP, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_finalExpr




    def finalExpr(self):

        localctx = CSELParser.FinalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_finalExpr)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(CSELParser.NUMLIT)
                pass
            elif token in [CSELParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(CSELParser.TRUE)
                pass
            elif token in [CSELParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                self.match(CSELParser.FALSE)
                pass
            elif token in [CSELParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 368
                self.match(CSELParser.STRINGLIT)
                pass
            elif token in [CSELParser.CALL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 369
                self.funcall()
                pass
            elif token in [CSELParser.LP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 370
                self.match(CSELParser.LP)
                self.state = 371
                self.expr()
                self.state = 372
                self.match(CSELParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSELParser.ID, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def LQP(self):
            return self.getToken(CSELParser.LQP, 0)

        def RQP(self):
            return self.getToken(CSELParser.RQP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSELParser.ExprContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_callList




    def callList(self):

        localctx = CSELParser.CallListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_callList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(CSELParser.ID)
            self.state = 377
            self.match(CSELParser.CM)
            self.state = 378
            self.match(CSELParser.LQP)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.ID) | (1 << CSELParser.NUMLIT) | (1 << CSELParser.STRINGLIT) | (1 << CSELParser.TRUE) | (1 << CSELParser.FALSE) | (1 << CSELParser.CALL) | (1 << CSELParser.SUB) | (1 << CSELParser.NOT) | (1 << CSELParser.LP))) != 0):
                self.state = 384
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 379
                        self.expr()
                        self.state = 380
                        self.match(CSELParser.CM) 
                    self.state = 386
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 387
                self.expr()


            self.state = 390
            self.match(CSELParser.RQP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





