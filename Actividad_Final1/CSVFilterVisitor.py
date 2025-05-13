# Generated from CSVFilter.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSVFilterParser import CSVFilterParser
else:
    from CSVFilterParser import CSVFilterParser

# This class defines a complete generic visitor for a parse tree produced by CSVFilterParser.

class CSVFilterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSVFilterParser#prog.
    def visitProg(self, ctx:CSVFilterParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#stat.
    def visitStat(self, ctx:CSVFilterParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#loadStat.
    def visitLoadStat(self, ctx:CSVFilterParser.LoadStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#filterStat.
    def visitFilterStat(self, ctx:CSVFilterParser.FilterStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#valueList.
    def visitValueList(self, ctx:CSVFilterParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#aggregateStat.
    def visitAggregateStat(self, ctx:CSVFilterParser.AggregateStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#sortStat.
    def visitSortStat(self, ctx:CSVFilterParser.SortStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#sortOrder.
    def visitSortOrder(self, ctx:CSVFilterParser.SortOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#limitStat.
    def visitLimitStat(self, ctx:CSVFilterParser.LimitStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#joinStat.
    def visitJoinStat(self, ctx:CSVFilterParser.JoinStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#groupStat.
    def visitGroupStat(self, ctx:CSVFilterParser.GroupStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#printStat.
    def visitPrintStat(self, ctx:CSVFilterParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSVFilterParser#value.
    def visitValue(self, ctx:CSVFilterParser.ValueContext):
        return self.visitChildren(ctx)



del CSVFilterParser