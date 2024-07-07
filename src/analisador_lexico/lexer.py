from ply import lex
from .token_rules import TokenRules

class Lexer:
    def __init__(self):
        self.token_rules = TokenRules()
        self.lexer = lex.lex(module=self.token_rules)
    
    def input(self, data):
        self.lexer.input(data)
    
    def token(self):
        return self.lexer.token()
    
    def tokenize(self):
        while True:
            tok = self.token()
            if not tok:
                break
            yield tok
