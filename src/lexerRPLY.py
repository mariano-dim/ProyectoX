from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('RESTA', r'\-')
        self.lexer.add('MULTIPLICACION', r'\\')
        self.lexer.add('DIVISION', r'\*')
        self.lexer.add('CONCATENATOR', r'\<')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Identificator
        self.lexer.add('IDENTIFICATOR', r'[a-zA-Z_][a-zA-Z_0-9]*')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
