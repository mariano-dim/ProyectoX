#!/usr/bin/python
#
#  Proyecto X
#  parser.py
#
#  Creado el 17/08/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

from src.commands.variableDeclaration import VariableDeclaration


class Parser(object):

    def __init__(self, tokens):
        # Tabla de simbolos para el control de scope de variables
        self.symbol_tree = []
        # Abstract Syntax tree
        self.source_ast = {'main_scope': []}
        self.tokens = tokens
        self.token_index = 0
        self.transpiled_code = ""

    def parse(self):
        """ Parser
        Este metodo parseara los tokens dados como argumento y los convertira en un
        arbol AST(Abstract Syntax Trees)
        """
        while self.token_index < len(self.tokens):

            # Accede a los elementos de la Tupla, siendo que el primer elemento es el identificador
            # del Token y el segundo el valor del Token

            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            # Los primero que debo hacer es aplicar la gramatica principal y a partir de ahi ir bajando
            # en la definicion. Con el metodo de de recursion decendente, para cada no terminal hay
            # un procedimiento asociado

            # print(token_type, token_value)

            # La primera palabra reservada del tipo variable nueva asignacion debe ser "var"
            # Se podria mejorar chequeando y enviando solamente la parte del stream que corresponde
            if token_type == "VARIABLE_DECLARATION":
                # Nota: no es necesario que los tokens sea de la misma linea, la unica condicion necesaria
                # es que esten ordenados como en el programa fuente
                # En el caso de las instrucciones monolinea, como print, todos los tokens son de la misma linea
                # y no es necesario realizar un analisis de contexto
                variableDeclaration = VariableDeclaration(self.tokens[self.token_index: len(self.tokens)])
                # variableDeclaration.parseBasedOnTokenIndex()
                if variableDeclaration.parseBasedOnGrammar() == False:
                    print("ERROR: parseBasedOnGrammar")
                self.token_index += variableDeclaration.token_index

            self.token_index += 1

        return self.source_ast
