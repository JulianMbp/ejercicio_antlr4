# Generated from CSVFilter.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\3\3\3\3\5\3\27\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7-\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7")
        buf.write("\7\65\n\7\f\7\16\78\13\7\3\7\2\3\f\b\2\4\6\b\n\f\2\2\2")
        buf.write("9\2\17\3\2\2\2\4\26\3\2\2\2\6\30\3\2\2\2\b\34\3\2\2\2")
        buf.write("\n \3\2\2\2\f,\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20")
        buf.write("\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23")
        buf.write("\27\5\6\4\2\24\27\5\b\5\2\25\27\5\n\6\2\26\23\3\2\2\2")
        buf.write("\26\24\3\2\2\2\26\25\3\2\2\2\27\5\3\2\2\2\30\31\7\3\2")
        buf.write("\2\31\32\7\r\2\2\32\33\7\4\2\2\33\7\3\2\2\2\34\35\7\5")
        buf.write("\2\2\35\36\5\f\7\2\36\37\7\4\2\2\37\t\3\2\2\2 !\7\6\2")
        buf.write("\2!\"\7\4\2\2\"\13\3\2\2\2#$\b\7\1\2$%\7\7\2\2%&\5\f\7")
        buf.write("\2&\'\7\b\2\2\'-\3\2\2\2()\7\t\2\2)*\7\r\2\2*+\7\f\2\2")
        buf.write("+-\7\16\2\2,#\3\2\2\2,(\3\2\2\2-\66\3\2\2\2./\f\6\2\2")
        buf.write("/\60\7\n\2\2\60\65\5\f\7\7\61\62\f\5\2\2\62\63\7\13\2")
        buf.write("\2\63\65\5\f\7\6\64.\3\2\2\2\64\61\3\2\2\2\658\3\2\2\2")
        buf.write("\66\64\3\2\2\2\66\67\3\2\2\2\67\r\3\2\2\28\66\3\2\2\2")
        buf.write("\7\21\26,\64\66")
        return buf.getvalue()


class CSVFilterParser ( Parser ):

    grammarFileName = "CSVFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'print'", 
                     "'('", "')'", "'column'", "'AND'", "'OR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "AND", "OR", "OPERATOR", "STRING", "INT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_printStat = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "printStat", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    AND=8
    OR=9
    OPERATOR=10
    STRING=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
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
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSVFilterParser.T__0) | (1 << CSVFilterParser.T__2) | (1 << CSVFilterParser.T__3))) != 0)):
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
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSVFilterParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.loadStat()
                pass
            elif token in [CSVFilterParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.filterStat()
                pass
            elif token in [CSVFilterParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
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
            self.state = 22
            self.match(CSVFilterParser.T__0)
            self.state = 23
            self.match(CSVFilterParser.STRING)
            self.state = 24
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

        def expr(self):
            return self.getTypedRuleContext(CSVFilterParser.ExprContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CSVFilterParser.T__2)
            self.state = 27
            self.expr(0)
            self.state = 28
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
        self.enterRule(localctx, 8, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(CSVFilterParser.T__3)
            self.state = 31
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.ExprContext,i)


        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def OPERATOR(self):
            return self.getToken(CSVFilterParser.OPERATOR, 0)

        def INT(self):
            return self.getToken(CSVFilterParser.INT, 0)

        def AND(self):
            return self.getToken(CSVFilterParser.AND, 0)

        def OR(self):
            return self.getToken(CSVFilterParser.OR, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSVFilterParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSVFilterParser.T__4]:
                self.state = 34
                self.match(CSVFilterParser.T__4)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(CSVFilterParser.T__5)
                pass
            elif token in [CSVFilterParser.T__6]:
                self.state = 38
                self.match(CSVFilterParser.T__6)
                self.state = 39
                self.match(CSVFilterParser.STRING)
                self.state = 40
                self.match(CSVFilterParser.OPERATOR)
                self.state = 41
                self.match(CSVFilterParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CSVFilterParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 45
                        self.match(CSVFilterParser.AND)
                        self.state = 46
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = CSVFilterParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 48
                        self.match(CSVFilterParser.OR)
                        self.state = 49
                        self.expr(4)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




