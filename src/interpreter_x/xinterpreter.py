#!/usr/bin/python
#
#  Proyecto X
#  xtranspiler.py
#
#  Creado el 29/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

import sys
import math
import random
import xast as AST


class XInterpreter:
    # Initialize the interpreter. prog is a dictionary
    # containing (line,statement) mappings

    def __init__(self, prog):
        self.prog = prog

    def do(self):
        self.vars = {}    # All variables

        print("Interpreting...")

        while 0 :
            print("Interpreting...")



# (
# 'LET', 'var01', ('INTEGER', 25), 
# 'PRINT', ('INTEGER', 1), 
# 'PRINT', ('BINOP', '+', ('INTEGER', 2), ('BINOP', '*', ('INTEGER', 98), ('INTEGER', 8))), 
# 'PRINT', ('ID', 'var01'), 
# 'LET', 'var02', ('INTEGER', 15), 
# 'PRINT', ('STRING', '"Hola Mundo"'), 
# 'PRINT', ('BINOP', '+', ('BINOP', '-', ('INTEGER', 1), ('INTEGER', 1)), ('BINOP', '/', ('INTEGER', 2), ('INTEGER', 1))), 
# 'LET', 'Var03', ('BINOP', '*', ('INTEGER', 15), ('INTEGER', 45)), 
# 'PRINT', ('BINOP', '+', ('STRING', '"Hola Mundo"'), ('BINOP', '*', ('INTEGER', 8), ('ID', 'var03')))
# )


# {
#     100: ('LET', ('X', None, None), ('NUM', 3)), 
#     110: ('GOSUB', 400), 
#     120: ('PRINT', [('', ('VAR', ('U', None, None))), ('', ('VAR', ('V', None, None))), ('', ('VAR', ('W', None, None)))], None), 
#     200: ('LET', ('X', None, None), ('NUM', 5)), 
#     210: ('GOSUB', 400),
#     220: ('LET', ('Z', None, None), ('BINOP', '+', ('BINOP', '+', ('VAR', ('U', None, None)), ('BINOP', '*', ('NUM', 2), ('VAR', ('V', None, None)))), ('BINOP', '*', ('NUM', 3), ('VAR', ('W', None, None))))), 
#     230: ('PRINT', [('', ('VAR', ('Z', None, None)))], None), 
#     240: ('GOTO', 999), 
#     400: ('LET', ('U', None, None), ('BINOP', '*', ('VAR', ('X', None, None)), ('VAR', ('X', None, None)))), 
#     410: ('LET', ('V', None, None), ('BINOP', '*', ('BINOP', '*', ('VAR', ('X', None, None)), ('VAR', ('X', None, None))), ('VAR', ('X', None, None)))), 
#     420: ('LET', ('W', None, None), ('BINOP', '+', ('BINOP', '+', ('BINOP', '+', ('BINOP', '*', ('BINOP', '*', ('BINOP', '*', ('VAR', ('X', None, None)), ('VAR', ('X', None, None))), ('VAR', ('X', None, None))), ('VAR', ('X', None, None))), ('BINOP', '*', ('BINOP', '*', ('VAR', ('X', None, None)), ('VAR', ('X', None, None))), 
#     ('VAR', ('X', None, None)))), ('BINOP', '*', ('VAR', ('X', None, None)), ('VAR', ('X', None, None)))), ('VAR', ('X', None, None)))),
#     430: ('RETURN',), 
#     999: ('END',)
# } 