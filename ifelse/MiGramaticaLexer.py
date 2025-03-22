# Generated from MiGramatica.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\7\22R\n\22\f\22\16\22U\13\22\3\23")
        buf.write("\6\23X\n\23\r\23\16\23Y\3\24\6\24]\n\24\r\24\16\24^\3")
        buf.write("\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write("\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17")
        buf.write("\"\"\2d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7")
        buf.write(".\3\2\2\2\t\60\3\2\2\2\13\62\3\2\2\2\r\64\3\2\2\2\17\66")
        buf.write("\3\2\2\2\21;\3\2\2\2\23=\3\2\2\2\25?\3\2\2\2\27B\3\2\2")
        buf.write("\2\31E\3\2\2\2\33G\3\2\2\2\35I\3\2\2\2\37K\3\2\2\2!M\3")
        buf.write("\2\2\2#O\3\2\2\2%W\3\2\2\2\'\\\3\2\2\2)*\7=\2\2*\4\3\2")
        buf.write("\2\2+,\7k\2\2,-\7h\2\2-\6\3\2\2\2./\7*\2\2/\b\3\2\2\2")
        buf.write("\60\61\7+\2\2\61\n\3\2\2\2\62\63\7}\2\2\63\f\3\2\2\2\64")
        buf.write("\65\7\177\2\2\65\16\3\2\2\2\66\67\7g\2\2\678\7n\2\289")
        buf.write("\7u\2\29:\7g\2\2:\20\3\2\2\2;<\7@\2\2<\22\3\2\2\2=>\7")
        buf.write(">\2\2>\24\3\2\2\2?@\7?\2\2@A\7?\2\2A\26\3\2\2\2BC\7#\2")
        buf.write("\2CD\7?\2\2D\30\3\2\2\2EF\7?\2\2F\32\3\2\2\2GH\7,\2\2")
        buf.write("H\34\3\2\2\2IJ\7\61\2\2J\36\3\2\2\2KL\7-\2\2L \3\2\2\2")
        buf.write("MN\7/\2\2N\"\3\2\2\2OS\t\2\2\2PR\t\3\2\2QP\3\2\2\2RU\3")
        buf.write("\2\2\2SQ\3\2\2\2ST\3\2\2\2T$\3\2\2\2US\3\2\2\2VX\t\4\2")
        buf.write("\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z&\3\2\2\2[")
        buf.write("]\t\5\2\2\\[\3\2\2\2]^\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_`")
        buf.write("\3\2\2\2`a\b\24\2\2a(\3\2\2\2\6\2SY^\3\b\2\2")
        return buf.getvalue()


class MiGramaticaLexer(Lexer):

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
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    ID = 17
    INT = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'if'", "'('", "')'", "'{'", "'}'", "'else'", "'>'", 
            "'<'", "'=='", "'!='", "'='", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "ID", "INT", "WS" ]

    grammarFileName = "MiGramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


