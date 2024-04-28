import numpy as np

# Создаем матрицу коэффициентов
A = np.array([[1, 1, 1, 1, 1],
              [0, 2, 1, 1, 1],
              [0, 0, 3, 1, 1],
              [0, 0, 0, 4, 1],
              [0, 0, 0, 0, 5]])

# Создаем вектор правой части уравнений
B = np.array([5, 4, 3, 2, 1])

# Используем функцию solve для решения системы
X = np.linalg.solve(A, B)

# Выводим решение
print("Решение с использованием функции solve:")
for i in range(len(X)):
    print("x" + str(i+1) + " =", X[i])