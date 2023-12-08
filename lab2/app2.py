import numpy as np
import matplotlib.pyplot as plt

# Координаты точки
x0, y0 = -4, -3

# Координаты вектора
a, b = 7, 1

# Параметрическое уравнение прямой
t = np.linspace(-1, 1, 400)
x = x0 + a * t
y = y0 + b * t

plt.scatter(x0, y0, color='red', alpha=1)
plt.text(x0, y0 - 0.15, 'A', fontsize=12, ha='right')

# Вектор нормали
normal = np.array([-b, a])
normal = normal / np.linalg.norm(normal)

# График
plt.plot(x, y, label="Прямая")
plt.arrow(x0, y0-0.5, a, b, head_width=0.1, head_length=0.15, fc='blue', ec='blue', label="Направляющий вектор")
plt.arrow(x0, y0, normal[0], normal[1], head_width=0.15, head_length=0.15, fc='red', ec='red', label="Вектор нормали")

# Подписи осей и векторов
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Вывод уравнения прямой
print(f'Уравнение прямой: (x - ({x0})) / {a} = (y - ({y0})) / {b}')

# Показать график
plt.show()


