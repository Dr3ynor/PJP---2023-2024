# Generated from project.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .projectParser import projectParser
else:
    from projectParser import projectParser

# This class defines a complete listener for a parse tree produced by projectParser.
class projectListener(ParseTreeListener):

    # Enter a parse tree produced by projectParser#program.
    def enterProgram(self, ctx:projectParser.ProgramContext):
        pass

    # Exit a parse tree produced by projectParser#program.
    def exitProgram(self, ctx:projectParser.ProgramContext):
        pass


    # Enter a parse tree produced by projectParser#statement.
    def enterStatement(self, ctx:projectParser.StatementContext):
        pass

    # Exit a parse tree produced by projectParser#statement.
    def exitStatement(self, ctx:projectParser.StatementContext):
        pass


    # Enter a parse tree produced by projectParser#block.
    def enterBlock(self, ctx:projectParser.BlockContext):
        pass

    # Exit a parse tree produced by projectParser#block.
    def exitBlock(self, ctx:projectParser.BlockContext):
        pass


    # Enter a parse tree produced by projectParser#statementList.
    def enterStatementList(self, ctx:projectParser.StatementListContext):
        pass

    # Exit a parse tree produced by projectParser#statementList.
    def exitStatementList(self, ctx:projectParser.StatementListContext):
        pass


    # Enter a parse tree produced by projectParser#mod.
    def enterMod(self, ctx:projectParser.ModContext):
        pass

    # Exit a parse tree produced by projectParser#mod.
    def exitMod(self, ctx:projectParser.ModContext):
        pass


    # Enter a parse tree produced by projectParser#or.
    def enterOr(self, ctx:projectParser.OrContext):
        pass

    # Exit a parse tree produced by projectParser#or.
    def exitOr(self, ctx:projectParser.OrContext):
        pass


    # Enter a parse tree produced by projectParser#bool.
    def enterBool(self, ctx:projectParser.BoolContext):
        pass

    # Exit a parse tree produced by projectParser#bool.
    def exitBool(self, ctx:projectParser.BoolContext):
        pass


    # Enter a parse tree produced by projectParser#string.
    def enterString(self, ctx:projectParser.StringContext):
        pass

    # Exit a parse tree produced by projectParser#string.
    def exitString(self, ctx:projectParser.StringContext):
        pass


    # Enter a parse tree produced by projectParser#assignment.
    def enterAssignment(self, ctx:projectParser.AssignmentContext):
        pass

    # Exit a parse tree produced by projectParser#assignment.
    def exitAssignment(self, ctx:projectParser.AssignmentContext):
        pass


    # Enter a parse tree produced by projectParser#negativeUnary.
    def enterNegativeUnary(self, ctx:projectParser.NegativeUnaryContext):
        pass

    # Exit a parse tree produced by projectParser#negativeUnary.
    def exitNegativeUnary(self, ctx:projectParser.NegativeUnaryContext):
        pass


    # Enter a parse tree produced by projectParser#notEqual.
    def enterNotEqual(self, ctx:projectParser.NotEqualContext):
        pass

    # Exit a parse tree produced by projectParser#notEqual.
    def exitNotEqual(self, ctx:projectParser.NotEqualContext):
        pass


    # Enter a parse tree produced by projectParser#addSub.
    def enterAddSub(self, ctx:projectParser.AddSubContext):
        pass

    # Exit a parse tree produced by projectParser#addSub.
    def exitAddSub(self, ctx:projectParser.AddSubContext):
        pass


    # Enter a parse tree produced by projectParser#concat.
    def enterConcat(self, ctx:projectParser.ConcatContext):
        pass

    # Exit a parse tree produced by projectParser#concat.
    def exitConcat(self, ctx:projectParser.ConcatContext):
        pass


    # Enter a parse tree produced by projectParser#less.
    def enterLess(self, ctx:projectParser.LessContext):
        pass

    # Exit a parse tree produced by projectParser#less.
    def exitLess(self, ctx:projectParser.LessContext):
        pass


    # Enter a parse tree produced by projectParser#float.
    def enterFloat(self, ctx:projectParser.FloatContext):
        pass

    # Exit a parse tree produced by projectParser#float.
    def exitFloat(self, ctx:projectParser.FloatContext):
        pass


    # Enter a parse tree produced by projectParser#parenthesis.
    def enterParenthesis(self, ctx:projectParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by projectParser#parenthesis.
    def exitParenthesis(self, ctx:projectParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by projectParser#int.
    def enterInt(self, ctx:projectParser.IntContext):
        pass

    # Exit a parse tree produced by projectParser#int.
    def exitInt(self, ctx:projectParser.IntContext):
        pass


    # Enter a parse tree produced by projectParser#mulDiv.
    def enterMulDiv(self, ctx:projectParser.MulDivContext):
        pass

    # Exit a parse tree produced by projectParser#mulDiv.
    def exitMulDiv(self, ctx:projectParser.MulDivContext):
        pass


    # Enter a parse tree produced by projectParser#equal.
    def enterEqual(self, ctx:projectParser.EqualContext):
        pass

    # Exit a parse tree produced by projectParser#equal.
    def exitEqual(self, ctx:projectParser.EqualContext):
        pass


    # Enter a parse tree produced by projectParser#not.
    def enterNot(self, ctx:projectParser.NotContext):
        pass

    # Exit a parse tree produced by projectParser#not.
    def exitNot(self, ctx:projectParser.NotContext):
        pass


    # Enter a parse tree produced by projectParser#and.
    def enterAnd(self, ctx:projectParser.AndContext):
        pass

    # Exit a parse tree produced by projectParser#and.
    def exitAnd(self, ctx:projectParser.AndContext):
        pass


    # Enter a parse tree produced by projectParser#greaterEqual.
    def enterGreaterEqual(self, ctx:projectParser.GreaterEqualContext):
        pass

    # Exit a parse tree produced by projectParser#greaterEqual.
    def exitGreaterEqual(self, ctx:projectParser.GreaterEqualContext):
        pass


    # Enter a parse tree produced by projectParser#id.
    def enterId(self, ctx:projectParser.IdContext):
        pass

    # Exit a parse tree produced by projectParser#id.
    def exitId(self, ctx:projectParser.IdContext):
        pass


    # Enter a parse tree produced by projectParser#lessEqual.
    def enterLessEqual(self, ctx:projectParser.LessEqualContext):
        pass

    # Exit a parse tree produced by projectParser#lessEqual.
    def exitLessEqual(self, ctx:projectParser.LessEqualContext):
        pass


    # Enter a parse tree produced by projectParser#greater.
    def enterGreater(self, ctx:projectParser.GreaterContext):
        pass

    # Exit a parse tree produced by projectParser#greater.
    def exitGreater(self, ctx:projectParser.GreaterContext):
        pass


    # Enter a parse tree produced by projectParser#readCommand.
    def enterReadCommand(self, ctx:projectParser.ReadCommandContext):
        pass

    # Exit a parse tree produced by projectParser#readCommand.
    def exitReadCommand(self, ctx:projectParser.ReadCommandContext):
        pass


    # Enter a parse tree produced by projectParser#writeCommand.
    def enterWriteCommand(self, ctx:projectParser.WriteCommandContext):
        pass

    # Exit a parse tree produced by projectParser#writeCommand.
    def exitWriteCommand(self, ctx:projectParser.WriteCommandContext):
        pass


    # Enter a parse tree produced by projectParser#condition.
    def enterCondition(self, ctx:projectParser.ConditionContext):
        pass

    # Exit a parse tree produced by projectParser#condition.
    def exitCondition(self, ctx:projectParser.ConditionContext):
        pass


    # Enter a parse tree produced by projectParser#conditionWithoutBrackets.
    def enterConditionWithoutBrackets(self, ctx:projectParser.ConditionWithoutBracketsContext):
        pass

    # Exit a parse tree produced by projectParser#conditionWithoutBrackets.
    def exitConditionWithoutBrackets(self, ctx:projectParser.ConditionWithoutBracketsContext):
        pass


    # Enter a parse tree produced by projectParser#loop.
    def enterLoop(self, ctx:projectParser.LoopContext):
        pass

    # Exit a parse tree produced by projectParser#loop.
    def exitLoop(self, ctx:projectParser.LoopContext):
        pass


    # Enter a parse tree produced by projectParser#forLoop.
    def enterForLoop(self, ctx:projectParser.ForLoopContext):
        pass

    # Exit a parse tree produced by projectParser#forLoop.
    def exitForLoop(self, ctx:projectParser.ForLoopContext):
        pass


    # Enter a parse tree produced by projectParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:projectParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by projectParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:projectParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by projectParser#relationalOperations.
    def enterRelationalOperations(self, ctx:projectParser.RelationalOperationsContext):
        pass

    # Exit a parse tree produced by projectParser#relationalOperations.
    def exitRelationalOperations(self, ctx:projectParser.RelationalOperationsContext):
        pass


