from ANALISADOR_LEXICO.lexer import Lexer

# Caminho para os arquivos de teste
TEST_FILES_PATH = "../COMPILADORES/tests/"

def test_case0():
    lexer = Lexer()
    test_file_path = TEST_FILES_PATH + 'test_case0.c'
    with open(test_file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        lexer.input(code)

    # Gerar a lista de tokens
    tokens = list(lexer.tokenize())

    # Realizar as verificações
    assert tokens[0].type == 'INT'        # int
    assert tokens[1].type == 'ID'         # main
    assert tokens[2].type == 'LPAREN'     # (
    assert tokens[3].type == 'RPAREN'     # )
    assert tokens[4].type == 'LBRACE'     # {
    assert tokens[5].type == 'INT'        # int
    assert tokens[6].type == 'ID'         # x
    assert tokens[7].type == 'EQUALS'     # =
    assert tokens[8].type == 'INTEGER'    # 10
    assert tokens[9].type == 'SEMICOLON'  # ;
    assert tokens[10].type == 'FLOAT'     # float
    assert tokens[11].type == 'ID'        # y
    assert tokens[12].type == 'EQUALS'    # =
    assert tokens[13].type == 'FLOAT_N'   # 20.5
    assert tokens[14].type == 'SEMICOLON' # ;
    assert tokens[15].type == 'CHAR'      # char
    assert tokens[16].type == 'ID'        # z
    assert tokens[17].type == 'EQUALS'    # =
    assert tokens[18].type == 'STRING'    # 'A'
    assert tokens[19].type == 'SEMICOLON' # ;
    assert tokens[20].type == 'RETURN'    # return
    assert tokens[21].type == 'INTEGER'   # 0
    assert tokens[22].type == 'SEMICOLON' # ;
    assert tokens[23].type == 'RBRACE'    # }
    assert len(tokens) == 24
