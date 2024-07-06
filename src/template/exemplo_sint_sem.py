# ATIVIDADE PRÁTICA - reconhecedor de estruturas em C

from ply import *

contexto = 0

def get_contexto():
    return contexto

# Tabela de simbolos
# {ID {valor, tipo, contexto}}
simbolos = {}


# Palavras reservadas <palavra>:<TOKEN>
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'int' : 'INT',
    'float' : 'FLOAT',
    'main': 'MAIN'
}

# Demais TOKENS
tokens = [
    'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'LPAREN', 'RPAREN', 'LT', 'LE', 'GT', 'GE', 'NE',
    'COMMA', 'SEMI', 'INTEGER', 'FLOATN', 'STRING',
    'ID', 'SEMICOLON', 'RBRACES', 'LBRACES'
] + list(reserved.values())

t_ignore = ' \t\n'

def t_REM(t):
    r'REM .*'
    return t

# Definição de Identificador com expressão regular r'<expressão>'
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_POWER = r'\^'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RBRACES = r'\}'
t_LBRACES = r'\{'
t_SEMICOLON = r'\;'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NE = r'!='
t_COMMA = r'\,'
t_SEMI = r';'
t_INTEGER = r'\d+'
t_FLOATN = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING = r'\".*?\"'

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# Constroi o analisador léxico
lexer = lex.lex()

def p_inicio(p):
    'inicio : INT MAIN LPAREN RPAREN blocoprincipal'
    print("reconheci bloco inicial")
    print(simbolos)

def p_blocoprincipal(p):
    'blocoprincipal : LBRACES declaracoes RBRACES SEMICOLON'
    print("reconheci bloco principal")

def p_declaracoes(p):
    '''declaracoes : tipo ID SEMICOLON
                    | tipo ID SEMICOLON declaracoes'''
    print("reconheci declaração")
    simbolos[p[2]] = {'valor': None, 'tipo': p[1], 'contexto':get_contexto()}
    print(str(simbolos[p[2]]))

def p_tipo(p):
    '''tipo : INT
            | FLOAT '''
    p[0] = p[1]


import ply.yacc as yacc
yacc.yacc()

import logging
logging.basicConfig(
    level=logging.INFO,
    filename="parselog.txt"
)

# entrada do arquivo
file = open("input.txt",'r')
data = file.read()

# string de teste como entrada do analisador léxico
lexer.input(data)

# Tokenização
for tok in lexer:
     print(tok)

yacc.parse(data, debug=logging.getLogger())
