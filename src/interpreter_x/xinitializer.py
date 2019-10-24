#!/usr/bin/python
#
#  Proyecto X
#  xinitializer.py
#
#  Creado el 29/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

import os
import sys
from builtins import print
#import xinterpreter

from xlexer import XLexer
from xparser import XParser


def main():
    content = ""  # Esta variable mandendra el contenido del archivo de entrada leido
    path = os.getcwd()

    print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-  Starting Interpreter  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|- \n')
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
    except:
        print('[ERROR] No se puede encontrar el archivo "' + fileName + '"')

    lexer = XLexer()
    print("Tokenizando...")
    print(content)
    lexer.startLexer()

    for tok in lexer.tokenize(content):
        print('type=%r, value=%r' % (tok.type, tok.value))

    print("Parseando...")
    parser = XParser()
    prog = parser.parse(lexer.tokenize(content))
    if not prog:
        raise SystemExit

    print("Generando salida...")
    print(prog)
    print(parser.getnames())


if __name__ == '__main__':
    main()
