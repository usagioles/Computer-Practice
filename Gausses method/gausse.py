import numpy as np

'''
Розв'язування СЛАР методом Гауса
'''

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

def gaussian(A, b):
    '''
    Приймає дві змінних :
    A - данна матриця (numpy array типу float)
    b - стовпчик вільних членів (numpy array типу float)
    Повертає готовий розв'язок
    '''

    # створюємо розширену матрицю
    reshaped_b = b.reshape((len(b), 1))
    A = np.hstack((A, reshaped_b))

    # i - основний рядок
    # j - данний рядок (завжди < i)
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            A[j] -= A[i] * A[j][i] / A[i][i]

    # обернено
    x = np.array([0] * len(b), dtype=float)  # вільні члени

    i = len(A) - 1
    while i >= 0:
        x[i] = (A[i][-1] - sum(x * A[i][0:-1])) / A[i][i]
        i -= 1

    return x


A_list = [[[0.405, 0.05, 0.4, 0, 0.09],
           [-0.061, 0.63, 0.073, 0.11, -0.06],
           [0.07, -0.036, 0.38, 0.03, 0.02],
           [-0.05, 0, 0.066, 0.58, 0.23],
           [0, 0.31, -0.05, 0, 0.41]]]

b_list = [[-1.77, 0.503, 0.66, 2.72, -1.001]]


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
    print(gaussian(A, b), '\n')