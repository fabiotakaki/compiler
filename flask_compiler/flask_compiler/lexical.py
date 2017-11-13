import ply.lex as lex

class Lexical:
  def __init__(self, code):
    self.code = code
    self.tokens = []

  def getTokens(self):
    return self.tokens

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
      'SE_IGUAL',
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

    # for syntatic
    self.tokens = tokens

    # Regular expression rules for simple tokens
    def t_IDENTIFICADOR(t):
      r'[a-zA-Z]([a-zA-Z]|[0-9]|_)*'
      if len(t.value) > 15:
        lexical_response.append(dict([('error', True), ('string', t.value[0]), ('line', t.lineno), ('start', t.lexpos), ('message', "Size string exceding 15 digits '%s'" % t.value)]))
        t.lexer.skip(1)
      else:
        t.type = reserved.get(t.value,'IDENTIFICADOR')    # Check for reserved words
        return t

    t_SE_IGUAL = r'=='
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

    return lexical_response

