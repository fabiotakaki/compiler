import ply.lex as lex
class Lexical:
  def __init__(self, code):
    self.code = code

  def run(self):
    reserved = {
        'program':'PALAVRA_RESERVADA_PROGRAM',
        'procedure':'PALAVRA_RESERVADA_PROCEDURE',
        'var':'PALAVRA_RESERVADA_VAR',
        'begin':'PALAVRA_RESERVADA_BEGIN',
        'end':'PALAVRA_RESERVADA_END',
        'if':'PALAVRA_RESERVADA_IF',
        'then':'PALAVRA_RESERVADA_THEN',
        'else':'PALAVRA_RESERVADA_ELSE',
        'while':'PALAVRA_RESERVADA_WHILE',
        'do':'PALAVRA_RESERVADA_DO',
    }
    # List of token names.   This is always required
    tokens = [
      'OPSOMA',
      'OPSUB',
      'OPMUL',
      'OPDIV',
      'NUMERO',
      'IDENTIFICADOR',
      'SIMBOLOS_ESPECIAIS_MAIOR',
      'SIMBOLOS_ESPECIAIS_MENOR',
      'SIMBOLOS_ESPECIAIS_MENOR_IGUAL',
      'SIMBOLOS_ESPECIAIS_MAIOR_IGUAL',
      'SIMBOLOS_ESPECIAIS_ATRIBUICAO',
      'SIMBOLOS_ESPECIAIS_DELIMITADOR',
      'SIMBOLOS_ESPECIAIS_VIRGULA',
      'SIMBOLOS_ESPECIAIS_DOIS_PONTOS',
      'SIMBOLOS_ESPECIAIS_PONTO_FINAL',
      'COMENTARIOS_UMA_LINHA',
      'COMENTARIOS_MULTI_LINHA',
      'AP',
      'FP',
    ] + list(reserved.values())

    # Regular expression rules for simple tokens
    def t_IDENTIFICADOR(t):
      r'[a-zA-Z]([a-zA-Z]|[0-9]|_)*'
      if len(t.value) > 15:
        response.append(dict([('error', True), ('string', t.value[0]), ('line', t.lineno), ('start', t.lexpos), ('message', "Size string exceding 15 digits '%s'" % t.value)]))
        t.lexer.skip(1)
      else:
        t.type = reserved.get(t.value,'IDENTIFICADOR')    # Check for reserved words
        return t

    t_SIMBOLOS_ESPECIAIS_MAIOR = r'>'
    t_SIMBOLOS_ESPECIAIS_MENOR = r'<'
    t_SIMBOLOS_ESPECIAIS_MENOR_IGUAL = r'<='
    t_SIMBOLOS_ESPECIAIS_MAIOR_IGUAL = r'>='
    t_SIMBOLOS_ESPECIAIS_ATRIBUICAO = r':='
    t_SIMBOLOS_ESPECIAIS_DELIMITADOR = r';'
    t_SIMBOLOS_ESPECIAIS_VIRGULA = r','
    t_SIMBOLOS_ESPECIAIS_DOIS_PONTOS = r':'
    t_SIMBOLOS_ESPECIAIS_PONTO_FINAL = r'\.'
    t_OPSOMA = r'\+'
    t_OPSUB  = r'-'
    t_OPMUL  = r'\*'
    t_OPDIV  = r'/'
    t_AP     = r'\('
    t_FP     = r'\)'

    # comments
    def t_COMENTARIOS_UMA_LINHA(t):
      r'(//.*)'
      t.value = '//'
      return t 

    def t_COMENTARIOS_MULTI_LINHA(t):
      r'{(.|\n)*}'
      t.value = '{}'
      return t

    # A regular expression rule with some action code
    def t_NUMERO(t):
      r'\d+\.?\d*'
      if len(t.value) > 5:
        response.append(dict([('error', True), ('string', t.value[0]), ('line', t.lineno), ('start', t.lexpos), ('message', "Size number exceding 5 digits '%s'" % t.value)]))
        t.lexer.skip(1)
      else:  
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
