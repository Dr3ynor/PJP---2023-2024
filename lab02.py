import re

def remove_keyword_tuples(tuple_list) -> list:
    if ('ID', 'mod') in tuple_list and ('MOD', 'mod') in tuple_list:
        tuple_list.remove(('ID', 'mod'))

    if ('ID', 'div') in tuple_list and ('DIV', 'div') in tuple_list:
        tuple_list.remove(('ID', 'div'))
    return tuple_list


def remove_comments(expression) -> str:
    cleaned_expression = re.sub(r'//.*', '', expression)
    return cleaned_expression


def print_tokens(tokens) -> tuple:
    for token in tokens:
        print(token)


def tokenize(expression) -> str:
    patterns = [
        (r'\b\d+\b', 'NUM'),
        (r'[+\-*/]', 'OP'),
        (r'\(', 'LPAR'),
        (r'\)', 'RPAR'),
        (r';', 'SEMICOLON'),
        (r'\b[a-zA-Z_]\w*\b', 'ID'),
        (r'div', 'DIV'),
        (r'mod', 'MOD'),
    ]
    expression = remove_comments(expression)
    tokens = []
    for pattern, token_type in patterns:
        matches = re.finditer(pattern, expression)
        for match in matches:
            tokens.append((match.start(), token_type, match.group()))

    tokens.sort(key=lambda x: x[0])

    ordered_tokens = []
    for position, token_type, value in tokens:
        ordered_tokens.append((token_type, value))

    ordered_tokens = remove_keyword_tuples(ordered_tokens)
    return ordered_tokens

input_1 = "    -2 + (245 div 3);  // note"
input_2 = "2 mod 3 * hello"

output_1 = tokenize(input_1)
output_2 = tokenize(input_2)


print("Input:", input_1)
print_tokens(output_1)
print("Input:", input_2)
print_tokens(output_2)
