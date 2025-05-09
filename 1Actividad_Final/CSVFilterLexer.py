# Generated from CSVFilter.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13M\n\13\3")
        buf.write("\f\3\f\7\fQ\n\f\f\f\16\fT\13\f\3\f\3\f\3\r\6\rY\n\r\r")
        buf.write("\r\16\rZ\3\16\6\16^\n\16\r\16\16\16_\3\16\3\16\2\2\17")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\3\2\6\4\2>>@@\5\2\f\f\17\17$$\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"\2i\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\"\3\2\2\2\7$\3\2\2")
        buf.write("\2\t+\3\2\2\2\13\61\3\2\2\2\r\63\3\2\2\2\17\65\3\2\2\2")
        buf.write("\21<\3\2\2\2\23@\3\2\2\2\25L\3\2\2\2\27N\3\2\2\2\31X\3")
        buf.write("\2\2\2\33]\3\2\2\2\35\36\7n\2\2\36\37\7q\2\2\37 \7c\2")
        buf.write("\2 !\7f\2\2!\4\3\2\2\2\"#\7=\2\2#\6\3\2\2\2$%\7h\2\2%")
        buf.write("&\7k\2\2&\'\7n\2\2\'(\7v\2\2()\7g\2\2)*\7t\2\2*\b\3\2")
        buf.write("\2\2+,\7r\2\2,-\7t\2\2-.\7k\2\2./\7p\2\2/\60\7v\2\2\60")
        buf.write("\n\3\2\2\2\61\62\7*\2\2\62\f\3\2\2\2\63\64\7+\2\2\64\16")
        buf.write("\3\2\2\2\65\66\7e\2\2\66\67\7q\2\2\678\7n\2\289\7w\2\2")
        buf.write("9:\7o\2\2:;\7p\2\2;\20\3\2\2\2<=\7C\2\2=>\7P\2\2>?\7F")
        buf.write("\2\2?\22\3\2\2\2@A\7Q\2\2AB\7T\2\2B\24\3\2\2\2CM\t\2\2")
        buf.write("\2DE\7?\2\2EM\7?\2\2FG\7#\2\2GM\7?\2\2HI\7@\2\2IM\7?\2")
        buf.write("\2JK\7>\2\2KM\7?\2\2LC\3\2\2\2LD\3\2\2\2LF\3\2\2\2LH\3")
        buf.write("\2\2\2LJ\3\2\2\2M\26\3\2\2\2NR\7$\2\2OQ\n\3\2\2PO\3\2")
        buf.write("\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2")
        buf.write("UV\7$\2\2V\30\3\2\2\2WY\t\4\2\2XW\3\2\2\2YZ\3\2\2\2ZX")
        buf.write("\3\2\2\2Z[\3\2\2\2[\32\3\2\2\2\\^\t\5\2\2]\\\3\2\2\2^")
        buf.write("_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\b\16\2\2b\34")
        buf.write("\3\2\2\2\7\2LRZ_\3\b\2\2")
        return buf.getvalue()


class CSVFilterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    AND = 8
    OR = 9
    OPERATOR = 10
    STRING = 11
    INT = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'load'", "';'", "'filter'", "'print'", "'('", "')'", "'column'", 
            "'AND'", "'OR'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "OPERATOR", "STRING", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "AND", "OR", "OPERATOR", "STRING", "INT", "WS" ]

    grammarFileName = "CSVFilter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


