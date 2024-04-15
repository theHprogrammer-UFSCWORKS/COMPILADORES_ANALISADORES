# Analisador Léxico para C
Este projeto é um analisador léxico para a linguagem de programação C, implementado em Python usando a biblioteca PLY (Python Lex-Yacc).

## Recursos

O analisador léxico é capaz de reconhecer:

- Palavras reservadas da linguagem C
- Identificadores
- Operadores aritméticos, lógicos e de comparação
- Delimitadores e pontuação
- Literais numéricos e strings
- Diretivas de pré-processamento

## Como Executar

### Configurar Ambiente

Primeiramente, configure o ambiente virtual Python e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Executando o Analisador Léxico no Terminal
Para executar o analisador léxico em um arquivo C:

```bash
python main.py caminho/para/arquivo.c
```

Caso, haja a necessidade de alterar os arquivos `c`, eles devem ser definidos dentro do diretório `tests`.

## Executando o Analisador Léxico pela IDE
Para executar o analisador léxico em um arquivo C diretamente da IDE, use o arquivo `estrutura_c.py`.

## Testes
Para executar os testes unitários, use o seguinte comando:

```bash
pytest
```

## Contribuindo
Contribuições para o analisador léxico são bem-vindas. Por favor, leia `CONTRIBUTING.md` para detalhes sobre nosso código de conduta e o processo de submissão de pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE.md` para detalhes.

## 👨‍💻 Author

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