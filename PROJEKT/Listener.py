from antlr.projectListener import projectListener
from antlr.projectParser import projectParser
from antlr.projectLexer import projectLexer

from VerboseErrorListener import VerboseErrorListener

from antlr4 import *


class Listener(projectListener):
    def __init__(self):
        super().__init__()
        self.blocks = [{}]
        self.error_listener = VerboseErrorListener()
        self.errors = []
        self.values = {}
        self.keywords = ['write', 'read', 'if', 'else', 'while', 'for', 'int', 'float', 'bool', 'string', 'true', 'false']
        self.numbers = ['int', 'float']

    def getAllBlocks(self):
        blocks = {}
        for block in self.blocks:
            for key in block:
                blocks[key] = block[key]
        return blocks
    
    def getBlockWithKey(self, key):
        for block in self.blocks:
            if key in block:
                return block
        return None
    
    def enterBlock(self, ctx: projectParser.BlockContext):
        self.blocks.append({})
                           
    def exitBlock(self, ctx: projectParser.BlockContext):
        self.blocks.pop()

    def getRuleType(self, ctx:ParserRuleContext):
        rule = type(ctx).__name__.replace("Context", "").lower()

        match type(ctx):
            case projectParser.IdContext:
                rule = self.getAllBlocks()[ctx.getText()][0]
            
            case projectParser.AddSubContext:
                left_type = self.getRuleType(ctx.expression(0))
                right_type = self.getRuleType(ctx.expression(1))
                if left_type not in self.numbers or right_type not in self.numbers:
                    self.errors.append(f"ERROR: Add/Sub requires int or float, but got {left_type} Add/Sub {right_type}")
                
                if left_type == "int" and right_type == "int":
                    rule = "int"
                else:
                    rule = "float"

            case projectParser.MulDivContext:
                left_type = self.getRuleType(ctx.expression(0))
                right_type = self.getRuleType(ctx.expression(1))
                if left_type not in self.numbers or right_type not in self.numbers:
                    self.errors.append(f"Mul/Div requires int, float, but got {left_type} Mul/Div {right_type}")
                
                if left_type == "int" and right_type == "int":
                    rule = "int"
                else:
                    rule = "float"

            case projectParser.ModContext:
                left_type = self.getRuleType(ctx.expression(0))
                right_type = self.getRuleType(ctx.expression(1))
                if left_type != "int" or right_type != "int":
                    self.errors.append(f"Mod requires int, but got {left_type} Mod {right_type}")
                rule = "int"

            case projectParser.NegativeUnaryContext:
                value_type = self.getRuleType(ctx.expression())
                if value_type != "int" and value_type != "float":
                    self.errors.append(f"Negative Unary requires int or float, but got {value_type}")
                rule = value_type
            case projectParser.NotContext:
                value_type = self.getRuleType(ctx.expression())
                if value_type != "bool":
                    self.errors.append(f"Not requires bool, but got {value_type}")
                rule = "bool"
            case projectParser.AndContext:
                left_type = self.getRuleType(ctx.expression(0))
                right_type = self.getRuleType(ctx.expression(1))
                if left_type != "bool" or right_type != "bool":
                    self.errors.append(f"And requires bool, but got {left_type} And {right_type}")
                rule = "bool"

            case projectParser.OrContext:
                left_type = self.getRuleType(ctx.expression(0))
                right_type = self.getRuleType(ctx.expression(1))

                if left_type != "bool" or right_type != "bool":
                    self.errors.append(f"Or requires bool, but got {left_type} Or {right_type}")
                rule = "bool"

            case projectParser.RelationalOperationsContext:
                left_type = self.getRuleType(ctx.expression(0))
                right_type = self.getRuleType(ctx.expression(1))
                operator = ctx.getText()
                match operator:
                    case "==":
                        if left_type not in ["int", "float", "string"] or right_type not in ["int", "float", "string"]:
                            self.errors.append(f"Error: == requires int,float,string, but got {left_type} == {right_type} | exitRelationalOperations")
                        if left_type != right_type:
                            self.errors.append(f"Error: == requires int,float,string, but got {left_type} == {right_type} | exitRelationalOperations")
                    case "!=":
                        if left_type not in ["int", "float", "string"] or right_type not in ["int", "float", "string"]:
                            self.errors.append(f"Error: != requires int,float,string, but got {left_type} != {right_type} | exitRelationalOperations")
                    case ">":
                        if left_type not in self.numbers or right_type not in self.numbers:
                            self.errors.append(f"Error: > requires int,float type, but got {left_type} > {right_type} | exitRelationalOperations")
                    case "<":
                        if left_type not in self.numbers or right_type not in self.numbers:
                            self.errors.append(f"Error: < requires int,float type, but got {left_type} < {right_type} | exitRelationalOperations")
                    case ">=":
                        if left_type not in self.numbers or right_type not in self.numbers:
                            self.errors.append(f"Error: >= requires int,float type, but got {left_type} >= {right_type} | exitRelationalOperations")
                    case "<=":
                        if left_type not in self.numbers or right_type not in self.numbers:
                            self.errors.append(f"Error: <= requires int,float type, but got {left_type} <= {right_type} | exitRelationalOperations")
                rule = "bool"
            case projectParser.ParenthesisContext:
                rule = self.getRuleType(ctx.expression())
        
        return rule
    
    def exitVariableDeclaration(self, ctx: projectParser.VariableDeclarationContext):
        for i in range(len(ctx.ID())):
            name = ctx.ID(i)
            data_type = ctx.TYPE_IDENTIFIER()

            if str(name) in self.getAllBlocks():
                self.errors.append(f"Error: Variable {name} already declared | exitVariableDeclaration")
            else:
                match data_type.getText():
                    case "int":
                        self.blocks[len(self.blocks) - 1][str(name)] = (data_type.getText(), 0)
                    case "float":
                        self.blocks[len(self.blocks) - 1][str(name)] = (data_type.getText(), 0.0)
                    case "string":
                        self.blocks[len(self.blocks) - 1][str(name)] = (data_type.getText(), "")
                    case "bool":
                        self.blocks[len(self.blocks) - 1][str(name)] = (data_type.getText(), False)
                    case _:
                        self.errors.append(f"Error: Unknown data type {data_type.getText()} | exitVariableDeclaration")

    # TODO: PROBLEM HERE!
    def exitAssignment(self, ctx: projectParser.AssignmentContext):
        name = ctx.ID()
        expression = None

        while True:
            if expression is None:
                expression = ctx.expression()
            else:
                expression = expression.expression()
            if type(expression).__name__.replace("Context", "").lower() != "assignment":
                break

        value = expression
        data_type = self.getRuleType(value)
        block = self.getBlockWithKey(str(name))
        if block is None:
            self.errors.append(f"Error: Variable {name} not declared | exitAssignment")
            return
        declaration_type = block[str(name)][0]
        
        if data_type == declaration_type:
            #conversion
            if data_type == "int" and declaration_type == "float":
                data_type = "float"
            else:
                self.errors.append(f"Error: Variable {name} is {declaration_type}, but got {data_type} | exitAssignment")

        if str(value.getText()).isdecimal() and declaration_type == "float":
            block[str(name)] = (str(declaration_type),float(value.getText()))
        else:
            block[str(name)] = (str(declaration_type),value.getText())

    def exitConcat(self, ctx: projectParser.ConcatContext):
        left_value = ctx.expression(0)
        right_value = ctx.expression(1)
        data_type_left= type(left_value).__name__.replace("Context", "").lower()
        data_type_right = type(right_value).__name__.replace("Context", "").lower()

        if data_type_left != "string" or data_type_right != "string":
            self.errors.append(f"Error: Concat requires string, but got {data_type_left} Concat {data_type_right} | exitConcat")

    # While loop
    def exitLoop(self, ctx: projectParser.LoopContext):
        value = ctx.expression()
        data_type = self.getRuleType(value)
        if data_type != "bool":
            self.errors.append(f"Error: Loop requires bool, but got {data_type} | exitLoop")

    def exitCondition(self, ctx: projectParser.ConditionContext):
        value = ctx.expression()
        data_type =self.getRuleType(value)
        if data_type != "bool":
            self.errors.append(f"Error: Condition requires bool, but got {data_type} | exitCondition")
    
    # TODO: TEST THIS:
    def exitConditionWithoutBrackets(self, ctx: projectParser.ConditionWithoutBracketsContext):
        value = ctx.expression()
        data_type =self.getRuleType(value)
        if data_type != "bool":
            self.errors.append(f"Error: Condition requires bool, but got {data_type} | exitCondition")

    def exitForLoop(self, ctx: projectParser.ForLoopContext):
        data_type2 = self.getRuleType(ctx.expression(1))
        if data_type2 != "bool":
            self.errors.append(f"Error: For Loop requires bool, but got {data_type2} | exitForLoop")

    def exitEveryRule(self, ctx):
        self.getRuleType(ctx)
    

    def enterProgram(self, ctx: projectParser.ProgramContext):
        print("Program Entered")

    def exitProgram(self, ctx: projectParser.ProgramContext):
        print("Program Exited")
        