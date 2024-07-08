### Versão em Português

# Analisador Sintático

## Descrição

O analisador sintático, também conhecido como parser, é responsável por analisar a estrutura gramatical do código fonte, validando se a sequência de tokens gerada pelo analisador léxico segue as regras gramaticais definidas para a linguagem. Ele constrói uma árvore sintática abstrata (AST) ou realiza ações baseadas na gramática para posterior análise semântica e geração de código.

## Estrutura do Projeto

O projeto do analisador sintático está organizado em dois arquivos principais:

1. **grammar_rules.py**: Define as regras gramaticais da linguagem, incluindo a precedência dos operadores e as ações associadas a cada regra.
2. **parser.py**: Configura o parser utilizando as regras definidas e fornece métodos para a análise sintática.

## grammar_rules.py

Este arquivo contém a classe `GrammarRules`, que define as regras gramaticais para a análise sintática.

### Principais Componentes

- **Tokens**: Lista de tokens utilizados nas regras gramaticais.
- **Precedência dos Operadores**: Tupla que define a precedência e associatividade dos operadores.
- **Regras Gramaticais**: Métodos que definem as produções da gramática e as ações associadas.

### Tabela de Regras Gramaticais

| Regra Gramatical                       | Descrição                                                                                          |
|----------------------------------------|----------------------------------------------------------------------------------------------------|
| `program`                              | Reconhece um programa completo, incluindo diretivas do pré-processador, declarações e funções.      |
| `optional_preprocessor_directives`     | Reconhece diretivas do pré-processador opcionais ou nenhuma diretiva.                              |
| `preprocessor_directive_list`          | Reconhece uma lista de diretivas do pré-processador.                                               |
| `preprocessor_directive`               | Reconhece uma única diretiva do pré-processador, como `include` ou `define`.                       |
| `include_directive`                    | Reconhece uma diretiva `include`.                                                                  |
| `define_directive`                     | Reconhece uma diretiva `define`.                                                                   |
| `optional_declaration_list`            | Reconhece uma lista opcional de declarações ou nenhuma declaração.                                 |
| `declaration_list`                     | Reconhece uma lista de declarações.                                                                |
| `function_list`                        | Reconhece uma lista de funções.                                                                    |
| `function`                             | Reconhece uma definição de função, incluindo a função principal `main`.                            |
| `main_function`                        | Reconhece a definição da função principal `main`.                                                  |
| `parameter_list`                       | Reconhece uma lista de parâmetros de função.                                                       |
| `parameter`                            | Reconhece um parâmetro de função.                                                                  |
| `compound_statement`                   | Reconhece um bloco de código delimitado por chaves `{}`.                                           |
| `statement_list`                       | Reconhece uma lista de instruções.                                                                 |
| `statement`                            | Reconhece uma única instrução, que pode ser de diversos tipos (declaração, atribuição, controle de fluxo, etc.). |
| `declaration`                          | Reconhece uma declaração de variável, typedef ou struct.                                           |
| `typedef_declaration`                  | Reconhece uma declaração `typedef`.                                                                |
| `struct_declaration`                   | Reconhece uma declaração de estrutura.                                                             |
| `struct_members`                       | Reconhece uma lista de membros de uma estrutura.                                                   |
| `struct_member`                        | Reconhece um único membro de uma estrutura.                                                        |
| `optional_id`                          | Reconhece um identificador opcional ou nenhum identificador.                                       |
| `init_declarator_list`                 | Reconhece uma lista de inicializadores de declaradores.                                            |
| `init_declarator`                      | Reconhece um inicializador de declarador.                                                          |
| `initializer_list`                     | Reconhece uma lista de inicializadores.                                                            |
| `type_specifier`                       | Reconhece um especificador de tipo.                                                                |
| `non_empty_pre_type_specifier`         | Reconhece um especificador de tipo não vazio.                                                      |
| `base_type`                            | Reconhece um tipo base (`int`, `char`, `float`, etc.).                                             |
| `pre_type_specifier`                   | Reconhece um especificador de tipo prévio (`const`, `volatile`, etc.).                             |
| `assignment`                           | Reconhece uma instrução de atribuição.                                                             |
| `expression`                           | Reconhece uma expressão, incluindo operações aritméticas e lógicas.                                |
| `term`                                 | Reconhece um termo em uma expressão aritmética.                                                    |
| `factor`                               | Reconhece um fator em uma expressão, como um número ou uma variável.                               |
| `if_statement`                         | Reconhece uma instrução `if` (condicional).                                                        |
| `while_statement`                      | Reconhece uma instrução `while` (laço de repetição).                                               |
| `do_while_statement`                   | Reconhece uma instrução `do-while` (laço de repetição).                                            |
| `for_statement`                        | Reconhece uma instrução `for` (laço de repetição).                                                 |
| `switch_statement`                     | Reconhece uma instrução `switch` (seleção múltipla).                                               |
| `case_list`                            | Reconhece uma lista de casos em uma instrução `switch`.                                            |
| `case`                                 | Reconhece um caso em uma instrução `switch`.                                                       |
| `default_case`                         | Reconhece o caso padrão em uma instrução `switch`.                                                 |
| `break_statement`                      | Reconhece uma instrução `break`.                                                                   |
| `continue_statement`                   | Reconhece uma instrução `continue`.                                                                |
| `return_statement`                     | Reconhece uma instrução `return`.                                                                  |
| `function_call`                        | Reconhece uma chamada de função.                                                                   |
| `argument_list`                        | Reconhece uma lista de argumentos em uma chamada de função.                                        |
| `empty`                                | Reconhece uma produção vazia.                                                                      |
| `p_error`                              | Função de tratamento de erros sintáticos.                                                          |

### Exemplo de Definição de Tokens

```python
from ..analisador_lexico.lexer import Lexer

class GrammarRules:
    tokens = Lexer().token_rules.tokens
```

### Exemplo de Precedência dos Operadores

```python
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'BITWISE_OR'),
    ('left', 'BITWISE_XOR'),
    ('left', 'BITWISE_AND'),
    ('left', 'COMPARATOR', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'LSHIFT', 'RSHIFT'),
    ('right', 'INCREMENT', 'DECREMENT'),
    ('right', 'DOT'),
)
```

### Exemplo de Regras Gramaticais

```python
def p_program(self, p):
    '''program : optional_preprocessor_directives optional_declaration_list function_list'''
    print("program recognized")
```

## parser.py

Este arquivo contém a classe `Parser`, que configura o parser utilizando as regras definidas em `GrammarRules`.

### Principais Componentes

- **Inicialização**: Configura o lexer e o parser utilizando as regras definidas nas classes `Lexer` e `GrammarRules`.
- **Método de Análise Sintática**: Método que recebe o código fonte e executa a análise sintática, retornando a árvore sintática ou realizando as ações definidas.

### Exemplo de Inicialização

```python
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
        self.lexer = Lexer()  # Instancia o analisador léxico
        self.grammar = GrammarRules()  # Instancia as regras gramaticais
        self.tokens = self.lexer.token_rules.tokens  # Obtém os tokens definidos no analisador léxico
        self.parser = yacc.yacc(module=self.grammar)  # Cria o parser com base nas regras gramaticais
```

### Exemplo de Método de Análise Sintática

```python
    def parse(self, data):
        """
        Método para analisar o código fonte fornecido.

        Parâmetros:
        data (str): Código fonte a ser analisado.

        Retorna:
        A análise sintática do código fonte, de acordo com as regras definidas.
        """
        self.lexer.input(data)  # Fornece o código fonte ao analisador léxico
        return self.parser.parse(lexer=self.lexer.lexer)  # Executa a análise sintática utilizando o lexer configurado
```

### Exemplo de Tratamento de Erros Sintáticos

```python
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
```

### Exemplo de Saída

Ao executar o analisador sintático, você verá uma saída semelhante a esta, onde cada parte do código reconhecida é impressa:

```
Tokens:
LexToken(INT,'int',2,1)
LexToken(MAIN,'main',2,5)
LexToken(LPAREN,'(',2,9)
LexToken(RPAREN,')',2,10)
LexToken(LBRACE,'{',3,12)
LexToken(UNSIGNED,'unsigned',4,18)
LexToken(INT,'int',4,27)
LexToken(ID,'a',4,31)
LexToken(COMMA,',',4,32)
LexToken(ID,'b',4,34)
LexToken(COMMA,',',4,35)
LexToken(ID,'resultado',4,37)
LexToken(SEMICOLON,';',4,46)
LexToken(ID,'a',5,52)
LexToken(EQUALS,'=',5,54)
LexToken(INTEGER,'4',5,56)
LexToken(SEMICOLON,';',5,57)
LexToken(ID,'b',6,63)
LexToken(EQUALS,'=',6,65)
LexToken(INTEGER,'6',6,67)
LexToken(SEMICOLON,';',6,68)
LexToken(IF,'if',7,74)
LexToken(LPAREN,'(',7,77)
LexToken(ID,'a',7,78)
LexToken(GE,'>=',7,80)
LexToken(INTEGER,'10',7,83)
LexToken(RPAREN,')',7,85)
LexToken(LBRACE,'{',8,91)
LexToken(ID,'resultado',9,101)
LexToken(EQUALS,'=',9,111)
LexToken(ID,'a',9,113)
LexToken(MINUS,'-',9,115)
LexToken(ID,'b',9,117)
LexToken(SEMICOLON,';',9,118)
LexToken(RBRACE,'}',10,124)
LexToken(ELSE,'else',11,130)
LexToken(LBRACE,'{',12,139)
LexToken(ID,'resultado',13,149)
LexToken(EQUALS,'=',13,159)
LexToken(ID,'a',13,161)
LexToken(PLUS,'+',13,163)
LexToken(ID,'b',13,165)
LexToken(SEMICOLON,';',13,166)
LexToken(RBRACE,'}',14,172)
LexToken(RBRACE,'}',15,174)

Parsing:
optional preprocessor directives recognized
empty declaration list recognized
optional declaration list recognized
pre-type specifier or empty recognized
non-empty pre-type specifier recognized
base type recognized
complex type specifier recognized
pre-type specifier or empty recognized
non-empty pre-type specifier recognized
base type recognized
complex type specifier recognized
init declarator recognized
init declarator list recognized
init declarator recognized
init declarator list recognized
init declarator recognized
init declarator list recognized
declaration recognized
statement recognized
statement list recognized
factor recognized
term recognized
expression recognized
assignment recognized
statement recognized
statement list recognized
factor recognized
term recognized
expression recognized
assignment recognized
statement recognized
statement list recognized
factor recognized
term recognized
expression recognized
factor recognized
term recognized
expression recognized
factor recognized
factor recognized
term recognized
expression recognized
factor recognized
term recognized
expression recognized
assignment recognized
statement recognized
statement list recognized
compound statement recognized
statement recognized
factor recognized
term recognized
expression recognized
factor recognized
term recognized
expression recognized
assignment recognized
statement recognized
statement list recognized
compound statement recognized
statement recognized
if statement recognized
statement recognized
statement list recognized
compound statement recognized
main function recognized
function recognized
function list recognized
program recognized
```

---

### English Version

# Syntactic Analyzer

## Description

The syntactic analyzer, also known as the parser, is responsible for analyzing the grammatical structure of the source code, validating if the sequence of tokens generated by the lexical analyzer follows the grammatical rules defined for the language. It constructs an Abstract Syntax Tree (AST) or performs actions based on the grammar for subsequent semantic analysis and code generation.

## Project Structure

The syntactic analyzer project is organized into two main files:

1. **grammar_rules.py**: Defines the grammatical rules of the language, including operator precedence and the actions associated with each rule.
2. **parser.py**: Configures the parser using the defined rules and provides methods for syntactic analysis.

## grammar_rules.py

This file contains the `GrammarRules` class, which defines the grammatical rules for syntactic analysis.

### Main Components

- **Tokens**: List of tokens used in the grammatical rules.
- **Operator Precedence**: A tuple that defines the precedence and associativity of operators.
- **Grammatical Rules**: Methods that define the grammar productions and associated actions.

### Table of Grammatical Rules

| Grammatical Rule                       | Description                                                                                          |
|----------------------------------------|------------------------------------------------------------------------------------------------------|
| `program`                              | Recognizes a complete program, including preprocessor directives, declarations, and functions.       |
| `optional_preprocessor_directives`     | Recognizes optional preprocessor directives or no directive.                                         |
| `preprocessor_directive_list`          | Recognizes a list of preprocessor directives.                                                        |
| `preprocessor_directive`               | Recognizes a single preprocessor directive, such as `include` or `define`.                           |
| `include_directive`                    | Recognizes an `include` directive.                                                                   |
| `define_directive`                     | Recognizes a `define` directive.                                                                     |
| `optional_declaration_list`            | Recognizes an optional list of declarations or no declarations.                                       |
| `declaration_list`                     | Recognizes a list of declarations.                                                                   |
| `function_list`                        | Recognizes a list of functions.                                                                      |
| `function`                             | Recognizes a function definition, including the main function `main`.                                |
| `main_function`                        | Recognizes the main function `main` definition.                                                      |
| `parameter_list`                       | Recognizes a list of function parameters.                                                            |
| `parameter`                            | Recognizes a function parameter.                                                                     |
| `compound_statement`                   | Recognizes a block of code delimited by braces `{}`.                                                 |
| `statement_list`                       | Recognizes a list of statements.                                                                     |
| `statement`                            | Recognizes a single statement, which can be of various types (declaration, assignment, control flow, etc.). |
| `declaration`                          | Recognizes a variable, typedef, or struct declaration.                                               |
| `typedef_declaration`                  | Recognizes a `typedef` declaration.                                                                  |
| `struct_declaration`                   | Recognizes a struct declaration.                                                                     |
| `struct_members`                       | Recognizes a list of struct members.                                                                 |
| `struct_member`                        | Recognizes a single struct member.                                                                   |
| `optional_id`                          | Recognizes an optional identifier or no identifier.                                                  |
| `init_declarator_list`                 | Recognizes a list of initializer declarators.                                                        |
| `init_declarator`                      | Recognizes an initializer declarator.                                                                |
| `initializer_list`                     | Recognizes a list of initializers.                                                                   |
| `type_specifier`                       | Recognizes a type specifier.                                                                         |
| `non_empty_pre_type_specifier`         | Recognizes a non-empty pre-type specifier.                                                           |
| `base_type`                            | Recognizes a base type (`int`, `char`, `float`, etc.).                                               |
| `pre_type_specifier`                   | Recognizes a pre-type specifier (`const`, `volatile`, etc.).                                         |
| `assignment`                           | Recognizes an assignment statement.                                                                  |
| `expression`                           | Recognizes an expression, including arithmetic and logical operations.                               |
| `term`                                 | Recognizes a term in an arithmetic expression.                                                       |
| `factor`                               | Recognizes a factor in an expression, such as a number or a variable.                                |
| `if_statement`                         | Recognizes an `if` statement (conditional).                                                          |
| `while_statement`                      | Recognizes a `while` statement (loop).                                                               |
| `do_while_statement`                   | Recognizes a `do-while` statement (loop).                                                            |
| `for_statement`                        | Recognizes a `for` statement (loop).                                                                 |
| `switch_statement`                     | Recognizes a `switch` statement (multiple selection).                                                |
| `case_list`                            | Recognizes a list of cases in a `switch` statement.                                                  |
| `case`                                 | Recognizes a case in a `switch` statement.                                                           |
| `default_case`                         | Recognizes the default case in a `switch` statement.                                                 |
| `break_statement`                      | Recognizes a `break` statement.                                                                      |
| `continue_statement`                   | Recognizes a `continue` statement.                                                                   |
| `return_statement`                     | Recognizes a `return` statement.                                                                     |
| `function_call`                        | Recognizes a function call.                                                                          |
| `argument_list`                        | Recognizes a list of arguments in a function call.                                                   |
| `empty`                                | Recognizes an empty production.                                                                      |
| `p_error`                              | Function for handling syntactic errors.                                                              |

### Example of Token Definition

```python
from ..analisador_lexico.lexer import Lexer

class GrammarRules:
    tokens = Lexer().token_rules.tokens
```

### Example of Operator Precedence

```python
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'BITWISE_OR'),
    ('left', 'BITWISE_XOR'),
    ('left', 'BITWISE_AND'),
    ('left', 'COMPARATOR', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'LSHIFT', 'RSHIFT'),
    ('right', 'INCREMENT', 'DECREMENT'),
    ('right', 'DOT'),
)
```

### Example of Grammatical Rules

```python
def p_program(self, p):
    '''program : optional_preprocessor_directives optional_declaration_list function_list'''
    print("program recognized")
```

## parser.py

This file contains the `Parser` class, which configures the parser using the rules defined in `GrammarRules`.

### Main Components

- **Initialization**: Configures the lexer and parser using the rules defined in the `Lexer` and `GrammarRules` classes.
- **Syntactic Analysis Method**: A method that takes the source code and performs syntactic analysis, returning the syntax tree or performing the defined actions.

### Example of Initialization

```python
from ply import yacc
from ..analisador_lexico.lexer import Lexer
from .grammar_rules import GrammarRules

class Parser:
    """
    The Parser class configures and uses the syntactic analyzer (parser) to analyze
    the source code according to the grammatical rules defined in the GrammarRules class.
    """

    def __init__(self):
        """
        Initializes the Parser class. Creates an instance of Lexer and GrammarRules,
        configures the tokens, and creates the parser using the PLY (Python Lex-Yacc) library.
        """
        self.lexer = Lexer()  # Instantiates the lexical analyzer
        self.grammar = GrammarRules()  # Instantiates the grammatical rules
        self.tokens = self.lexer.token_rules.tokens  # Gets the tokens defined in the lexical analyzer
        self.parser = yacc.yacc(module=self.grammar)  # Creates the parser based on the grammatical rules
```

### Example of Syntactic Analysis Method

```python
    def parse(self, data):
        """
        Method to analyze the provided source code.

        Parameters:
        data (str): Source code to be analyzed.

        Returns:
        The syntactic analysis of the source code, according to the defined rules.
        """
        self.lexer.input(data)  # Provides the source code to the lexical analyzer
        return self.parser.parse(lexer=self.lexer.lexer)  # Performs the syntactic analysis using the configured lexer
```

### Example of Syntactic Error Handling

```python
def p_error(p):
    """
    Function for handling syntactic errors.

    Parameters:
    p: Token where the error occurred.

    Prints the error message with the value and line of the token where the error occurred.
    If p is None, indicates that the error occurred at the end of the file.
    """
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")
```

### Example of Output

When running the syntactic analyzer, you will see an output similar to this, where each recognized part of the code is printed:

```
Tokens:
LexToken(INT,'int',2,1)
LexToken(MAIN,'main',2,5)
LexToken(LPAREN,'(',2,9)
LexToken(RPAREN,')',2,10)
LexToken(LBRACE,'{',3,12)
LexToken(UNSIGNED,'unsigned',4,18)
LexToken(INT,'int',4,27)
LexToken(ID,'a',4,31)
LexToken(COMMA,',',4,

32)
LexToken(ID,'b',4,34)
LexToken(COMMA,',',4,35)
LexToken(ID,'resultado',4,37)
LexToken(SEMICOLON,';',4,46)
LexToken(ID,'a',5,52)
LexToken(EQUALS,'=',5,54)
LexToken(INTEGER,'4',5,56)
LexToken(SEMICOLON,';',5,57)
LexToken(ID,'b',6,63)
LexToken(EQUALS,'=',6,65)
LexToken(INTEGER,'6',6,67)
LexToken(SEMICOLON,';',6,68)
LexToken(IF,'if',7,74)
LexToken(LPAREN,'(',7,77)
LexToken(ID,'a',7,78)
LexToken(GE,'>=',7,80)
LexToken(INTEGER,'10',7,83)
LexToken(RPAREN,')',7,85)
LexToken(LBRACE,'{',8,91)
LexToken(ID,'resultado',9,101)
LexToken(EQUALS,'=',9,111)
LexToken(ID,'a',9,113)
LexToken(MINUS,'-',9,115)
LexToken(ID,'b',9,117)
LexToken(SEMICOLON,';',9,118)
LexToken(RBRACE,'}',10,124)
LexToken(ELSE,'else',11,130)
LexToken(LBRACE,'{',12,139)
LexToken(ID,'resultado',13,149)
LexToken(EQUALS,'=',13,159)
LexToken(ID,'a',13,161)
LexToken(PLUS,'+',13,163)
LexToken(ID,'b',13,165)
LexToken(SEMICOLON,';',13,166)
LexToken(RBRACE,'}',14,172)
LexToken(RBRACE,'}',15,174)

Parsing:
optional preprocessor directives recognized
empty declaration list recognized
optional declaration list recognized
pre-type specifier or empty recognized
non-empty pre-type specifier recognized
base type recognized
complex type specifier recognized
pre-type specifier or empty recognized
non-empty pre-type specifier recognized
base type recognized
complex type specifier recognized
init declarator recognized
init declarator list recognized
init declarator recognized
init declarator list recognized
init declarator recognized
init declarator list recognized
declaration recognized
statement recognized
statement list recognized
factor recognized
term recognized
expression recognized
assignment recognized
statement recognized
statement list recognized
factor recognized
term recognized
expression recognized
assignment recognized
statement recognized
statement list recognized
factor recognized
term recognized
expression recognized
factor recognized
term recognized
expression recognized
factor recognized
factor recognized
term recognized
expression recognized
factor recognized
term recognized
expression recognized
assignment recognized
statement recognized
statement list recognized
compound statement recognized
statement recognized
factor recognized
term recognized
expression recognized
factor recognized
term recognized
expression recognized
assignment recognized
statement recognized
statement list recognized
compound statement recognized
statement recognized
if statement recognized
statement recognized
statement list recognized
compound statement recognized
main function recognized
function recognized
function list recognized
program recognized
```