import math


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return b / a


def square(a):
    return a * a


def root(a):
    return math.sqrt(a)


class Calculator:
    result = 0

    def init(self):
        pass

    def add(self, a, b):
        a = int(a)
        b = int(b)
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        a = int(a)
        b = int(b)
        self.result = a - b
        return self.result

    def multiplication(self, a, b):
        a = int(a)
        b = int(b)
        self.result = multiplication(a, b)
        return self.result

