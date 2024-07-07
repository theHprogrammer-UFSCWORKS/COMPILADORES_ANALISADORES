class SymbolTable:
    def __init__(self):
        self.global_scope = {}
        self.local_scope_stack = []
        self.standard_functions = {'printf', 'scanf'}

    def enter_scope(self):
        self.local_scope_stack.append({})

    def exit_scope(self):
        self.local_scope_stack.pop()

    def add(self, name, type_, lineno):
        scope = self.local_scope_stack[-1] if self.local_scope_stack else self.global_scope
        if name in scope:
            raise Exception(f"Error: Variable '{name}' already declared at line {lineno}.")
        scope[name] = {'type': type_, 'lineno': lineno}

    def lookup(self, name):
        for scope in reversed(self.local_scope_stack):
            if name in scope:
                return scope[name]
        if name in self.global_scope:
            return self.global_scope[name]
        if name in self.standard_functions:
            return {'type': 'function', 'lineno': -1}
        raise Exception(f"Error: Variable '{name}' used without declaration.")

    def __str__(self):
        return str(self.global_scope)
