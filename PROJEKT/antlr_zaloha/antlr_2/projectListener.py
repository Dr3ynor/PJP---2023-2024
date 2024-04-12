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


    # Enter a parse tree produced by projectParser#whileLoop.
    def enterWhileLoop(self, ctx:projectParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by projectParser#whileLoop.
    def exitWhileLoop(self, ctx:projectParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by projectParser#add.
    def enterAdd(self, ctx:projectParser.AddContext):
        pass

    # Exit a parse tree produced by projectParser#add.
    def exitAdd(self, ctx:projectParser.AddContext):
        pass


    # Enter a parse tree produced by projectParser#sub.
    def enterSub(self, ctx:projectParser.SubContext):
        pass

    # Exit a parse tree produced by projectParser#sub.
    def exitSub(self, ctx:projectParser.SubContext):
        pass


    # Enter a parse tree produced by projectParser#or.
    def enterOr(self, ctx:projectParser.OrContext):
        pass

    # Exit a parse tree produced by projectParser#or.
    def exitOr(self, ctx:projectParser.OrContext):
        pass


    # Enter a parse tree produced by projectParser#mul.
    def enterMul(self, ctx:projectParser.MulContext):
        pass

    # Exit a parse tree produced by projectParser#mul.
    def exitMul(self, ctx:projectParser.MulContext):
        pass


    # Enter a parse tree produced by projectParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:projectParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by projectParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:projectParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by projectParser#concat.
    def enterConcat(self, ctx:projectParser.ConcatContext):
        pass

    # Exit a parse tree produced by projectParser#concat.
    def exitConcat(self, ctx:projectParser.ConcatContext):
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


    # Enter a parse tree produced by projectParser#string_literal.
    def enterString_literal(self, ctx:projectParser.String_literalContext):
        pass

    # Exit a parse tree produced by projectParser#string_literal.
    def exitString_literal(self, ctx:projectParser.String_literalContext):
        pass


    # Enter a parse tree produced by projectParser#not.
    def enterNot(self, ctx:projectParser.NotContext):
        pass

    # Exit a parse tree produced by projectParser#not.
    def exitNot(self, ctx:projectParser.NotContext):
        pass


    # Enter a parse tree produced by projectParser#boolean.
    def enterBoolean(self, ctx:projectParser.BooleanContext):
        pass

    # Exit a parse tree produced by projectParser#boolean.
    def exitBoolean(self, ctx:projectParser.BooleanContext):
        pass


    # Enter a parse tree produced by projectParser#and.
    def enterAnd(self, ctx:projectParser.AndContext):
        pass

    # Exit a parse tree produced by projectParser#and.
    def exitAnd(self, ctx:projectParser.AndContext):
        pass


    # Enter a parse tree produced by projectParser#id.
    def enterId(self, ctx:projectParser.IdContext):
        pass

    # Exit a parse tree produced by projectParser#id.
    def exitId(self, ctx:projectParser.IdContext):
        pass


    # Enter a parse tree produced by projectParser#negative_unary.
    def enterNegative_unary(self, ctx:projectParser.Negative_unaryContext):
        pass

    # Exit a parse tree produced by projectParser#negative_unary.
    def exitNegative_unary(self, ctx:projectParser.Negative_unaryContext):
        pass


    # Enter a parse tree produced by projectParser#writeCommand.
    def enterWriteCommand(self, ctx:projectParser.WriteCommandContext):
        pass

    # Exit a parse tree produced by projectParser#writeCommand.
    def exitWriteCommand(self, ctx:projectParser.WriteCommandContext):
        pass


    # Enter a parse tree produced by projectParser#readCommand.
    def enterReadCommand(self, ctx:projectParser.ReadCommandContext):
        pass

    # Exit a parse tree produced by projectParser#readCommand.
    def exitReadCommand(self, ctx:projectParser.ReadCommandContext):
        pass


    # Enter a parse tree produced by projectParser#assignment.
    def enterAssignment(self, ctx:projectParser.AssignmentContext):
        pass

    # Exit a parse tree produced by projectParser#assignment.
    def exitAssignment(self, ctx:projectParser.AssignmentContext):
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


