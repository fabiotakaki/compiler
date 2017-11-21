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
      program : RES_PROGRAM IDENTIFICADOR SE_DELIMITADOR block SE_PONTO_FINAL
      '''
      pass

    def p_block(p):
      '''
      block : part_declare_variables declare_procedure compound_command
      '''
      pass

    def p_type(p):
      '''
      type : RES_INT
           | RES_BOOLEAN
      '''
      pass

    def p_part_declare_variables(p):
      '''
      part_declare_variables : declare_variables part_declare_variables_loop
                             | empty
      '''
      pass

    def p_part_declare_variables_loop(p):
      '''
      part_declare_variables_loop : SE_DELIMITADOR part_declare_variables
                                  | empty
      '''
      pass


    def p_declare_variables(p):
      '''
      declare_variables : type list_ids
      '''
      pass

    def p_list_ids(p):
      '''
      list_ids : IDENTIFICADOR list_ids_loop
      '''
      pass

    def p_list_ids_loop(p):
      '''
      list_ids_loop : SE_VIRGULA IDENTIFICADOR list_ids_loop
                    | empty
      '''
      pass

    def p_declare_procedure(p):
      '''
      declare_procedure : RES_PROCEDURE IDENTIFICADOR param_form SE_DELIMITADOR block SE_DELIMITADOR
                        | empty
      '''
      pass

    def p_param_form(p):
      '''
      param_form : AP param_form_1 param_form_1_loop FP
                 | empty
      '''
      pass

    def p_param_form_1(p):
      '''
      param_form_1 : RES_VAR list_ids SE_DOIS_PONTOS type
                   | list_ids SE_DOIS_PONTOS type
      '''
      pass

    def p_param_form_1_loop(p):
      '''
      param_form_1_loop : SE_DELIMITADOR param_form_1 param_form_1_loop
                        | empty
      '''
      pass

    def p_compound_command(p):
      '''
      compound_command : RES_BEGIN command command_loop RES_END
      '''
      pass

    def p_command_loop(p):
      '''
      command_loop : SE_DELIMITADOR command command_loop
                   | empty
      '''
      pass

    def p_command(p):
      '''
      command : start_ident
              | compound_command
              | conditional_command
              | loop_command
      '''
      pass

    def p_start_ident(p):
      '''
      start_ident : IDENTIFICADOR opt_ident
      '''
      pass

    def p_opt_ident(p):
      '''
      opt_ident : SE_ATRIBUICAO expression
                | opt_expression_list
                | opt_expression
      '''
      pass

    def p_opt_expression_list(p):
      '''
      opt_expression_list : AP list_expression FP
                          | empty
      '''
      pass

    def p_opt_expression(p):
      '''
      opt_expression : expression
                     | empty
      '''
      pass

    def p_conditional_command(p):
      '''
      conditional_command : RES_IF expression RES_THEN command opt_else
      '''
      pass

    def p_opt_else(p):
      '''
      opt_else : RES_ELSE command
               | empty
      '''
      pass

    def p_loop_command(p):
      '''
      loop_command : RES_WHILE expression RES_DO command
      '''
      pass

    def p_expression(p):
      '''
      expression : simple_expression opt_relation
      '''
      pass

    def p_opt_relation(p):
      '''
      opt_relation : relation simple_expression
                   | empty
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
      simple_expression : opt_signal term term_loop
      '''
      pass

    def p_signal(p):
      '''
      signal : OPSOMA
             | OPSUB
      '''
      pass

    def p_opt_signal(p):
      '''
      opt_signal : signal
                 | empty
      '''
      pass

    def p_term_loop(p):
      '''
      term_loop : signal term term_loop
                | RES_OR term term_loop
                | empty
      '''
      pass

    def p_term(p):
      '''
      term : factor factor_loop
      '''
      pass

    def p_factor_loop(p):
      '''
      factor_loop : OPMUL factor factor_loop
                  | RES_DIV factor factor_loop
                  | RES_AND factor factor_loop
                  | empty
      '''
      pass

    def p_variable(p):
      '''
      variable : IDENTIFICADOR opt_expression
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

    def p_list_expression(p):
      '''
      list_expression : expression loop_expression
      '''
      pass

    def p_loop_expression(p):
      '''
      loop_expression : SE_VIRGULA expression loop_expression
                      | empty
      '''
      pass

    def p_empty(p):
      '''
      empty :
      '''
      pass

    def p_error(p):
      if p:
        syntatic_response.append(dict([('message', "Syntax error at token "+p.type), ('line',p.lineno), ('start', p.lexpos)]))
        # Just discard the token and tell the parser it's okay.
        parser.errok()
      else:
        print("Syntax error at EOF")


    syntatic_response = []

    parser = yacc.yacc()
    parser.parse(self.code)
    # file = open("./flask_compiler/parser.out")
    # syntatic_response = ''
    # for line in file: 
    #   syntatic_response += line+'<br>'


    return syntatic_response
