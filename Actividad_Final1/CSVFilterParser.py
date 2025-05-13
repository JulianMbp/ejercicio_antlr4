# Generated from CSVFilter.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,138,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,
        2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,53,8,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,81,8,3,1,4,1,4,1,4,5,4,86,8,4,10,
        4,12,4,89,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,3,5,106,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,
        24,0,2,1,0,11,12,2,0,25,26,29,30,138,0,27,1,0,0,0,2,39,1,0,0,0,4,
        41,1,0,0,0,6,80,1,0,0,0,8,82,1,0,0,0,10,105,1,0,0,0,12,107,1,0,0,
        0,14,113,1,0,0,0,16,115,1,0,0,0,18,119,1,0,0,0,20,127,1,0,0,0,22,
        132,1,0,0,0,24,135,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,
        0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,40,3,4,2,0,32,40,
        3,6,3,0,33,40,3,10,5,0,34,40,3,12,6,0,35,40,3,16,8,0,36,40,3,18,
        9,0,37,40,3,20,10,0,38,40,3,22,11,0,39,31,1,0,0,0,39,32,1,0,0,0,
        39,33,1,0,0,0,39,34,1,0,0,0,39,35,1,0,0,0,39,36,1,0,0,0,39,37,1,
        0,0,0,39,38,1,0,0,0,40,3,1,0,0,0,41,42,5,1,0,0,42,43,5,29,0,0,43,
        44,5,2,0,0,44,5,1,0,0,0,45,46,5,3,0,0,46,47,5,4,0,0,47,48,5,29,0,
        0,48,49,5,28,0,0,49,52,3,24,12,0,50,51,5,27,0,0,51,53,3,6,3,0,52,
        50,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,2,0,0,55,81,1,0,0,
        0,56,57,5,3,0,0,57,58,5,4,0,0,58,59,5,29,0,0,59,60,5,19,0,0,60,61,
        3,24,12,0,61,62,5,20,0,0,62,63,3,24,12,0,63,64,5,2,0,0,64,81,1,0,
        0,0,65,66,5,3,0,0,66,67,5,4,0,0,67,68,5,29,0,0,68,69,5,21,0,0,69,
        70,5,5,0,0,70,71,3,8,4,0,71,72,5,6,0,0,72,73,5,2,0,0,73,81,1,0,0,
        0,74,75,5,3,0,0,75,76,5,4,0,0,76,77,5,29,0,0,77,78,5,22,0,0,78,79,
        5,29,0,0,79,81,5,2,0,0,80,45,1,0,0,0,80,56,1,0,0,0,80,65,1,0,0,0,
        80,74,1,0,0,0,81,7,1,0,0,0,82,87,3,24,12,0,83,84,5,7,0,0,84,86,3,
        24,12,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,
        88,9,1,0,0,0,89,87,1,0,0,0,90,91,5,8,0,0,91,92,5,24,0,0,92,93,5,
        4,0,0,93,94,5,29,0,0,94,106,5,2,0,0,95,96,5,8,0,0,96,97,5,24,0,0,
        97,98,5,4,0,0,98,99,5,29,0,0,99,100,5,23,0,0,100,101,5,29,0,0,101,
        102,5,28,0,0,102,103,3,24,12,0,103,104,5,2,0,0,104,106,1,0,0,0,105,
        90,1,0,0,0,105,95,1,0,0,0,106,11,1,0,0,0,107,108,5,9,0,0,108,109,
        5,10,0,0,109,110,5,29,0,0,110,111,3,14,7,0,111,112,5,2,0,0,112,13,
        1,0,0,0,113,114,7,0,0,0,114,15,1,0,0,0,115,116,5,13,0,0,116,117,
        5,30,0,0,117,118,5,2,0,0,118,17,1,0,0,0,119,120,5,14,0,0,120,121,
        5,29,0,0,121,122,5,15,0,0,122,123,5,29,0,0,123,124,5,16,0,0,124,
        125,5,29,0,0,125,126,5,2,0,0,126,19,1,0,0,0,127,128,5,17,0,0,128,
        129,5,10,0,0,129,130,5,29,0,0,130,131,5,2,0,0,131,21,1,0,0,0,132,
        133,5,18,0,0,133,134,5,2,0,0,134,23,1,0,0,0,135,136,7,1,0,0,136,
        25,1,0,0,0,6,29,39,52,80,87,105
    ]

class CSVFilterParser ( Parser ):

    grammarFileName = "CSVFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'('", "')'", "','", "'aggregate'", "'sort'", "'by'", 
                     "'asc'", "'desc'", "'limit'", "'join'", "'on'", "'='", 
                     "'group'", "'print'", "'between'", "'and'", "'in'", 
                     "'like'", "'where'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "K_BETWEEN", 
                      "K_AND", "K_IN", "K_LIKE", "K_WHERE", "AGGR_FUNC", 
                      "BOOLEAN", "FLOAT", "LOGICAL_OP", "OPERATOR", "STRING", 
                      "INT", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_valueList = 4
    RULE_aggregateStat = 5
    RULE_sortStat = 6
    RULE_sortOrder = 7
    RULE_limitStat = 8
    RULE_joinStat = 9
    RULE_groupStat = 10
    RULE_printStat = 11
    RULE_value = 12

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "valueList", 
                   "aggregateStat", "sortStat", "sortOrder", "limitStat", 
                   "joinStat", "groupStat", "printStat", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    K_BETWEEN=19
    K_AND=20
    K_IN=21
    K_LIKE=22
    K_WHERE=23
    AGGR_FUNC=24
    BOOLEAN=25
    FLOAT=26
    LOGICAL_OP=27
    OPERATOR=28
    STRING=29
    INT=30
    COMMENT=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.StatContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.StatContext,i)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CSVFilterParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.stat()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 418570) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStat(self):
            return self.getTypedRuleContext(CSVFilterParser.LoadStatContext,0)


        def filterStat(self):
            return self.getTypedRuleContext(CSVFilterParser.FilterStatContext,0)


        def aggregateStat(self):
            return self.getTypedRuleContext(CSVFilterParser.AggregateStatContext,0)


        def sortStat(self):
            return self.getTypedRuleContext(CSVFilterParser.SortStatContext,0)


        def limitStat(self):
            return self.getTypedRuleContext(CSVFilterParser.LimitStatContext,0)


        def joinStat(self):
            return self.getTypedRuleContext(CSVFilterParser.JoinStatContext,0)


        def groupStat(self):
            return self.getTypedRuleContext(CSVFilterParser.GroupStatContext,0)


        def printStat(self):
            return self.getTypedRuleContext(CSVFilterParser.PrintStatContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = CSVFilterParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.loadStat()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.filterStat()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.aggregateStat()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.sortStat()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.limitStat()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 36
                self.joinStat()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 37
                self.groupStat()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 38
                self.printStat()
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


    class LoadStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_loadStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStat" ):
                listener.enterLoadStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStat" ):
                listener.exitLoadStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStat" ):
                return visitor.visitLoadStat(self)
            else:
                return visitor.visitChildren(self)




    def loadStat(self):

        localctx = CSVFilterParser.LoadStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(CSVFilterParser.T__0)
            self.state = 42
            self.match(CSVFilterParser.STRING)
            self.state = 43
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.STRING)
            else:
                return self.getToken(CSVFilterParser.STRING, i)

        def OPERATOR(self):
            return self.getToken(CSVFilterParser.OPERATOR, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.ValueContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.ValueContext,i)


        def LOGICAL_OP(self):
            return self.getToken(CSVFilterParser.LOGICAL_OP, 0)

        def filterStat(self):
            return self.getTypedRuleContext(CSVFilterParser.FilterStatContext,0)


        def K_BETWEEN(self):
            return self.getToken(CSVFilterParser.K_BETWEEN, 0)

        def K_AND(self):
            return self.getToken(CSVFilterParser.K_AND, 0)

        def K_IN(self):
            return self.getToken(CSVFilterParser.K_IN, 0)

        def valueList(self):
            return self.getTypedRuleContext(CSVFilterParser.ValueListContext,0)


        def K_LIKE(self):
            return self.getToken(CSVFilterParser.K_LIKE, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_filterStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStat" ):
                listener.enterFilterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStat" ):
                listener.exitFilterStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStat" ):
                return visitor.visitFilterStat(self)
            else:
                return visitor.visitChildren(self)




    def filterStat(self):

        localctx = CSVFilterParser.FilterStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStat)
        self._la = 0 # Token type
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(CSVFilterParser.T__2)
                self.state = 46
                self.match(CSVFilterParser.T__3)
                self.state = 47
                self.match(CSVFilterParser.STRING)
                self.state = 48
                self.match(CSVFilterParser.OPERATOR)
                self.state = 49
                self.value()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 50
                    self.match(CSVFilterParser.LOGICAL_OP)
                    self.state = 51
                    self.filterStat()


                self.state = 54
                self.match(CSVFilterParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(CSVFilterParser.T__2)
                self.state = 57
                self.match(CSVFilterParser.T__3)
                self.state = 58
                self.match(CSVFilterParser.STRING)
                self.state = 59
                self.match(CSVFilterParser.K_BETWEEN)
                self.state = 60
                self.value()
                self.state = 61
                self.match(CSVFilterParser.K_AND)
                self.state = 62
                self.value()
                self.state = 63
                self.match(CSVFilterParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(CSVFilterParser.T__2)
                self.state = 66
                self.match(CSVFilterParser.T__3)
                self.state = 67
                self.match(CSVFilterParser.STRING)
                self.state = 68
                self.match(CSVFilterParser.K_IN)
                self.state = 69
                self.match(CSVFilterParser.T__4)
                self.state = 70
                self.valueList()
                self.state = 71
                self.match(CSVFilterParser.T__5)
                self.state = 72
                self.match(CSVFilterParser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.match(CSVFilterParser.T__2)
                self.state = 75
                self.match(CSVFilterParser.T__3)
                self.state = 76
                self.match(CSVFilterParser.STRING)
                self.state = 77
                self.match(CSVFilterParser.K_LIKE)
                self.state = 78
                self.match(CSVFilterParser.STRING)
                self.state = 79
                self.match(CSVFilterParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.ValueContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.ValueContext,i)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_valueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueList" ):
                listener.enterValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueList" ):
                listener.exitValueList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueList" ):
                return visitor.visitValueList(self)
            else:
                return visitor.visitChildren(self)




    def valueList(self):

        localctx = CSVFilterParser.ValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valueList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.value()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 83
                self.match(CSVFilterParser.T__6)
                self.state = 84
                self.value()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGR_FUNC(self):
            return self.getToken(CSVFilterParser.AGGR_FUNC, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.STRING)
            else:
                return self.getToken(CSVFilterParser.STRING, i)

        def K_WHERE(self):
            return self.getToken(CSVFilterParser.K_WHERE, 0)

        def OPERATOR(self):
            return self.getToken(CSVFilterParser.OPERATOR, 0)

        def value(self):
            return self.getTypedRuleContext(CSVFilterParser.ValueContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_aggregateStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStat" ):
                listener.enterAggregateStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStat" ):
                listener.exitAggregateStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStat" ):
                return visitor.visitAggregateStat(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStat(self):

        localctx = CSVFilterParser.AggregateStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_aggregateStat)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(CSVFilterParser.T__7)
                self.state = 91
                self.match(CSVFilterParser.AGGR_FUNC)
                self.state = 92
                self.match(CSVFilterParser.T__3)
                self.state = 93
                self.match(CSVFilterParser.STRING)
                self.state = 94
                self.match(CSVFilterParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(CSVFilterParser.T__7)
                self.state = 96
                self.match(CSVFilterParser.AGGR_FUNC)
                self.state = 97
                self.match(CSVFilterParser.T__3)
                self.state = 98
                self.match(CSVFilterParser.STRING)
                self.state = 99
                self.match(CSVFilterParser.K_WHERE)
                self.state = 100
                self.match(CSVFilterParser.STRING)
                self.state = 101
                self.match(CSVFilterParser.OPERATOR)
                self.state = 102
                self.value()
                self.state = 103
                self.match(CSVFilterParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def sortOrder(self):
            return self.getTypedRuleContext(CSVFilterParser.SortOrderContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_sortStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortStat" ):
                listener.enterSortStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortStat" ):
                listener.exitSortStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortStat" ):
                return visitor.visitSortStat(self)
            else:
                return visitor.visitChildren(self)




    def sortStat(self):

        localctx = CSVFilterParser.SortStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sortStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(CSVFilterParser.T__8)
            self.state = 108
            self.match(CSVFilterParser.T__9)
            self.state = 109
            self.match(CSVFilterParser.STRING)
            self.state = 110
            self.sortOrder()
            self.state = 111
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortOrderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVFilterParser.RULE_sortOrder

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSortOrder" ):
                listener.enterSortOrder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSortOrder" ):
                listener.exitSortOrder(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortOrder" ):
                return visitor.visitSortOrder(self)
            else:
                return visitor.visitChildren(self)




    def sortOrder(self):

        localctx = CSVFilterParser.SortOrderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sortOrder)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
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


    class LimitStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSVFilterParser.INT, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_limitStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitStat" ):
                listener.enterLimitStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitStat" ):
                listener.exitLimitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitStat" ):
                return visitor.visitLimitStat(self)
            else:
                return visitor.visitChildren(self)




    def limitStat(self):

        localctx = CSVFilterParser.LimitStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_limitStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(CSVFilterParser.T__12)
            self.state = 116
            self.match(CSVFilterParser.INT)
            self.state = 117
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(CSVFilterParser.STRING)
            else:
                return self.getToken(CSVFilterParser.STRING, i)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_joinStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinStat" ):
                listener.enterJoinStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinStat" ):
                listener.exitJoinStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoinStat" ):
                return visitor.visitJoinStat(self)
            else:
                return visitor.visitChildren(self)




    def joinStat(self):

        localctx = CSVFilterParser.JoinStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_joinStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(CSVFilterParser.T__13)
            self.state = 120
            self.match(CSVFilterParser.STRING)
            self.state = 121
            self.match(CSVFilterParser.T__14)
            self.state = 122
            self.match(CSVFilterParser.STRING)
            self.state = 123
            self.match(CSVFilterParser.T__15)
            self.state = 124
            self.match(CSVFilterParser.STRING)
            self.state = 125
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_groupStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupStat" ):
                listener.enterGroupStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupStat" ):
                listener.exitGroupStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupStat" ):
                return visitor.visitGroupStat(self)
            else:
                return visitor.visitChildren(self)




    def groupStat(self):

        localctx = CSVFilterParser.GroupStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_groupStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(CSVFilterParser.T__16)
            self.state = 128
            self.match(CSVFilterParser.T__9)
            self.state = 129
            self.match(CSVFilterParser.STRING)
            self.state = 130
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVFilterParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)




    def printStat(self):

        localctx = CSVFilterParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(CSVFilterParser.T__17)
            self.state = 133
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def INT(self):
            return self.getToken(CSVFilterParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSVFilterParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(CSVFilterParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = CSVFilterParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1711276032) != 0)):
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





