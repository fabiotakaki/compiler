import ply.lex as lex
class Lexical:
  def __init__(self, code):
    self.code = code

  def run(self):
    # List of token names.   This is always required
    tokens = (
      'OPSOMA',
      'OPSUB',
      'OPMUL',
      'OPDIV',
      'NUMERO',
      'IDENTIFICADOR',
      'PALAVRA_RESERVADA',
      'SIMBOLOS_ESPECIAIS',
      'COMENTARIOS',
      'AP',
      'FP',
    )

    # Regular expression rules for simple tokens
    t_IDENTIFICADOR = r'[a-zA-Z]([a-zA-Z]|[0-9]|_)*'
    t_PALAVRA_RESERVADA  = r'(program|procedure|var|begin|end|if|then|else|while|do)'
    t_SIMBOLOS_ESPECIAIS = r'(>|<|<=|>=|:=|;|,|:|\.)'
    t_OPSOMA = r'\+'
    t_OPSUB  = r'-'
    t_OPMUL  = r'\*'
    t_OPDIV  = r'^/$'
    t_AP     = r'\('
    t_FP     = r'\)'

    # comments
    def t_COMENTARIOS(t):
      r'{(.|\n)*}|(//.*)'
      if(t.value[0] == '{'):
        t.value = '{}'
      else:
        t.value = '//'
      return t


    # A regular expression rule with some action code
    def t_NUMERO(t):
      r'\d+\.?\d*'
      return t

    # Define a rule so we can track line numbers
    def t_newline(t):
      r'\n+'
      t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
      response.append(dict([('error', True), ('string', t.value[0]), ('line', t.lineno), ('start', t.lexpos), ('message', "Illegal character '%s'" % t.value[0])]))
      t.lexer.skip(1)

    # Build the lexer
    lexer = lex.lex()

    # Test it out
    # data = '''
    # 3 + 4.3 * huihu 10
    #   + -20 *2
    # '''
    data = self.code

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    response = []
    while True:
      tok = lexer.token()
      if not tok: 
        break      # No more input
      response.append(dict([('token', tok.type), ('string',tok.value), ('line', tok.lineno), ('start', tok.lexpos), ('end', (tok.lexpos+len(tok.value)-1))]))
    return response
