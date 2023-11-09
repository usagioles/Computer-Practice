'''
Розв'язування СЛАР методом Крамера
'''

import numpy as np

def get_det(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        D = 0
        for i in range(len(m)):  # i - індекс закресленого стовпця
            M = m[0, i]
            new_m = []

            for j in range(len(m)):
                for k in range(len(m)):
                    if (j != 0 and k != i):
                        new_m.append(m[j, k])

            new_m = np.array(new_m).reshape((len(m) - 1, len(m) - 1))

            if (i + 1) % 2 == 0:
                D += M * get_det(new_m)
            else:
                D -= M * get_det(new_m)

        return D


def kramer(A, b):
    '''
    Приймає дві змінних :
    A - данна матриця (numpy array типу float)
    b - стовпчик вільних членів (numpy array типу float)
    Повертає готовий розв'язок
    '''

    # Обчислюємо головний визначник, дельта
    D = get_det(A)

    if (D == 0):
        print("Неможливо розв'язати методом Крамера (дельта = 0)")
    else:
        dets = []

        for i in range(len(A)):
            copied_A = np.array(A)
            copied_A[:, i] = b
            dets.append(get_det(copied_A))

        # стовпець розв'язків
        x = []
        for curr_det in dets:
            x.append(float(curr_det) / D)

        return x


"Тестування"

A_list = [[[0.405, 0.05, 0.4, 0, 0.09],
           [-0.061, 0.63, 0.073, 0.11, -0.06],
           [0.07, -0.036, 0.38, 0.03, 0.02],
           [-0.05, 0, 0.066, 0.58, 0.23],
           [0, 0.31, -0.05, 0, 0.41]]]

b_list = [[-1.77, 0.503, 0.66, 2.72, -1.001]]

# Перетворюємо python масиви в numpy
for A in A_list:
    A = np.array(A, dtype=float)

for b in b_list:
    b = np.array(b, dtype=float)

for i in range(len(A_list)):
    print('Матриця:')
    for row in A_list[i]:
        print(row)

    print('Стовпець вільних членів:')
    print(b_list[i])

    print('Відповідь:')
    print(kramer(A, b))

