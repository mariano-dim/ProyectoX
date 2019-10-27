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
    tokens = {ID, LPAREN, RPAREN, EQUALS, COLON, SEMI_COLON, PLUS, MINUS, TIMES, DIVIDE,
              BEGIN, START, END, PRINT, LET, IN, ST, TYPE_INT, TYPE_STR}
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

    # Ignored pattern
    ignore_newline = r'\n+'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    ignore_comment = r'#.*\n'

    def startLexer(self):
        print("Inicializando Lexer...")

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

if __name__ == '__main__':
    data = 'x := 3 + 42 * (s - t)'
    lexer = XLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))

