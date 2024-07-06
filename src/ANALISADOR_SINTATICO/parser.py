from ply import yacc
from ..ANALISADOR_LEXICO.lexer import Lexer
from .grammar_rules import GrammarRules

class Parser:
    def __init__(self):
        self.lexer = Lexer()
        self.grammar = GrammarRules()
        self.tokens = self.lexer.token_rules.tokens
        self.parser = yacc.yacc(module=self.grammar)
    
    def parse(self, data):
        self.lexer.input(data)
        return self.parser.parse(lexer=self.lexer.lexer)

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")