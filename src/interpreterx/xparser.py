#!/usr/bin/python
#
#  Proyecto X
#  xparser.py
#
#  Creado el 29/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

from ply import *
import xlexer as LEXER
import xast as AST

tokens = LEXER.tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# dictionary of names (tabla de simbolos)
names = {}

def p_prog(p):
    """prog : START com END"""
    p[0] = {p[2]}


def p_command_sec_com(p):
    """com : BEGIN block END"""
    p[0] = p[2]

def p_command_print2(p):
    """com : PRINT LPAREN expr RPAREN SEMI_COLON"""
    p[0] = ('PRINT',p[3])


def p_command_assign(p):
    '''com : ID EQUALS expr SEMI_COLON'''
    p[0] = ('ASSIGN', p[1], p[3])


def p_command_print(p):
    """block : sec_com"""
    p[0] = ('PRINT',p[1])


def p_command_let(p):
    '''block : LET ID COLON type EQUALS expr SEMI_COLON block '''
    p[0] = ('LET', p[2], p[4], p[6]) + p[8]


def p_sec_com(p):
    """sec_com : sec_com com
               | com"""
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_expr_integer(p):
    '''expr : ER_INT'''
    p[0] = ('ER_INT', int(p[1]))


def p_expr_string(p):
    '''expr : ER_STR'''
    p[0] = ('ER_STR', p[1])


def p_expr_id(p):
    '''expr : ID'''
    p[0] = ('ID', p[1])


def p_expr_enclosed(p):
    '''expr : LPAREN expr RPAREN'''
    p[0] = ('OP_ENCLOSED', p[2])
    

def p_expr_binary(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
    '''
    p[0] = ('BINOP', p[2], p[1], p[3])


def p_command_type(p):
    '''type : ST
            | IN'''
    p[0] = ('TYPE', p[1])


# Catastrophic error handler
def p_error(p):
    if not p:
        print("Error de sintaxis en EOF")


#--------------------------------------------------------------------#


xparser = yacc.yacc()


def parse(data, debug=0):
    xparser.error = 0
    p = xparser.parse(data, debug=debug)
    if xparser.error:
        return None
    return p
