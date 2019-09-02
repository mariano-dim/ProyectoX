#
#  Proyecto X
#  parser.py
#
#  Creato el 17/08/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

from src.Objects.varObjects import VariableObjects


class Parser(object):

    def __init__(self, tokens):
        # Abstract Syntax tree
        self.source_ast = {'main_scope': []}
        self.tokens = tokens
        self.token_index = 0
        self.transpiled_code = ""

    def parse(self):
        """ Parser
        Este metodo parseara los tokens dados como argumento y la convertira en un
        arbol AST(Abstract Syntax Trees)
        """
        while self.token_index < len(self.tokens):

            # Accede a los elementos de la Tupla, siendo que el primer elemento es el identificador
            # del Token y el segundo el valor del Token

            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            # print(token_type, token_value)

            # La primera palabra reservada del tipo variable nueva asignacion debe ser "var"
            # Se podria mejorar chequeando y enviando solamente la parte del stream que corresponde
            if token_type == "DECLARACION_DE_VARIABLE" and token_value == "var":
                self.parse_variable_declaration(self.tokens[self.token_index: len(self.tokens)])

            self.token_index += 1

        print("Codigo fuente generado...")
        print(self.transpiled_code)

        return self.source_ast

    # Este metodo atiende la declaracion de una variable
    def parse_variable_declaration(self, token_stream):

        token_checked = 0
        name = ""
        operator = ""
        value = ""

        # Verifico que la instruccion este completa
        # if len(token_stream) != 5:
        #     print("ERROR: Instruccion invalida, parece que hay menos elementos de los necesarios")
        #     print("Hay " + str(len(token_stream)) + " elementos en la instruccion")
        #     quit()

        # Para la asignacion de una variable el bucle va de 0 a 4 (5 posiciones).
        for token in range(0, len(token_stream)):

            token_type = token_stream[token_checked][0]
            token_value = token_stream[token_checked][1]

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

        varobj = VariableObjects()
        self.transpiled_code = varobj.transpile(name, operator, value)

        self.token_index += token_checked
