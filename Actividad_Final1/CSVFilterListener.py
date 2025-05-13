# Generated from CSVFilter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSVFilterParser import CSVFilterParser
else:
    from CSVFilterParser import CSVFilterParser

# This class defines a complete listener for a parse tree produced by CSVFilterParser.
class CSVFilterListener(ParseTreeListener):

    # Enter a parse tree produced by CSVFilterParser#prog.
    def enterProg(self, ctx:CSVFilterParser.ProgContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#prog.
    def exitProg(self, ctx:CSVFilterParser.ProgContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#stat.
    def enterStat(self, ctx:CSVFilterParser.StatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#stat.
    def exitStat(self, ctx:CSVFilterParser.StatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#loadStat.
    def enterLoadStat(self, ctx:CSVFilterParser.LoadStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#loadStat.
    def exitLoadStat(self, ctx:CSVFilterParser.LoadStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#filterStat.
    def enterFilterStat(self, ctx:CSVFilterParser.FilterStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#filterStat.
    def exitFilterStat(self, ctx:CSVFilterParser.FilterStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#valueList.
    def enterValueList(self, ctx:CSVFilterParser.ValueListContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#valueList.
    def exitValueList(self, ctx:CSVFilterParser.ValueListContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#aggregateStat.
    def enterAggregateStat(self, ctx:CSVFilterParser.AggregateStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#aggregateStat.
    def exitAggregateStat(self, ctx:CSVFilterParser.AggregateStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#filterCondition.
    def enterFilterCondition(self, ctx:CSVFilterParser.FilterConditionContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#filterCondition.
    def exitFilterCondition(self, ctx:CSVFilterParser.FilterConditionContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#sortStat.
    def enterSortStat(self, ctx:CSVFilterParser.SortStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#sortStat.
    def exitSortStat(self, ctx:CSVFilterParser.SortStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#sortOrder.
    def enterSortOrder(self, ctx:CSVFilterParser.SortOrderContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#sortOrder.
    def exitSortOrder(self, ctx:CSVFilterParser.SortOrderContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#limitStat.
    def enterLimitStat(self, ctx:CSVFilterParser.LimitStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#limitStat.
    def exitLimitStat(self, ctx:CSVFilterParser.LimitStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#joinStat.
    def enterJoinStat(self, ctx:CSVFilterParser.JoinStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#joinStat.
    def exitJoinStat(self, ctx:CSVFilterParser.JoinStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#groupStat.
    def enterGroupStat(self, ctx:CSVFilterParser.GroupStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#groupStat.
    def exitGroupStat(self, ctx:CSVFilterParser.GroupStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#printStat.
    def enterPrintStat(self, ctx:CSVFilterParser.PrintStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#printStat.
    def exitPrintStat(self, ctx:CSVFilterParser.PrintStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#aggregateType.
    def enterAggregateType(self, ctx:CSVFilterParser.AggregateTypeContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#aggregateType.
    def exitAggregateType(self, ctx:CSVFilterParser.AggregateTypeContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#value.
    def enterValue(self, ctx:CSVFilterParser.ValueContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#value.
    def exitValue(self, ctx:CSVFilterParser.ValueContext):
        pass



del CSVFilterParser