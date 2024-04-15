from antlr.projectListener import projectListener
from antlr.projectParser import projectParser
from antlr4 import *

class InstructionGenerator2(projectListener):
    def __init__(self):
        self.itof = False
        self.blocks = [{}]
        self.index = 0
    # Done
    def getAllBlocks(self):
        blocks = {}
        for block in self.blocks:
            for key in block:
                blocks[key] = block[key]
        return blocks
    

    def intToFloat(self, ctx):
        left_expression = ctx.expression(0).getText()
        right_expression = ctx.expression(1).getText()
        left_data_type = self.get_type(left_expression)
        right_data_type = self.get_type(right_expression)
        
        if left_data_type == 'I' and right_data_type == 'F':
            self.itof = True
        

        if right_data_type == 'I' and left_data_type == 'F':
            self.itof = True

    # Done
    def getRuleType(self, ctx:ParserRuleContext):
        rule = type(ctx).__name__.replace("Context", "").lower()

        match type(ctx):
            case projectParser.IdContext:
                rule = self.getAllBlocks()[ctx.getText()]
            
            case projectParser.AddSubContext:
                left_type = self.getRuleType(ctx.expression(0))
                right_type = self.getRuleType(ctx.expression(1))

                if left_type == "int" and right_type == "int":
                    rule = "int"
                else:
                    "float"

            case projectParser.MulDivContext:
                left_type = self.getRuleType(ctx.expression(0))
                right_type = self.getRuleType(ctx.expression(1))
                
                if left_type == "int" and right_type == "int":
                    rule = "int"
                else:
                    rule = "float"

            case projectParser.ModContext:
                rule = "int"

            case projectParser.NegativeUnaryContext:
                value_type = self.getRuleType(ctx.expression())
                rule = value_type

            case projectParser.NotContext:
                value_type = self.getRuleType(ctx.expression())
                rule = value_type

            case projectParser.AndContext | projectParser.OrContext:
                rule = "bool"

            case projectParser.EqualContext | projectParser.NotEqualContext:
                rule = "bool"

            case projectParser.LessContext |projectParser.GreaterContext | projectParser.GreaterEqualContext  | projectParser.LessEqualContext:
                rule = "bool"

            case projectParser.ParenthesisContext:
                rule = self.getRuleType(ctx.expression())
        
        return rule



    def get_type(self, value):
        if isinstance(value, int):
            return 'I'
        elif '.' in value and value.replace('.', '', 1).isdigit() and value.count('.') < 2:
            return 'F'

        elif value in ['true', 'false']:
            return 'B'
        elif isinstance(value, str):
            if value.isdigit():
                return 'I'
            elif value == '+':
                return 'add'
            elif value == '-':
                return 'sub'
            elif value == '*':
                return 'mul'
            elif value == '/':
                return 'div'
            elif value == '%':
                return 'mod'
            else:
                return 'S'
        else:
            return 'Unknown'
        


        


    # >
    def enterGreater(self, ctx: projectParser.GreaterContext):
        self.intToFloat(ctx)

    def exitGreater(self, ctx: projectParser.GreaterContext):
        print(f"gt")



    # <
    def enterLess(self, ctx: projectParser.LessContext):
        self.intToFloat(ctx)
    def exitLess(self, ctx: projectParser.LessContext):
        print(f"lt")
    


    # ==
    def enterEqual(self, ctx: projectParser.EqualContext):
        self.intToFloat(ctx)
    def exitEqual(self, ctx: projectParser.EqualContext):
        print(f"eq")



    # !=
    def exitNotEqual(self, ctx: projectParser.NotEqualContext):
        self.intToFloat(ctx)
    def exitNotEqual(self, ctx: projectParser.NotEqualContext):
        print(f"eq")
        print(f"not")



















    def enterWriteCommand(self, ctx: projectParser.WriteCommandContext):
        string_literal = ctx.STRING_LITERAL().getText()
        expressions = [expr.getText() for expr in ctx.expression()]
        print(f"push S {string_literal}")


    # Done
    def exitAddSub(self, ctx: projectParser.AddSubContext):
        if ctx.op.text == '+':
            print(f"add")
        else:
            print(f"sub")

    # Done
    def enterAddSub(self, ctx: projectParser.AddSubContext):
        left_type = self.getRuleType(ctx.expression(0))
        right_type = self.getRuleType(ctx.expression(1))

        if(left_type == "int" and right_type == "float") or (left_type == "float" and right_type == "int"):
            self.itof = True

    # Done
    def exitMulDiv(self, ctx: projectParser.MulDivContext):
        if ctx.op.text == '*':
            print(f"mul")
        else:
            print(f"div")
    # Done
    def exitMod(self, ctx: projectParser.ModContext):
        print(f"mod")
    # Done
    def exitAnd(self, ctx: projectParser.AndContext):
        print(f"and")
    # Done
    def exitOr(self, ctx: projectParser.OrContext):
        print(f"or")

    # Done
    def exitConcat(self, ctx: projectParser.ConcatContext):
        print(f"concat")

    def exitProgram(self, ctx: projectParser.ProgramContext):
        print("EXIT PROGRAM")

    # Done 
    def enterAssignment(self, ctx: projectParser.AssignmentContext):
        name = ctx.ID()
        declaration_type = self.getAllBlocks()[name.getText()]
        expected_type = self.getRuleType(ctx.expression())
        if declaration_type == "float" and expected_type == "int":
            self.itof = True

    # Done
    def exitAssignment(self, ctx: projectParser.AssignmentContext):
        name = ctx.ID()
        print(f"save {name.getText()}")
        print(f"load {name.getText()}")

        if ctx.parentCtx.getChild(0) == ctx:
            print(f"pop")
    # Done
    def enterBlock(self, ctx:projectParser.BlockContext):
        self.blocks.append({})
    # Done
    def exitBlock(self, ctx: projectParser.BlockContext):
        self.blocks.pop()
    # Done
    def exitString(self, ctx: projectParser.StringContext):
        print(f"push S {ctx.getText()}")
    # Done
    def exitInt(self, ctx: projectParser.IntContext):
        print(f"push I {ctx.getText()}")
        if self.itof:
            print(f"itof")
            self.itof = False
    # Done    
    def exitFloat(self, ctx: projectParser.FloatContext):
        print(f"push F {ctx.getText()}")
    # Done
    def exitBool(self, ctx: projectParser.BoolContext):
        print(f"push B {ctx.getText()}")
    # Done
    def exitWriteCommand(self, ctx: projectParser.WriteCommandContext):
        print(f"print {len(ctx.expression())+1}")
    

    # Done
    def exitReadCommand(self, ctx: projectParser.ReadCommandContext):
        #print("DEBUG STARTS HERE")
        for i in range(len(ctx.expression())):
            expression = ctx.expression(i)
            expression_text = ctx.expression(i).getText() 
            expression_type = self.get_type(expression_text)
            match expression_type:
                case "int":
                    print("read I")
                    print(f"save {expression.ID()}")
                case "float":
                    print("read F")
                    print(f"save {expression.ID()}")
                case "str":
                    print("read S")
                    print(f"save {expression.ID()}")
                case "bool":
                    print("read B")
                    print(f"save {expression.ID()}")
                case _:
                    print(f"read I")
                    print(f"save {expression.ID()}")
        #print("DEBUG ENDS HERE")
    # Done
    def exitId(self, ctx: projectParser.IdContext):
        if (type(ctx.parentCtx) is not projectParser.ReadCommandContext):
            print(f"load {str(ctx.ID())}")
    #-25
    # Done
    def exitNegativeUnary(self, ctx: projectParser.NegativeUnaryContext):
        print("uminus")


    # !bool
    # Done
    def exitNot(self, ctx: projectParser.NotContext):
        print("not")


    # TODO: exitRPar context not found ????


    """
    def exitRPar(self, ctx: projectParser.RParContext):
        match type(ctx.parentCtx):
            case projectParser.ConditionContext:
                self.write_to_file(f"fjmp {self.index}")
                self.index += 1
            case projectParser.LoopContext:
                self.index += 1
                self.write_to_file(f"fjmp {self.index}")
    """
    # Done
    # TODO: test this shit elseStatement?
    def exitCondition(self, ctx: projectParser.ConditionContext):
        if ctx.elseStatement is None:
            print(f"jmp {self.index}")
            print(f"label {self.index - 1}")
            print(f"label {self.index}")
            self.index += 1
    # Done
    def enterElseStatement(self, ctx: projectParser.ElseStatementContext):
        print(f"jmp {self.index}")
        print(f"label {self.index - 1}")
        self.index += 1
    # Done
    def exitElseStatement(self, ctx: projectParser.ElseStatementContext):
        print(f"label {self.index - 1}")
    # Done
    def enterLoop(self, ctx: projectParser.LoopContext):
        print(f"label {self.index}")
    # Done
    def exitLoop(self, ctx: projectParser.LoopContext):
        print(f"jmp {self.index - 1}")
        print(f"label {self.index}")
        self.index += 1
    
    # Done
    def exitVariableDeclaration(self, ctx: projectParser.VariableDeclarationContext):
        for i in range(len(ctx.ID())):
            name = ctx.ID(i)
            type = ctx.TYPE_IDENTIFIER()         
            match type.getText():
                case "int":
                    print(f"push I 0")
                    self.blocks[len(self.blocks) - 1][str(name)] = (type.getText())
                case "float":
                    print(f"push F 0.0")
                    self.blocks[len(self.blocks) - 1][str(name)] = (type.getText())
                case "string":
                    print(f"push S \"\"")
                    self.blocks[len(self.blocks) - 1][str(name)] = (type.getText())
                case "bool":
                    print(f"push B false")
                    self.blocks[len(self.blocks) - 1][str(name)] = (type.getText())

            print(f"save {name.getText()}")

    # Done
    def enterMulDiv(self, ctx: projectParser.MulDivContext):
        left = self.getRuleType(ctx.expression(0))
        right = self.getRuleType(ctx.expression(1))

        if(left == "int" and right == "float") or (left == "float" and right == "int"):
           self.itof = True

    def pushTwoExpressions(self, ctx):
            left_expression = ctx.expression(0).getText()
            right_expression = ctx.expression(1).getText()
            left_data_type = self.get_type(left_expression)
            right_data_type = self.get_type(right_expression)
            print(f"push {left_data_type} {left_expression}")
            print(f"push {right_data_type} {right_expression}")

