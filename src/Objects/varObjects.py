#
#  Proyecto X
#  varObjects.py
#
#  Creato el 17/08/2019
#  Mariano Andres Di Maggio <mariano.dim@gmail.com>
#

class VariableObjects(object):

    def __init__(self):
        self.exec_string = ""

    def transpile(self, name, operator, value):
        self.exec_string += name + " " + operator + " " + value + "\n"
        return self.exec_string
