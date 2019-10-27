#!/usr/bin/python
#
#  Proyecto X
#  xtranspiler.py
#
#  Creado el 29/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

import sys
import math
import random
from xast import Print


class XInterpreter:
    # Initialize the interpreter. prog is a tuple


    def __init__(self, prog):
        self.prog = prog

    def do(self):
        self.names = {} # Tabla de tipos, es un diccionario

        print("Interpreting...")

        print("Printing commands to interprete...")
        for command in self.prog[1]:
            print(command)




