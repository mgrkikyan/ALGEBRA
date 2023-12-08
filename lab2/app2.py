import numpy as np
import matplotlib.pyplot as plt

# Задаем точку A и вектор u
A = np.array([-4, -3])
u = np.array([7, 1])

# Вычисляем координаты конечной точки прямой
B = A + u

# Вычисляем нормальный вектор к прямой
n = np.array([-u[1], u[0]])

# Вычисляем коэффициенты уравнения прямой y = kx + b
k = u[1] / u[0]
b = A[1] - k * A[0]

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Рисуем прямую, проходящую через точку A в направлении вектора u
ax.plot([A[0], B[0]], [A[1], B[1]], 'r', label='Прямая')

# Рисуем нормальный вектор
ax.arrow(A[0], A[1], n[0], n[1], head_width=0.5, head_length=0.5, fc='b', ec='b', label='Нормаль')

# Подписываем оси
ax.set_xlabel('x')
ax.set_ylabel('y')

# Подписываем точку A и векторы u и n
ax.annotate('A', A, textcoords="offset points", xytext=(-10,-10), ha='center')
ax.annotate('u', B, textcoords="offset points", xytext=(10,10), ha='center')
ax.annotate('n', A + n, textcoords="offset points", xytext=(-10,10), ha='center')

# Выводим уравнение прямой
print(f'Уравнение прямой: y = {k}x + {b}')

# Выводим график
plt.legend()
plt.grid(True)
plt.show()
