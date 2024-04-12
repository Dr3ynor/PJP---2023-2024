from antlr4 import error

class VerboseErrorListener(error.ErrorListener.ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    #def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        #self.errors.append(f"Line {line}:{column} {msg}")
    
    def syntaxError(self,msg):
        self.errors.append(msg)

    """
    def syntaxError(self, recognizer, offendingSymbol, line, charPositionInLine, msg, e):
    stack = list(recognizer.getRuleInvocationStack())
    stack.reverse()
    print("rule stack: " + ', '.join(stack))
    print(f"line {line}:{charPositionInLine} at {offendingSymbol}: {msg}")
    """
