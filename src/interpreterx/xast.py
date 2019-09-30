#!/usr/bin/python
#
#  Proyecto X
#  xast.py
#
#  Creado el 29/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

import sys
import math
import random


class Semantic_Error(Exception):
    pass


class Syntax_Error(Exception):
    pass


class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0


class NumberNode(Node):
    def __init__(self, v):
        if '.' in v:
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value


class StringNode(Node):
    def __init__(self, v):
        self.value = v

    def evaluate(self):
        return self.value


class PrintNode(Node):
    def __init__(self, v):
        self.value = v

    def execute(self):
        print(self.value.evaluate())


class AssignNode(Node):
    def __init__(self, t, val):
        self.target = t
        self.value = val

    def execute(self):
        # Chequeo que la variable no haya sido definida previamente
        print("Verificando que la variable no haya sido definida previamente")
        return self.value


class VariableNode(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        # if self.name not in names:
        #     raise Semantic_Error()
        # else:
        #     return names[self.name]
        print("evaluate")
        return self.value
