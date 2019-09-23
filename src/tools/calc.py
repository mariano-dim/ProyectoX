from ply import lex
import ply.yacc as yacc
import os
import sys
from builtins import print

tokens = (
    'PLUS',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'SEMI_COLON',
    'PRINT',
    'BEGIN',
    'END',
)

precedence = (
)

t_ignore = ' \t'

t_PLUS = r'\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI_COLON = r'\;'
t_PRINT = r'print'
t_BEGIN = r'begin'
t_END = r'end'


def t_NUMBER(t):
    r"""[0-9]+"""
    t.value = int(t.value)
    return t


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Invalid Token:", t.value[0])
    t.lexer.skip(1)


def p_main(p):
    """prog : BEGIN expr END"""
    p[0] = p[2]


def p_print(p):
    """expr : PRINT LPAREN expr RPAREN SEMI_COLON"""
    p[0] = p[3]


def p_add(p):
    """expr : expr PLUS expr"""
    p[0] = p[1] + p[3]


def p_expr2NUM(p):
    'expr : NUMBER'
    p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")


def main():
    content = ""  # Esta variable mandendra el contenido del archivo de entrada leido
    path = os.getcwd()

    print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-  Starting Compilador  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|- \n')
    print("Leyendo archivo...")

    # Verifico que el usuario haya ingresado el nombre del archivo como parametro
    try:
        fileName = sys.argv[1]
    except:
        print(
            "[ERROR] Se esperaba el nombre de archivo, como parametro para iniciar procesamiento, por ejemplo: 'demo.x'")
        return

    # Chequeo si la extension del archivo es correcta
    if fileName[len(fileName) - 2:len(fileName)] != ".x":
        print("[ERROR] Extension de archivo no reconocida, asegurese que la extension del archivo sea '.x'")
        return

    # Abre el archivo de entrada (en modo lectura) y lo graba en la variable 'content'
    try:
        with open(path + "/" + fileName, "r") as sourceCodeFile:
            content = sourceCodeFile.read()
        print(content)
    except:
        print('[ERROR] No se puede encontrar el archivo "' + fileName + '"')

    lexer = lex.lex()

    parser = yacc.yacc()

    res = parser.parse(content)  # the input
    print(res)


if __name__ == '__main__':
    main()
