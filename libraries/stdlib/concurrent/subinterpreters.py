"""Demonstration of subinterpreters implemented in Python 3.14"""

from concurrent import interpreters


interpreter = interpreters.create()
interpreter.exec("print('hello subinterpreter')")

def square(n):
    return n * n

print(interpreter.call(square, 15))

