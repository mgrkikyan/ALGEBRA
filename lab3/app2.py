import numpy as np

# Заданные матрицы
A = np.array([[-1, 2, -4], [1, -1, 7], [-1, 0, 0]])
B = np.array([[1, 0, 0], [0, 2, 0], [1, 0, 3]])
C = np.array([[3, 8, -1], [0, 8, 0], [2, -1, 3]])

# Вычисление (A^2 * B + B^3 * A)^T
term1 = np.dot(np.dot(A, A), B)
term2 = np.dot(np.dot(B, B), np.dot(B, A))
result = np.transpose(term1 + term2)

# Решение уравнения (A^2 * B + B^3 * A)^T * X = B * C
X = np.linalg.solve(result, np.dot(B, C))

print(X)

# Проверка решения с использованием подстановки
equation = np.dot(np.transpose(term1 + term2), X)
print(np.allclose(equation, np.dot(B, C)))  # True, если все элементы достаточно близки (с учетом заданной точности)
print("\nРезультаты:")
print(X)