
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN END LPAREN NUMBER PLUS PRINT RPAREN SEMI_COLONprog : BEGIN expr ENDexpr : PRINT LPAREN expr RPAREN SEMI_COLONexpr : expr PLUS exprexpr : NUMBER'
    
_lr_action_items = {'BEGIN':([0,],[2,]),'$end':([1,6,],[0,-1,]),'PRINT':([2,7,8,],[4,4,4,]),'NUMBER':([2,7,8,],[5,5,5,]),'END':([3,5,9,12,],[6,-4,-3,-2,]),'PLUS':([3,5,9,10,12,],[7,-4,7,7,-2,]),'LPAREN':([4,],[8,]),'RPAREN':([5,9,10,12,],[-4,-3,11,-2,]),'SEMI_COLON':([11,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'expr':([2,7,8,],[3,9,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> BEGIN expr END','prog',3,'p_main','calc.py',49),
  ('expr -> PRINT LPAREN expr RPAREN SEMI_COLON','expr',5,'p_print','calc.py',54),
  ('expr -> expr PLUS expr','expr',3,'p_add','calc.py',59),
  ('expr -> NUMBER','expr',1,'p_expr2NUM','calc.py',64),
]
