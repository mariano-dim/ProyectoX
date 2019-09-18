#!/usr/bin/python

#
#  Proyecto X
#  ifStatement.py
#
#  Creato el 15/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#


class IfStatement:

    def __init__(self):
        self.token_stream = ""

    def parse(self, token_stream):
        print(token_stream)
