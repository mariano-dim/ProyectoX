#!/usr/bin/python
#
#  Proyecto X
#  xparser.py
#
#  Creado el 29/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

from sly import *
from xlexer import XLexer


class XParser(Parser):
    tokens = XLexer.tokens

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
#        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.names = {}

    def getnames(self):
        return self.names


    @_('START com END')
    def prog(self, p):
        return p.com


    @_('sec_com com')
    def sec_com(self, p):
        return p.com


    @_('com')
    def sec_com(self, p):
        return p.com


    @_('LET ID COLON type EQUALS expr SEMI_COLON block')
    def block(self, p):
        # Agrego una lista de valores asociados al ID al diccionario basado en el nombre del ID
        print("Adding ID: '%s' to names" % p.ID)
        self.names[p.ID] = [p.type, p.expr]
        return p.expr

    @_('sec_com')
    def block(self, p):
        return p.sec_com

    @_('IN')
    def type(self, p):
        return p.IN

    @_('ST')
    def type(self, p):
        return p.ST

    @_('BEGIN block END')
    def com(self, p):
        return p.block


    @_('PRINT LPAREN expr RPAREN SEMI_COLON')
    def com(self, p):
        return p.expr


    @_('ID EQUALS expr SEMI_COLON')
    def com(self, p):
        # Actualizo el valor del ID, si no existe es ERROR
        if not p.ID in self.names:
            print("Undefined ID '%s' in assing" % p.ID)
            return 0
        self.names[p.ID] = p.expr
        return p.expr


    @_('TYPE_INT')
    def expr(self, p):
        return p.TYPE_INT


    @_('TYPE_STR')
    def expr(self, p):
        return p.TYPE_STR

    @_('ID')
    def expr(self, p):
        try:
            return self.names[p.ID]
        except LookupError:
            print("Undefined ID '%s' in expr" % p.ID)
            return 0

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr


