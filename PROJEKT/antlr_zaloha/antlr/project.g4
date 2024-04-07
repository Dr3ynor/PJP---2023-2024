grammar project;

program: statement* EOF;

statement: emptyCommand=';' //empty command
         | variableDeclaration
         | writeCommand
         | assignment
         | readCommand
         | condition
         | loop
         | expression ';'
         | block
         ;
block: '{' statement* '}';

expression:
     INT                                                            #int
    | FLOAT                                                         #float
    | BOOLEAN                                                       #boolean
    | '!' expression                                                #not
    | '-' expression                                                #neg
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

condition: 'if' '(' expression ')' statement ('else' statement)?;

loop: 'while' '(' expression ')' statement;

variableDeclaration: TYPE_IDENTIFIER ID ((',' ID)+)? (ASSIGN expression)? ';';


TYPE_IDENTIFIER: ('int' | 'float' | 'bool' | 'string');

INT: [1-9][0-9]* | '0';

FLOAT: [0-9]+ '.' [0-9]+ | [1-9][0-9]*;

BOOLEAN: ('true' | 'false');

STRING_LITERAL: '"' .*? '"';

ID: [a-zA-Z][a-zA-Z0-9]*;

COMMENT: '//' ~[\r\n]* -> skip;

ASSIGN: '=';

WS: [ \t\r\n]+ -> skip;
