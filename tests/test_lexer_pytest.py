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
    assert tokens[1].type == 'MAIN'       # main
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

def test_case1():
    lexer = Lexer()
    test_file_path = TEST_FILES_PATH + 'test_case1.c'
    with open(test_file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        lexer.input(code)
        
    # A lista de tipos de tokens esperados para esse caso de teste
    expected_tokens_types = [
        'INT', 'MAIN', 'LPAREN', 'RPAREN', 'LBRACE',
        'INT', 'ID', 'EQUALS', 'INTEGER', 'SEMICOLON',
        'INT', 'ID', 'EQUALS', 'INTEGER', 'SEMICOLON',
        'IF', 'LPAREN', 'ID', 'LT', 'INTEGER', 'RPAREN', 'LBRACE',
        'ID', 'EQUALS', 'INTEGER', 'SEMICOLON', 'RBRACE',
        'ELSE', 'LBRACE', 'IF', 'LPAREN', 'ID', 'LE', 'INTEGER', 'RPAREN', 'LBRACE',
        'ID', 'EQUALS', 'INTEGER', 'SEMICOLON', 'RBRACE', 'ELSE', 'LBRACE',
        'ID', 'EQUALS', 'INTEGER', 'SEMICOLON', 'RBRACE', 'RBRACE', 'RBRACE'
    ]
    
    # Gerar a lista de tokens
    tokens = list(lexer.tokenize())
    
    # Realizar as verificações
    for tipo_esperado, token in zip(expected_tokens_types, tokens):
        assert token.type == tipo_esperado, f"Esperado {tipo_esperado}, obtido {token.type if token else 'None'}"
    
    # Verifica se todos os tokens esperados foram encontrados
    assert len(tokens) == len(expected_tokens_types), f"Número de tokens esperados {len(expected_tokens_types)}, mas obtido {len(tokens)}"
    
    # Após a lista de tokens esperados, não deve haver mais tokens
    assert lexer.token() is None, "Tokens extras encontrados após os esperados."

def test_case2():
    lexer = Lexer()
    test_file_path = TEST_FILES_PATH + 'test_case2.c'
    with open(test_file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        lexer.input(code)
        
            # A lista de tipos de tokens esperados para esse caso de teste
    expected_tokens_types = [
        'INT', 'MAIN', 'LPAREN', 'RPAREN', 'LBRACE',
        'INT', 'ID', 'EQUALS', 'INTEGER', 'SEMICOLON',
        'FLOAT', 'ID', 'EQUALS', 'FLOAT_N', 'SEMICOLON',
        'WHILE', 'LPAREN', 'ID', 'GT', 'INTEGER', 'RPAREN', 'LBRACE',
        'ID', 'LPAREN', 'RPAREN', 'SEMICOLON',
        'RBRACE', 'RBRACE', 'SEMICOLON'
    ]
    
    # Gerar a lista de tokens
    tokens = list(lexer.tokenize())
    
    # Realizar as verificações
    for expected_type, token in zip(expected_tokens_types, tokens):
        assert token.type == expected_type, f"Esperado {expected_type}, obtido {token.type if token else 'Nenhum'}"
    
    # Verifica se todos os tokens esperados foram encontrados
    assert len(tokens) == len(expected_tokens_types), f"Número de tokens esperado {len(expected_tokens_types)}, mas obtido {len(tokens)}"
    
    # Após a lista de tokens esperados, não deve haver mais tokens
    assert lexer.token() is None, "Tokens extras encontrados após os esperados."

def test_case3():
    lexer = Lexer()
    test_file_path = TEST_FILES_PATH + 'test_case3.c'
    with open(test_file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        lexer.input(code)
    
    expected_tokens_types = [
        'INT', 'MAIN', 'LPAREN', 'RPAREN', 'LBRACE',
        'INT', 'ID', 'EQUALS', 'INTEGER', 'SEMICOLON',
        'INT', 'ID', 'EQUALS', 'INTEGER', 'SEMICOLON',
        'WHILE', 'LPAREN', 'ID', 'LE', 'INTEGER', 'RPAREN', 'LBRACE',
        'ID', 'EQUALS', 'ID', 'PLUS', 'INTEGER', 'SEMICOLON',
        'RBRACE', 'RBRACE'
    ]
    
    tokens = list(lexer.tokenize())
    
    # Realizar as verificações
    for expected_type, token in zip(expected_tokens_types, tokens):
        assert token.type == expected_type, f"Esperado {expected_type}, obtido {token.type if token else 'Nenhum'}"
    
    # Verifica se todos os tokens esperados foram encontrados
    assert len(tokens) == len(expected_tokens_types), f"Número de tokens esperado {len(expected_tokens_types)}, mas obtido {len(tokens)}"
    
    # Após a lista de tokens esperados, não deve haver mais tokens
    assert lexer.token() is None, "Tokens extras encontrados após os esperados."

def test_case4():
    lexer = Lexer()
    test_file_path = TEST_FILES_PATH + 'test_case4.c'
    with open(test_file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        lexer.input(code)
    
    expected_tokens_types = [
        'INCLUDE', 'LIBRARY',
        'VOID', 'ID', 'LPAREN', 'RPAREN', 'LBRACE',
        'ID', 'LPAREN', 'STRING', 'RPAREN', 'SEMICOLON', 'RBRACE',
        'INT', 'ID', 'LPAREN', 'INT', 'ID', 'COMMA', 'INT', 'ID', 'RPAREN', 'LBRACE',
        'RETURN', 'ID', 'PLUS', 'ID', 'SEMICOLON', 'RBRACE',
        'INT', 'MAIN', 'LPAREN', 'RPAREN', 'LBRACE',
        'INT', 'ID', 'EQUALS', 'ID', 'LPAREN', 'INTEGER', 'COMMA', 'INTEGER', 'RPAREN', 'SEMICOLON',
        'IF', 'LPAREN', 'ID', 'GT', 'INTEGER', 'RPAREN', 'LBRACE',
        'ID', 'LPAREN', 'RPAREN', 'SEMICOLON', 'RBRACE',
        'RETURN', 'INTEGER', 'SEMICOLON', 'RBRACE'
    ]
    
    tokens = list(lexer.tokenize())
    
    # Realizar as verificações
    for expected_type, token in zip(expected_tokens_types, tokens):
        assert token.type == expected_type, f"Esperado {expected_type}, obtido {token.type if token else 'Nenhum'}"
    
    # Verifica se todos os tokens esperados foram encontrados
    assert len(tokens) == len(expected_tokens_types), f"Número de tokens esperado {len(expected_tokens_types)}, mas obtido {len(tokens)}"
    
    # Após a lista de tokens esperados, não deve haver mais tokens
    assert lexer.token() is None, "Tokens extras encontrados após os esperados."

def test_case5():
    lexer = Lexer()
    test_file_path = TEST_FILES_PATH + 'test_case5.c'
    with open(test_file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        lexer.input(code)
    
    expected_tokens_types = [
        'INCLUDE', 'LIBRARY',
        'INCLUDE', 'LIBRARY',
        'DEFINE', 'ID', 'INTEGER', 
        'TYPEDEF', 'STRUCT', 'LBRACE', 
        'FLOAT', 'ID', 'SEMICOLON', 'FLOAT', 'ID', 'SEMICOLON', 'RBRACE', 'ID', 'SEMICOLON', 
        'FLOAT', 'ID', 'LPAREN', 'ID', 'ID', 'COMMA', 'ID', 'ID', 'RPAREN', 'LBRACE', 
        'FLOAT', 'ID', 'EQUALS', 'ID', 'DOT', 'ID', 'MINUS', 'ID', 'DOT', 'ID', 'SEMICOLON', 
        'FLOAT', 'ID', 'EQUALS', 'ID', 'DOT', 'ID', 'MINUS', 'ID', 'DOT', 'ID', 'SEMICOLON', 
        'RETURN', 'ID', 'LPAREN', 'ID', 'TIMES', 'ID', 'PLUS', 'ID', 'TIMES', 'ID', 'RPAREN', 'SEMICOLON', 'RBRACE', 
        'INT', 'MAIN', 'LPAREN', 'RPAREN', 'LBRACE', 
        'ID', 'ID', 'EQUALS', 'LBRACE', 'FLOAT_N', 'COMMA', 'FLOAT_N', 'RBRACE', 'SEMICOLON', 
        'ID', 'ID', 'EQUALS', 'LBRACE', 'FLOAT_N', 'COMMA', 'FLOAT_N', 'RBRACE', 'SEMICOLON', 
        'FLOAT', 'ID', 'EQUALS', 'ID', 'LPAREN', 'ID', 'COMMA', 'ID', 'RPAREN', 'SEMICOLON', 
        'ID', 'LPAREN', 'STRING', 'COMMA', 'ID', 'RPAREN', 'SEMICOLON', 
        'FOR', 'LPAREN', 'INT', 'ID', 'EQUALS', 'INTEGER', 'SEMICOLON', 'ID', 'LT', 'ID', 'SEMICOLON', 'ID', 'PLUS', 'PLUS', 'RPAREN', 'LBRACE', 
        'IF', 'LPAREN', 'ID', 'MOD', 'INTEGER', 'COMPARATOR', 'INTEGER', 'RPAREN', 'LBRACE', 
        'ID', 'LPAREN', 'STRING', 'COMMA', 'ID', 'RPAREN', 'SEMICOLON', 'RBRACE', 
        'ELSE', 'LBRACE', 'ID', 'LPAREN', 'STRING', 'COMMA', 'ID', 'RPAREN', 'SEMICOLON', 'RBRACE', 'RBRACE', 
        'INT', 'ID', 'EQUALS', 'INTEGER', 'SEMICOLON', 
        'ID', 'PLUS', 'PLUS', 'SEMICOLON', 
        'ID', 'MINUS', 'MINUS', 'SEMICOLON', 
        'RETURN', 'INTEGER', 'SEMICOLON', 'RBRACE'
    ]
    
    tokens = list(lexer.tokenize())
    
    # Realizar as verificações
    for expected_type, token in zip(expected_tokens_types, tokens):
        assert token.type == expected_type, f"Esperado {expected_type}, obtido {token.type if token else 'Nenhum'}"
    
    # Verifica se todos os tokens esperados foram encontrados
    assert len(tokens) == len(expected_tokens_types), f"Número de tokens esperado {len(expected_tokens_types)}, mas obtido {len(tokens)}"
    
    # Após a lista de tokens esperados, não deve haver mais tokens
    assert lexer.token() is None, "Tokens extras encontrados após os esperados."
