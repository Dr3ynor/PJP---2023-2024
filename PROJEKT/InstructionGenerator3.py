# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
# DEPRECATED DO NOT USE!!!!!!!!!!!!!!!!!!
from antlr.projectListener import projectListener
from antlr.projectParser import projectParser


# TODO: Add the rest of the instructions
# TODO: make it work so it will accept correctly for example: true and false or false
# TODO: WTF ARE THESE INSTRUCTIONS? PROBABLY IF, FOR, WHILE, ETC.
"""
push T x	Instruction pushs the value x of type T. Where T represents I - int, F - float, S - string, B - bool. Example: push I 10, push B true, push S "A B C "
pop	Instruction takes on value from the stack and discards it.
load id	Instruction loads value of variable id on stack.
save id	Instruction takes value from the top of the stack and stores it into the variable with name id
label n	Instruction marks the spot in source code with unique number n
jmp n	Instruction jumps to the label defined by unique number n
fjmp n	Instruction takes boolean value from the stack and if it is false, it will perform a jump to a label with unique number n
print n	Instruction takes n values from stack and prints them on standard output
read T
"""


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
    
    def pushTwoExpressions(self, ctx):
            left_expression = ctx.expression(0).getText()
            right_expression = ctx.expression(1).getText()
            left_data_type = self.get_type(left_expression)
            right_data_type = self.get_type(right_expression)
            print(f"push {left_data_type} {left_expression}")
            print(f"push {right_data_type} {right_expression}")


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

    # TODO: ENTER OR EXIT ?????
    def enterWriteCommand(self, ctx: projectParser.WriteCommandContext):
        string_literal = ctx.STRING_LITERAL().getText()
        expressions = [expr.getText() for expr in ctx.expression()]
        print(f"push S {string_literal}")

        if "operators" in string_literal:
            print(f"print 1")
        elif "" == string_literal:
            print(f"print 1")


        #print(f"EXPRESSIONS: {expressions}")
        
        """
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
        """

    def enterGreater(self, ctx: projectParser.GreaterContext):
        left_expression = ctx.expression(0).getText()
        right_expression = ctx.expression(1).getText()

        left_data_type = self.get_type(left_expression)
        right_data_type = self.get_type(right_expression)

        print(f"push {left_data_type} {left_expression}")
        
        if left_data_type == 'I' and right_data_type == 'F':
            print(f"itof")
        
        print(f"push {right_data_type} {right_expression}")

        if right_data_type == 'I' and left_data_type == 'F':
            print(f"itof")


        print(f"gt")
        print("print 2")

        """
        self.pushTwoExpressions(ctx)
        print(f"gt")
        print("print 2")
        


        left_expression = ctx.expression(0).getText()
        right_expression = ctx.expression(1).getText()
        left_data_type = self.get_type(left_expression)
        right_data_type = self.get_type(right_expression)
        print(f"push {left_data_type} {left_expression}")
        print(f"push {right_data_type} {right_expression}")


        """


    def enterGreaterEqual(self, ctx: projectParser.GreaterEqualContext):
        pass

    def enterLess(self, ctx: projectParser.LessContext):
        self.pushTwoExpressions(ctx)
        print(f"lt")
        print("print 2")
    
    def enterLessEqual(self, ctx: projectParser.LessEqualContext):
        pass


    def enterEqual(self, ctx: projectParser.EqualContext):
        self.pushTwoExpressions(ctx)
        print(f"eq")
        print("print 2")

    def enterNotEqual(self, ctx: projectParser.NotEqualContext):
        self.pushTwoExpressions(ctx)
        print(f"eq")
        print(f"not")
        print("print 2")

    # !bool
    def enterNot(self, ctx: projectParser.NotContext):
        expression = ctx.expression().getText()
        data_type = self.get_type(expression)
        print(f"push {data_type} {expression}")
        print(f"not")
        print("print 1")


    def enterAddSub(self, ctx: projectParser.AddSubContext):
        self.pushTwoExpressions(ctx)
        if ctx.op.text == '+':
            print(f"add")
        else:
            print(f"sub")
        print("print 2")

    def enterMulDiv(self, ctx: projectParser.MulDivContext):
        self.pushTwoExpressions(ctx)
        if ctx.op.text == '*':
            print(f"mul")
        else:
            print(f"div")
        print("print 2")

    def enterMod(self, ctx: projectParser.ModContext):
        self.pushTwoExpressions(ctx)
        print(f"mod")
        print("print 2")

    def enterAnd(self, ctx: projectParser.AndContext):
        self.pushTwoExpressions(ctx)
        print(f"and")
        print("print 2")

    def enterOr(self, ctx: projectParser.OrContext):
        self.pushTwoExpressions(ctx)
        print(f"or")
        print("print 2")

    # -25
    def enterNegativeUnary(self, ctx: projectParser.NegativeUnaryContext):
        expression = ctx.expression().getText()
        data_type = self.get_type(expression)
        print(f"push {data_type} {expression}")
        print(f"neg")
        #print("print 1")

    def enterConcat(self, ctx: projectParser.ConcatContext):
        self.pushTwoExpressions(ctx)
        print(f"concat")
        print("print 2")

    def enterParenthesis(self, ctx: projectParser.ParenthesisContext):
        print("ENTER PARENTHESIS")

    def exitParenthesis(self, ctx: projectParser.ParenthesisContext):
        expression = ctx.expression().getText()
        data_type = self.get_type(expression)
        print(f"push {data_type} {expression}")
        print("EXIT PARENTHESIS")

    def exitProgram(self, ctx: projectParser.ProgramContext):
        print("EXIT PROGRAM")

    def pushTwoExpressions(self, ctx):
            left_expression = ctx.expression(0).getText()
            right_expression = ctx.expression(1).getText()
            left_data_type = self.get_type(left_expression)
            right_data_type = self.get_type(right_expression)
            print(f"push {left_data_type} {left_expression}")
            print(f"push {right_data_type} {right_expression}")