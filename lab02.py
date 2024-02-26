# TODO: REMOVE COMMENTS! LINE 16
import re

def print_tokens(tokens):
    for token in tokens:
        print(token)

def tokenize(expression):
    patterns = [
        (r'\b\d+\b', 'NUM'),
        (r'[+\-*/]', 'OP'),
        (r'\(', 'LPAR'),
        (r'\)', 'RPAR'),
        (r';', 'SEMICOLON'),
        (r'\b[a-zA-Z_]\w*\b', 'ID'),
        (r'//.*', 'COMMENT'), 
    ]

    tokens = []
    for pattern, token_type in patterns:
        matches = re.finditer(pattern, expression)
        for match in matches:
            tokens.append((match.start(), token_type, match.group()))

    tokens.sort(key=lambda x: x[0])

    ordered_tokens = []
    for position, token_type, value in tokens:
        ordered_tokens.append((token_type, value))

    
    return ordered_tokens

example_input_1 = "-2 + (245 / 3);  // note"
example_input_2 = "2 / 3 * hello"

output_1 = tokenize(example_input_1)
output_2 = tokenize(example_input_2)


print("Input:", example_input_1)
print_tokens(output_1)
print("\nInput:", example_input_2)
print_tokens(output_2)
