from ..ANALISADOR_LEXICO.lexer import Lexer

class GrammarRules:
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
        pass

    def p_program(self, p):
        '''program : optional_preprocessor_directives optional_declaration_list function_list'''
        print("program recognized")


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
        print("function recognized")


    def p_main_function(self, p):
        '''main_function : type_specifier MAIN LPAREN RPAREN compound_statement'''
        print("main function recognized")


    def p_parameter_list(self, p):
        '''parameter_list : parameter
                          | parameter_list COMMA parameter
                          | empty'''
        print("parameter list recognized")


    def p_parameter(self, p):
        '''parameter : type_specifier ID'''
        print("parameter recognized")


    def p_compound_statement(self, p):
        'compound_statement : LBRACE statement_list RBRACE'
        print("compound statement recognized")


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


    def p_typedef_declaration(self, p):
        '''typedef_declaration : TYPEDEF struct_declaration'''
        print("typedef declaration recognized")


    def p_struct_declaration(self, p):
        '''struct_declaration : STRUCT optional_id LBRACE struct_members RBRACE ID SEMICOLON'''
        print("struct declaration recognized")


    def p_struct_members(self, p):
        '''struct_members : struct_member
                          | struct_members struct_member'''
        print("struct members recognized")


    def p_struct_member(self, p):
        '''struct_member : type_specifier ID SEMICOLON'''
        print("struct member recognized")


    def p_optional_id(self, p):
        '''optional_id : ID
                       | empty'''
        print("optional id recognized")


    def p_init_declarator_list(self, p):
        '''init_declarator_list : init_declarator
                                | init_declarator_list COMMA init_declarator'''
        print("init declarator list recognized")


    def p_init_declarator(self, p):
        '''init_declarator : ID
                           | ID EQUALS expression
                           | ID EQUALS LBRACE initializer_list RBRACE'''
        print("init declarator recognized")


    def p_initializer_list(self, p):
        '''initializer_list : expression
                            | initializer_list COMMA expression'''
        print("initializer list recognized")


    def p_type_specifier(self, p):
        '''type_specifier : non_empty_pre_type_specifier base_type
                        | non_empty_pre_type_specifier ID
                        | ID'''
        if len(p) == 3:
            print("complex type specifier recognized")
        else:
            print("simple type specifier recognized")

    def p_non_empty_pre_type_specifier(self, p):
        '''non_empty_pre_type_specifier : pre_type_specifier'''
        print("non-empty pre-type specifier recognized")

    def p_base_type(self, p):
        '''base_type : INT
                     | CHAR
                     | FLOAT
                     | DOUBLE
                     | VOID'''
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
        print("pre-type specifier or empty recognized")


    def p_assignment(self, p):
        'assignment : ID EQUALS expression SEMICOLON'
        print("assignment recognized")


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
        print("expression recognized")


    def p_term(self, p):
        '''term : factor
                | term TIMES factor
                | term DIVIDE factor
                | term MOD factor
                | term LSHIFT factor
                | term RSHIFT factor'''
        print("term recognized")


    def p_factor(self, p):
        '''factor : INTEGER
                  | FLOAT_N
                  | STRING
                  | ID
                  | ID INCREMENT
                  | ID DECREMENT
                  | LPAREN expression RPAREN'''
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
