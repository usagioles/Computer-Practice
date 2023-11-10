import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

def f(x):
    return math.cos(2/x)-2*math.sin(1/x)+1/x

def half_div(a, b, e):
    k = 0
    while True:
        x = (a + b) / 2.0
        k += 1
        if abs(f(x)) < e:
            break
        if f(a) * f(x) < 0:
            a = a
            b = x
        else:
            a = x
            b = b

    return x, k

def plot_graph(a, b, x_root):
    x_values = [i for i in range(int(a) - 1, int(b) + 2)]
    y_values = [f(x) for x in x_values]

    plt.plot(x_values, y_values, label='f(x)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(x_root, color='red', linestyle='--', label='Root x')
    plt.legend()
    plt.title('Graph of f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')

def calculate():
    a = float(entry_a.get())
    b = float(entry_b.get())
    e = float(entry_e.get())

    result, iterations = half_div(a, b, e)
    result_label.config(text=f"Корінь x = {result}")
    iterations_label.config(text=f"К-сть ітерацій k = {iterations}")

    # Графік
    plot_graph(a, b, result)
    canvas.draw()

# Створення головного вікна
root = tk.Tk()
root.title("Метод половинного ділення")
label_prog = tk.Label(root, text="Рівняння cot(x) - x/4 = 0")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Створення і розміщення елементів у вікні
ttk.Label(frame, text="Введіть початок відрізку (a):").grid(column=0, row=0, sticky=tk.W)
entry_a = ttk.Entry(frame)
entry_a.grid(column=1, row=0, sticky=tk.W)

ttk.Label(frame, text="Введіть кінець відрізку (b):").grid(column=0, row=1, sticky=tk.W)
entry_b = ttk.Entry(frame)
entry_b.grid(column=1, row=1, sticky=tk.W)

ttk.Label(frame, text="Точність (e):").grid(column=0, row=2, sticky=tk.W)
entry_e = ttk.Entry(frame)
entry_e.grid(column=1, row=2, sticky=tk.W)

calculate_button = ttk.Button(frame, text="Обчислити", command=calculate)
calculate_button.grid(column=0, row=3, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=4, columnspan=2)

iterations_label = ttk.Label(frame, text="")
iterations_label.grid(column=0, row=5, columnspan=2)

# Matplotlib setup
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=1, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.mainloop()
