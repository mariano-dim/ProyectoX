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
from xast import ASTNode, Number, String, Print, Assign, Variable, VarDec


class XParser(Parser):
    tokens = XLexer.tokens

    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
    )

    def __init__(self):
        self.lines = []

    @_('START com END')
    def prog(self, p):
        return p.com


    @_('sec_com com')
    def sec_com(self, p):
        return p.sec_com + [p.com]


    @_('com')
    def sec_com(self, p):
        return [p.com]


    @_('LET ID COLON type EQUALS expr SEMI_COLON block')
    def block(self, p):
        #return [('LET', p.ID, p.type, p.expr)] + p.block
        return [VarDec(p.ID, p.type, p.expr)] + p.block

    @_('sec_com')
    def block(self, p):
        return p.sec_com

    @_('IN')
    def type(self, p):
        return ('IN', p.IN)

    @_('ST')
    def type(self, p):
        return ('ST', p.ST)

    @_('BEGIN block END')
    def com(self, p):
        return ('BLOCK', p.block)

    @_('PRINT LPAREN expr RPAREN SEMI_COLON')
    def com(self, p):
        #return ('PRINT', p.expr)
        return Print(p.expr)

    @_('ID EQUALS expr SEMI_COLON')
    def com(self, p):
        #return ('ASSIGN', p.ID, p.expr)
        return Assign(p.ID, p.expr)

    @_('TYPE_INT')
    def expr(self, p):
        #return ('TYPE_INT', p.TYPE_INT)
        return Number(p.TYPE_INT)

    @_('TYPE_STR')
    def expr(self, p):
        #return ('TYPE_STR', p.TYPE_STR)
        return String(p.TYPE_STR)

    @_('ID')
    def expr(self, p):
        return ('ID', p.ID)

    @_('expr PLUS expr')
    def expr(self, p):
        return ('PLUS', p.expr0, p.expr1)

    @_('expr MINUS expr')
    def expr(self, p):
        return ('MINUS', p.expr0, p.expr1)

    @_('expr TIMES expr')
    def expr(self, p):
        return ('TIMES', p.expr0, p.expr1)

    @_('expr DIVIDE expr')
    def expr(self, p):
        return ('DIVIDE', p.expr0, p.expr1)

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr


