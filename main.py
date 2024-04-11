import os
import sys
from ANALISADOR_LEXICO.lexer import Lexer

def main(file_path):
    if not os.path.exists(file_path):
        print(f"O arquivo {file_path} não foi encontrado.")
        return
    
    # Cria uma instância do lexer
    lexer = Lexer()
    
    # Abre o arquivo de código C e passa seu conteúdo para o lexer
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        lexer.input(code)

    # Itera sobre os tokens produzidos pelo lexer e os imprime
    for token in lexer.tokenize():
        print(token)
        
# FILE_PATH = '../COMPILADORES/tests/test_case5.c'
# main(FILE_PATH)

if __name__ == "__main__":
    # Verifica se um caminho de arquivo foi passado como argumento da linha de comando
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Uso: python main.py <caminho_para_o_arquivo_c>")
