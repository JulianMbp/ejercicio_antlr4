# Generated from CSVFilter.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
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


    # Enter a parse tree produced by CSVFilterParser#printStat.
    def enterPrintStat(self, ctx:CSVFilterParser.PrintStatContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#printStat.
    def exitPrintStat(self, ctx:CSVFilterParser.PrintStatContext):
        pass


    # Enter a parse tree produced by CSVFilterParser#expr.
    def enterExpr(self, ctx:CSVFilterParser.ExprContext):
        pass

    # Exit a parse tree produced by CSVFilterParser#expr.
    def exitExpr(self, ctx:CSVFilterParser.ExprContext):
        pass



del CSVFilterParser