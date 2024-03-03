import re

def remove_spaces(input_string):
    return ''.join(char for char in input_string if char != ' ')


def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = [] 
    postfix = ''
    for char in expression:
        if char not in "+-*/()":
            postfix += char
        elif char == '(':
            stack.append('(')
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            try:
                stack.pop()
            except:
                return "ERROR" 
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix


def evaluate_postfix(expression):
    stack = []
    for char in expression:
        print(stack)
        if char.isdigit(): # fix this in order to process more digit numbers
            stack.append(int(char))
        elif char in "+-*/":
            right = stack.pop()
            try:
                left = stack.pop()
            except:
                return "ERROR"
            if char == '+':
                stack.append(left + right)
            elif char == '-':
                stack.append(left - right)
            elif char == '*':
                stack.append(left * right)
            elif char == '/':
                stack.append(left / right)
        else:
            return "ERROR"
    return stack[0] if stack else "ERROR"


def evaluate_expressions(expressions):
    results = []
    for expression in expressions:
        postfix = infix_to_postfix(expression)
        postfix_without_space = remove_spaces(postfix)
        result = evaluate_postfix(postfix_without_space)
        results.append(result)
    return results


def contains_operator_combinations(input_string):
    operators = ['+', '-', '*', '/']
    combinations = [op1 + op2 for op1 in operators for op2 in operators]

    if any(combination in input_string for combination in combinations):
        return "ERROR"
    else:
        return input_string


expressions = ["2 * (3+5)", "2^5", "15 - 2**7", "5**2", "-2",'4', "abc", "2 * (3 + 5 - 2)","(55+8)*9"]

for exp in expressions:
    print(f"EXPRESSION: {exp}")
    print(f"EVALUATED: {evaluate_postfix(infix_to_postfix(contains_operator_combinations(remove_spaces(exp))))}")
    print("-----------------------------------")
