import ply.yacc as yacc

class Syntatic:
  def __init__(self, code, tokens):
    self.code = code
    self.tokens = tokens

  def run(self):
    ##################
    # Syntatic
    ##################

    tokens = self.tokens

    # DECLARATIONS
    def p_program(p):
      '''
      program : RES_PROGRAM IDENTIFICADOR SE_DELIMITADOR block
      '''
      pass

    def p_block(p):
      '''
      block : part_declare_variables compound_command
            | part_declare_subroutines compound_command
            | compound_command
      '''
      pass

    def p_part_declare_variables(p):
      '''
      part_declare_variables : declare_variables SE_DELIMITADOR part_declare_variables
                             | empty
      '''
      pass

    def p_type(p):
      '''
      type : RES_INT
           | RES_BOOLEAN
      '''

    def p_declare_variables(p):
      '''
      declare_variables : type list_ids
      '''
      pass

    def p_list_ids(p):
      '''
      list_ids : IDENTIFICADOR
               | SE_VIRGULA list_ids
               | empty
      '''
      pass

    def p_part_declare_subroutines(p):
      '''
      part_declare_subroutines : declare_procedure part_declare_subroutines
                               | empty
      '''
      pass

    def p_declare_procedure(p):
      '''
      declare_procedure : RES_PROCEDURE IDENTIFICADOR formal_parameters block
                        | RES_PROCEDURE IDENTIFICADOR block
      '''
      pass

    def p_formal_parameters(p):
      '''
      formal_parameters : AP section_formal_parameters FP
      '''
      pass

    def p_section_formal_parameters(p):
      '''
      section_formal_parameters : RES_VAR list_ids SE_DOIS_PONTOS IDENTIFICADOR
                                | list_ids SE_DOIS_PONTOS IDENTIFICADOR
      '''
      pass


    # COMMANDS
    def p_compound_command(p):
      '''
      compound_command : RES_BEGIN commands RES_END
      '''
      pass

    def p_commands(p):
      '''
      commands : command
               | commands
      '''
      pass


    def p_command(p):
      '''
      command : assignment
              | calling_procedure
              | compound_command
              | command_conditional_1
              | command_loop_1
      '''
      pass

    def p_assignment(p):
      '''
      assignment : variable
                 | expression
      '''
      pass


    def p_calling_procedure(p):
      '''
      calling_procedure : IDENTIFICADOR
                        | IDENTIFICADOR AP list_expression FP
      '''
      pass

    def p_command_conditional_1(p):
      '''
      command_conditional_1 : RES_IF expression RES_THEN command
                            | RES_IF expression RES_THEN command RES_ELSE command
      '''
      pass

    def p_command_loop_1(p):
      '''
      command_loop_1 : RES_WHILE expression RES_DO command
      '''
      pass

    # EXPRESSIONS
    def p_expression(p):
      '''
      expression : simple_expression
                 | simple_expression relation simple_expression
      '''
      pass

    def p_relation(p):
      '''
      relation : SE_IGUAL
               | SE_DIFERENTE                      
               | SE_MENOR                      
               | SE_MENOR_IGUAL                      
               | SE_MAIOR_IGUAL                      
               | SE_MAIOR
      '''
      pass

    def p_simple_expression(p):
      '''
      simple_expression : OPSOMA term simple_expression_1
                        | OPSUB term simple_expression_1
                        | OPSOMA term
                        | OPSUB term
      '''
      pass


    def p_simple_expression_1(p):
      '''
      simple_expression_1 : OPSOMA term simple_expression_1
                          | OPSUB term simple_expression_1
                          | RES_OR term simple_expression_1
                          | empty
      '''
      pass

    def p_term(p):
      '''
      term : factor term_1
           | factor
      '''
      pass

    def p_term_1(p):
      '''
      term_1 : OPMUL factor
             | RES_DIV factor
             | RES_AND factor 
             | term_1  
      '''
      pass

    def p_factor(p):
      '''
      factor : variable
             | NUMERO
             | AP expression FP
             | RES_NOT factor
      '''
      pass

    def p_variable(p):
      '''
      variable : IDENTIFICADOR
               | IDENTIFICADOR expression
      '''
      pass

    def p_list_expression(p):
      '''
      list_expression : expression
                      | expression expression_1
      '''
      pass

    def p_expression_1(p):
      '''
      expression_1 : SE_VIRGULA expression
                   | expression_1
      '''
      pass

    def p_empty(p):
      '''
      empty :
      '''
      pass

    def p_error(p):
      if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
      else:
        print("Syntax error at EOF")



    parser = yacc.yacc()

    # syntatic_response = []
    # while True:
    #   try:
    #     s = input('')
    #   except EOFError:
    #     break
    #   parser.parse(str(s))

    parser.parse(self.code)
    file = open("./flask_compiler/parser.out")
    syntatic_response = ''
    for line in file: 
      syntatic_response += line+'<br>'


    return syntatic_response
