import matplotlib.pyplot as plt 
import numpy as np

if __name__ == "__main__":
    A = np.array([1, 2])
    B = np.array([2, 5])

def plot_pic():
    # прямая 
    plt.plot([A[0], B[0]], [A[1], B[1]], color='blue')
    plt.scatter(A[0], A[1], color='red', alpha=1)
    plt.scatter(B[0], B[1], color='red', alpha=1)

    # нормаль
    normal = np.array([B[1] - A[1], A[0] - B[0]])
    mid_point = (A + B) / 2
    plt.arrow(mid_point[0], mid_point[1], normal[0], normal[1], color='red', 
              head_width=0.15, head_length=0.3, fc='red', ec='red')

    # подписи точек
    plt.text(A[0] + 0.2, A[1], 'A', fontsize=12, ha='right')
    plt.text(B[0] + 0.2, B[1], 'B', fontsize=12, ha='right')
    plt.text(mid_point[0] + normal[0]/2, mid_point[1] + normal[1]/2 + 0.2, 'n', fontsize=12, ha='right')

    # подписи координатных осей
    plt.xlabel("x", fontsize="xx-large",
    fontstyle="italic", family="serif")
    plt.ylabel("y", fontsize="xx-large",
    fontstyle="italic", family="serif")

    plt.show()

plot_pic()

# получение уравнения прямой
k = (B[1] - A[1]) / (B[0] - A[0])
b = A[1] - k * A[0]
print(f"Уравнение прямой: y = {k}x + ({b})")