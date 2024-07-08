class SymbolTable:
    """
    A classe SymbolTable gerencia as variáveis e seus escopos dentro do programa.
    Ela permite adicionar novas variáveis, buscar variáveis existentes e gerenciar
    os diferentes escopos (global e locais) durante a execução do programa.
    """

    def __init__(self):
        """
        Inicializa a tabela de símbolos com um escopo global e uma pilha para os escopos locais.
        Também define um conjunto de funções padrão que são reconhecidas pelo compilador.
        """
        self.global_scope = {}
        self.local_scope_stack = []
        self.standard_functions = {'printf', 'scanf'}

    def enter_scope(self):
        """
        Entra em um novo escopo local, adicionando um dicionário vazio à pilha de escopos locais.
        """
        self.local_scope_stack.append({})

    def exit_scope(self):
        """
        Sai do escopo local atual, removendo o dicionário do topo da pilha de escopos locais.
        """
        self.local_scope_stack.pop()

    def add(self, name, type_, lineno):
        """
        Adiciona uma nova variável à tabela de símbolos no escopo atual.

        Parâmetros:
        - name (str): Nome da variável.
        - type_ (str): Tipo da variável.
        - lineno (int): Número da linha onde a variável foi declarada.

        Lança uma exceção se a variável já foi declarada no escopo atual.
        """
        scope = self.local_scope_stack[-1] if self.local_scope_stack else self.global_scope
        if name in scope:
            raise Exception(f"Erro: Variável '{name}' já declarada na linha {lineno}.")
        scope[name] = {'type': type_, 'lineno': lineno}

    def lookup(self, name):
        """
        Procura uma variável na tabela de símbolos, começando pelo escopo mais interno até o global.

        Parâmetros:
        - name (str): Nome da variável a ser buscada.

        Retorna as informações da variável se encontrada.
        Lança uma exceção se a variável não foi declarada.
        """
        for scope in reversed(self.local_scope_stack):
            if name in scope:
                return scope[name]
        if name in self.global_scope:
            return self.global_scope[name]
        if name in self.standard_functions:
            return {'type': 'function', 'lineno': -1}
        raise Exception(f"Erro: Variável '{name}' usada sem declaração.")

    def __str__(self):
        """
        Retorna uma representação em string do escopo global da tabela de símbolos.
        """
        return str(self.global_scope)
