from ply import yacc
from ..analisador_lexico.lexer import Lexer
from .grammar_rules import GrammarRules

class Parser:
    """
    A classe Parser configura e utiliza o analisador sintático (parser) para analisar
    o código fonte de acordo com as regras gramaticais definidas na classe GrammarRules.
    """

    def __init__(self):
        """
        Inicializa a classe Parser. Cria uma instância do Lexer e do GrammarRules,
        configura os tokens e cria o parser utilizando a biblioteca PLY (Python Lex-Yacc).
        """
        self.lexer = Lexer()
        self.grammar = GrammarRules()
        self.tokens = self.lexer.token_rules.tokens
        self.parser = yacc.yacc(module=self.grammar)

    def parse(self, data):
        """
        Método para analisar o código fonte fornecido.

        Parâmetros:
        data (str): Código fonte a ser analisado.

        Retorna:
        A análise sintática do código fonte, de acordo com as regras definidas.
        """
        self.lexer.input(data)
        return self.parser.parse(lexer=self.lexer.lexer)

def p_error(p):
    """
    Função de tratamento de erros sintáticos. 

    Parâmetros:
    p: Token onde o erro ocorreu.

    Imprime a mensagem de erro com o valor e a linha do token onde o erro ocorreu.
    Se p for None, indica que o erro ocorreu no final do arquivo.
    """
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")
