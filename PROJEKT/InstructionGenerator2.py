from antlr.projectListener import projectListener
from antlr.projectParser import projectParser
from antlr.projectLexer import projectLexer

import re
import ast
class InstructionGenerator2(projectListener):
    def __init__(self):
        self.instruction = []
    """
        def get_type(self, value):
        if value.isdigit():
            return 'I'
        elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
            return 'F'
        elif value.lower() in ['true', 'false']:
            return 'B'
        elif '+' == value:
            return 'add'
        elif '-' == value:
            return 'sub'
        elif '*' == value:
            return 'mul'
        elif '/' == value:
            return 'div'
        elif '%' == value:
            return 'mod'
        else:
            return 'S'
    """
    
    
    def get_type(self, value):
        if isinstance(value, int):
            return 'I'
        elif isinstance(value, float):
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


    def exitWriteCommand(self, ctx: projectParser.WriteCommandContext):
        string_literal = ctx.STRING_LITERAL().getText()
        expressions = [expr.getText() for expr in ctx.expression()]

        print(f"EXPRESSIONS: {expressions}")
        self.instruction.append("print 1")
        self.instruction.append(f"push S {string_literal}")

        for string in expressions:
            elements = re.split(r'(\+|-|\*|/|%)', string)
            for element in elements:
                try:
                    if element in ['+', '-', '*', '/', '%']:
                        data_type = self.get_type(element)
                        print(f"element: {element} | type: {data_type}")
                        continue

                    else:
                        value = ast.literal_eval(element)
                        
                    data_type = self.get_type(value)
                    print(f"value: {value} | type: {data_type}")
                except (ValueError, SyntaxError):
                    value = str(element)
                    print(f"EXCEPTION: {value}")
                    #print(f"Cannot parse {element} into a Python literal.")


    def exitAddSub(self, ctx: projectParser.AddSubContext):
        pass

    def exitMulDiv(self, ctx: projectParser.MulDivContext):
        pass

    def exitProgram(self, ctx: projectParser.ProgramContext):
        print("EXIT PROGRAM")

        for instruction in self.instruction:
            print(instruction)
