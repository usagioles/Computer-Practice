import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, y0, x0, h, x_end):
    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]

    for i in range(1, len(x_values)):
        y0 = y0 + h * f(x_values[i - 1], y0)
        y_values.append(y0)

    return x_values, y_values

# Задане диференціальне рівняння
def f(x, y):
    return x + np.cos(y / np.exp(1))

# Початкові умови
x0 = 1.4
y0 = 2.5

# Крок
h = 0.1

# Кінцева точка відрізку
x_end = 2.4

# Застосовуємо метод Ейлера
x_values, y_values = euler_method(f, y0, x0, h, x_end)

# Графік розв'язку
plt.plot(x_values, y_values, label='Euler Method')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler Method for y\' = x + cos(y/e)')
plt.legend()
plt.show()
