# Generated from Simple.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16A\n")
        buf.write("\16\r\16\16\16B\3\17\3\17\7\17G\n\17\f\17\16\17J\13\17")
        buf.write("\3\20\6\20M\n\20\r\20\16\20N\3\20\3\20\2\2\21\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21\3\2\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\13\f\17\17\"\"\2T\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2")
        buf.write("\2\2\5\'\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13/\3\2\2\2\r\61")
        buf.write("\3\2\2\2\17\63\3\2\2\2\21\65\3\2\2\2\23\67\3\2\2\2\25")
        buf.write("9\3\2\2\2\27;\3\2\2\2\31=\3\2\2\2\33@\3\2\2\2\35D\3\2")
        buf.write("\2\2\37L\3\2\2\2!\"\7e\2\2\"#\7n\2\2#$\7c\2\2$%\7u\2\2")
        buf.write("%&\7u\2\2&\4\3\2\2\2\'(\7}\2\2(\6\3\2\2\2)*\7\177\2\2")
        buf.write("*\b\3\2\2\2+,\7k\2\2,-\7p\2\2-.\7v\2\2.\n\3\2\2\2/\60")
        buf.write("\7=\2\2\60\f\3\2\2\2\61\62\7*\2\2\62\16\3\2\2\2\63\64")
        buf.write("\7+\2\2\64\20\3\2\2\2\65\66\7?\2\2\66\22\3\2\2\2\678\7")
        buf.write(",\2\28\24\3\2\2\29:\7\61\2\2:\26\3\2\2\2;<\7-\2\2<\30")
        buf.write("\3\2\2\2=>\7/\2\2>\32\3\2\2\2?A\t\2\2\2@?\3\2\2\2AB\3")
        buf.write("\2\2\2B@\3\2\2\2BC\3\2\2\2C\34\3\2\2\2DH\t\3\2\2EG\t\4")
        buf.write("\2\2FE\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\36\3\2\2")
        buf.write("\2JH\3\2\2\2KM\t\5\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2N")
        buf.write("O\3\2\2\2OP\3\2\2\2PQ\b\20\2\2Q \3\2\2\2\6\2BHN\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class SimpleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    INT = 13
    ID = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'{'", "'}'", "'int'", "';'", "'('", "')'", "'='", 
            "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "INT", "ID", 
                  "WS" ]

    grammarFileName = "Simple.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


