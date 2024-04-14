#!/usr/bin/env python3
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, InputStream
from antlr4.tree.Trees import Trees

from antlr.projectLexer import projectLexer
from antlr.projectParser import projectParser
from VerboseErrorListener import VerboseErrorListener
from Listener import Listener
from InstructionGenerator2 import InstructionGenerator2
def main():
    file_name = 'inputs/PLC_t2.in'
    # file_name = 'inputs/PLC_errors.in'
    with open(file_name, 'r') as file:
        data = file.read()
    
    print(f"FILE: {file_name}")
    input_stream = InputStream(data)
    lexer = projectLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = projectParser(stream)
    listener = Listener()
    walker = ParseTreeWalker()


    error_listener = VerboseErrorListener()

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    print("--------------------------Parsing--------------------------")
    print("Parsing...")
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("---------------------")
        print("Syntax errors found!")
        for error in error_listener.errors:
            print(error)
        print("---------------------")
        return
    print("Parsing completed")

    walker.walk(listener, tree)
    print("-----------------------Type Checking-----------------------")
    print("Type checking...")
    if listener.errors.__len__() > 0:
        print("---------------------")
        print("TYPE CHECKING ERRORS FOUND!:")
        for error in listener.errors:
            print(error)
        print("---------------------")
        return
    print("Type checking completed")

    print("-----------------------Generating instructions-------------")

    instruction_generator = InstructionGenerator2()
    walker.walk(instruction_generator, tree)

    #print(Trees.toStringTree(tree, None, parser))
if __name__ == '__main__':
    main()