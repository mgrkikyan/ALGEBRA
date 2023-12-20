<h2 style="text-align: center;">Бюджетное учреждение высшего образования Ханты-Мансийского автономного округа – Югры</h2>  

<h1 style="text-align: center;">«СУРГУТСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»</h1>

<h2 style="text-align: center;">Политехнический институт</h2>

<p style="text-align: center;">Кафедра прикладной математики</p>

<p style="text-align: center;">Гркикян Мисак Эдикович</p>

<h1 style="text-align: center;">ИНДИВИДУАЛЬНОЕ ЗАДАНИЕ №2</h1>

<p style="text-align: center;">Дисциплина «Алгебра и геометрия»</p>

<p style="text-align: center;">направление 01.03.02 «Прикладная математика и информатика»</p>

<p style="text-align: center;">направленность (профиль): «Технологии программирования и анализ данных»</p>

<pre>

</pre>

<p style="text-align: right;">Преподаватель: Шапошникова Ирина Вадимовна </p>

<p style="text-align: right;">Студент гр. № 601-31</p>

<p style="text-align: right;">Гркикян Мисак Эдикович</p>

<pre>




</pre>

<p style="text-align: center;">Сургут 2023 г.</p>



#### Задание 1

Даны две точки 𝐴 = (1, 2) и 𝐵 = (2, 5). Написать программу на языке
Python с использованием библиотек matplotlib и numpy, которая строит рисунок,
изобращающий прямую, проходящую через эти точки, а также единичный вектор n
нормали этой прямой. На рисунке должны быть подписаны оси 𝑂𝑥 и 𝑂𝑦, точки 𝐴 и
𝐵 и вектор n. Построенный рисунок должен приблизительно иметь вид, показанный
на рис. 1. Также программа должна выводить уравнение построенной прямой в виде
𝑦 = 𝑘𝑥 + 𝑏.

#### Программное решение 1

```python
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
```

#### Иллюстрация решения 1

![](рисунок1.png)
<p style="text-align: center;">Рис. 1.1. Иллюстрация решения задачи.</p>

![](вывод1.png)
<p style="text-align: center;">Рис. 2.1. Вывод программы в терминале.</p>


#### Задание 2

Дана точка 𝐴 = (−4,−3) и вектор u = (7,1). Написать программу на языке Python
с использованием библиотек matplotlib и numpy, которая строит рисунок, изобращающий
прямую, проходящую через точку 𝐴 в направлении вектора u, а также единичный вектор n
нормали этой прямой. На рисунке должны быть подписаны оси 𝑂𝑥 и 𝑂𝑦, точка 𝐴 и векторы
u и n. Также программа должна выводить уравнение построенной прямой в виде
𝑦 = 𝑘𝑥 + 𝑏.

#### Программное решение 2

```python
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
```

#### Иллюстрация решения 2

![](рисунок2.png)
<p style="text-align: center;">Рис. 1.2. Иллюстрация решения задачи.</p>

![](вывод2.png)
<p style="text-align: center;">Рис. 2.2. Вывод программы в терминале.</p>


#### Задание 3

Дана точка 𝐴 = (−2, 7) и вектор u = (−1, −1). Написать программу на
языке Python с использованием библиотек matplotlib и numpy, которая строит
рисунок, изобращающий прямую, проходящую через точку 𝐴 перпендикулярно
вектору u. На рисунке должны быть подписаны оси 𝑂𝑥 и
𝑂𝑦, точка 𝐴 и вектор u. Также программа должна выводить уравнение построенной
прямой в виде 𝑦 = 𝑘𝑥 + 𝑏.

#### Программное решение 3

```python
import numpy as np
import matplotlib.pyplot as plt

# Задаем точку A и вектор u
A = np.array([-2, 7])
u = np.array([-1, -1])

# Находим коэффициенты прямой
k = -u[0] / u[1]
b = A[1] - k * A[0]

# Создаем массив значений x
x = np.linspace(-10, 10, 100)

# Вычисляем соответствующие значения y
y = k * x + b

# Строим график
plt.plot(x, y, label='Прямая')
plt.scatter(A[0], A[1], color='red', label='Точка A')
plt.arrow(A[0], A[1], u[0], u[1], color='blue', width=0.1, head_width=0.5, length_includes_head=True, label='Вектор u')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Выводим уравнение прямой
print('Уравнение прямой: y = {}x + {}'.format(k, b))
```

#### Иллюстрация решения 3

![](рисунок3.png)
<p style="text-align: center;">Рис. 1.3. Иллюстрация решения задачи.</p>

![](вывод3.png)
<p style="text-align: center;">Рис. 2.3. Вывод программы в терминале.</p>