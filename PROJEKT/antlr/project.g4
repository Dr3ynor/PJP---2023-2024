grammar project;

program: statement+ EOF;

statement:
	emptyCommand = ';'
	| variableDeclaration
	| writeCommand
	| readCommand
	| condition
	| loop
	| forLoop
	| expression ';'
	| block;

block: '{' statementList '}';

statementList: statement (statement)*;

expression:
	INT											# int
	| '(' expression ')'						# parenthesis
	| FLOAT										# float
	| BOOL										# bool
	| op = NOT expression						# not
	| op = SUB expression						# negativeUnary
	| STRING_LITERAL							# string
	| ID										# id
	| expression op = (MUL | DIV) expression	# mulDiv
	| expression op = (ADD | SUB) expression	# addSub
	| expression op = MOD expression			# mod
	| expression op = AND expression			# and
	| expression op = OR expression				# or
	| expression op = DOT expression			# concat
	| <assoc = right> ID op = '=' expression	# assignment
	| expression EQUAL expression				# equal
	| expression NOT_EQUAL expression			# notEqual
	| expression LESS expression				# less
	| expression GREATER expression				# greater
	| expression LESS_EQUAL expression			# lessEqual
	| expression GREATER_EQUAL expression		# greaterEqual;

rPar: ')';

readCommand: 'read' expression (',' expression)* ';';

writeCommand: 'write' STRING_LITERAL (',' expression)* ';';

condition:
	'if' '(' expression rPar statement (elseStatement)?;

elseStatement: 'else' statement;

loop: 'while' '(' expression rPar '{' statement* '}';

forLoop:
	'for' '(' expression ';' expression ';' expression rPar '{' statement* '}';

variableDeclaration: TYPE_IDENTIFIER ID (',' ID)* ';';

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

BOOL: ('true' | 'false');

STRING_LITERAL: '"' .*? '"';

ID: [a-zA-Z][a-zA-Z0-9]*;

COMMENT: '//' ~[\r\n]* -> skip;

WS: [ \t\r\n]+ -> skip;