#!/usr/bin/env python3
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, InputStream
from antlr4.tree.Trees import Trees

from antlr.projectLexer import projectLexer
from antlr.projectParser import projectParser
from VerboseErrorListener import VerboseErrorListener
from Listener import Listener

def main():
    with open('inputs/PLC_errors.in', 'r') as file:
    #with open('inputs/PLC_t3.in', 'r') as file:
        data = file.read()
    input_stream = InputStream(data)
    lexer = projectLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = projectParser(stream)
    
    error_listener = VerboseErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("---------------------")
        print("Syntax errors found!")
        for error in error_listener.errors:
            print(error)
        print("---------------------")
        return

    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    if listener.errors.__len__() > 0:
        print("---------------------")
        print("TYPE CHECKING ERRORS FOUND!:")
        for error in listener.errors:
            print(error)
        print("---------------------")
        return
    print("Parsing completed")
    #print(Trees.toStringTree(tree, None, parser))
if __name__ == '__main__':
    main()