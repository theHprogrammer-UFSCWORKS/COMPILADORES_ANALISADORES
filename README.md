### Portuguese Version

# Implementação Parcial de Compilador da Linguagem C com Python e PLY

## Sumário

1. [Descrição Geral](#descrição-geral)
2. [Configurando o Ambiente](#configurando-o-ambiente)
3. [Executando os Analisadores](#executando-os-analisadores)
   - [Executando o Analisador Léxico](#executando-o-analisador-léxico)
   - [Executando o Analisador Sintático](#executando-o-analisador-sintático)
   - [Executando o Analisador Semântico](#executando-o-analisador-semântico)
4. [Testes](#testes)
5. [Teoria e Conceitos](#teoria-e-conceitos)
   - [LALR](#lalr-lookahead-lr)
   - [S-atributos e Atributos Sintetizados](#s-atributos-e-atributos-sintetizados)

## Descrição Geral

Este projeto visa a implementação parcial de um compilador para a linguagem C utilizando Python e a biblioteca PLY (Python Lex-Yacc). Um compilador é um programa que traduz o código fonte escrito em uma linguagem de programação de alto nível (como C) para uma linguagem de máquina que pode ser executada por um computador.

### Fases de um Compilador

1. **Análise Léxica**: A primeira fase do compilador, responsável por ler o código fonte e gerar tokens. Cada token representa uma unidade léxica, como palavras-chave, identificadores, operadores e símbolos de pontuação.

2. **Análise Sintática**: A segunda fase do compilador, que verifica se a sequência de tokens segue a gramática da linguagem. Esta fase constrói a árvore sintática abstrata (AST).

3. **Análise Semântica**: A terceira fase do compilador, que verifica a consistência semântica do código. Garante que variáveis sejam declaradas antes de serem usadas, verifica a compatibilidade de tipos e gerencia os escopos.

### Leia os READMEs de Cada Analisador para Mais Detalhes

Para mais detalhes sobre a implementação e o funcionamento de cada analisador, consulte os READMEs específicos:

- [README do Analisador Léxico](src/analisador_lexico/README.md)
- [README do Analisador Sintático](src/analisador_sintatico/README.md)
- [README do Analisador Semântico](src/analisador_semantico/README.md)

## Configurando o Ambiente

Primeiramente, clone ou faça o fork do repositório e configure o ambiente virtual Python:

### Clonar o Repositório

```bash
git clone https://github.com/theHprogrammer-UFSCWORKS/compiladores-c-parcial-compiler.git
cd compiladores-c-parcial-compiler
```

### Configurar o Ambiente Virtual

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Executando os Analisadores

### Executando o Analisador Léxico

Para executar o analisador léxico em um arquivo C:

```bash
python main.py <caminho/para/arquivo.c> lexical
```

### Executando o Analisador Sintático

Para executar o analisador sintático em um arquivo C:

```bash
python main.py <caminho/para/arquivo.c> syntactic
```

### Executando o Analisador Semântico

Para executar o analisador semântico em um arquivo C:

```bash
python main.py <caminho/para/arquivo.c> semantic
```

**Nota**: O arquivo `tests/test_case5.c` está bloqueado para o modo semântico devido à complexidade parcial das declarações de estruturas, o que pode acarretar erros.

### Checklists de Implementação

#### Analisador Léxico

- [x] Identificação de palavras-chave
- [x] Identificação de identificadores
- [x] Reconhecimento de operadores
- [x] Reconhecimento de literais
- [x] Ignorar espaços e tabulações

#### Analisador Sintático

- [x] Validação de comandos de atribuição
- [x] Validação de operações aritméticas simples
- [x] Validação de estruturas condicionais (simples e aninhadas)
- [x] Validação de laços de repetição

#### Analisador Semântico

- [x] Declarações de variáveis
- [x] Compatibilidade de tipos em atribuições
- [x] Compatibilidade de tipos em operações aritméticas e lógicas
- [x] Verificação de declaração de funções

## Testes

Para realizar os testes nos analisadores, os arquivos de teste devem ser colocados dentro do diretório `tests`. Utilize o caminho do teste dentro desse diretório para executar os códigos no terminal. Por exemplo, para executar o teste no arquivo `test_case0.c`, use:

```bash
python main.py tests/test_case0.c <modo>
```

### Tabela de Testes

| Teste        | Funcionalidades Testadas                                                                 |
|--------------|------------------------------------------------------------------------------------------|
| `test_case0.c` | Declaração de variáveis (`int`, `float`, `char`), função `main`, retorno de função       |
| `test_case1.c` | Declaração de variáveis, estrutura `if-else`, estrutura `if-else` aninhada, função `main`|
| `test_case2.c` | Declaração de variáveis, comentários (`//`, `/* */`), estrutura `while`, função `main`   |
| `test_case3.c` | Declaração de variáveis, estrutura `while`, função `main`                                |
| `test_case4.c` | Inclusão de bibliotecas (`#include`), declaração e chamada de funções, estrutura `if-else`, função `main` |
| `test_case5.c` | Inclusão de bibliotecas (`#include`), definição de macros (`#define`), estruturas (`struct`), loops (`for`), incremento e decremento de variáveis (`++`, `--`), função `main` |
| `test_case6.c` | Declaração de variáveis (`unsigned int`), estrutura `if-else`, operações aritméticas (`+`, `-`), função `main` |

## Teoria e Conceitos

### LALR (Lookahead LR)

LALR (Lookahead LR) é um método eficiente de análise sintática utilizado por muitos compiladores, incluindo aqueles construídos com PLY. O método combina a capacidade de análise eficiente do LR com a compactação de estados, o que reduz a memória necessária para a tabela de análise. Isso é especialmente útil para linguagens de programação complexas, como C.

### S-atributos e Atributos Sintetizados

Em análise semântica, os atributos podem ser sintetizados ou herdados:

- **S-atributos**: São atributos sintetizados que dependem exclusivamente dos valores dos filhos do nó na árvore sintática. Eles são computados de baixo para cima na árvore.
- **Atributos Sintetizados**: São usados para passar informações de nós filhos para seus pais na árvore sintática. São fundamentais para a construção de compiladores S-atribuídos, onde todas as ações semânticas associadas às produções de uma gramática atribuem valores a atributos sintetizados.

## Estrutura de Diretórios

```plaintext
.github/
.venv/
src/
├── analisador_lexico/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── lexer.py
│   ├── README.md
│   ├── token_rules.py
├── analisador_semantico/
│   ├── __pycache__/
│   ├── parsetab.py
│   ├── README.md
│   ├── semantic_actions.py
│   ├── semantic_parser.py
│   ├── semantic_rules.py
├── analisador_sintatico/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── grammar_rules.py
│   ├── parser.py
│   ├── parsetab.py
│   ├── README.md
template/
├── exemplo_lex.py
├── exemplo_sint_sem.py
tests/
├── __init__.py
├── test_case0.c
├── test_case1.c
├── test_case2.c
├── test_case3.c
├── test_case4.c
├── test_case5.c
├── test_case6.c
.gitignore
.pre-commit-config.yaml
.pylintrc
.tool-versions
CONTRIBUTING.md
LICENSE.md
README.md
main.py
requirements.txt
```

## Contribuindo

Contribuições para o analisador são bem-vindas. Por favor, leia `CONTRIBUTING.md` para detalhes sobre nosso código de conduta e o processo de submissão de pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE.md` para detalhes.

## Autor

<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/theHprogrammer">
                <img src="https://avatars.githubusercontent.com/u/79870881?v=4" width="150px;" alt="Helder's Image" />
                <br />
                <sub><b>Helder Henrique</b></sub>
            </a>
        </td>    
    </tr>
</table>
<h4 align="center">
   By: <a href="https://www.linkedin.com/in/theHprogrammer/" target="_blank"> Helder Henrique </a>
</h4>

---

### English Version

# Partial Implementation of a C Language Compiler with Python and PLY

## Table of Contents

1. [General Description](#general-description)
2. [Setting Up the Environment](#setting-up-the-environment)
3. [Running the Analyzers](#running-the-analyzers)
   - [Running the Lexical Analyzer](#running-the-lexical-analyzer)
   - [Running the Syntactic Analyzer](#running-the-syntactic-analyzer)
   - [Running the Semantic Analyzer](#running-the-semantic-analyzer)
4. - [Tests](#tests)
5. [Theory and Concepts](#theory-and-concepts)
   - [LALR](#lalr-lookahead-lr)
   - [S-attributes and Synthesized Attributes](#s-attributes-and-synthesized-attributes)

## General Description

This project aims to partially implement a compiler for the C language using Python and the PLY (Python Lex-Yacc) library. A compiler is a program that translates source code written in a high-level programming language (such as C) into machine language that

 can be executed by a computer.

### Compiler Phases

1. **Lexical Analysis**: The first phase of the compiler, responsible for reading the source code and generating tokens. Each token represents a lexical unit such as keywords, identifiers, operators, and punctuation symbols.

2. **Syntactic Analysis**: The second phase of the compiler, which verifies if the sequence of tokens follows the grammar of the language. This phase constructs the abstract syntax tree (AST).

3. **Semantic Analysis**: The third phase of the compiler, which checks the semantic consistency of the code. It ensures that variables are declared before being used, checks type compatibility, and manages scopes.

### Read the READMEs of Each Analyzer for More Details

For more details on the implementation and functioning of each analyzer, refer to the specific READMEs:

- [README of the Lexical Analyzer](src/analisador_lexico/README.md)
- [README of the Syntactic Analyzer](src/analisador_sintatico/README.md)
- [README of the Semantic Analyzer](src/analisador_semantico/README.md)

## Setting Up the Environment

First, clone or fork the repository and set up the Python virtual environment:

### Clone the Repository

```bash
git clone https://github.com/theHprogrammer-UFSCWORKS/compiladores-c-parcial-compiler.git
cd compiladores-c-parcial-compiler
```

### Set Up the Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Analyzers

### Running the Lexical Analyzer

To run the lexical analyzer on a C file:

```bash
python main.py <path/to/file.c> lexical
```

### Running the Syntactic Analyzer

To run the syntactic analyzer on a C file:

```bash
python main.py <path/to/file.c> syntactic
```

### Running the Semantic Analyzer

To run the semantic analyzer on a C file:

```bash
python main.py <path/to/file.c> semantic
```

**Note**: The file `tests/test_case5.c` is blocked for the semantic mode due to the partial complexity of structure declarations, which may cause errors.

### Implementation Checklists

#### Lexical Analyzer

- [x] Keyword identification
- [x] Identifier identification
- [x] Operator recognition
- [x] Literal recognition
- [x] Ignore spaces and tabs

#### Syntactic Analyzer

- [x] Validation of assignment commands
- [x] Validation of simple arithmetic operations
- [x] Validation of conditional structures (simple and nested)
- [x] Validation of loops

#### Semantic Analyzer

- [x] Variable declarations
- [x] Type compatibility in assignments
- [x] Type compatibility in arithmetic and logical operations
- [x] Function declaration verification

## Tests

To run tests on the analyzers, the test files should be placed inside the `tests` directory. Use the path of the test within this directory to run the codes in the terminal. For example, to run the test on the file `test_case0.c`, use:

```bash
python main.py tests/test_case0.c <mode>
```

### Test Table

| Test        | Features Tested                                                                       |
|-------------|---------------------------------------------------------------------------------------|
| `test_case0.c` | Variable declaration (`int`, `float`, `char`), `main` function, function return       |
| `test_case1.c` | Variable declaration, `if-else` structure, nested `if-else` structure, `main` function |
| `test_case2.c` | Variable declaration, comments (`//`, `/* */`), `while` structure, `main` function    |
| `test_case3.c` | Variable declaration, `while` structure, `main` function                             |
| `test_case4.c` | Library inclusion (`#include`), function declaration and call, `if-else` structure, `main` function |
| `test_case5.c` | Library inclusion (`#include`), macro definitions (`#define`), structures (`struct`), loops (`for`), variable increment and decrement (`++`, `--`), `main` function |
| `test_case6.c` | Variable declaration (`unsigned int`), `if-else` structure, arithmetic operations (`+`, `-`), `main` function |

## Theory and Concepts

### LALR (Lookahead LR)

LALR (Lookahead LR) is an efficient syntactic analysis method used by many compilers, including those built with PLY. The method combines the efficient parsing capability of LR with state compression, reducing the memory required for the parsing table. This is especially useful for complex programming languages like C.

### S-attributes and Synthesized Attributes

In semantic analysis, attributes can be synthesized or inherited:

- **S-attributes**: These are synthesized attributes that depend exclusively on the values of the children nodes in the syntax tree. They are computed bottom-up in the tree.
- **Synthesized Attributes**: These are used to pass information from child nodes to their parents in the syntax tree. They are fundamental for constructing S-attributed compilers, where all semantic actions associated with grammar productions assign values to synthesized attributes.

## Directory Structure

```plaintext
.github/
.venv/
src/
├── analisador_lexico/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── lexer.py
│   ├── README.md
│   ├── token_rules.py
├── analisador_semantico/
│   ├── __pycache__/
│   ├── parsetab.py
│   ├── README.md
│   ├── semantic_actions.py
│   ├── semantic_parser.py
│   ├── semantic_rules.py
├── analisador_sintatico/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── grammar_rules.py
│   ├── parser.py
│   ├── parsetab.py
│   ├── README.md
template/
├── exemplo_lex.py
├── exemplo_sint_sem.py
tests/
├── __init__.py
├── test_case0.c
├── test_case1.c
├── test_case2.c
├── test_case3.c
├── test_case4.c
├── test_case5.c
├── test_case6.c
.gitignore
.pre-commit-config.yaml
.pylintrc
.tool-versions
CONTRIBUTING.md
LICENSE.md
README.md
main.py
requirements.txt
```

## Contributing

Contributions to the analyzer are welcome. Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Author

<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/theHprogrammer">
                <img src="https://avatars.githubusercontent.com/u/79870881?v=4" width="150px;" alt="Helder's Image" />
                <br />
                <sub><b>Helder Henrique</b></sub>
            </a>
        </td>    
    </tr>
</table>
<h4 align="center">
   By: <a href="https://www.linkedin.com/in/theHprogrammer/" target="_blank"> Helder Henrique </a>
</h4>