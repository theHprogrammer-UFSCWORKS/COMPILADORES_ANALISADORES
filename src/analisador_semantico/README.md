### Versão em Português

# Analisador Semântico

## Descrição

O analisador semântico é responsável por verificar a consistência semântica do código fonte, ou seja, validar regras de contexto que não são verificáveis apenas pela sintaxe. Ele garante que as variáveis sejam declaradas antes de serem usadas, verifica a compatibilidade de tipos em operações e atribuições, e gerencia os escopos de variáveis.

## Estrutura do Projeto

O projeto do analisador semântico está organizado em três arquivos principais:

1. **semantic_rules.py**: Define a tabela de símbolos e suas operações.
2. **semantic_parser.py**: Configura o parser para a análise semântica.
3. **semantic_actions.py**: Define as regras gramaticais e as ações semânticas.

### Regras Semânticas Implementadas

- [x] Declarações de variáveis
- [x] Compatibilidade de tipos em atribuições
- [x] Compatibilidade de tipos em operações aritméticas e lógicas
- [x] Verificação de declaração de funções
- [ ] Próximas regras implementadas

## semantic_rules.py

Este arquivo contém a classe `SymbolTable`, que gerencia as variáveis e seus escopos dentro do programa.

### Principais Componentes

| Componente                | Descrição                                                                 |
|---------------------------|---------------------------------------------------------------------------|
| `global_scope`            | Gerencia as variáveis no escopo global.                                    |
| `local_scope_stack`       | Pilha que gerencia os escopos locais.                                      |
| `standard_functions`      | Conjunto de funções padrão reconhecidas pelo compilador (por exemplo, `printf`, `scanf`). |
| `enter_scope`             | Entra em um novo escopo local.                                             |
| `exit_scope`              | Sai do escopo local atual.                                                 |
| `add`                     | Adiciona uma nova variável à tabela de símbolos no escopo atual.            |
| `lookup`                  | Procura uma variável na tabela de símbolos, começando pelo escopo mais interno até o global. |
| `__str__`                 | Retorna uma representação em string do escopo global da tabela de símbolos. |

## semantic_parser.py

Este arquivo contém a classe `SemanticParser`, que configura o parser para a análise semântica.

### Principais Componentes

| Componente      | Descrição                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------|
| `__init__`      | Inicializa a classe, cria instâncias de `Lexer` e `SemanticGrammarRules`, e configura o parser. |
| `parse`         | Método para analisar semanticamente o código fonte fornecido.                             |
| `p_error`       | Função de tratamento de erros sintáticos.                                                  |

## semantic_actions.py

Este arquivo contém a classe `SemanticGrammarRules`, que define as regras gramaticais e as ações semânticas.

### Tabela de Regras Semânticas

| Regra Semântica           | Descrição                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------|
| `p_function`              | Adiciona a função à tabela de símbolos e entra em um novo escopo.                           |
| `p_main_function`         | Adiciona a função `main` à tabela de símbolos e entra em um novo escopo.                    |
| `p_parameter`             | Adiciona o parâmetro da função à tabela de símbolos.                                        |
| `p_compound_statement`    | Entra em um novo escopo ao reconhecer um bloco de código e sai do escopo ao final.          |
| `p_declaration`           | Adiciona a variável declarada à tabela de símbolos.                                         |
| `p_struct_declaration`    | Adiciona a estrutura e seus membros à tabela de símbolos.                                   |
| `p_assignment`            | Verifica a compatibilidade de tipos na instrução de atribuição.                            |
| `p_expression`            | Verifica a compatibilidade de tipos em operações aritméticas e lógicas.                    |
| `p_term`                  | Verifica a compatibilidade de tipos em termos de uma expressão aritmética.                 |
| `p_function_call`         | Verifica se a função chamada foi declarada.                                                 |

### Explicação Detalhada das Implementações

- **p_function**:
  - Adiciona a função à tabela de símbolos.
  - Entra em um novo escopo ao iniciar a definição da função.
  
- **p_main_function**:
  - Adiciona a função `main` à tabela de símbolos.
  - Entra em um novo escopo ao iniciar a definição da função `main`.

- **p_parameter**:
  - Adiciona o parâmetro da função à tabela de símbolos para garantir que ele seja reconhecido dentro do escopo da função.

- **p_compound_statement**:
  - Entra em um novo escopo ao reconhecer um bloco de código delimitado por chaves `{}`.
  - Sai do escopo ao final do bloco para manter a consistência dos escopos.

- **p_declaration**:
  - Adiciona a variável declarada à tabela de símbolos, verificando se a variável já foi declarada no escopo atual para evitar redefinições.

- **p_struct_declaration**:
  - Adiciona a estrutura e seus membros à tabela de símbolos, permitindo o uso de tipos definidos pelo usuário.

- **p_assignment**:
  - Verifica a compatibilidade de tipos na instrução de atribuição para garantir que o tipo do valor atribuído seja compatível com o tipo da variável.

- **p_expression**:
  - Verifica a compatibilidade de tipos em operações aritméticas e lógicas para garantir que as operações sejam realizadas entre tipos compatíveis.

- **p_term**:
  - Verifica a compatibilidade de tipos em termos de uma expressão aritmética, garantindo que operações como multiplicação e divisão sejam realizadas entre tipos compatíveis.

- **p_function_call**:
  - Verifica se a função chamada foi declarada para garantir que apenas funções conhecidas sejam utilizadas.

## Exemplo de Saída

Ao executar o analisador semântico, você verá uma saída semelhante a esta, onde cada parte do código reconhecida e verificada semanticamente é impressa:

```
Symbol Table initialized.
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

Parsing and Semantic Analysis:
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
{'a': {'type': 'unsigned int', 'lineno': 0}, 'b': {'type': 'unsigned int', 'lineno': 0}, 'resultado': {'type': 'unsigned int', 'lineno': 0}, 'main': {'type': ' int', 'lineno': 2}}
```

---

### English Version

# Semantic Analyzer

## Description

The semantic analyzer is responsible for verifying the semantic consistency of the source code, ensuring that context-dependent rules, which cannot be checked by syntax alone, are adhered to. It ensures variables are declared before they are used, checks type compatibility in operations and assignments, and manages variable scopes.

## Project Structure

The semantic analyzer project is organized into three main files:

1. **semantic_rules.py**: Defines the symbol table and its operations.
2. **semantic_parser.py**: Configures the parser for semantic analysis.
3. **semantic_actions.py**: Defines the grammar rules and semantic actions.

### Implemented Semantic Rules

- [x] Variable declarations
- [x] Type compatibility in assignments
- [x] Type compatibility in arithmetic and logical operations
- [x] Function declaration verification
- [ ] Next implemented rules

## semantic_rules.py

This file contains the `SymbolTable` class, which manages variables and their scopes within the program.

### Main Components

| Component                | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `global_scope`           | Manages variables in the global scope.                                       |
| `local_scope_stack`      | Stack that manages local scopes.                                             |
| `standard_functions`     | Set of standard functions recognized by the compiler (e.g., `printf`, `scanf`). |
| `enter_scope`            | Enters a new local scope.                                                    |
| `exit_scope`             | Exits the current local scope.                                               |
| `add`                    | Adds a new variable to the symbol table in the current scope.                |
| `lookup`                 | Searches for a variable in the symbol table, starting from the innermost scope to the global. |
| `__str__`                | Returns a string representation of the global scope of the symbol table.     |

## semantic_parser.py

This file contains the `SemanticParser` class, which configures the parser for semantic analysis.

### Main Components

| Component      | Description                                                                                 |
|----------------|---------------------------------------------------------------------------------------------|
| `__init__`     | Initializes the class, creates instances of `Lexer` and `SemanticGrammarRules`, and configures the parser. |
| `parse`        | Method to semantically analyze the provided source code.                                     |
| `p_error`      | Function for handling syntactic errors.                                                     |

## semantic_actions.py

This file contains the `SemanticGrammarRules` class, which defines the grammar rules and semantic actions.

### Semantic Rules Table

| Semantic Rule            | Description                                                                                   |
|--------------------------|-----------------------------------------------------------------------------------------------|
| `p_function`             | Adds the function to the symbol table and enters a new scope.                                  |
| `p_main_function`        | Adds the `main` function to the symbol table and enters a new scope.                           |
| `p_parameter`            | Adds the function parameter to the symbol table.                                               |
| `p_compound_statement`   | Enters a new scope when recognizing a block of code and exits the scope at the end.            |
| `p_declaration`          | Adds the declared variable to the symbol table.                                                |
| `p_struct_declaration`   | Adds the structure and its members to the symbol table.                                        |
| `p_assignment`           | Checks type compatibility in the assignment statement.                                         |
| `p_expression`           | Checks type compatibility in arithmetic and logical operations.                                |
| `p_term`                 | Checks type compatibility in terms of an arithmetic expression.                                |
| `p_function_call`        | Checks if the called function has been declared.                                               |

### Detailed Explanation of Implementations

- **p_function**:
  - Adds the function to the symbol table.
  - Enters a new scope at the start of the function definition.
  
- **p_main_function**:
  - Adds the `main` function to the symbol table.
  - Enters a new scope at the start of the `main` function definition.

- **p_parameter**:
  - Adds the function parameter to the symbol table to ensure it is recognized within the function's scope.

- **p_compound_statement**:
  - Enters a new scope when recognizing a block of code enclosed by `{}`.
  - Exits the scope at the end of the block to maintain scope consistency.

- **p_declaration**:
  - Adds the declared variable to the symbol table, checking if the variable has already been declared in the current scope to avoid redeclarations.

- **p_struct_declaration**:
  - Adds the structure and its members to the symbol table, allowing the use of user-defined types.

- **p_assignment**:
  - Checks type compatibility in the assignment statement to ensure the type of the assigned value is compatible with the variable's type.

- **p_expression**:
  - Checks type compatibility in arithmetic and logical operations to ensure operations are performed between compatible types.

- **p_term**:
  - Checks type compatibility in terms of an arithmetic expression, ensuring operations like multiplication and division are performed between compatible types.

- **p_function_call**:
  - Checks if the called function has been declared to ensure only known functions are used.

## Example Output

When running the semantic analyzer, you will see an output similar to this, where each recognized and semantically verified part of the code is printed:

```
Symbol Table initialized.
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

Parsing and Semantic Analysis:
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
{'a': {'type': 'unsigned int', 'lineno': 0}, 'b': {'type': 'unsigned int', 'lineno': 0}, 'resultado': {'type': 'unsigned int', 'lineno': 0}, 'main': {'type': ' int', 'lineno': 2}}
```