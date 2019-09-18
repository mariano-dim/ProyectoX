#!/usr/bin/python
#
#  Proyecto X
#  variableDeclaration.py
#
#  Creato el 15/09/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

from src.exceptions.exceptions import SyntaxException


class VariableDeclaration:

    def __init__(self, token_stream):
        self.token_stream = token_stream
        self.token_index = 0
        self.actual_token_type = None
        self.actual_token_value = None

    def parseBasedOnGrammar(self):
        print(self.token_stream)


        # Gramatica basica para la deginicion de variables-->No es recursiva, pero esta alcanzada por
        # una gramatica de mas alto nivel que si es recursiva
        # <variable-declaration> ::= <variable-type> <variable-name> = <variable-valor>
        # <variable-type> ::= string | integer | Boolean
        # <variable-name> ::= LETRAS_Y_NUMEROS
        # <variable-valor> ::= LETRAS_Y_NUMEROS

        print("parseBasedOnGrammar")

        self.actual_token_type = self.token_stream[self.token_index][0]
        self.actual_token_value = self.token_stream[self.token_index][1]
        if not self.matchVariableType(self.actual_token_type, self.actual_token_value):
            print("ERROR: not matchVariableType in an expression")
            return bool("False")

        self.token_index += 1
        self.actual_token_type = self.token_stream[self.token_index][0]
        self.actual_token_value = self.token_stream[self.token_index][1]
        if not self.matchVariableName(self.actual_token_type, self.actual_token_value):
            print("ERROR: not matchVariableName in an expression")
            return bool("False")

        self.token_index += 1
        self.actual_token_type = self.token_stream[self.token_index][0]
        self.actual_token_value = self.token_stream[self.token_index][1]
        if not self.matchVariableOperator(self.actual_token_type, self.actual_token_value):
            print("ERROR: not matchVariableOperator in an expression")
            return bool("False")

        self.token_index += 1
        self.actual_token_type = self.token_stream[self.token_index][0]
        self.actual_token_value = self.token_stream[self.token_index][1]
        self.matchVariableValue(self.actual_token_type, self.actual_token_value)

        return bool("True")

    def matchVariableType(self, token_type, token_value):
        print("matchVariableType")
        if token_type not in ["INTEGER", "STRING", "BOOLEAN"]:
            return bool("False")

    def matchVariableName(self, token_type, token_value):
        print("matchVariableName")
        if token_type not in ["IDENTIFICADOR"]:
            return bool("False")

    def matchVariableOperator(self, token_type, token_value):
        print("matchVariableOperator")
        if token_type not in ["OPERATOR"]:
            return bool("False")


    def match(self, t):
        if self.look.tag == t:
            self.move()
        else:
            self.error("syntax error")

    def error(self, s):
        raise SyntaxException("Error generico")


    def matchVariableValue(self, token_type, token_value):
        print("matchVariableValue")

    def parseBasedOnTokenIndex(self):
        print(self.token_stream)
        token_checked = 0

        # Verifico que la instruccion este completa
        # if len(token_stream) != 5:
        #     print("ERROR: Instruccion invalida, parece que hay menos elementos de los necesarios")
        #     print("Hay " + str(len(token_stream)) + " elementos en la instruccion")
        #     quit()

        # Para la asignacion de una variable el bucle va de 0 a 4 (5 posiciones).
        for token in range(0, len(self.token_stream)):

            token_type = self.token_stream[token_checked][0]
            token_value = self.token_stream[token_checked][1]

            # Chequear que pasa si la instruccion esta formada unicamente por "var ;"
            # El error se daria solamente si el stream de token tiene dos elementos, chequear
            # Si se detecta el final de instruccion se sale del bucle
            if token == 4 and token_type == "FIN_DE_INSTRUCCION":
                print("Fonalizacion de instruccion: " + token_value)
                break
            elif token == 4 and token_type not in ["FIN_DE_INSTRUCCION"]:
                print("ERROR: Finalizacion de instruccion invalido: '" + token_value + "'")
                quit()

            elif token == 1 and token_type == "IDENTIFICADOR":
                print("Nombre de variable: " + token_value)
                name = token_value
            elif token == 1 and token_type != "IDENTIFICADOR":
                print("ERROR: Nombre de variable erroneo: ' " + token_value + "'")
                quit()

            elif token == 2 and token_type == "OPERADOR":
                print("Operador de asignacion: " + token_value)
                operator = token_value
            elif token == 2 and token_type != "OPERADOR":
                print("ERROR: Operador de asignacion no existe o es invalido. Este deberia ser =")
                quit()

            elif token == 3 and token_type in ["ENTERO"]:
                print("Valor de Variable: " + token_value)
                value = token_value
            elif token == 3 and token_type not in ["ENTERO"]:
                print("ERROR: Valor de asignacion de variable invalido: '" + token_value + "'")
                quit()

            token_checked += 1

        self.token_index += token_checked
