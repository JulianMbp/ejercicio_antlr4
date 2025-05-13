// Generated from CSVFilter.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CSVFilterParser}.
 */
public interface CSVFilterListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(CSVFilterParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(CSVFilterParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(CSVFilterParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(CSVFilterParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#loadStat}.
	 * @param ctx the parse tree
	 */
	void enterLoadStat(CSVFilterParser.LoadStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#loadStat}.
	 * @param ctx the parse tree
	 */
	void exitLoadStat(CSVFilterParser.LoadStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#filterStat}.
	 * @param ctx the parse tree
	 */
	void enterFilterStat(CSVFilterParser.FilterStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#filterStat}.
	 * @param ctx the parse tree
	 */
	void exitFilterStat(CSVFilterParser.FilterStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#valueList}.
	 * @param ctx the parse tree
	 */
	void enterValueList(CSVFilterParser.ValueListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#valueList}.
	 * @param ctx the parse tree
	 */
	void exitValueList(CSVFilterParser.ValueListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#aggregateStat}.
	 * @param ctx the parse tree
	 */
	void enterAggregateStat(CSVFilterParser.AggregateStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#aggregateStat}.
	 * @param ctx the parse tree
	 */
	void exitAggregateStat(CSVFilterParser.AggregateStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#sortStat}.
	 * @param ctx the parse tree
	 */
	void enterSortStat(CSVFilterParser.SortStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#sortStat}.
	 * @param ctx the parse tree
	 */
	void exitSortStat(CSVFilterParser.SortStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#sortOrder}.
	 * @param ctx the parse tree
	 */
	void enterSortOrder(CSVFilterParser.SortOrderContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#sortOrder}.
	 * @param ctx the parse tree
	 */
	void exitSortOrder(CSVFilterParser.SortOrderContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#limitStat}.
	 * @param ctx the parse tree
	 */
	void enterLimitStat(CSVFilterParser.LimitStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#limitStat}.
	 * @param ctx the parse tree
	 */
	void exitLimitStat(CSVFilterParser.LimitStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#joinStat}.
	 * @param ctx the parse tree
	 */
	void enterJoinStat(CSVFilterParser.JoinStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#joinStat}.
	 * @param ctx the parse tree
	 */
	void exitJoinStat(CSVFilterParser.JoinStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#groupStat}.
	 * @param ctx the parse tree
	 */
	void enterGroupStat(CSVFilterParser.GroupStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#groupStat}.
	 * @param ctx the parse tree
	 */
	void exitGroupStat(CSVFilterParser.GroupStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#printStat}.
	 * @param ctx the parse tree
	 */
	void enterPrintStat(CSVFilterParser.PrintStatContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#printStat}.
	 * @param ctx the parse tree
	 */
	void exitPrintStat(CSVFilterParser.PrintStatContext ctx);
	/**
	 * Enter a parse tree produced by {@link CSVFilterParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(CSVFilterParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link CSVFilterParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(CSVFilterParser.ValueContext ctx);
}