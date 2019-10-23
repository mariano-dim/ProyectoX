#!/usr/bin/python
#
#  Proyecto X
#  xlexer.py
#
#  Creado el 29/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

from sly import Lexer


class XLexer(Lexer):
    tokens = {ID, NAME, LPAREN, RPAREN, EQUALS, COLON, SEMI_COLON, PLUS, MINUS, TIMES, DIVIDE,
              BEGIN, START, END, PRINT, LET, IN, ST, TYPE_INT, TYPE_STR}
#    ignore = ' \t'
#    literals = {'=', '+', '-', '*', '/', '(', ')'}

    ignore = ' \t'

    # Tokens
    TYPE_STR = r'\".[ a-zA-Z]*?\"'
    ID = r'[a-zA-Z][a-zA-Z]*'
    TYPE_INT = r'\d+'
    LPAREN = r'\('
    RPAREN = r'\)'
    EQUALS = r'\:='
    COLON = r'\:'
    SEMI_COLON = r'\;'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'

    # Special cases
    ID['BEGIN'] = BEGIN
    ID['END'] = END
    ID['START'] = START
    ID['PRINT'] = PRINT
    ID['LET'] = LET
    ID['IN'] = IN
    ID['ST'] = ST

    def startLexer(self):
        print("Inicializando Lexer...")

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

if __name__ == '__main__':
    data = 'x := 3 + 42 * (s - t)'
    lexer = XLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))