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
    """prog : BEGIN props END"""
    # prog es un diccoinario, indexado por...
    p[0] = {p[2]}

# Esta es una regla del tipo catch-all y es usada para errores generales

def p_prog_error(p):
    '''prog : BEGIN error END'''
    print("Error en expresion principal %s" % p[1])
    p[0] = None
    p.parser.error = 1


# 'props' es la regla principal interior a BEGIN-END, y la misma puede ser vacia, con lo cual el
# programa no hace nada o no genera nada

def p_props(p):
    """props : sec_props
             | empty"""
    p[0] = p[1]


# 'sec_props' es la regla recurrente principal de instrucciones del programa

def p_sec_props(p):
    """sec_props : sec_props statement
                 | statement"""
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_prop(p):
    """statement : command SEMI_COLON"""
    p[0] = p[1]


def p_command_print(p):
    """command : PRINT LPAREN expr RPAREN"""
    p[0] = ('PRINT',p[3])
    #p[0] = (AST.PrintNode(p[3]),)


def p_command_let(p):
    '''command : LET ID EQUALS expr'''
    p[0] = ('LET', p[2], p[4])
    #print(type(p[0]))
    #p[0] = (AST.AssignNode(p[2], p[4]),)


def p_expr_integer(p):
    '''expr : INTEGER'''
    p[0] = ('INTEGER', int(p[1]))


def p_expr_string(p):
    '''expr : STRING'''
    p[0] = ('STRING', p[1])


def p_expr_id(p):
    '''expr : ID'''
    p[0] = ('ID', p[1])


def p_expr_binary(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
    '''
    p[0] = ('BINOP', p[2], p[1], p[3])


def p_empty(p):
    """empty :"""
    pass


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
