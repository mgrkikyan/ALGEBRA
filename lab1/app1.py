import numpy as np 
import matplotlib.pyplot as plt 
import math

if __name__ == "__main__":
	v = np.array([-1, -2])
	u = np.array([-3, 2])
	A = np.array([0, 2])

def plot_vectors():
	#подписи координатных осей
	plt.xlabel("x", fontsize="xx-large",
	fontstyle="italic", family="serif")
	plt.ylabel("y", fontsize="xx-large",
	fontstyle="italic", family="serif")

	#изображение векторов в виде стрелок
	plt.arrow(A[0], A[1], v[0], v[1], linewidth=2,
	head_width=0.1, head_length=0.1,
	length_includes_head=True)

	plt.arrow(A[0], A[1], u[0], u[1], linewidth=2,
	head_width=0.1, head_length=0.1,
	length_includes_head=True)

	#создание подписей для A, u, v
	dr = np.array([0.05, -0.2])
	dt = np.array([-0.5, 5.1])
	dp = np.array([2.5, -1.3])

	plt.text(A[0]+dr[0], A[1]+dr[1], "A", fontsize="xx-large", fontstyle="italic", family="serif")
	plt.text(v[0]+dt[0], v[1]+dt[1], "v", fontsize="xx-large", fontstyle="italic", family="serif")
	plt.text(u[0]+dp[0], u[1]+dp[1], "u",fontsize="xx-large", fontstyle="italic", family="serif")

	# Вычисляем точку B путем сложения векторов
	B = A + v + u #B=(-4; 2)
	
	# Векторы с помощью которых мы будем достраивать до параллелограмма
	z = B - v
	f = B - u

	x1, y1 = zip(z, B)
	x2, y2 = zip(f, B)
	plt.plot(x1, y1, linewidth=2, color='Blue')
	plt.plot(x2, y2, linewidth=2, color='Blue')

	plt.show()

plot_vectors()

vA = np.array([A[0]-v[0], A[1]-v[1]])
uA = np.array([A[0]-u[0], A[1]-u[1]])

# Вычисление векторного произведения
vp = np.cross(vA, uA)

# Вычисление модуля векторного произведения
vp_mod = np.linalg.norm(vp)

print("Модуль векторного произведения: ", vp_mod)