class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Identificator():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value.value


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class AssignParameters():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ConcatenateStrings(BinaryOp):
    def eval(self):
        leftOp = self.left
        rightOp = self.right
        value = self.left.eval() + self.right.eval()
        return value


class Assign(AssignParameters):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Multiplicacion(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Division(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
