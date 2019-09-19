from rply import ParserGenerator
from src.ast import Number, Sum, Sub, Multiplicacion, Division, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN','SEMI_COLON', 'SUM', 'RESTA'
             , 'MULTIPLICACION', 'DIVISION'],
            # A list of precedence rules with ascending precedence, to
            # disambiguate ambiguous production rules.
            precedence=[
                ('left', ['MULTIPLICACION', 'DIVISION'])
            ]
        )

    def parse(self):
        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : lexpression DIVISION rexpression')
        @self.pg.production('expression : lexpression MULTIPLICACION rexpression')
        @self.pg.production('expression : lexpression RESTA rexpression')
        @self.pg.production('expression : lexpression SUM rexpression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'RESTA':
                return Sub(left, right)
            elif operator.gettokentype() == 'MULTIPLICACION':
                return Multiplicacion(left, right)
            elif operator.gettokentype() == 'DIVISION':
                return Division(left, right)
            else:
                raise AssertionError('Error: No es posible realizar la operacion, Operador desconocido!')

        @self.pg.production('lexpression : NUMBER')
        @self.pg.production('rexpression : NUMBER')
        def number(p):
            return Number(int(p[0].getstr()))

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
