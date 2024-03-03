def first(grammar, term):
    result = set()
    if term not in grammar:
        return {term}
    for expression in grammar[term]:
        for symbol in expression:
            symbol_first = first(grammar, symbol)
            result.update(symbol_first - {'epsilon'})
            if 'epsilon' not in symbol_first:
                break
        else:
            result.add('epsilon')
    return result


def first_of_rule(grammar, rule):
    result = set()
    for symbol in rule:
        symbol_first = first(grammar, symbol)
        result.update(symbol_first - {'epsilon'})
        if 'epsilon' not in symbol_first:
            break
    else:
        result.add('epsilon')
    return result


def follow(grammar, term, start_symbol=None, visited=None):
    if visited is None:
        visited = set()
    if start_symbol is None:
        start_symbol = term
    result = set()
    if term == start_symbol:
        result.add('$')
    for key, expressions in grammar.items():
        for expression in expressions:
            try:
                position = expression.index(term)
            except ValueError:
                continue
            follow_in_production = set()
            if position + 1 < len(expression):
                follow_in_production = first(grammar, expression[position + 1]) - {'epsilon'}
            if 'epsilon' in follow_in_production or position + 1 == len(expression):
                if key != term and key not in visited:
                    visited.add(key)
                    follow_in_production.update(follow(grammar, key, start_symbol, visited))
            result.update(follow_in_production)
    return result

grammar = {
    'A': [['b', 'C'], ['B', 'd']],
    'B': [['C', 'C'], ['b', 'A']],
    'C': [['c', 'C'], ['epsilon']]
}


#for non_terminal in grammar:
    #print(f"First[{non_terminal}] = {first(grammar, non_terminal)}")
for non_terminal, rules in grammar.items():
    for rule in rules:
        print(f"First[{non_terminal}:{''.join(rule)}] = {first_of_rule(grammar, rule)}")
print("-----------------------------------------")
for non_terminal in grammar:
    print(f"Follow[{non_terminal}] = {follow(grammar, non_terminal)}")
