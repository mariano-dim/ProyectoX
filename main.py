#!/usr/bin/python

#
#  Proyecto X
#  main.py
#
#  Creado el 17/08/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#
from src import lexerOriginal
from src.parser import Parser

__author__ = 'Mariano Andres Di Maggio'

import os
import sys
from builtins import print
from src.lexer import Lexer



def main():
    content = ""  # Esta variable mandendra el contenido del archivo de entrada leido
    path = os.getcwd()

    print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-  Starting Compilador  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|- \n')
    print("Leyendo archivo...")

    # Verifico que el usuario haya ingresado el nombre del archivo como parametro
    try:
        fileName = sys.argv[1]
    except:
        print("[ERROR] Se esperaba el nombre de archivo, como parametro para iniciar procesamiento, por ejemplo: 'demo.x'")
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

    # --------------------------------------
    #  LEXER
    # --------------------------------------
    print('\n|-|-|-|-|-|-|-|-|-|-|-|-|-|-  LEXER  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|- \n')

    # Crea una instancia nueva de la clase lexer
    # lex = lexerOriginal.Lexer(content)
    # tokens = lex.tokenize
    # print(tokens)
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(content)

    # for token in tokens:
    #     print(token)


    # --------------------------------------
    #  PARSER
    # --------------------------------------
    print('\n|-|-|-|-|-|-|-|-|-|-|-|-|-|-  PARSER  -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|- \n')

    # Crea una instancia nueva de la clase Parser y le pasa los Tokens generados como parametro
    # parse = parser.Parser(tokens)

    # source_ast = parse.parse()

    # print(source_ast)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()

# Llamada a la funcion de arranque
main()
