grammar project;

program: statement+ EOF;

statement:
	emptyCommand = ';'
	| variableDeclaration
	| writeCommand
	| assignment
	| readCommand
	| conditionWithoutBrackets
	| condition
	| loop
	| forLoop
	| expression ';'
	| block;

block: '{' statementList '}';
statementList: statement (statement)*;

expression:
	INT													# int
	| FLOAT												# float
	| BOOLEAN											# boolean
	| op = NOT expression								# not
	| op = SUB expression								# negativeUnary
	| STRING_LITERAL									# stringLiteral
	| ID												# id
	| expression op = (MUL | DIV) expression			# mulDiv
	| expression op = (ADD | SUB) expression			# addSub
	| expression op = MOD expression					# mod
	| expression op = AND expression					# and
	| expression op = OR expression						# or
	| expression op = DOT expression					# concat
	| expression op = relationalOperations expression	# relationaloperations
	| '(' expression ')'								# parenthesis;

readCommand: 'read' expression (',' expression)* ';';

writeCommand: 'write' STRING_LITERAL (',' expression)* ';';

assignment: ID ('=' ID)* '=' expression;

condition:
	'if' '(' expression ')' '{' statement* '}' ('else' statement)?;

conditionWithoutBrackets:
	'if' '(' expression ')' statement ('else' statement)?;

loop: 'while' '(' expression ')' '{' statement* '}';

forLoop:
	'for' '(' assignment ';' expression ';' assignment ')' '{' statement* '}';

variableDeclaration:
	TYPE_IDENTIFIER ID ((',' ID)+)? (ASSIGN expression)? ';';

relationalOperations:
	EQUAL
	| NOT_EQUAL
	| LESS
	| GREATER
	| LESS_EQUAL
	| GREATER_EQUAL;

SEMICOLON: ';';
COMMA: ',';
DOT: '.';
MUL: '*';
DIV: '/';
MOD: '%';
ADD: '+';
SUB: '-';

EQUAL: '==';
NOT_EQUAL: '!=';
LESS: '<';
GREATER: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';

NOT: '!';
AND: '&&';
OR: '||';

TYPE_IDENTIFIER: ('int' | 'float' | 'bool' | 'string');

INT: ([0-9]+);

FLOAT: [0-9]+ '.' [0-9]+;

BOOLEAN: ('true' | 'false');

STRING_LITERAL: '"' .*? '"';

ID: [a-zA-Z][a-zA-Z0-9]*;

COMMENT: '//' ~[\r\n]* -> skip;

ASSIGN: '=';

WS: [ \t\r\n]+ -> skip;