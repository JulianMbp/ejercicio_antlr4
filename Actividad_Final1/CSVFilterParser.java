// Generated from CSVFilter.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CSVFilterParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, K_BETWEEN=19, K_AND=20, K_IN=21, K_LIKE=22, K_WHERE=23, AGGR_FUNC=24, 
		BOOLEAN=25, FLOAT=26, LOGICAL_OP=27, OPERATOR=28, STRING=29, INT=30, COMMENT=31, 
		WS=32;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_loadStat = 2, RULE_filterStat = 3, 
		RULE_valueList = 4, RULE_aggregateStat = 5, RULE_sortStat = 6, RULE_sortOrder = 7, 
		RULE_limitStat = 8, RULE_joinStat = 9, RULE_groupStat = 10, RULE_printStat = 11, 
		RULE_value = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "loadStat", "filterStat", "valueList", "aggregateStat", 
			"sortStat", "sortOrder", "limitStat", "joinStat", "groupStat", "printStat", 
			"value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'load'", "';'", "'filter'", "'column'", "'('", "')'", "','", "'aggregate'", 
			"'sort'", "'by'", "'asc'", "'desc'", "'limit'", "'join'", "'on'", "'='", 
			"'group'", "'print'", "'between'", "'and'", "'in'", "'like'", "'where'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "K_BETWEEN", "K_AND", "K_IN", 
			"K_LIKE", "K_WHERE", "AGGR_FUNC", "BOOLEAN", "FLOAT", "LOGICAL_OP", "OPERATOR", 
			"STRING", "INT", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CSVFilter.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CSVFilterParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(26);
				stat();
				}
				}
				setState(29); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 418570L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public LoadStatContext loadStat() {
			return getRuleContext(LoadStatContext.class,0);
		}
		public FilterStatContext filterStat() {
			return getRuleContext(FilterStatContext.class,0);
		}
		public AggregateStatContext aggregateStat() {
			return getRuleContext(AggregateStatContext.class,0);
		}
		public SortStatContext sortStat() {
			return getRuleContext(SortStatContext.class,0);
		}
		public LimitStatContext limitStat() {
			return getRuleContext(LimitStatContext.class,0);
		}
		public JoinStatContext joinStat() {
			return getRuleContext(JoinStatContext.class,0);
		}
		public GroupStatContext groupStat() {
			return getRuleContext(GroupStatContext.class,0);
		}
		public PrintStatContext printStat() {
			return getRuleContext(PrintStatContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitStat(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(39);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				loadStat();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(32);
				filterStat();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(33);
				aggregateStat();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 4);
				{
				setState(34);
				sortStat();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 5);
				{
				setState(35);
				limitStat();
				}
				break;
			case T__13:
				enterOuterAlt(_localctx, 6);
				{
				setState(36);
				joinStat();
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 7);
				{
				setState(37);
				groupStat();
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 8);
				{
				setState(38);
				printStat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoadStatContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(CSVFilterParser.STRING, 0); }
		public LoadStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loadStat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterLoadStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitLoadStat(this);
		}
	}

	public final LoadStatContext loadStat() throws RecognitionException {
		LoadStatContext _localctx = new LoadStatContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_loadStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(T__0);
			setState(42);
			match(STRING);
			setState(43);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FilterStatContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(CSVFilterParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(CSVFilterParser.STRING, i);
		}
		public TerminalNode OPERATOR() { return getToken(CSVFilterParser.OPERATOR, 0); }
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public TerminalNode LOGICAL_OP() { return getToken(CSVFilterParser.LOGICAL_OP, 0); }
		public FilterStatContext filterStat() {
			return getRuleContext(FilterStatContext.class,0);
		}
		public TerminalNode K_BETWEEN() { return getToken(CSVFilterParser.K_BETWEEN, 0); }
		public TerminalNode K_AND() { return getToken(CSVFilterParser.K_AND, 0); }
		public TerminalNode K_IN() { return getToken(CSVFilterParser.K_IN, 0); }
		public ValueListContext valueList() {
			return getRuleContext(ValueListContext.class,0);
		}
		public TerminalNode K_LIKE() { return getToken(CSVFilterParser.K_LIKE, 0); }
		public FilterStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterStat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterFilterStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitFilterStat(this);
		}
	}

	public final FilterStatContext filterStat() throws RecognitionException {
		FilterStatContext _localctx = new FilterStatContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_filterStat);
		int _la;
		try {
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				match(T__2);
				setState(46);
				match(T__3);
				setState(47);
				match(STRING);
				setState(48);
				match(OPERATOR);
				setState(49);
				value();
				setState(52);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==LOGICAL_OP) {
					{
					setState(50);
					match(LOGICAL_OP);
					setState(51);
					filterStat();
					}
				}

				setState(54);
				match(T__1);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				match(T__2);
				setState(57);
				match(T__3);
				setState(58);
				match(STRING);
				setState(59);
				match(K_BETWEEN);
				setState(60);
				value();
				setState(61);
				match(K_AND);
				setState(62);
				value();
				setState(63);
				match(T__1);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(65);
				match(T__2);
				setState(66);
				match(T__3);
				setState(67);
				match(STRING);
				setState(68);
				match(K_IN);
				setState(69);
				match(T__4);
				setState(70);
				valueList();
				setState(71);
				match(T__5);
				setState(72);
				match(T__1);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(74);
				match(T__2);
				setState(75);
				match(T__3);
				setState(76);
				match(STRING);
				setState(77);
				match(K_LIKE);
				setState(78);
				match(STRING);
				setState(79);
				match(T__1);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueListContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public ValueListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valueList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterValueList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitValueList(this);
		}
	}

	public final ValueListContext valueList() throws RecognitionException {
		ValueListContext _localctx = new ValueListContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_valueList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			value();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(83);
				match(T__6);
				setState(84);
				value();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AggregateStatContext extends ParserRuleContext {
		public TerminalNode AGGR_FUNC() { return getToken(CSVFilterParser.AGGR_FUNC, 0); }
		public List<TerminalNode> STRING() { return getTokens(CSVFilterParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(CSVFilterParser.STRING, i);
		}
		public TerminalNode K_WHERE() { return getToken(CSVFilterParser.K_WHERE, 0); }
		public TerminalNode OPERATOR() { return getToken(CSVFilterParser.OPERATOR, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public AggregateStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aggregateStat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterAggregateStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitAggregateStat(this);
		}
	}

	public final AggregateStatContext aggregateStat() throws RecognitionException {
		AggregateStatContext _localctx = new AggregateStatContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_aggregateStat);
		try {
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				match(T__7);
				setState(91);
				match(AGGR_FUNC);
				setState(92);
				match(T__3);
				setState(93);
				match(STRING);
				setState(94);
				match(T__1);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				match(T__7);
				setState(96);
				match(AGGR_FUNC);
				setState(97);
				match(T__3);
				setState(98);
				match(STRING);
				setState(99);
				match(K_WHERE);
				setState(100);
				match(STRING);
				setState(101);
				match(OPERATOR);
				setState(102);
				value();
				setState(103);
				match(T__1);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SortStatContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(CSVFilterParser.STRING, 0); }
		public SortOrderContext sortOrder() {
			return getRuleContext(SortOrderContext.class,0);
		}
		public SortStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sortStat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterSortStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitSortStat(this);
		}
	}

	public final SortStatContext sortStat() throws RecognitionException {
		SortStatContext _localctx = new SortStatContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_sortStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(T__8);
			setState(108);
			match(T__9);
			setState(109);
			match(STRING);
			setState(110);
			sortOrder();
			setState(111);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SortOrderContext extends ParserRuleContext {
		public SortOrderContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sortOrder; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterSortOrder(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitSortOrder(this);
		}
	}

	public final SortOrderContext sortOrder() throws RecognitionException {
		SortOrderContext _localctx = new SortOrderContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_sortOrder);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			_la = _input.LA(1);
			if ( !(_la==T__10 || _la==T__11) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LimitStatContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(CSVFilterParser.INT, 0); }
		public LimitStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_limitStat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterLimitStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitLimitStat(this);
		}
	}

	public final LimitStatContext limitStat() throws RecognitionException {
		LimitStatContext _localctx = new LimitStatContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_limitStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(T__12);
			setState(116);
			match(INT);
			setState(117);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JoinStatContext extends ParserRuleContext {
		public List<TerminalNode> STRING() { return getTokens(CSVFilterParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(CSVFilterParser.STRING, i);
		}
		public JoinStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinStat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterJoinStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitJoinStat(this);
		}
	}

	public final JoinStatContext joinStat() throws RecognitionException {
		JoinStatContext _localctx = new JoinStatContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_joinStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(T__13);
			setState(120);
			match(STRING);
			setState(121);
			match(T__14);
			setState(122);
			match(STRING);
			setState(123);
			match(T__15);
			setState(124);
			match(STRING);
			setState(125);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GroupStatContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(CSVFilterParser.STRING, 0); }
		public GroupStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_groupStat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterGroupStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitGroupStat(this);
		}
	}

	public final GroupStatContext groupStat() throws RecognitionException {
		GroupStatContext _localctx = new GroupStatContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_groupStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(T__16);
			setState(128);
			match(T__9);
			setState(129);
			match(STRING);
			setState(130);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStatContext extends ParserRuleContext {
		public PrintStatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterPrintStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitPrintStat(this);
		}
	}

	public final PrintStatContext printStat() throws RecognitionException {
		PrintStatContext _localctx = new PrintStatContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_printStat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(T__17);
			setState(133);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(CSVFilterParser.STRING, 0); }
		public TerminalNode INT() { return getToken(CSVFilterParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(CSVFilterParser.FLOAT, 0); }
		public TerminalNode BOOLEAN() { return getToken(CSVFilterParser.BOOLEAN, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CSVFilterListener ) ((CSVFilterListener)listener).exitValue(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1711276032L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001 \u008a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0004\u0000\u001c\b\u0000\u000b\u0000\f\u0000\u001d"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001(\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u00035\b\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u0003Q\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0005\u0004V\b\u0004\n\u0004\f\u0004Y\t\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0003\u0005j\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0000\u0000\r\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0002\u0001\u0000\u000b"+
		"\f\u0002\u0000\u0019\u001a\u001d\u001e\u008a\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0002\'\u0001\u0000\u0000\u0000\u0004)\u0001\u0000\u0000\u0000"+
		"\u0006P\u0001\u0000\u0000\u0000\bR\u0001\u0000\u0000\u0000\ni\u0001\u0000"+
		"\u0000\u0000\fk\u0001\u0000\u0000\u0000\u000eq\u0001\u0000\u0000\u0000"+
		"\u0010s\u0001\u0000\u0000\u0000\u0012w\u0001\u0000\u0000\u0000\u0014\u007f"+
		"\u0001\u0000\u0000\u0000\u0016\u0084\u0001\u0000\u0000\u0000\u0018\u0087"+
		"\u0001\u0000\u0000\u0000\u001a\u001c\u0003\u0002\u0001\u0000\u001b\u001a"+
		"\u0001\u0000\u0000\u0000\u001c\u001d\u0001\u0000\u0000\u0000\u001d\u001b"+
		"\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000\u0000\u001e\u0001"+
		"\u0001\u0000\u0000\u0000\u001f(\u0003\u0004\u0002\u0000 (\u0003\u0006"+
		"\u0003\u0000!(\u0003\n\u0005\u0000\"(\u0003\f\u0006\u0000#(\u0003\u0010"+
		"\b\u0000$(\u0003\u0012\t\u0000%(\u0003\u0014\n\u0000&(\u0003\u0016\u000b"+
		"\u0000\'\u001f\u0001\u0000\u0000\u0000\' \u0001\u0000\u0000\u0000\'!\u0001"+
		"\u0000\u0000\u0000\'\"\u0001\u0000\u0000\u0000\'#\u0001\u0000\u0000\u0000"+
		"\'$\u0001\u0000\u0000\u0000\'%\u0001\u0000\u0000\u0000\'&\u0001\u0000"+
		"\u0000\u0000(\u0003\u0001\u0000\u0000\u0000)*\u0005\u0001\u0000\u0000"+
		"*+\u0005\u001d\u0000\u0000+,\u0005\u0002\u0000\u0000,\u0005\u0001\u0000"+
		"\u0000\u0000-.\u0005\u0003\u0000\u0000./\u0005\u0004\u0000\u0000/0\u0005"+
		"\u001d\u0000\u000001\u0005\u001c\u0000\u000014\u0003\u0018\f\u000023\u0005"+
		"\u001b\u0000\u000035\u0003\u0006\u0003\u000042\u0001\u0000\u0000\u0000"+
		"45\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u000067\u0005\u0002\u0000"+
		"\u00007Q\u0001\u0000\u0000\u000089\u0005\u0003\u0000\u00009:\u0005\u0004"+
		"\u0000\u0000:;\u0005\u001d\u0000\u0000;<\u0005\u0013\u0000\u0000<=\u0003"+
		"\u0018\f\u0000=>\u0005\u0014\u0000\u0000>?\u0003\u0018\f\u0000?@\u0005"+
		"\u0002\u0000\u0000@Q\u0001\u0000\u0000\u0000AB\u0005\u0003\u0000\u0000"+
		"BC\u0005\u0004\u0000\u0000CD\u0005\u001d\u0000\u0000DE\u0005\u0015\u0000"+
		"\u0000EF\u0005\u0005\u0000\u0000FG\u0003\b\u0004\u0000GH\u0005\u0006\u0000"+
		"\u0000HI\u0005\u0002\u0000\u0000IQ\u0001\u0000\u0000\u0000JK\u0005\u0003"+
		"\u0000\u0000KL\u0005\u0004\u0000\u0000LM\u0005\u001d\u0000\u0000MN\u0005"+
		"\u0016\u0000\u0000NO\u0005\u001d\u0000\u0000OQ\u0005\u0002\u0000\u0000"+
		"P-\u0001\u0000\u0000\u0000P8\u0001\u0000\u0000\u0000PA\u0001\u0000\u0000"+
		"\u0000PJ\u0001\u0000\u0000\u0000Q\u0007\u0001\u0000\u0000\u0000RW\u0003"+
		"\u0018\f\u0000ST\u0005\u0007\u0000\u0000TV\u0003\u0018\f\u0000US\u0001"+
		"\u0000\u0000\u0000VY\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000"+
		"WX\u0001\u0000\u0000\u0000X\t\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000"+
		"\u0000Z[\u0005\b\u0000\u0000[\\\u0005\u0018\u0000\u0000\\]\u0005\u0004"+
		"\u0000\u0000]^\u0005\u001d\u0000\u0000^j\u0005\u0002\u0000\u0000_`\u0005"+
		"\b\u0000\u0000`a\u0005\u0018\u0000\u0000ab\u0005\u0004\u0000\u0000bc\u0005"+
		"\u001d\u0000\u0000cd\u0005\u0017\u0000\u0000de\u0005\u001d\u0000\u0000"+
		"ef\u0005\u001c\u0000\u0000fg\u0003\u0018\f\u0000gh\u0005\u0002\u0000\u0000"+
		"hj\u0001\u0000\u0000\u0000iZ\u0001\u0000\u0000\u0000i_\u0001\u0000\u0000"+
		"\u0000j\u000b\u0001\u0000\u0000\u0000kl\u0005\t\u0000\u0000lm\u0005\n"+
		"\u0000\u0000mn\u0005\u001d\u0000\u0000no\u0003\u000e\u0007\u0000op\u0005"+
		"\u0002\u0000\u0000p\r\u0001\u0000\u0000\u0000qr\u0007\u0000\u0000\u0000"+
		"r\u000f\u0001\u0000\u0000\u0000st\u0005\r\u0000\u0000tu\u0005\u001e\u0000"+
		"\u0000uv\u0005\u0002\u0000\u0000v\u0011\u0001\u0000\u0000\u0000wx\u0005"+
		"\u000e\u0000\u0000xy\u0005\u001d\u0000\u0000yz\u0005\u000f\u0000\u0000"+
		"z{\u0005\u001d\u0000\u0000{|\u0005\u0010\u0000\u0000|}\u0005\u001d\u0000"+
		"\u0000}~\u0005\u0002\u0000\u0000~\u0013\u0001\u0000\u0000\u0000\u007f"+
		"\u0080\u0005\u0011\u0000\u0000\u0080\u0081\u0005\n\u0000\u0000\u0081\u0082"+
		"\u0005\u001d\u0000\u0000\u0082\u0083\u0005\u0002\u0000\u0000\u0083\u0015"+
		"\u0001\u0000\u0000\u0000\u0084\u0085\u0005\u0012\u0000\u0000\u0085\u0086"+
		"\u0005\u0002\u0000\u0000\u0086\u0017\u0001\u0000\u0000\u0000\u0087\u0088"+
		"\u0007\u0001\u0000\u0000\u0088\u0019\u0001\u0000\u0000\u0000\u0006\u001d"+
		"\'4PWi";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}