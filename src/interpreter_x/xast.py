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


class ASTNode:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0


class Number(ASTNode):
    def __init__(self, value):
        self.value = int(value)

    def evaluate(self):
        return self.value


class String(ASTNode):
    def __init__(self, v):
        self.value = v

    def evaluate(self):
        return self.value


class Print(ASTNode):
    def __init__(self, v):
        self.value = v

    def execute(self):
        print(self.value.evaluate())


class Assign(ASTNode):
    def __init__(self, t, val):
        self.target = t
        self.value = val

    def execute(self):
        # Chequeo que la variable no haya sido definida previamente
        print("Verificando que la variable no haya sido definida previamente")
        return self.value


class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        # if self.name not in names:
        #     raise Semantic_Error()
        # else:
        #     return names[self.name]
        print("evaluate")
        return self.value


class VarDec(ASTNode):
    def __init__(self, name, type, value):
        self.name = name
        self.value = value
        self.type = type

    def evaluate(self):
        return self.value


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOp):
    def eval(self):
        i = self.left.eval() + self.right.eval()
        return i


class Sub(BinaryOp):
    def eval(self):
        i = self.left.eval() - self.right.eval()
        return i


class Mul(BinaryOp):
    def eval(self):
        i = self.left.eval() * self.right.eval()
        return i


class Div(BinaryOp):
    def eval(self):
        i = self.left.eval() / self.right.eval()
        return i


