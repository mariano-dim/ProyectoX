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
    'INTEGER',
    'STRING',
)

tokens = keywords + (
    'LPAREN', 
    'RPAREN',
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
t_COLON = r'\:'
t_EQUALS = r'\:='
t_SEMI_COLON = r'\;'
t_ER_INT = r'\d+'
t_ER_STR = r'\".*?\"'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'


def t_error(t):
    print("Caracter no permitido %s" % t.value[0])
    t.lexer.skip(1)


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


lex.lex(debug=0)
