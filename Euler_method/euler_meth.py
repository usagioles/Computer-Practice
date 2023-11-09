import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Label, Entry, Button, Text, Scrollbar, messagebox

def euler_method(f, y0, x0, h, x_end):
    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]

    for i in range(1, len(x_values)):
        y0 = y0 + h * f(x_values[i - 1], y0)
        y_values.append(y0)

    return x_values, y_values

def differential_equation(x, y):
    return x + np.cos(y / np.exp(1))

def plot_solution(x_values, y_values):
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label='Метод Ейлера')
    ax.set(xlabel='x', ylabel='y', title='Метод Ейлера для y\' = x + cos(y/e)')
    ax.legend()

    # Встановлення меж графіка для обмеження масштабу
    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values), max(y_values))
    return fig

def on_calculate():
    try:
        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        h = float(entry_h.get())
        x_end = float(entry_x_end.get())

        x_values, y_values = euler_method(differential_equation, y0, x0, h, x_end)
        fig = plot_solution(x_values, y_values)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=5, columnspan=4)

        # Виведення значень x та y у текстове поле
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "x\t\t\ty\n")
        for x, y in zip(x_values, y_values):
            result_text.insert(tk.END, f"{x:.4f}\t\t{y:.4f}\n")
        result_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values")

# Створення графічного інтерфейсу
window = tk.Tk()
window.title("Метод Ейлера GUI")

Label(window, text="Початкове значення x (x0):").grid(row=0, column=0)
Label(window, text="Початкове значення y (y0):").grid(row=1, column=0)
Label(window, text="Крок (h):").grid(row=2, column=0)
Label(window, text="Границя відрізку (x_end):").grid(row=3, column=0)

entry_x0 = Entry(window)
entry_x0.grid(row=0, column=1)
entry_y0 = Entry(window)
entry_y0.grid(row=1, column=1)
entry_h = Entry(window)
entry_h.grid(row=2, column=1)
entry_x_end = Entry(window)
entry_x_end.grid(row=3, column=1)

calculate_button = Button(window, text="Обчислити", command=on_calculate)
calculate_button.grid(row=4, columnspan=2)

# Додавання текстового поля для виведення масиву значень x та y
result_text = Text(window, height=10, width=30, state=tk.DISABLED)
result_text.grid(row=6, columnspan=4)

# Додавання вертикального скролбару для текстового поля
scrollbar = Scrollbar(window, command=result_text.yview)
scrollbar.grid(row=6, column=4, sticky='ns')
result_text.config(yscrollcommand=scrollbar.set)

window.mainloop()

