import numpy as np

# Создаем матрицу коэффициентов
A = np.array([[1, 2, -1],
              [2, -3, 1],
              [1, 1, -1]])

# Создаем вектор правой части уравнений
B = np.array([7, 3, 16])

# Инициализируем решения
X = np.zeros(3)

# Вычисляем определитель матрицы коэффициентов
detA = np.linalg.det(A)

# Вычисляем определитель для каждой неизвестной
for i in range(3):
    # Заменяем i-ый столбец матрицы коэффициентов на вектор правых частей
    A[:, i] = B

    # Вычисляем определитель новой матрицы
    detAi = np.linalg.det(A)

    # Вычисляем i-ую неизвестную
    X[i] = detAi / detA

    # Возвращаем исходную матрицу коэффициентов
    A = np.array([[1, 2, -1],
                  [2, -3, 1],
                  [1, 1, -1]])

# Выводим решение
print("Решение с использованием метода Крамера:")
print("x1 =", X[0])
print("x2 =", X[1])
print("x3 =", X[2])
