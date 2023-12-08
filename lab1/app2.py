import numpy as np
import matplotlib.pyplot as plt

# Задание векторов
a = np.array([1, -1])
b = np.array([2, -3])
c = np.array([-2, 5])
d = np.array([1, 3])

# Создание фигуры и осей
fig, ax = plt.subplots()

def plot_vectors():
	# Построение векторов
	ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='r', label='a')
	ax.quiver(a[0], a[1], b[0], b[1], angles='xy', scale_units='xy', scale=1, color='g', label='b')
	ax.quiver(a[0]+b[0], a[1]+b[1], c[0], c[1], angles='xy', scale_units='xy', scale=1, color='b', label='c')
	ax.quiver(a[0]+b[0]+c[0], a[1]+b[1]+c[1], d[0], d[1], angles='xy', scale_units='xy', scale=1, color='m', label='d')
	ax.quiver(0, 0, a[0]+b[0]+c[0]+d[0], a[1]+b[1]+c[1]+d[1], angles='xy', scale_units='xy', scale=1, color='k', label='a+b+c+d')

	# Настройка осей и меток
	ax.set_xlim([-6, 6])
	ax.set_ylim([-6, 6])
	ax.axhline(0, color='black',linewidth=0.5)
	ax.axvline(0, color='black',linewidth=0.5)
	ax.set_xlabel('Ox')
	ax.set_ylabel('Oy')

	# Добавление легенды
	ax.legend()

	# Отображение рисунка
	plt.show()

plot_vectors()