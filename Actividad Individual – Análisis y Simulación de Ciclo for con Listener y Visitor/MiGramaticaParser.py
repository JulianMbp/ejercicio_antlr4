# Generated from MiGramatica.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3%\n\3\3\3\3")
        buf.write("\3\7\3)\n\3\f\3\16\3,\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tV\n\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\7\t^\n\t\f\t\16\ta\13\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\2\4\4\20\f\2\4\6\b\n\f\16\20\22\24\2\6\3\2\n\13\3\2\f")
        buf.write("\r\3\2\16\23\4\2\t\t\24\27\2d\2\27\3\2\2\2\4$\3\2\2\2")
        buf.write("\6-\3\2\2\2\b>\3\2\2\2\nB\3\2\2\2\fF\3\2\2\2\16J\3\2\2")
        buf.write("\2\20U\3\2\2\2\22b\3\2\2\2\24d\3\2\2\2\26\30\5\4\3\2\27")
        buf.write("\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2")
        buf.write("\32\33\3\2\2\2\33\34\7\2\2\3\34\3\3\2\2\2\35\36\b\3\1")
        buf.write("\2\36\37\5\6\4\2\37 \7\3\2\2 %\3\2\2\2!\"\5\16\b\2\"#")
        buf.write("\7\3\2\2#%\3\2\2\2$\35\3\2\2\2$!\3\2\2\2%*\3\2\2\2&\'")
        buf.write("\f\3\2\2\')\5\4\3\4(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3")
        buf.write("\2\2\2+\5\3\2\2\2,*\3\2\2\2-.\7\4\2\2./\7\5\2\2/\60\5")
        buf.write("\b\5\2\60\61\7\3\2\2\61\62\5\n\6\2\62\63\7\3\2\2\63\64")
        buf.write("\5\f\7\2\64\65\7\6\2\2\659\7\7\2\2\668\5\4\3\2\67\66\3")
        buf.write("\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3\2")
        buf.write("\2\2<=\7\b\2\2=\7\3\2\2\2>?\7\30\2\2?@\7\t\2\2@A\5\20")
        buf.write("\t\2A\t\3\2\2\2BC\7\30\2\2CD\5\22\n\2DE\5\20\t\2E\13\3")
        buf.write("\2\2\2FG\7\30\2\2GH\5\24\13\2HI\5\20\t\2I\r\3\2\2\2JK")
        buf.write("\7\30\2\2KL\7\t\2\2LM\5\20\t\2M\17\3\2\2\2NO\b\t\1\2O")
        buf.write("V\7\31\2\2PV\7\30\2\2QR\7\5\2\2RS\5\20\t\2ST\7\6\2\2T")
        buf.write("V\3\2\2\2UN\3\2\2\2UP\3\2\2\2UQ\3\2\2\2V_\3\2\2\2WX\f")
        buf.write("\7\2\2XY\t\2\2\2Y^\5\20\t\bZ[\f\6\2\2[\\\t\3\2\2\\^\5")
        buf.write("\20\t\7]W\3\2\2\2]Z\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2")
        buf.write("\2\2`\21\3\2\2\2a_\3\2\2\2bc\t\4\2\2c\23\3\2\2\2de\t\5")
        buf.write("\2\2e\25\3\2\2\2\t\31$*9U]_")
        return buf.getvalue()


class MiGramaticaParser ( Parser ):

    grammarFileName = "MiGramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'for'", "'('", "')'", "'{'", "'}'", 
                     "'='", "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", "'=='", 
                     "'!='", "'<='", "'>='", "'+='", "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_forLoop = 2
    RULE_inicializacion = 3
    RULE_condicion = 4
    RULE_actualizacion = 5
    RULE_asignacion = 6
    RULE_expresion = 7
    RULE_operadorComparacion = 8
    RULE_operadorAsignacion = 9

    ruleNames =  [ "programa", "sentencia", "forLoop", "inicializacion", 
                   "condicion", "actualizacion", "asignacion", "expresion", 
                   "operadorComparacion", "operadorAsignacion" ]

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
    T__18=19
    T__19=20
    T__20=21
    ID=22
    INT=23
    WS=24
    COMENTARIO=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiGramaticaParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MiGramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.sentencia(0)
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiGramaticaParser.T__1 or _la==MiGramaticaParser.ID):
                    break

            self.state = 25
            self.match(MiGramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoop(self):
            return self.getTypedRuleContext(MiGramaticaParser.ForLoopContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.AsignacionContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)



    def sentencia(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiGramaticaParser.SentenciaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_sentencia, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiGramaticaParser.T__1]:
                self.state = 28
                self.forLoop()
                self.state = 29
                self.match(MiGramaticaParser.T__0)
                pass
            elif token in [MiGramaticaParser.ID]:
                self.state = 31
                self.asignacion()
                self.state = 32
                self.match(MiGramaticaParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiGramaticaParser.SentenciaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_sentencia)
                    self.state = 36
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 37
                    self.sentencia(2) 
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inicializacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.InicializacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(MiGramaticaParser.CondicionContext,0)


        def actualizacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ActualizacionContext,0)


        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = MiGramaticaParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MiGramaticaParser.T__1)
            self.state = 44
            self.match(MiGramaticaParser.T__2)
            self.state = 45
            self.inicializacion()
            self.state = 46
            self.match(MiGramaticaParser.T__0)
            self.state = 47
            self.condicion()
            self.state = 48
            self.match(MiGramaticaParser.T__0)
            self.state = 49
            self.actualizacion()
            self.state = 50
            self.match(MiGramaticaParser.T__3)
            self.state = 51
            self.match(MiGramaticaParser.T__4)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiGramaticaParser.T__1 or _la==MiGramaticaParser.ID:
                self.state = 52
                self.sentencia(0)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(MiGramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacion" ):
                listener.enterInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacion" ):
                listener.exitInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = MiGramaticaParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inicializacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(MiGramaticaParser.ID)
            self.state = 61
            self.match(MiGramaticaParser.T__6)
            self.state = 62
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def operadorComparacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.OperadorComparacionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = MiGramaticaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MiGramaticaParser.ID)
            self.state = 65
            self.operadorComparacion()
            self.state = 66
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def operadorAsignacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.OperadorAsignacionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_actualizacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActualizacion" ):
                listener.enterActualizacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActualizacion" ):
                listener.exitActualizacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActualizacion" ):
                return visitor.visitActualizacion(self)
            else:
                return visitor.visitChildren(self)




    def actualizacion(self):

        localctx = MiGramaticaParser.ActualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actualizacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(MiGramaticaParser.ID)
            self.state = 69
            self.operadorAsignacion()
            self.state = 70
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = MiGramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MiGramaticaParser.ID)
            self.state = 73
            self.match(MiGramaticaParser.T__6)
            self.state = 74
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiGramaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiGramaticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiGramaticaParser.INT]:
                localctx = MiGramaticaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 77
                self.match(MiGramaticaParser.INT)
                pass
            elif token in [MiGramaticaParser.ID]:
                localctx = MiGramaticaParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(MiGramaticaParser.ID)
                pass
            elif token in [MiGramaticaParser.T__2]:
                localctx = MiGramaticaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.match(MiGramaticaParser.T__2)
                self.state = 80
                self.expresion(0)
                self.state = 81
                self.match(MiGramaticaParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MiGramaticaParser.MulDivContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 85
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 86
                        _la = self._input.LA(1)
                        if not(_la==MiGramaticaParser.T__7 or _la==MiGramaticaParser.T__8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = MiGramaticaParser.AddSubContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 88
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 89
                        _la = self._input.LA(1)
                        if not(_la==MiGramaticaParser.T__9 or _la==MiGramaticaParser.T__10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 90
                        self.expresion(5)
                        pass

             
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperadorComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_operadorComparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorComparacion" ):
                listener.enterOperadorComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorComparacion" ):
                listener.exitOperadorComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorComparacion" ):
                return visitor.visitOperadorComparacion(self)
            else:
                return visitor.visitChildren(self)




    def operadorComparacion(self):

        localctx = MiGramaticaParser.OperadorComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operadorComparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiGramaticaParser.T__11) | (1 << MiGramaticaParser.T__12) | (1 << MiGramaticaParser.T__13) | (1 << MiGramaticaParser.T__14) | (1 << MiGramaticaParser.T__15) | (1 << MiGramaticaParser.T__16))) != 0)):
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


    class OperadorAsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_operadorAsignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperadorAsignacion" ):
                listener.enterOperadorAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperadorAsignacion" ):
                listener.exitOperadorAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperadorAsignacion" ):
                return visitor.visitOperadorAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def operadorAsignacion(self):

        localctx = MiGramaticaParser.OperadorAsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operadorAsignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiGramaticaParser.T__6) | (1 << MiGramaticaParser.T__17) | (1 << MiGramaticaParser.T__18) | (1 << MiGramaticaParser.T__19) | (1 << MiGramaticaParser.T__20))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.sentencia_sempred
        self._predicates[7] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def sentencia_sempred(self, localctx:SentenciaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




