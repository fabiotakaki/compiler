import ply.lex as lex
import ply.yacc as yacc

class Lexical:
  def __init__(self, code):
    self.code = code

  def run(self):
    states = (
      ('COMENTARIOMULTILINHA','exclusive'),
    )

    reserved = {
        'program':'RES_PROGRAM',
        'procedure':'RES_PROCEDURE',
        'var':'RES_VAR',
        'int':'RES_INT',
        'boolean':'RES_BOOLEAN',
        'begin':'RES_BEGIN',
        'end':'RES_END',
        'if':'RES_IF',
        'then':'RES_THEN',
        'else':'RES_ELSE',
        'while':'RES_WHILE',
        'do':'RES_DO',
        'and':'RES_AND',
        'div':'RES_DIV',
        'or':'RES_OR',
        'not':'RES_NOT',
    }
    
    # List of token names.   This is always required
    tokens = [
      'OPSOMA',
      'OPSUB',
      'OPMUL',
      'OPDIV',
      'NUMERO',
      'IDENTIFICADOR',
      'SE_MAIOR',
      'SE_MENOR',
      'SE_MENOR_IGUAL',
      'SE_MAIOR_IGUAL',
      'SE_DIFERENTE',
      'SE_ATRIBUICAO',
      'SE_DELIMITADOR',
      'SE_VIRGULA',
      'SE_DOIS_PONTOS',
      'SE_PONTO_FINAL',
      'COMENTARIOS_UMA_LINHA',
      'COMENTARIOMULTILINHA',
      'FIMCOMENTARIO',
      'AP',
      'FP',
    ] + list(reserved.values())


    # Regular expression rules for simple tokens
    def t_IDENTIFICADOR(t):
      r'[a-zA-Z]([a-zA-Z]|[0-9]|_)*'
      if len(t.value) > 15:
        lexical_response.append(dict([('error', True), ('string', t.value[0]), ('line', t.lineno), ('start', t.lexpos), ('message', "Size string exceding 15 digits '%s'" % t.value)]))
        t.lexer.skip(1)
      else:
        t.type = reserved.get(t.value,'IDENTIFICADOR')    # Check for reserved words
        return t

    t_SE_MAIOR = r'>'
    t_SE_MENOR = r'<'
    t_SE_MENOR_IGUAL = r'<='
    t_SE_MAIOR_IGUAL = r'>='
    t_SE_DIFERENTE = r'<>'
    t_SE_ATRIBUICAO = r':='
    t_SE_DELIMITADOR = r';'
    t_SE_VIRGULA = r','
    t_SE_DOIS_PONTOS = r':'
    t_SE_PONTO_FINAL = r'\.'
    t_OPSOMA = r'\+'
    t_OPSUB  = r'-'
    t_OPMUL  = r'\*'
    t_OPDIV  = r'/'
    t_AP     = r'\('
    t_FP     = r'\)'

    # comments
    def t_COMENTARIOS_UMA_LINHA(t):
      r'(//.*)'
      return t 

    # def t_COMENTARIOMULTILINHA(t):
    #   r'{(.|\n)*}'
    #   return t

    def t_begin_COMENTARIOMULTILINHA(t):
      r'\{'
      t.lexer.code_start = t.lexer.lexpos        # Record the starting position
      t.lexer.level = 1                          # Initial brace level
      t.lexer.begin('COMENTARIOMULTILINHA')                     # Enter 'ccode' state 

    def t_COMENTARIOMULTILINHA_FIMCOMENTARIO(t):
      r'\}'
      t.lexer.level -=1

      # If closing brace, return the code fragment
      if t.lexer.level == 0:
          t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos+1]
          t.lexer.lineno += t.value.count('\n')
          t.lexer.begin('INITIAL')           
          return t

    def t_COMENTARIOMULTILINHA_COMENTARIOMULTILINHA(t):
      r'([^{}]|\n)+'
      pass

    def t_COMENTARIOMULTILINHA_error(t):
      lexical_response.append(dict([('error', True), ('string', t.value[0]), ('line', t.lineno), ('start', t.lexpos), ('message', "Illegal character '%s'" % t.value)]))
      t.lexer.skip(1)

    # A regular expression rule with some action code
    def t_NUMERO(t):
      r'\d+'
      if len(t.value) > 5:
        lexical_response.append(dict([('error', True), ('string', t.value[0]), ('line', t.lineno), ('start', t.lexpos), ('message', "Size number exceding 5 digits '%s'" % t.value)]))
        t.lexer.skip(1)
      else:  
        t.value = int(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(t):
      r'\n+'
      t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
      lexical_response.append(dict([('error', True), ('string', t.value[0]), ('line', t.lineno), ('start', t.lexpos), ('message', "Illegal character '%s'" % t.value)]))
      t.lexer.skip(1)

    # Build the lexer
    lexer = lex.lex()

    precedence = (
        ('left', 'OPSOMA', 'OPSUB'),
        ('left', 'OPMUL', 'OPDIV')
      )

    # Test it out
    # data = '''
    # 3 + 4.3 * huihu 10
    #   + -20 *2
    # '''
    data = self.code

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    lexical_response = []
    while True:
      tok = lexer.token()
      if not tok: 
        break      # No more input
      lexical_response.append(dict([('token', tok.type), ('string',tok.value), ('line', tok.lineno), ('start', tok.lexpos), ('end', (tok.lexpos+len(str(tok.value))-1))]))


    ##################
    # Syntatic
    ##################

    # DECLARATIONS
    def p_program(p):
      '''
      program : RES_PROGRAM IDENTIFICADOR SE_DELIMITADOR block
      '''
      print(p[1])

    def p_block(p):
      '''
      block : part_declare_variables compound_command
            | part_declare_subroutines compound_command
            | compound_command
      '''
      p[0] = (p[2], p[1], p[3])

    def p_part_declare_variables(p):
      '''
      part_declare_variables : declare_variables SE_DELIMITADOR
                             | part_declare_variables
      '''
      p[0] = p[1]

    def p_declare_variables(p):
      '''
      declare_variables : type list_ids
      '''
      p[0] = (p[1], p[2])

    def p_list_ids(p):
      '''
      list_ids : IDENTIFICADOR
               | SE_VIRGULA list_ids
      '''
      p[0] = p[1]

    def p_part_declare_subroutines(p):
      '''
      part_declare_subroutines : declare_procedure
                               | part_declare_subroutines
      '''
      p[0] = p[1]

    def p_declare_procedure(p):
      '''
      declare_procedure : RES_PROCEDURE IDENTIFICADOR formal_parameters block
                        | RES_PROCEDURE IDENTIFICADOR block
      '''
      p[0] = p[1]

    def p_formal_parameters(p):
      '''
      formal_parameters : AP section_formal_parameters FP
      '''
      p[0] = (p[1], p[2], p[3])

    def p_section_formal_parameters(p):
      '''
      section_formal_parameters : RES_VAR list_ids SE_DOIS_PONTOS IDENTIFICADOR
                                | list_ids SE_DOIS_PONTOS IDENTIFICADOR
      '''
      p[0] = p[1]


    # COMMANDS
    def p_compound_command(p):
      '''
      compound_command : RES_BEGIN commands RES_END
      '''
      p[0] = (p[0], p[1], p[2])

    def p_commands(p):
      '''
      commands : command
               | commands
      '''
      p[0] = p[1]


    def p_command(p):
      '''
      command : assignment
              | calling_procedure
              | compound_command
              | command_conditional_1
              | command_loop_1
      '''
      p[0] = p[1]

    def p_assignment(p):
      '''
      assignment : variable
                 | expression
      '''
      p[0] = p[1]


    def p_calling_procedure(p):
      '''
      calling_procedure : IDENTIFICADOR
                        | IDENTIFICADOR AP list_expressions FP
      '''
      p[0] = p[1]

    def p_command_conditional_1(p):
      '''
      command_conditional_1 : RES_IF expression RES_THEN command
                            | RES_IF expression RES_THEN command RES_ELSE command
      '''
      p[0] = p[1]

    def p_command_loop_1(p):
      '''
      command_loop_1 : RES_WHILE expression RES_DO command
      '''
      p[0] = p[1]

    # EXPRESSIONS
    def p_expression(p):
      '''
      expression : simple_expression
                 | simple_expression relation simple_expression
      '''
      p[0] = p[1]

    def p_relation(p):
      '''
      relation : RES_IGUAL
               | RES_DIFERENTE                      
               | RES_MENOR                      
               | RES_MENOR_IGUAL                      
               | RES_MAIOR_IGUAL                      
               | RES_MAIOR
      '''
      p[0] = p[1]

    def p_simple_expression(p):
      '''
      simple_expression : OPSOMA term simple_expression_1
                        | OPSUB term simple_expression_1
                        | OPSOMA term
                        | OPSUB term
      '''
      p[0] = p[1]


    def p_simple_expression_1(p):
      '''
      simple_expression_1 : OPSOMA term
                          | OPSUB term
                          | RES_OR term
                          | simple_expression_1
      '''
      p[0] = p[1]

    def p_term(p):
      '''
      term : factor term_1
           | factor
      '''
      p[0] = p[1]

    def p_term_1(p):
      '''
      term_1 : OPMUL factor
             | RES_DIV factor
             | RES_AND factor 
             | term_1  
      '''
      p[0] = p[1]

    def p_factor(p):
      '''
      factor : variable
             | NUMERO
             | AP expression FP
             | RES_NOT factor
      '''
      p[0] = p[1]

    def p_variable(p):
      '''
      variable : IDENTIFICADOR
               | IDENTIFICADOR expression
      '''
      p[0] = p[1]

    def p_list_expression(p):
      '''
      list_expression : expression
                      | expression expression_1
      '''
      p[0] = p[1]

    def p_expression_1(p):
      '''
      expression_1 : SE_VIRGULA expression
                   | expression_1
      '''
      p[0] = p[1]

    def p_empty(p):
      '''
      empty :
      '''
      p[0] = None

    def p_error(p):
      if p is not None:
        raise ParserSyntaxError("Syntax error at line %d, illegal token '%s' found" % (p.lineno, p.value))
      raise ParserSyntaxError("Unexpected end of input")


    parser = yacc.yacc()

    # syntatic_response = []
    # while True:
    #   try:
    #     s = input('')
    #   except EOFError:
    #     break
    #   parser.parse(str(s))

    parser.parse(data)
    file = open("./flask_compiler/parser.out")
    syntatic_response = ''
    for line in file: 
      syntatic_response += line+'<br>'

    return [lexical_response, syntatic_response]

