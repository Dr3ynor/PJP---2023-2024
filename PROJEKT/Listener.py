from antlr.projectListener import projectListener
from antlr.projectParser import projectParser

class Listener(projectListener):
    def __init__(self):
        super().__init__()
        self.symbol_table = [{}]
        self.errors = []


    def enterLoop(self, ctx: projectParser.LoopContext):
        print("Entered Loop")
        print(f"ENTER | Symbol table: {self.symbol_table}")
        self.symbol_table.append({})

    def exitLoop(self, ctx: projectParser.LoopContext):
        print(f"EXIT | Symbol table: {self.symbol_table}")
        print("Exited Loop")
        self.symbol_table.pop()



    """def enterBlock(self, ctx:projectParser.BlockContext):
        print("Entered block")
        print(f"ENTER | Symbol table: {self.symbol_table}")
        self.symbol_table.append({})

    def exitBlock(self, ctx:projectParser.BlockContext):
        print(f"EXIT | Symbol table: {self.symbol_table}")
        print("Exited block")
        self.symbol_table.pop()"""

    def enterVariableDeclaration(self, ctx:projectParser.VariableDeclarationContext):
        type_identifier = ctx.TYPE_IDENTIFIER().getText()
        ids = ctx.ID()

        for id in ids:
            id_text = id.getText()
            if id_text in self.symbol_table[-1]:
                self.errors.append(f"Error: Duplicate variable {id_text}")
                # print(f"Error: Duplicate variable {id_text}")
                # exit(-1)
            else:
                #print(f"Variable {id_text} of type {type_identifier}")
                # Set a default value based on the type of the variable
                if type_identifier == 'int':
                    default_value = 0
                elif type_identifier == 'float':
                    default_value = 0.0
                elif type_identifier == 'bool':
                    default_value = False
                elif type_identifier == 'string':
                    default_value = ''
                else:
                    #print(f"Error: Unknown type {type_identifier}")
                    self.errors.append(f"Error: Unknown type {type_identifier}")
                    #exit(-1)

                self.symbol_table[-1][id_text] = {'type': type_identifier, 'value': default_value}
        """
        for id in ids:
            print(f"Variable {id.getText()} of type {type_identifier}")
            self.symbol_table[id.getText()] = type_identifier
        """
    def exitDeclaration(self, ctx: projectParser.VariableDeclarationContext):
        type_identifier = ctx.TYPE().getText()
        ids = ctx.ID()

        for id in ids:
            id_text = id.getText()
            if id_text in self.symbol_table[-1]:
                self.errors.append(f"Variable {id_text} already declared")
                #print(f"Variable {id_text} already declared")
                #exit(-1)

            self.symbol_table[-1][id_text] = {'type': type_identifier, 'value': None}



    def exitAssignment(self, ctx: projectParser.AssignmentContext):
        var_name = ctx.ID().getText()
        expression = ctx.expression()[0].getText()

    



        if var_name in self.symbol_table[-1]:
            var_info = self.symbol_table[-1][var_name]
            var_type = var_info['type']
            print(f"VAR_TYPE: {var_type}")
            print(f"EXPRESSION: {expression}")

            #expected float, got int
            if '.' not in expression and var_type == 'float':
                expression = self.float_to_int_conversion(expression)

            elif var_type == 'int' and not self.is_int(expression):
                self.errors.append(f"Type error: Expected int, got {type(expression)}. Name: {var_name}")
            elif var_type == 'float' and not self.is_float(expression):
                self.errors.append(f"Type error: Expected float, got {type(expression)}. Name: {var_name}")
            elif var_type == 'bool' and not self.is_bool(expression):
                self.errors.append(f"Type error: Expected bool, got {type(expression)}. Name: {var_name}")
            elif var_type == 'string' and not self.is_string(expression):
                self.errors.append(f"Type error: Expected string, got {type(expression)}. Name: {var_name}")

            var_info['value'] = expression
        else:
            pass
            #self.errors.append(f"Variable {var_name} not declared")
            # print(f"Variable {var_name} not declared")

    def exitComparisonExpression(self, ctx: projectParser.ComparisonExpressionContext):
        left = ctx.expression(0).getText()
        right = ctx.expression(1).getText()
        operator = ctx.getChild(1).getText()

        print(f"LEFT: {left} | RIGHT: {right}")

        if '.' in left:
            left = float(left)
        elif left.isdigit():
            left = int(left)
        elif left != 'true' and left != 'false' or right != 'true' and right != 'false':
            pass
        else:
            self.errors.append(f"Type error: Expected int or float, got {type(left)} | {left}")
        if '.' in right:
            right = float(right)
        elif right.isdigit():
            right = int(right)
        elif left != 'true' and left != 'false' or right != 'true' and right != 'false':
            pass
        else:
            self.errors.append(f"Type error: Expected int or float, got {type(right)} | {right}")

        print(F"LEFT TYPE: {type(left).__name__}")
        print(F"RIGHT TYPE: {type(right).__name__}")

        #write here

        if operator == '==':
            print(f"{left} equals {right}")

        elif operator == '!=':
            print(f"{left} cant equal {right}")

        elif operator == '<':
            print(f"{left} smaller than {right}")

        elif operator == '<=':
            print(f"{left} smaller/equal than {right}")

        elif operator == '>':
            print(f"{left} greater than {right}")

        elif operator == '>=':
            print(f"{left} greater/equals {right}")

        pass


    def exitOr(self, ctx: projectParser.OrContext):
        left = ctx.expression(0).getText()
        right = ctx.expression(1).getText()
        print(f"LEFT: {left} | RIGHT: {right}")

        if str(left) != 'true' and str(left) != 'false':
            self.errors.append(f"Type error: Expected bool, got {type(left)}")
        elif str(right) != 'true' and str(right) != 'false':
            self.errors.append(f"Type error: Expected bool, got {type(right)}")

        print(f"{left} OR {right}")

    def exitAnd(self, ctx: projectParser.AndContext):
        left = ctx.expression(0).getText()
        right = ctx.expression(1).getText()
        print(f"LEFT: {left} | RIGHT: {right}")

        if str(left) != 'true' and str(left) != 'false':
            self.errors.append(f"Type error: Expected bool, got {type(left)}")
        elif str(right) != 'true' and str(right) != 'false':
            self.errors.append(f"Type error: Expected bool, got {type(right)}")

        print(f"{left} AND {right}")

    # + and -
    def exitAdd(self, ctx: projectParser.AddContext):
        left = ctx.expression(0).getText()
        right = ctx.expression(1).getText()
        operator = ctx.getChild(1).getText()

        if '.' in left:
            left = float(left)
        elif left.isdigit():
            left = int(left)
        else:
            self.errors.append(f"Type error: Expected int or float, got {type(left)}")
        if '.' in right:
            right = float(right)
        elif right.isdigit():
            right = int(right)
        else:
            self.errors.append(f"Type error: Expected int or float, got {type(right)}")

        print(f"LEFT: {left} | RIGHT: {right}")
    # * or / or %
    def exitMul(self, ctx: projectParser.MulContext):
        left = ctx.expression(0).getText()
        right = ctx.expression(1).getText()
        operator = ctx.getChild(1).getText()

        if '.' in left:
            left = float(left)
        elif left.isdigit():
            left = int(left)
        else:
            self.errors.append(f"Type error: Expected int or float, got {type(left)}")
        if '.' in right:
            right = float(right)
        elif right.isdigit():
            right = int(right)
        else:
            self.errors.append(f"Type error: Expected int or float, got {type(right)}")

        print(f"OPERATOR: {operator}")

        if operator == '*':
            print(f"{left} * {right}")
        elif operator == '/':
            print(f"{left} / {right}")
        elif operator == '%':
            print(f"{left} % {right}")
        else:
            self.errors.append(f"Unknown operator {operator}")

    
    def exitConcat(self, ctx: projectParser.ConcatContext):
        left = ctx.expression(0).getText()
        right = ctx.expression(1).getText()
        operator = ctx.getChild(1).getText()

        if self.is_string(left) and self.is_string(right):
            print(f"CONCAT: {left} + {right}")
        else:
            self.errors.append(f"Type error: Expected string, got {type(left)}")
    def enterProgram(self, ctx:projectParser.ProgramContext):
        print("Entered program")

    def exitProgram(self, ctx:projectParser.ProgramContext):
        print(f"{self.symbol_table}")
        print("Exited program")
    
    def is_float(self, s):
        if'.' in s:
            return True
        else:
            return False
        
    def is_string(self,s):
        if '"' in s:
            return True
        else:
            return False
        
    def is_bool(self,s):
        if s == 'true' or s == 'false':
            return True
        else:
            return False
    def is_int(self, s):
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()
    
    def float_to_int_conversion(self, s):
        return int(float(s))
    