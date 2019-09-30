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
import xlexer
import xparser
import xinterpreter

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
        print("Tokenizando...")
        print(content)
    except:
        print('[ERROR] No se puede encontrar el archivo "' + fileName + '"')

    prog = xparser.parse(content)
    if not prog:
        raise SystemExit
    print("AST Tree...")
    print(prog)
    t = xinterpreter.XInterpreter(prog)
    try:
        t.do()
        raise SystemExit
    except RuntimeError:
        pass


if __name__ == '__main__':
    main()
