#
#  Proyecto X
#  lexer.py
#
#  Creato el 17/08/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

import re


class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

    @property
    def tokenize(self):

        """ Tokenize

                Este metodo se utiliza para tokenizar el archivo de codigo fuente y retornar
                los tokens al parser para que este pueda construir el AST

                Argumentos:
                    source_code (str) : Este es el archivo con el codigo fuente X a tokenizar

                Retorna:
                    tokens (list) : Retorna una lista completa de Tokens
        """

        tokens = []

        # Antes de realizar el split, reemplazo las apariciones del caracter ";" por " ;", de esa
        # forma evito tener que analizar en cada caso si el ultimo caracter de un identificador es
        # dicho caracter
        source_code = self.source_code.replace(";", " ; ").split()

        # print("Imprimiendo Source Code Spliting")
        # Cuando realizo el split, los separadores se pierden, por lo tanto no es factible separar por un
        # valor que luego voy a necesitar
        # print(source_code)

        source_index = 0

        while source_index < len(source_code):

            word = source_code[source_index]

            # Cada token es una tupla o un par de valores, el primero identifica el tipo de Token
            # y el segundo valor representa el valor de ese tipo
            if word in "\n": pass

            if word == "var":
                tokens.append(["DECLARACION_DE_VARIABLE", word])

            elif re.match("[a-z]", word) or re.match("[A-Z]", word):
                tokens.append(["IDENTIFICADOR", word])

            elif re.match("[0-9]", word):
                tokens.append(["ENTERO", word])

            # elif re.match("\'[a-z..A-Z]\'", word):
            #     tokens.append(["CADENA", word])

            elif word in "=":
                tokens.append(["OPERADOR", word])

            if word in ";":
                tokens.append(["FIN_DE_INSTRUCCION", ";"])

            source_index += 1

        return tokens
