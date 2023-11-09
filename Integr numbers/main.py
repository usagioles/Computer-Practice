import tkinter as tk
import math


def middle(f, a, b, n):
    h = (b-a)/n
    result = 0
    for i in (range(n)):
        result += f(a+(i+0.5)*h)*h
    return result


def left(f, a, b, n):
    h = (b-a)/n
    result_l = 0
    for i in (range(n)):
        result_l += f(a+i*h)*h
    return result_l


def right(f, a, b, n):
    h = (b-a)/n
    result_r = 0
    for i in (range(1, n)):
        result_r += f(a+i*h)*h
    return result_r


def f(x):
    return math.exp(-2*x+math.sin(x))


a = float(input("a: "))
b = float(input("b: "))
n = int(input("n: "))
result = middle(f, a, b, n)
result_l = left(f, a, b, n)
result_r = right(f, a, b, n)
print("Серединні прямокутн ", result)
print("Left прямокутн ", result_l)
print("Right прямокутн ", result_r)
