from ply import lex
from .token_rules import TokenRules

class Lexer:
    """
    Classe Lexer configura e utiliza o analisador léxico (lexer) para converter 
    o código fonte em tokens utilizando as regras definidas na classe TokenRules.
    """

    def __init__(self):
        """
        Inicializa a classe Lexer. Cria uma instância de TokenRules e configura
        o lexer utilizando a biblioteca PLY (Python Lex-Yacc).
        """
        self.token_rules = TokenRules()
        self.lexer = lex.lex(module=self.token_rules)
    
    def input(self, data):
        """
        Método para fornecer o código fonte ao lexer.

        Parâmetros:
        data (str): Código fonte a ser analisado.
        """
        self.lexer.input(data)
    
    def token(self):
        """
        Método para obter o próximo token do lexer.

        Retorna:
        LexToken: O próximo token identificado pelo lexer.
        """
        return self.lexer.token()
    
    def tokenize(self):
        """
        Método para gerar uma sequência de tokens a partir do código fonte fornecido.
        
        Este método é um gerador que continua retornando tokens até que não haja mais tokens a serem gerados.

        Uso:
        for token in lexer.tokenize():
            print(token)
        
        Yields:
        LexToken: O próximo token identificado pelo lexer.
        """
        while True:
            tok = self.token()
            if not tok:
                break
            yield tok
