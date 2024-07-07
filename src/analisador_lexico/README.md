### Versão em Português

# Analisador Léxico

## Descrição

O analisador léxico é a primeira fase de um compilador. Sua função é ler o código fonte, reconhecer os padrões lexicais e gerar uma sequência de tokens. Cada token representa uma unidade léxica do código, como palavras-chave, identificadores, operadores, literais e símbolos de pontuação.

## Estrutura do Projeto

O projeto do analisador léxico está organizado em dois arquivos principais:

1. **token_rules.py**: Define as regras dos tokens e a lógica para a criação dos mesmos.
2. **lexer.py**: Configura o lexer utilizando as regras definidas e fornece métodos para a análise léxica.

## token_rules.py

Este arquivo contém a classe `TokenRules`, que define as regras para a criação de tokens.

### Principais Componentes

- **Palavras Reservadas**: Um dicionário que mapeia palavras-chave para seus respectivos tokens.
- **Lista de Tokens**: Uma lista que inclui todos os tokens possíveis, combinando palavras reservadas e tokens adicionais.
- **Definições de Tokens**: Métodos e expressões regulares que definem como identificar cada tipo de token no código fonte.

### Exemplo de Palavras Reservadas

```python
self.reserved = {
    'if' : 'IF',
    'do' : 'DO',
    'int' : 'INT',
    'for' : 'FOR',
    'else' : 'ELSE',
    # ... outras palavras reservadas
}
```

### Exemplo de Definições de Tokens

```python
# Ignora espaços em branco e tabulações
t_ignore = ' \t'

# Define novas linhas
def t_NEWLINE(self, t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define o identificador
def t_ID(self, t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = self.reserved.get(t.value,'ID')
    return t

# Define o token de número flutuante
def t_FLOAT_N(self, t):
    r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
    t.value = float(t.value)
    return t

# ... outras definições de tokens
```

## lexer.py

Este arquivo contém a classe `Lexer`, que configura o lexer utilizando as regras definidas em `TokenRules`.

### Principais Componentes

- **Inicialização**: Configura o lexer utilizando as regras definidas na classe `TokenRules`.
- **Métodos de Entrada e Tokenização**: Métodos para fornecer o código fonte ao lexer e para gerar a sequência de tokens.

### Exemplo de Inicialização

```python
from ply import lex
from .token_rules import TokenRules

class Lexer:
    def __init__(self):
        self.token_rules = TokenRules()
        self.lexer = lex.lex(module=self.token_rules)
```

### Exemplo de Método de Tokenização

```python
def tokenize(self):
    while True:
        tok = self.token()
        if not tok:
            break
        yield tok
```

### Exemplo de Saída

Ao executar o analisador léxico, você verá uma saída semelhante a esta, onde cada token identificado no código fonte é impresso:

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
```

---

### English Version

# Lexical Analyzer

## Description

The lexical analyzer is the first phase of a compiler. Its function is to read the source code, recognize lexical patterns, and generate a sequence of tokens. Each token represents a lexical unit of the code, such as keywords, identifiers, operators, literals, and punctuation symbols.

## Project Structure

The lexical analyzer project is organized into two main files:

1. **token_rules.py**: Defines the rules for tokens and the logic for creating them.
2. **lexer.py**: Configures the lexer using the defined rules and provides methods for lexical analysis.

## token_rules.py

This file contains the `TokenRules` class, which defines the rules for creating tokens.

### Main Components

- **Reserved Words**: A dictionary that maps keywords to their respective tokens.
- **Token List**: A list that includes all possible tokens, combining reserved words and additional tokens.
- **Token Definitions**: Methods and regular expressions that define how to identify each type of token in the source code.

### Example of Reserved Words

```python
self.reserved = {
    'if' : 'IF',
    'do' : 'DO',
    'int' : 'INT',
    'for' : 'FOR',
    'else' : 'ELSE',
    # ... other reserved words
}
```

### Example of Token Definitions

```python
# Ignore whitespace and tabs
t_ignore = ' \t'

# Define newlines
def t_NEWLINE(self, t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define the identifier
def t_ID(self, t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = self.reserved.get(t.value,'ID')
    return t

# Define the floating-point number token
def t_FLOAT_N(self, t):
    r'((\d*\.\d+)(E[\+-]?\

d+)?|([1-9]\d*E[\+-]?\d+))'
    t.value = float(t.value)
    return t

# ... other token definitions
```

## lexer.py

This file contains the `Lexer` class, which configures the lexer using the rules defined in `TokenRules`.

### Main Components

- **Initialization**: Configures the lexer using the rules defined in the `TokenRules` class.
- **Input and Tokenization Methods**: Methods to provide the source code to the lexer and to generate the sequence of tokens.

### Example of Initialization

```python
from ply import lex
from .token_rules import TokenRules

class Lexer:
    def __init__(self):
        self.token_rules = TokenRules()
        self.lexer = lex.lex(module=self.token_rules)
```

### Example of Tokenization Method

```python
def tokenize(self):
    while True:
        tok = self.token()
        if not tok:
            break
        yield tok
```

### Example of Output

When running the lexical analyzer, you will see an output similar to this, where each token identified in the source code is printed:

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
```
