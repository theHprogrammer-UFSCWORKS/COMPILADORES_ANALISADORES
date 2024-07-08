from .semantic_rules import SymbolTable
from ..analisador_lexico.lexer import Lexer

class SemanticGrammarRules:
    tokens = Lexer().token_rules.tokens

    # Definindo a precedência dos operadores
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

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.current_struct = None
        
        print("Symbol Table initialized.")

    def p_program(self, p):
        '''program : optional_preprocessor_directives optional_declaration_list function_list'''
        print("program recognized")
        print(self.symbol_table)

    def p_optional_preprocessor_directives(self, p):
        '''optional_preprocessor_directives : preprocessor_directive_list
                                            | empty'''
        print("optional preprocessor directives recognized")

    def p_preprocessor_directive_list(self, p):
        '''preprocessor_directive_list : preprocessor_directive
                                        | preprocessor_directive_list preprocessor_directive'''
        print("preprocessor directive list recognized")

    def p_preprocessor_directive(self, p):
        '''preprocessor_directive : include_directive
                                    | define_directive'''
        print("preprocessor directive recognized")

    def p_include_directive(self, p):
        '''include_directive : HASH INCLUDE LIBRARY'''
        print("include directive recognized")

    def p_define_directive(self, p):
        '''define_directive : HASH DEFINE ID expression
                            | HASH DEFINE ID'''
        print("define directive recognized")

    
    def p_optional_declaration_list(self, p):
        '''optional_declaration_list : declaration_list'''
        print("optional declaration list recognized")

    def p_declaration_list(self, p):
        '''declaration_list : declaration_list declaration
                            | empty'''
        if len(p) == 3:
            print("declaration list extended")
        else:
            print("empty declaration list recognized")

    def p_function_list(self, p):
        '''function_list : function
                            | function_list function'''
        print("function list recognized")

    def p_function(self, p):
        '''function : main_function
                    | type_specifier ID LPAREN parameter_list RPAREN compound_statement
                    | type_specifier ID LPAREN RPAREN compound_statement'''
        if len(p) == 6 or len(p) == 7:
            self.symbol_table.add(p[2], p[1], p.lineno(2))
        self.symbol_table.enter_scope()
        print("function recognized")
        self.symbol_table.exit_scope()

    def p_main_function(self, p):
        '''main_function : type_specifier MAIN LPAREN RPAREN compound_statement'''
        self.symbol_table.add('main', p[1], p.lineno(2))
        self.symbol_table.enter_scope()
        print("main function recognized")
        self.symbol_table.exit_scope()

    def p_parameter_list(self, p):
        '''parameter_list : parameter
                            | parameter_list COMMA parameter
                            | empty'''
        print("parameter list recognized")

    def p_parameter(self, p):
        '''parameter : type_specifier ID'''
        self.symbol_table.add(p[2], p[1], p.lineno(2))
        print("parameter recognized")

    def p_compound_statement(self, p):
        'compound_statement : LBRACE statement_list RBRACE'
        self.symbol_table.enter_scope()
        print("compound statement recognized")
        self.symbol_table.exit_scope()

    def p_statement_list(self, p):
        '''statement_list : statement
                            | statement_list statement'''
        print("statement list recognized")

    def p_statement(self, p):
        '''statement : declaration
                        | assignment
                        | if_statement
                        | while_statement
                        | return_statement
                        | compound_statement
                        | function_call SEMICOLON
                        | break_statement
                        | continue_statement
                        | switch_statement
                        | do_while_statement
                        | for_statement
                        | expression SEMICOLON'''
        print("statement recognized")

    def p_declaration(self, p):
        '''declaration : type_specifier init_declarator_list SEMICOLON
                        | typedef_declaration
                        | struct_declaration'''
        print("declaration recognized")
        if len(p) == 4:
            for declarator in p[2]:
                self.symbol_table.add(declarator['name'], p[1], p.lineno(1))

    def p_typedef_declaration(self, p):
        '''typedef_declaration : TYPEDEF struct_declaration'''
        print("typedef declaration recognized")

    def p_struct_declaration(self, p):
        '''struct_declaration : STRUCT optional_id LBRACE struct_members RBRACE ID SEMICOLON'''
        print("struct declaration recognized")
        struct_name = p[6]
        self.current_struct = struct_name  # Definindo a estrutura atual antes de adicionar os membros
        self.symbol_table.add(struct_name, 'struct', p.lineno(6))
        # Processo de membros da estrutura
        members = p[4]
        for member in members:
            self.symbol_table.add_struct_member(struct_name, member['name'], member['type'], member['lineno'])
        self.current_struct = None  # Redefinindo após adicionar a estrutura

    def p_struct_members(self, p):
        '''struct_members : struct_member
                            | struct_members struct_member'''
        print("struct members recognized")
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_struct_member(self, p):
        '''struct_member : type_specifier ID SEMICOLON'''
        member_info = {'name': p[2], 'type': p[1], 'lineno': p.lineno(2)}
        p[0] = member_info
        print("struct member recognized")

    def p_optional_id(self, p):
        '''optional_id : ID
                        | empty'''
        p[0] = p[1] if len(p) > 1 else ''
        print("optional id recognized")

    def p_init_declarator_list(self, p):
        '''init_declarator_list : init_declarator
                                | init_declarator_list COMMA init_declarator'''
        print("init declarator list recognized")
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_init_declarator(self, p):
        '''init_declarator : ID
                            | ID EQUALS expression
                            | ID EQUALS LBRACE initializer_list RBRACE'''
        print("init declarator recognized")
        p[0] = {'name': p[1]}

    def p_initializer_list(self, p):
        '''initializer_list : expression
                            | initializer_list COMMA expression'''
        print("initializer list recognized")

    def p_type_specifier(self, p):
        '''type_specifier : non_empty_pre_type_specifier base_type
                        | non_empty_pre_type_specifier ID
                        | ID'''
        if len(p) == 3:
            p[0] = (p[1] if p[1] else '') + ' ' + p[2]
            print("complex type specifier recognized")
        else:
            p[0] = p[1]
            print("simple type specifier recognized")

    def p_non_empty_pre_type_specifier(self, p):
        '''non_empty_pre_type_specifier : pre_type_specifier'''
        p[0] = p[1]
        print("non-empty pre-type specifier recognized")

    def p_base_type(self, p):
        '''base_type : INT
                        | CHAR
                        | FLOAT
                        | DOUBLE
                        | VOID'''
        p[0] = p[1]
        print("base type recognized")

    def p_pre_type_specifier(self, p):
        '''pre_type_specifier : CONST
                            | VOLATILE
                            | AUTO
                            | REGISTER
                            | STATIC
                            | EXTERN
                            | SIGNED
                            | UNSIGNED
                            | SHORT
                            | LONG
                            | empty'''
        if p[1] == 'empty':
            p[0] = ''
        else:
            p[0] = p[1]
        print("pre-type specifier or empty recognized")

    def p_assignment(self, p):
        'assignment : ID EQUALS expression SEMICOLON'
        print("assignment recognized")
        var_info = self.symbol_table.lookup(p[1])
        expr_type = p[3]['type'] if isinstance(p[3], dict) else self.get_type(p[3])
        if not self.are_types_compatible(var_info['type'], expr_type):
            raise Exception(f"Type error: Cannot assign '{expr_type}' to variable '{p[1]}' of type '{var_info['type']}'.")


    def p_expression(self, p):
        '''expression : term
                        | expression PLUS term
                        | expression MINUS term
                        | expression LT term
                        | expression LE term
                        | expression GT term
                        | expression GE term
                        | expression NE term
                        | expression COMPARATOR term
                        | expression BITWISE_AND term
                        | expression BITWISE_OR term
                        | expression BITWISE_XOR term
                        | expression AND term
                        | expression OR term
                        | expression DOT ID
                        | expression INCREMENT
                        | expression DECREMENT
                        | function_call'''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            if p.slice[2].type in ['INCREMENT', 'DECREMENT']:
                p[0] = self.symbol_table.lookup(p[1])
        elif len(p) == 4:
            if p.slice[2].type == 'DOT':
                base_name = p[1]['name'] if isinstance(p[1], dict) else p[1]
                member_name = p[3]
                struct_type = self.symbol_table.lookup(base_name)['type']
                if struct_type not in self.symbol_table.structs:
                    raise Exception(f"Error: '{base_name}' is not a struct.")
                if member_name not in self.symbol_table.structs[struct_type]['members']:
                    raise Exception(f"Error: '{member_name}' is not a member of struct '{struct_type}'.")
                p[0] = self.symbol_table.structs[struct_type]['members'][member_name]
            else:
                left_type = self.get_type(p[1])
                right_type = self.get_type(p[3])
                if not self.are_types_compatible(left_type, right_type):
                    raise Exception(f"Type error: Cannot perform operation '{p[2]}' between '{left_type}' and '{right_type}'.")
                p[0] = {'type': left_type}
        print("expression recognized")

    def p_term(self, p):
        '''term : factor
                | term TIMES factor
                | term DIVIDE factor
                | term MOD factor
                | term LSHIFT factor
                | term RSHIFT factor'''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            left_type = self.get_type(p[1])
            right_type = self.get_type(p[3])
            if not self.are_types_compatible(left_type, right_type):
                raise Exception(f"Type error: Cannot perform operation '{p[2]}' between '{left_type}' and '{right_type}'.")
            p[0] = {'type': left_type}
        print("term recognized")

    def get_type(self, operand):
        if isinstance(operand, dict):
            return operand['type'].strip()  # Normaliza removendo espaços em branco
        elif isinstance(operand, str):
            var_info = self.symbol_table.lookup(operand)
            return var_info['type'].strip()  # Normaliza removendo espaços em branco
        else:
            return type(operand).__name__.lower()
    
    def are_types_compatible(self, type1, type2):
        # Normaliza removendo espaços em branco
        type1 = type1.strip()
        type2 = type2.strip()

        # Tipos são compatíveis se forem exatamente iguais
        if type1 == type2:
            return True

        # Definindo conjuntos de tipos compatíveis
        int_types = {'int', 'unsigned int', 'short', 'unsigned short', 'long', 'unsigned long'}
        float_types = {'float', 'double', 'long double'}
        char_types = {'char', 'unsigned char', 'signed char'}

        # Verificação de compatibilidade entre tipos inteiros
        if type1 in int_types and type2 in int_types:
            return True

        # Verificação de compatibilidade entre tipos de ponto flutuante
        if type1 in float_types and type2 in float_types:
            return True

        # Verificação de compatibilidade entre tipos de caracteres
        if type1 in char_types and type2 in char_types:
            return True

        # Compatibilidade entre tipos inteiros e float (conversão implícita permitida)
        if (type1 in int_types and type2 in float_types) or (type1 in float_types and type2 in int_types):
            return True

        # Caso contrário, os tipos não são compatíveis
        return False

    def p_factor(self, p):
        '''factor : INTEGER
                    | FLOAT_N
                    | STRING
                    | ID
                    | ID INCREMENT
                    | ID DECREMENT
                    | LPAREN expression RPAREN'''
        if len(p) == 2:
            if p.slice[1].type == 'ID':
                p[0] = self.symbol_table.lookup(p[1])
            elif p.slice[1].type == 'INTEGER':
                p[0] = {'type': 'int'}
            elif p.slice[1].type == 'FLOAT_N':
                p[0] = {'type': 'float'}
            elif p.slice[1].type == 'STRING':
                p[0] = {'type': 'char'}  # Assumindo que strings são tratadas como arrays de chars
        elif len(p) == 3:
            p[0] = self.symbol_table.lookup(p[1])
        elif len(p) == 4:
            p[0] = p[2]
        print("factor recognized")

    def p_if_statement(self, p):
        '''if_statement : IF factor statement
                        | IF factor statement ELSE statement'''
        print("if statement recognized")

    def p_while_statement(self, p):
        '''while_statement : WHILE factor statement'''
        print("while statement recognized")

    def p_do_while_statement(self, p):
        '''do_while_statement : DO statement WHILE factor SEMICOLON'''
        print("do-while statement recognized")

    def p_for_statement(self, p):
        '''for_statement : FOR LPAREN declaration expression SEMICOLON expression RPAREN statement
                            | FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement'''
        print("for statement recognized")

    def p_switch_statement(self, p):
        '''switch_statement : SWITCH factor LBRACE case_list default_case RBRACE'''
        print("switch statement recognized")

    def p_case_list(self, p):
        '''case_list : case
                        | case_list case
                        | empty'''
        print("case list recognized")

    def p_case(self, p):
        '''case : CASE expression COLON statement_list'''
        print("case recognized")

    def p_default_case(self, p):
        '''default_case : DEFAULT COLON statement_list
                        | empty'''
        print("default case recognized")

    def p_break_statement(self, p):
        '''break_statement : BREAK SEMICOLON'''
        print("break statement recognized")

    def p_continue_statement(self, p):
        '''continue_statement : CONTINUE SEMICOLON'''
        print("continue statement recognized")

    def p_return_statement(self, p):
        'return_statement : RETURN expression SEMICOLON'
        print("return statement recognized")

    def p_function_call(self, p):
        '''function_call : ID LPAREN RPAREN
                            | ID LPAREN argument_list RPAREN'''
        self.symbol_table.lookup(p[1])
        print("function call recognized")

    def p_argument_list(self, p):
        '''argument_list : expression
                            | argument_list COMMA expression'''
        print("argument list recognized")

    def p_empty(self, p):
        'empty :'

    def p_error(self, p):
        if p:
            print(f"Syntax error at '{p.value}', line {p.lineno}")
        else:
            print("Syntax error at EOF")
