import numpy as np

A = np.array([[2, -1, -1], [0, 2, -1], [0, 0, -1]])
B = np.array([[-1, 0, 0], [1, -3, 0], [1, 1, -5]])

# Вычисляем A^3, A^2 и A
A_cubed = np.linalg.matrix_power(A, 3)
A_squared = np.linalg.matrix_power(A, 2)

# Вычисляем выражение (A^3 - 2A^2 + 3A)
expression = A_cubed - 2 * A_squared + 3 * A

# Вычисляем транспонированное выражение
expression_transpose = expression.T

# Вычисляем 4B^2 - B
B_squared = np.linalg.matrix_power(B, 2)
result = 4 * B_squared - B

# Решаем уравнение (A^3 - 2A^2 + 3A)^T * X = 4B^2 - B
X = np.linalg.solve(expression_transpose, result)

print(X)

