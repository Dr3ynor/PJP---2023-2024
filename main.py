import re

def to_string(char_list):
    return ''.join(char_list)

def remove_spaces(input_string):
    return ''.join(char for char in input_string if char != ' ')

def validate_constraints(expression):
    valid_pattern = r'^[\d()+\-*/%]+$'
    return bool(re.match(valid_pattern, expression))


def evaluate_expression(expression):
    if "**" in expression:
        return "ERROR"
    expression = remove_spaces(expression)
    
    if not validate_constraints(expression):
        return "VALIDATION ERROR"

    stack = []

    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "ERROR: BRACKETS NOT FORMATTED CORRECTLY!"
            stack.pop()

    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "ERROR: DIVISION BY ZERO"
    except Exception as e:
        return "ERROR"

num_of_lines = input("Insert a positive integer:")
print(num_of_lines)
tmp = 0
while tmp < int(num_of_lines):
    expression = input("Enter expression: ")
    print(evaluate_expression(expression))
    tmp = tmp+1