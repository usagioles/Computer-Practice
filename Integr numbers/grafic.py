import tkinter as tk
from tkinter import ttk
import math

def f(x):
    return math.exp(-2*x+math.sin(x))

def middle(f, a, b, n):
    h = (b-a)/n
    result = 0
    for i in range(n):
        result += f(a+(i+0.5)*h)*h
    return result

def left(f, a, b, n):
    h = (b-a)/n
    result_l = 0
    for i in range(n):
        result_l += f(a+i*h)*h
    return result_l

def right(f, a, b, n):
    h = (b-a)/n
    result_r = 0
    for i in range(1, n):
        result_r += f(a+i*h)*h
    return result_r

def calculate_integral():
    a = float(entry_a.get())
    b = float(entry_b.get())
    n = int(entry_n.get())

    result_middle = middle(f, a, b, n)
    result_left = left(f, a, b, n)
    result_right = right(f, a, b, n)

    result_label.config(text=f"Серединні прямокутники: {result_middle}\nLeft прямокутники: {result_left}\nRight прямокутники: {result_right}")

# Створюємо вікно
window = tk.Tk()
window.title("Графічний інтерфейс для формул прямокутників")

# Створюємо та розміщуємо елементи у вікні
label_a = ttk.Label(window, text="a:")
label_a.grid(row=0, column=0, padx=10, pady=5)
entry_a = ttk.Entry(window)
entry_a.grid(row=0, column=1, padx=10, pady=5)

label_b = ttk.Label(window, text="b:")
label_b.grid(row=1, column=0, padx=10, pady=5)
entry_b = ttk.Entry(window)
entry_b.grid(row=1, column=1, padx=10, pady=5)

label_n = ttk.Label(window, text="n:")
label_n.grid(row=2, column=0, padx=10, pady=5)
entry_n = ttk.Entry(window)
entry_n.grid(row=2, column=1, padx=10, pady=5)

calculate_button = ttk.Button(window, text="Обчислити", command=calculate_integral)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Запускаємо головний цикл програми
window.mainloop()
