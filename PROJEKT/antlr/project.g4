grammar project;

program: statement* EOF;

statement: emptyCommand=';'
         | variableDeclaration
         | writeCommand
         | assignment
         | readCommand
         | conditionWithoutBrackets
         | condition
         | loop
         | expression ';'
         | whileLoop
         | block
         ;
block: '{' statement* '}';
whileLoop: '[' statement* ']';

expression:
     INT                                                            #int
    | FLOAT                                                         #float
    | BOOLEAN                                                       #boolean
    | '!' expression                                                #not
    | '-' expression                                                #negative_unary
    | STRING_LITERAL                                                #string_literal
    | ID                                                            #id
    | expression ('*' | '/' | '%') expression                       #mul
    | expression ('+' | '-') expression                             #add
    | expression ('&&') expression                                  #and
    | expression ('||') expression                                  #or
    | expression ('.') expression                                   #concat
    | expression ('==' | '!=' | '<' | '<=' | '>' | '>=') expression #comparisonExpression
    | '(' expression ')'                                            #parenthesis
    ;

writeCommand: 'write' expression (',' expression)* ';';
readCommand: 'read' ID (',' ID)* ';';

assignment: ID (ASSIGN expression)* ';';
//assignment: (ID ASSIGN)+ expression ';';


condition: 'if' '(' expression ')' '{' statement* '}' ('else' statement)?;
conditionWithoutBrackets: 'if' '(' expression ')' statement ('else' statement)?;

loop: 'while' '(' expression ')' '{' statement* '}';

variableDeclaration: TYPE_IDENTIFIER ID ((',' ID)+)? (ASSIGN expression)? ';';


TYPE_IDENTIFIER: ('int' | 'float' | 'bool' | 'string');

INT: ('-'? [0-9]+);

FLOAT: '-'? [0-9]+ '.'[0-9]+;

BOOLEAN: ('true' | 'false');

STRING_LITERAL: '"' .*? '"';

ID: [a-zA-Z][a-zA-Z0-9]*;

COMMENT: '//' ~[\r\n]* -> skip;

ASSIGN: '=';

WS: [ \t\r\n]+ -> skip;
