import os
import sys
from src.ANALISADOR_LEXICO.lexer import Lexer
from src.ANALISADOR_SINTATICO.parser import Parser

def main(file_path):
    if not os.path.exists(file_path):
        print(f"O arquivo {file_path} não foi encontrado.")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    
    lexer = Lexer()
    parser = Parser()
    
    print("Tokens:")
    lexer.input(code)
    for token in lexer.tokenize():
        print(token)
    
    print("\nParsing:")
    parser.parse(code)

if __name__ == "__main__":
    FILE_PATH = 'tests/test_case5.c'
    main(FILE_PATH)

# if __name__ == "__main__":
#     # Verifica se um caminho de arquivo foi passado como argumento da linha de comando
#     if len(sys.argv) > 1:
#         main(sys.argv[1])
#     else:
#         print("Uso: python main.py <caminho_para_o_arquivo_c>")
