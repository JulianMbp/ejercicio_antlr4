# Generated from CSVFilter.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,32,276,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,3,23,195,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,3,24,206,8,24,1,25,4,25,209,8,25,11,25,12,25,210,1,25,1,25,
        4,25,215,8,25,11,25,12,25,216,1,26,1,26,1,26,1,26,1,26,3,26,224,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,3,27,243,8,27,1,28,1,28,5,28,247,8,28,10,
        28,12,28,250,9,28,1,28,1,28,1,29,4,29,255,8,29,11,29,12,29,256,1,
        30,1,30,1,30,1,30,5,30,263,8,30,10,30,12,30,266,9,30,1,30,1,30,1,
        31,4,31,271,8,31,11,31,12,31,272,1,31,1,31,0,0,32,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,
        16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,
        27,55,28,57,29,59,30,61,31,63,32,1,0,5,1,0,48,57,2,0,60,60,62,62,
        3,0,10,10,13,13,34,34,2,0,10,10,13,13,3,0,9,10,13,13,32,32,292,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,
        0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,
        0,0,0,0,63,1,0,0,0,1,65,1,0,0,0,3,70,1,0,0,0,5,72,1,0,0,0,7,79,1,
        0,0,0,9,86,1,0,0,0,11,88,1,0,0,0,13,90,1,0,0,0,15,92,1,0,0,0,17,
        102,1,0,0,0,19,107,1,0,0,0,21,110,1,0,0,0,23,114,1,0,0,0,25,119,
        1,0,0,0,27,125,1,0,0,0,29,130,1,0,0,0,31,133,1,0,0,0,33,135,1,0,
        0,0,35,141,1,0,0,0,37,147,1,0,0,0,39,155,1,0,0,0,41,159,1,0,0,0,
        43,162,1,0,0,0,45,167,1,0,0,0,47,194,1,0,0,0,49,205,1,0,0,0,51,208,
        1,0,0,0,53,223,1,0,0,0,55,242,1,0,0,0,57,244,1,0,0,0,59,254,1,0,
        0,0,61,258,1,0,0,0,63,270,1,0,0,0,65,66,5,108,0,0,66,67,5,111,0,
        0,67,68,5,97,0,0,68,69,5,100,0,0,69,2,1,0,0,0,70,71,5,59,0,0,71,
        4,1,0,0,0,72,73,5,102,0,0,73,74,5,105,0,0,74,75,5,108,0,0,75,76,
        5,116,0,0,76,77,5,101,0,0,77,78,5,114,0,0,78,6,1,0,0,0,79,80,5,99,
        0,0,80,81,5,111,0,0,81,82,5,108,0,0,82,83,5,117,0,0,83,84,5,109,
        0,0,84,85,5,110,0,0,85,8,1,0,0,0,86,87,5,40,0,0,87,10,1,0,0,0,88,
        89,5,41,0,0,89,12,1,0,0,0,90,91,5,44,0,0,91,14,1,0,0,0,92,93,5,97,
        0,0,93,94,5,103,0,0,94,95,5,103,0,0,95,96,5,114,0,0,96,97,5,101,
        0,0,97,98,5,103,0,0,98,99,5,97,0,0,99,100,5,116,0,0,100,101,5,101,
        0,0,101,16,1,0,0,0,102,103,5,115,0,0,103,104,5,111,0,0,104,105,5,
        114,0,0,105,106,5,116,0,0,106,18,1,0,0,0,107,108,5,98,0,0,108,109,
        5,121,0,0,109,20,1,0,0,0,110,111,5,97,0,0,111,112,5,115,0,0,112,
        113,5,99,0,0,113,22,1,0,0,0,114,115,5,100,0,0,115,116,5,101,0,0,
        116,117,5,115,0,0,117,118,5,99,0,0,118,24,1,0,0,0,119,120,5,108,
        0,0,120,121,5,105,0,0,121,122,5,109,0,0,122,123,5,105,0,0,123,124,
        5,116,0,0,124,26,1,0,0,0,125,126,5,106,0,0,126,127,5,111,0,0,127,
        128,5,105,0,0,128,129,5,110,0,0,129,28,1,0,0,0,130,131,5,111,0,0,
        131,132,5,110,0,0,132,30,1,0,0,0,133,134,5,61,0,0,134,32,1,0,0,0,
        135,136,5,103,0,0,136,137,5,114,0,0,137,138,5,111,0,0,138,139,5,
        117,0,0,139,140,5,112,0,0,140,34,1,0,0,0,141,142,5,112,0,0,142,143,
        5,114,0,0,143,144,5,105,0,0,144,145,5,110,0,0,145,146,5,116,0,0,
        146,36,1,0,0,0,147,148,5,98,0,0,148,149,5,101,0,0,149,150,5,116,
        0,0,150,151,5,119,0,0,151,152,5,101,0,0,152,153,5,101,0,0,153,154,
        5,110,0,0,154,38,1,0,0,0,155,156,5,97,0,0,156,157,5,110,0,0,157,
        158,5,100,0,0,158,40,1,0,0,0,159,160,5,105,0,0,160,161,5,110,0,0,
        161,42,1,0,0,0,162,163,5,108,0,0,163,164,5,105,0,0,164,165,5,107,
        0,0,165,166,5,101,0,0,166,44,1,0,0,0,167,168,5,119,0,0,168,169,5,
        104,0,0,169,170,5,101,0,0,170,171,5,114,0,0,171,172,5,101,0,0,172,
        46,1,0,0,0,173,174,5,99,0,0,174,175,5,111,0,0,175,176,5,117,0,0,
        176,177,5,110,0,0,177,195,5,116,0,0,178,179,5,115,0,0,179,180,5,
        117,0,0,180,195,5,109,0,0,181,182,5,97,0,0,182,183,5,118,0,0,183,
        184,5,101,0,0,184,185,5,114,0,0,185,186,5,97,0,0,186,187,5,103,0,
        0,187,195,5,101,0,0,188,189,5,109,0,0,189,190,5,105,0,0,190,195,
        5,110,0,0,191,192,5,109,0,0,192,193,5,97,0,0,193,195,5,120,0,0,194,
        173,1,0,0,0,194,178,1,0,0,0,194,181,1,0,0,0,194,188,1,0,0,0,194,
        191,1,0,0,0,195,48,1,0,0,0,196,197,5,116,0,0,197,198,5,114,0,0,198,
        199,5,117,0,0,199,206,5,101,0,0,200,201,5,102,0,0,201,202,5,97,0,
        0,202,203,5,108,0,0,203,204,5,115,0,0,204,206,5,101,0,0,205,196,
        1,0,0,0,205,200,1,0,0,0,206,50,1,0,0,0,207,209,7,0,0,0,208,207,1,
        0,0,0,209,210,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,212,1,
        0,0,0,212,214,5,46,0,0,213,215,7,0,0,0,214,213,1,0,0,0,215,216,1,
        0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,52,1,0,0,0,218,219,5,65,
        0,0,219,220,5,78,0,0,220,224,5,68,0,0,221,222,5,79,0,0,222,224,5,
        82,0,0,223,218,1,0,0,0,223,221,1,0,0,0,224,54,1,0,0,0,225,226,5,
        62,0,0,226,243,5,61,0,0,227,228,5,60,0,0,228,243,5,61,0,0,229,243,
        7,1,0,0,230,231,5,61,0,0,231,243,5,61,0,0,232,233,5,33,0,0,233,243,
        5,61,0,0,234,235,5,99,0,0,235,236,5,111,0,0,236,237,5,110,0,0,237,
        238,5,116,0,0,238,239,5,97,0,0,239,240,5,105,0,0,240,241,5,110,0,
        0,241,243,5,115,0,0,242,225,1,0,0,0,242,227,1,0,0,0,242,229,1,0,
        0,0,242,230,1,0,0,0,242,232,1,0,0,0,242,234,1,0,0,0,243,56,1,0,0,
        0,244,248,5,34,0,0,245,247,8,2,0,0,246,245,1,0,0,0,247,250,1,0,0,
        0,248,246,1,0,0,0,248,249,1,0,0,0,249,251,1,0,0,0,250,248,1,0,0,
        0,251,252,5,34,0,0,252,58,1,0,0,0,253,255,7,0,0,0,254,253,1,0,0,
        0,255,256,1,0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,60,1,0,0,0,
        258,259,5,47,0,0,259,260,5,47,0,0,260,264,1,0,0,0,261,263,8,3,0,
        0,262,261,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,
        0,265,267,1,0,0,0,266,264,1,0,0,0,267,268,6,30,0,0,268,62,1,0,0,
        0,269,271,7,4,0,0,270,269,1,0,0,0,271,272,1,0,0,0,272,270,1,0,0,
        0,272,273,1,0,0,0,273,274,1,0,0,0,274,275,6,31,0,0,275,64,1,0,0,
        0,11,0,194,205,210,216,223,242,248,256,264,272,1,6,0,0
    ]

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
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    K_BETWEEN = 19
    K_AND = 20
    K_IN = 21
    K_LIKE = 22
    K_WHERE = 23
    AGGR_FUNC = 24
    BOOLEAN = 25
    FLOAT = 26
    LOGICAL_OP = 27
    OPERATOR = 28
    STRING = 29
    INT = 30
    COMMENT = 31
    WS = 32

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'load'", "';'", "'filter'", "'column'", "'('", "')'", "','", 
            "'aggregate'", "'sort'", "'by'", "'asc'", "'desc'", "'limit'", 
            "'join'", "'on'", "'='", "'group'", "'print'", "'between'", 
            "'and'", "'in'", "'like'", "'where'" ]

    symbolicNames = [ "<INVALID>",
            "K_BETWEEN", "K_AND", "K_IN", "K_LIKE", "K_WHERE", "AGGR_FUNC", 
            "BOOLEAN", "FLOAT", "LOGICAL_OP", "OPERATOR", "STRING", "INT", 
            "COMMENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "K_BETWEEN", "K_AND", 
                  "K_IN", "K_LIKE", "K_WHERE", "AGGR_FUNC", "BOOLEAN", "FLOAT", 
                  "LOGICAL_OP", "OPERATOR", "STRING", "INT", "COMMENT", 
                  "WS" ]

    grammarFileName = "CSVFilter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


