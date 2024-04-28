import numpy as np

# Заданные матрицы
A = np.array([[4, -1, 7], [0, 1, -2], [0, 0, 9]])
B = np.array([[-1, 1, 0], [0, 0, 3], [6, 2, -1]])
C = np.array([[5, 1, 1], [1, 5, 1], [1, 1, 5]])

# Вычисление B^T и A^T
B_T = np.transpose(B)
A_T = np.transpose(A)

# Вычисление (A+3B^T) и (3A^T-B)
term1 = np.add(A, 3*B_T)
term2 = 3*A_T - B

# Вычисление (A+3B^T)(3A^T-B)
product = np.dot(term1, term2)

# Решение уравнения (A+3B^T)(3A^T-B)X = C
X = np.linalg.solve(product, C)

# Проверка решения с использованием подстановки
equation = np.dot(np.dot((A+3*B_T), (3*A_T-B)), X)
print(np.allclose(equation, C))  # True, если все элементы достаточно близки (с учетом заданной точности)
print("\nРезультаты:")
print(X)