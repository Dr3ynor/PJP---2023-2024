grammar project;

program: statement+ EOF;

statement:
	emptyCommand = ';' //empty command
	| variableDeclaration
	| writeCommand
	| assignment
	| readCommand
	| condition
	| loop
	| forLoop
	| expression ';'
	| block;

statementList: statement (statement)*;

block: '{' statementList '}';

expression:
	INT													# int
	| FLOAT												# float
	| BOOLEAN											# boolean
	| op = NOT expression								# not
	| SUB expression									# neg
	| STRING_LITERAL									# stringLiteral
	| ID												# id
	| expression op = (ADD | SUB) expression			# addSub
	| expression op = (MUL | DIV) expression			# mulDiv
	| expression op = MOD expression					# mod
	| expression op = AND expression					# and
	| expression op = OR expression						# or
	| expression op = AND expression					# and
	| expression op = DOT expression					# concat
	| expression op = relationalOperations expression	# comparisonExpression
	| '(' expression ')'								# parenthesis;

writeCommand: 'write' STRING_LITERAL (',' expression)* ';';

readCommand: 'read' ID (',' ID)* ';';

assignment: ID (ASSIGN expression)* ';';

condition:
	'if' '(' expression ')' statement ('else' statement)?;

loop: 'while' '(' expression ')' statement;

forLoop:
	'for' '(' assignment ';' expression ';' assignment ')' statement;

variableDeclaration:
	TYPE_IDENTIFIER ID ((',' ID)+)? (ASSIGN expression)? ';';

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

relationalOperations:
	EQUAL
	| NOT_EQUAL
	| LESS
	| GREATER
	| LESS_EQUAL
	| GREATER_EQUAL;

TYPE_IDENTIFIER: ('int' | 'float' | 'bool' | 'string');

INT: [1-9][0-9]* | '0';

FLOAT: [0-9]+ '.' [0-9]+ | [1-9][0-9]*;

BOOLEAN: ('true' | 'false');

STRING_LITERAL: '"' .*? '"';

ID: [a-zA-Z][a-zA-Z0-9]*;

COMMENT: '//' ~[\r\n]* -> skip;

ASSIGN: '=';

WS: [ \t\r\n]+ -> skip;