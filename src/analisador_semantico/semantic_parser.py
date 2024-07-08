from ply import yacc
from ..analisador_lexico.lexer import Lexer
from .semantic_actions import SemanticGrammarRules

class SemanticParser:
    """
    A classe SemanticParser configura e utiliza o analisador sintático para realizar a análise semântica
    do código fonte, utilizando as regras gramaticais definidas na classe SemanticGrammarRules.
    """

    def __init__(self):
        """
        Inicializa a classe SemanticParser. Cria uma instância do Lexer e do SemanticGrammarRules,
        configura os tokens e cria o parser utilizando a biblioteca PLY (Python Lex-Yacc).
        """
        self.lexer = Lexer()
        self.grammar = SemanticGrammarRules()
        self.tokens = self.lexer.token_rules.tokens
        self.parser = yacc.yacc(module=self.grammar)

    def parse(self, data):
        """
        Método para analisar semanticamente o código fonte fornecido.

        Parâmetros:
        - data (str): Código fonte a ser analisado.

        Retorna:
        A análise semântica do código fonte, de acordo com as regras definidas.
        """
        self.lexer.input(data)
        return self.parser.parse(lexer=self.lexer.lexer)

def p_error(p):
    """
    Função de tratamento de erros sintáticos.

    Parâmetros:
    - p: Token onde o erro ocorreu.

    Imprime a mensagem de erro com o valor e a linha do token onde o erro ocorreu.
    Se p for None, indica que o erro ocorreu no final do arquivo.
    """
    if p:
        print(f"Erro sintático em '{p.value}', linha {p.lineno}")
    else:
        print("Erro sintático no final do arquivo (EOF)")
