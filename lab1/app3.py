import numpy as np
import matplotlib.pyplot as plt

A = np.array([3, 1])
B = np.array([-2, 3])
C = np.array([-4, 0])
D = np.array([-1, 3])

def plot_pic():

	plt.plot([A[0], D[0]], [A[1], D[1]], color='b')
	plt.plot([B[0], C[0]], [B[1], C[1]], color='b')
	plt.plot([C[0], A[0]], [C[1], A[1]], color='b')
	plt.plot([D[0], B[0]], [D[1], B[1]], color='b')
	plt.plot([C[0], D[0]], [C[1], D[1]], color='red', linestyle='--') # Это потом пригодится для вычиления площади
	plt.scatter(A[0], A[1], color='red', label='A=(3, 1)', alpha=1)
	plt.scatter(B[0], B[1], color='red', label='B=(-2, 3)', alpha=1)
	plt.scatter(C[0], C[1], color='red', label='C=(-4, 0)', alpha=1)
	plt.scatter(D[0], D[1], color='red', label='D=(-1, 3)', alpha=1)
	
	#создание подписей для A, u, v
	dA = np.array([0.0, 0.15])
	dB = np.array([-0.6, -0.1])
	dC = np.array([-0.3, 0.1])
	dD = np.array([0.4, -0.1])

	plt.text(A[0]+dA[0], A[1]+dA[1], "A", fontsize="xx-large", fontstyle="italic", family="serif")
	plt.text(B[0]+dB[0], B[1]+dB[1], "B", fontsize="xx-large", fontstyle="italic", family="serif")
	plt.text(C[0]+dC[0], C[1]+dC[1], "C", fontsize="xx-large", fontstyle="italic", family="serif")
	plt.text(D[0]+dD[0], D[1]+dD[1], "D", fontsize="xx-large", fontstyle="italic", family="serif")

	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.axhline(0, color='black',linewidth=0.5)
	plt.axvline(0, color='black',linewidth=0.5)
	plt.grid(True, linewidth=0.5, linestyle='dotted')

	plt.show()

plot_pic()

# Вычисление площади четырехугольника ABCD
# Для начала вычислим площади треугольников, которые образовались из-за диаагонали CD
def calculate_bdc():
	square_bdc = 0.5 * abs(((D[0]-C[0]) * (B[1]-C[1]) - (B[0]-C[0]) * (D[1]-C[1])))
	print(f"Площадь треугольника BDC = {square_bdc}")
	return square_bdc

square1 = calculate_bdc()

def calculate_adc():
	square_adc = 0.5 * abs(((D[0]-C[0]) * (A[1]-C[1]) - (A[0]-C[0]) * (D[1]-C[1])))
	print(f"Площадь треугольника ADC = {square_adc}")
	return square_adc

square2 = calculate_adc()

# Вычислим площадь четырехугольника ABCD, просуммировав площади треугольников 
sum = square1 + square2
print(f"Площадь четырехугольника ABCD = {sum}")