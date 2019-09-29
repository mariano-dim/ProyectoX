from ply import lex
import ply.yacc as yacc
import os
import sys
from builtins import print

tokens = (
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'SEMI_COLON',
    'PRINT',
    'HAS',
    'BEGIN',
    'END',
)

precedence = (
)

t_ignore = ' \t'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI_COLON = r'\;'
t_PRINT = r'print'
t_HAS = r'has'
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


def p_prog(p):
    """prog : BEGIN props END"""
    print("prog", p[2])
    p[0] = p[2]


def p_props(p):
    """props : sec_props
             | empty"""
    print("props", p[1])
    p[0] = p[1]



def p_sec_props(p):
    """sec_props : sec_props prop
                   | prop"""
    if len(p) > 2:
        print("sec_props", p[1])
        p[0] = p[1]
    else:
        print("sec_props", p[1])
        p[0] = p[1]


def p_prop(p):
    """prop : prop_print SEMI_COLON
            | prop_has SEMI_COLON"""
    print("prop", p[1])
    p[0] = p[1]


def p_prop_print(p):
    """prop_print : PRINT LPAREN number RPAREN"""
    print("prop_print", p[3])
    p[0] = p[3]


def p_prop_has(p):
    """prop_has : HAS LPAREN number RPAREN"""
    print("prop_has", p[3])
    p[0] = p[3]


def p_number(p):
    """number : NUMBER"""
    print("number", p[1])
    p[0] = p[1]


def p_empty(p):
    """empty :"""
    print("empty")
    pass


def p_error(p):
    print("Error de sintaxis, compruebe su programa fuente!")


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
