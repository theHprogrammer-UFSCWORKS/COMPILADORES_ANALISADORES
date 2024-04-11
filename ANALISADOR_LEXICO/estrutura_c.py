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
    'EQUALS',       # =
    'PLUS',         # +
    'MINUS',        # -
    'TIMES',        # *
    'DIVIDE',       # /
    'POWER',        # ^
    'LPAREN',       # (
    'RPAREN',       # )
    'LT',           # <
    'LE',           # <=
    'GT',           # >
    'GE',           # >=
    'NE',           # !=
    'COMMA',        # ,
    'SEMI',         # ;
    'INTEGER',      # 123
    'FLOAT_N',      # 123.123
    'STRING',       # "string"
    'ID',           # identificador
    'NEWLINE',      # \n
    'SEMICOLON',    # ;
    'RBRACES',      # }
    'LBRACES',      # {
    'COMPARATOR',   # ==
    'MOD',          # %
    'INCREMENT',    # ++
    'DECREMENT',    # --
    'AND',          # &&
    'OR',           # ||
    'NOT',          # !
    'BITWISE_AND',  # &
    'BITWISE_OR',   # |
    'BITWISE_XOR',  # ^
    'BITWISE_NOT',  # ~
    'LEFT_SHIFT',   # <<
    'RIGHT_SHIFT',  # >>
    'MOD_ASSIGN',   # %=
    'AND_ASSIGN',   # &=
    'OR_ASSIGN',    # |=
    'XOR_ASSIGN',   # ^=
    'LSHIFT_ASSIGN',# <<=
    'RSHIFT_ASSIGN',# >>=
    'PLUS_ASSIGN',  # +=
    'MINUS_ASSIGN', # -=
    'TIMES_ASSIGN', # *=
    'DIVIDE_ASSIGN',# /=
    'TERNARY',      # ? (operador ternário)
    'ELLIPSIS',     # ...
    'HASH',         # #
    'HASH_HASH',    # ##
    'DOT',          # .
    'ARROW',        # ->
    'POINTER',      # *
    'DEFINE',       # define
    'INCLUDE',      # include
] + list(reserved.values())

# Ignora espaços em branco e tabulações
t_ignore = ' \t\n'

# Ignora comentários de uma linha ou multiplas linhas
def t_IGNORE_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    t.lexer.lineno += t.value.count('\n')

# Operadores Aritméticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'\%'

# Operadores de Comparação
t_EQUALS = r'='
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
t_BITWISE_XOR = r'\^'
t_BITWISE_NOT = r'~'
t_LEFT_SHIFT = r'<<'
t_RIGHT_SHIFT = r'>>'

# Operadores de Atribuição
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
t_LBRACES = r'\{'
t_RBRACES = r'\}'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'

# Literais Numéricos e Strings
t_INTEGER = r'\d+'
t_FLOAT_N = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"' 

# Definição de Identificador com expressão regular r'<expressão>'
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Operadores Especiais e Diretivas de Pré-processamento
t_TERNARY = r'\?'
t_ELLIPSIS = r'\.\.\.'
t_DOT = r'\.'
t_ARROW = r'->'
t_HASH = r'\#'
t_HASH_HASH = r'\#\#'

def t_error(t):
    # Imprime o caractere ilegal e sua posição
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    
    # Avança até o próximo caractere
    t.lexer.skip(1)

# Constroi o analisador léxico
lexer = lex.lex()

# Abrir arquivo de entrada em Exemplos
with open('../COMPILADORES/ANALISADOR_LEXICO/test/exemplo2.c', 'r', encoding='utf-8') as file:
    data = file.read()

# string de teste como entrada do analisador léxico
lexer.input(data)

# Tokenização
for tok in lexer:
    print(tok)
