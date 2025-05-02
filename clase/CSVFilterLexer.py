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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7:\n\7\3\b\3\b\7\b>\n\b\f\b\16\bA\13\b\3\b\3")
        buf.write("\b\3\t\6\tF\n\t\r\t\16\tG\3\t\3\t\6\tL\n\t\r\t\16\tM\5")
        buf.write("\tP\n\t\3\n\6\nS\n\n\r\n\16\nT\3\n\3\n\2\2\13\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\6\4\2>>@@\5\2\f")
        buf.write("\f\17\17$$\3\2\62;\5\2\13\f\17\17\"\"\2`\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2")
        buf.write("\2\2\5\32\3\2\2\2\7\34\3\2\2\2\t#\3\2\2\2\13*\3\2\2\2")
        buf.write("\r9\3\2\2\2\17;\3\2\2\2\21E\3\2\2\2\23R\3\2\2\2\25\26")
        buf.write("\7n\2\2\26\27\7q\2\2\27\30\7c\2\2\30\31\7f\2\2\31\4\3")
        buf.write("\2\2\2\32\33\7=\2\2\33\6\3\2\2\2\34\35\7h\2\2\35\36\7")
        buf.write("k\2\2\36\37\7n\2\2\37 \7v\2\2 !\7g\2\2!\"\7t\2\2\"\b\3")
        buf.write("\2\2\2#$\7e\2\2$%\7q\2\2%&\7n\2\2&\'\7w\2\2\'(\7o\2\2")
        buf.write("()\7p\2\2)\n\3\2\2\2*+\7r\2\2+,\7t\2\2,-\7k\2\2-.\7p\2")
        buf.write("\2./\7v\2\2/\f\3\2\2\2\60:\t\2\2\2\61\62\7@\2\2\62:\7")
        buf.write("?\2\2\63\64\7>\2\2\64:\7?\2\2\65\66\7?\2\2\66:\7?\2\2")
        buf.write("\678\7#\2\28:\7?\2\29\60\3\2\2\29\61\3\2\2\29\63\3\2\2")
        buf.write("\29\65\3\2\2\29\67\3\2\2\2:\16\3\2\2\2;?\7$\2\2<>\n\3")
        buf.write("\2\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2")
        buf.write("A?\3\2\2\2BC\7$\2\2C\20\3\2\2\2DF\t\4\2\2ED\3\2\2\2FG")
        buf.write("\3\2\2\2GE\3\2\2\2GH\3\2\2\2HO\3\2\2\2IK\7\60\2\2JL\t")
        buf.write("\4\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2")
        buf.write("\2OI\3\2\2\2OP\3\2\2\2P\22\3\2\2\2QS\t\5\2\2RQ\3\2\2\2")
        buf.write("ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2UV\3\2\2\2VW\b\n\2\2W\24")
        buf.write("\3\2\2\2\t\29?GMOT\3\b\2\2")
        return buf.getvalue()


class CSVFilterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    OPERATOR = 6
    STRING = 7
    NUMBER = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'load'", "';'", "'filter'", "'column'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "OPERATOR", "STRING", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "OPERATOR", "STRING", 
                  "NUMBER", "WS" ]

    grammarFileName = "CSVFilter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


