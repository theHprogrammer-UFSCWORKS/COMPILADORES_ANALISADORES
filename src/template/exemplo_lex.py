# ATIVIDADE PRÁTICA - reconhecedor de estruturas em C
# Implementado pelo professor: Alison Roberto
# Editado por: Helder Henrique da Silva
from ply import lex

# Palavras reservadas <palavra>:<TOKEN>
reserved = {
    'if' : 'IF',
    'do' : 'DO',
    'int' : 'INT',
    'for' : 'FOR',
    'else' : 'ELSE',
    'char' : 'CHAR',
    'void' : 'VOID',
    'auto' : 'AUTO',
    'case' : 'CASE',
    'goto' : 'GOTO',
    'enum' : 'ENUM',
    'long' : 'LONG',
    'float' : 'FLOAT',
    'const' : 'CONST',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'short' : 'SHORT',
    'union' : 'UNION',
    'return' : 'RETURN',
    'double' : 'DOUBLE',
    'extern' : 'EXTERN',
    'signed' : 'SIGNED',
    'sizeof' : 'SIZEOF',
    'static' : 'STATIC',
    'struct' : 'STRUCT',
    'switch' : 'SWITCH',
    'default' : 'DEFAULT',
    'typedef' : 'TYPEDEF',
    'continue' : 'CONTINUE',
    'register' : 'REGISTER',
    'unsigned' : 'UNSIGNED',
    'volatile' : 'VOLATILE',
        }

# Demais TOKENS
tokens = [
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 'MOD', 'INCREMENT', 'DECREMENT',
    'LT', 'LE', 'GT', 'GE', 'NE', 'COMPARATOR',
    'EQUALS', 'MOD_ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'TIMES_ASSIGN', 'DIVIDE_ASSIGN',
    'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN', 'LSHIFT_ASSIGN', 'RSHIFT_ASSIGN',
    'AND', 'OR', 'NOT',
    'BITWISE_AND', 'BITWISE_OR', 'BITWISE_XOR', 'LSHIFT', 'RSHIFT', 'BITWISE_NOT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'COMMA', 'SEMICOLON', 'NEWLINE',
    'INTEGER', 'FLOAT_N', 'STRING', 'ID', 'INCLUDE', 'DEFINE', 'MAIN', 'LIBRARY',
    'TERNARY', 'ELLIPSIS', 'ARROW', 'DOT', 'HASH', 'DOUBLEHASH'
] + list(reserved.values())

# Ignora comentários de uma linha ou multiplas linhas
def t_IGNORE_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    t.lexer.lineno += t.value.count('\n')

# Imprime o caractere ilegal e sua posição
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")

    # Avança até o próximo caractere
    t.lexer.skip(1)

# Ignora espaços em branco e tabulações
t_ignore = ' \t\n'

# Define o token de função principal
def t_MAIN(t):
    r'main'
    return t

# Define o identificador
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t

# Define o token de número flutuante
def t_FLOAT_N(t):
    r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
    t.value = float(t.value)
    return t

# Define o token de biblioteca
def t_LIBRARY(t):
    r'[<][a-zA-Z_][a-zA-Z0-9_]*\.h[>]'
    return t

# Define o token de string entre aspas duplas
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Define o token de inclusão de biblioteca
def t_INCLUDE(t):
    r'\#include'
    return t

# Define o token de definição
def t_DEFINE(t):
    r'\#define'
    return t

# Definições simples de tokens
# Operadores Aritméticos
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_MOD = r'\%'

# Operadores de Comparação
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'!='
t_COMPARATOR = r'=='

# Operadores Lógicos
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Operadores Bit a Bit
t_BITWISE_AND = r'&'
t_BITWISE_OR = r'\|'
t_BITWISE_NOT = r'~'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'

# Operadores de Atribuição
t_EQUALS = r'='
t_MOD_ASSIGN = r'%='
t_AND_ASSIGN = r'&='
t_OR_ASSIGN = r'\|='
t_XOR_ASSIGN = r'^='
t_LSHIFT_ASSIGN = r'<<='
t_RSHIFT_ASSIGN = r'>>='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='

# Pontuação e Delimitadores
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_NEWLINE = r'\n'

# Literais Numéricos e Strings
t_INTEGER = r'\d+'

# Operadores Especiais e Diretivas de Pré-processamento
t_TERNARY = r'\?'
t_ELLIPSIS = r'\.\.\.'
t_DOT = r'\.'
t_ARROW = r'->'
t_HASH = r'\#'
t_DOUBLEHASH = r'\#\#'

# Constroi o analisador léxico
lexer = lex.lex()

# Abrir arquivo de entrada em Exemplos
with open('tests/test_case5.c', 'r', encoding='utf-8') as file:
    data = file.read()

# string de teste como entrada do analisador léxico
lexer.input(data)

# Tokenização
for tok in lexer:
    print(tok)
