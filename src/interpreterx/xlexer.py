#!/usr/bin/python
#
#  Proyecto X
#  xlexer.py
#
#  Creado el 29/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

from ply import *

keywords = (
    'BEGIN',
    'END',
    'PRINT',
    'LET',
    'IN',
    'ST',
)

tokens = keywords + (
    'LPAREN', 
    'RPAREN',
    'LCB',
    'RCB',
    'SEMI_COLON',
    'COLON',
    'EQUALS',
    'ID',
    'ER_INT',
    'ER_STR',
    'PLUS',
    'MINUS', 
    'TIMES', 
    'DIVIDE',

)

precedence = (
)

t_ignore = ' \t'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_LCB = r'\{'
t_RCB = r'\}'

t_COLON = r'\:'
t_EQUALS = r'\:='
t_SEMI_COLON = r'\;'
t_ER_INT = r'\d+'
t_ER_STR = r'\".[a-zA-Z]*?\"'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'


def t_error(t):
    print("Caracter no permitido %s" % t.value[0])
    t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-Z][a-zA-Z]*'
    if t.value in keywords:
        t.type = t.value
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


lex.lex(debug=0)
