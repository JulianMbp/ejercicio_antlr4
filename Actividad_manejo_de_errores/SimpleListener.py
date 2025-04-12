# Generated from Simple.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleParser import SimpleParser
else:
    from SimpleParser import SimpleParser

# This class defines a complete listener for a parse tree produced by SimpleParser.
class SimpleListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleParser#prog.
    def enterProg(self, ctx:SimpleParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleParser#prog.
    def exitProg(self, ctx:SimpleParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleParser#classDef.
    def enterClassDef(self, ctx:SimpleParser.ClassDefContext):
        pass

    # Exit a parse tree produced by SimpleParser#classDef.
    def exitClassDef(self, ctx:SimpleParser.ClassDefContext):
        pass


    # Enter a parse tree produced by SimpleParser#member.
    def enterMember(self, ctx:SimpleParser.MemberContext):
        pass

    # Exit a parse tree produced by SimpleParser#member.
    def exitMember(self, ctx:SimpleParser.MemberContext):
        pass


    # Enter a parse tree produced by SimpleParser#stat.
    def enterStat(self, ctx:SimpleParser.StatContext):
        pass

    # Exit a parse tree produced by SimpleParser#stat.
    def exitStat(self, ctx:SimpleParser.StatContext):
        pass


    # Enter a parse tree produced by SimpleParser#FuncCall.
    def enterFuncCall(self, ctx:SimpleParser.FuncCallContext):
        pass

    # Exit a parse tree produced by SimpleParser#FuncCall.
    def exitFuncCall(self, ctx:SimpleParser.FuncCallContext):
        pass


    # Enter a parse tree produced by SimpleParser#Variable.
    def enterVariable(self, ctx:SimpleParser.VariableContext):
        pass

    # Exit a parse tree produced by SimpleParser#Variable.
    def exitVariable(self, ctx:SimpleParser.VariableContext):
        pass


    # Enter a parse tree produced by SimpleParser#MulDiv.
    def enterMulDiv(self, ctx:SimpleParser.MulDivContext):
        pass

    # Exit a parse tree produced by SimpleParser#MulDiv.
    def exitMulDiv(self, ctx:SimpleParser.MulDivContext):
        pass


    # Enter a parse tree produced by SimpleParser#AddSub.
    def enterAddSub(self, ctx:SimpleParser.AddSubContext):
        pass

    # Exit a parse tree produced by SimpleParser#AddSub.
    def exitAddSub(self, ctx:SimpleParser.AddSubContext):
        pass


    # Enter a parse tree produced by SimpleParser#Parens.
    def enterParens(self, ctx:SimpleParser.ParensContext):
        pass

    # Exit a parse tree produced by SimpleParser#Parens.
    def exitParens(self, ctx:SimpleParser.ParensContext):
        pass


    # Enter a parse tree produced by SimpleParser#Int.
    def enterInt(self, ctx:SimpleParser.IntContext):
        pass

    # Exit a parse tree produced by SimpleParser#Int.
    def exitInt(self, ctx:SimpleParser.IntContext):
        pass



del SimpleParser