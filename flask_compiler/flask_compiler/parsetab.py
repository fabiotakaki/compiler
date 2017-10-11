
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOPSOMAOPSUBleftOPMULOPDIVOPSOMA OPSUB OPMUL OPDIV NUMERO_INTEIRO NUMERO_REAL IDENTIFICADOR SIMBOLOS_ESPECIAIS_MAIOR SIMBOLOS_ESPECIAIS_MENOR SIMBOLOS_ESPECIAIS_MENOR_IGUAL SIMBOLOS_ESPECIAIS_MAIOR_IGUAL SIMBOLOS_ESPECIAIS_ATRIBUICAO SIMBOLOS_ESPECIAIS_DELIMITADOR SIMBOLOS_ESPECIAIS_VIRGULA SIMBOLOS_ESPECIAIS_DOIS_PONTOS SIMBOLOS_ESPECIAIS_PONTO_FINAL COMENTARIOS_UMA_LINHA COMENTARIOMULTILINHA AP FP PALAVRA_RESERVADA_THEN PALAVRA_RESERVADA_BEGIN PALAVRA_RESERVADA_PROGRAM PALAVRA_RESERVADA_END PALAVRA_RESERVADA_DO PALAVRA_RESERVADA_VAR PALAVRA_RESERVADA_ELSE PALAVRA_RESERVADA_WHILE PALAVRA_RESERVADA_PROCEDURE PALAVRA_RESERVADA_IF\n      root : expression\n           | var_assign\n           | empty\n      \n      expression : expression OPMUL expression\n                 | expression OPDIV expression\n                 | expression OPSOMA expression\n                 | expression OPSUB expression\n      \n      expression : NUMERO_INTEIRO\n                 | NUMERO_REAL\n      \n      empty :\n      \n      var_assign : IDENTIFICADOR SIMBOLOS_ESPECIAIS_ATRIBUICAO expression\n                 | IDENTIFICADOR SIMBOLOS_ESPECIAIS_ATRIBUICAO IDENTIFICADOR\n      '
    
_lr_action_items = {'OPDIV':([3,5,7,14,15,16,17,18,],[-9,11,-8,11,-4,11,-5,11,]),'IDENTIFICADOR':([0,8,],[2,13,]),'OPSOMA':([3,5,7,14,15,16,17,18,],[-9,10,-8,10,-4,-6,-5,-7,]),'OPSUB':([3,5,7,14,15,16,17,18,],[-9,12,-8,12,-4,-6,-5,-7,]),'SIMBOLOS_ESPECIAIS_ATRIBUICAO':([2,],[8,]),'NUMERO_REAL':([0,8,9,10,11,12,],[3,3,3,3,3,3,]),'OPMUL':([3,5,7,14,15,16,17,18,],[-9,9,-8,9,-4,9,-5,9,]),'$end':([0,1,3,4,5,6,7,13,14,15,16,17,18,],[-10,0,-9,-2,-1,-3,-8,-12,-11,-4,-6,-5,-7,]),'NUMERO_INTEIRO':([0,8,9,10,11,12,],[7,7,7,7,7,7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,8,9,10,11,12,],[5,14,15,16,17,18,]),'var_assign':([0,],[4,]),'root':([0,],[1,]),'empty':([0,],[6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> expression','root',1,'p_root','lexical.py',167),
  ('root -> var_assign','root',1,'p_root','lexical.py',168),
  ('root -> empty','root',1,'p_root','lexical.py',169),
  ('expression -> expression OPMUL expression','expression',3,'p_expression','lexical.py',175),
  ('expression -> expression OPDIV expression','expression',3,'p_expression','lexical.py',176),
  ('expression -> expression OPSOMA expression','expression',3,'p_expression','lexical.py',177),
  ('expression -> expression OPSUB expression','expression',3,'p_expression','lexical.py',178),
  ('expression -> NUMERO_INTEIRO','expression',1,'p_expression_int_float','lexical.py',184),
  ('expression -> NUMERO_REAL','expression',1,'p_expression_int_float','lexical.py',185),
  ('empty -> <empty>','empty',0,'p_empty','lexical.py',191),
  ('var_assign -> IDENTIFICADOR SIMBOLOS_ESPECIAIS_ATRIBUICAO expression','var_assign',3,'p_var_assign','lexical.py',197),
  ('var_assign -> IDENTIFICADOR SIMBOLOS_ESPECIAIS_ATRIBUICAO IDENTIFICADOR','var_assign',3,'p_var_assign','lexical.py',198),
]