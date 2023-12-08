
<h2 style="text-align: center;">Бюджетное учреждение высшего образования Ханты-Мансийского автономного округа – Югры</h2>  

<h1 style="text-align: center;">«СУРГУТСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»</h1>

<h2 style="text-align: center;">Политехнический институт</h2>

<p style="text-align: center;">Кафедра прикладной математики</p>

<p style="text-align: center;">Гркикян Мисак Эдикович</p>

<h1 style="text-align: center;">ИНДИВИДУАЛЬНОЕ ЗАДАНИЕ №1</h1>

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

<h3 style="text-align: center;">Индивидуальное задание №1</h3>

#### Задание

Вычислить пределы данных числовых последовательностей двумя способами: 

- аналитически 
- используя библиотеки Python для символьных вычислений. 

<p style="text-align: justify;">Для каждой числовой последовательности $\{x_k\}_{k=1}^\infty$ на одном рисунке построить (используя графические пакеты Python) следующие множества точек ($k = 1, \ldots, m$):</p>

- (k, 0) – синий цвет
- (0, $x_k$) – зеленый цвет
- (k, $x_k$) – красный цвет

<p style="text-align: justify;">В случае, если последовательность сходится, построить на соответствующем рисунке точку (оранжевый цвет) изображающую предел последовательности $\{x_k\}_{k=1}^\infty$.</p> 

<p style="text-align: justify;">В задаче 1 для сходящихся последовательностей, для заданного $\varepsilon>0$ найти такой номер $n(\varepsilon)$, начиная с которого $|x_k-A|<\varepsilon, \forall k\geq n(\varepsilon)$ </p>

#### Аналитическое решение

Рассмотрим предел: 

$\lim\limits_{n\rightarrow\infty}\frac{-3n^3+4n^2-8n-6}{4n^2+2n}$

Найдем пределы числителя и знаменателя: 

  - $\lim\limits_{n\rightarrow\infty}(-3n^3+4n^2-8n-6)=-\infty$
  - $\lim\limits_{n\rightarrow\infty}(4n^2+2n)=+\infty$

<p style="text-align: justify;">Поскольку выражение $\frac{-\infty}{\infty}$ является неопределенностью, преобразуем его, деля каждое слагаемое в числителе и знаменателе на старшую степень, в данном случае это $n^3$:</p>

$\lim\limits_{n\rightarrow\infty}\frac{-3n^3+4n^2-8n-6}{4n^2+2n} = \lim\limits_{n\rightarrow\infty} \frac{\frac{-3n^3+4n^2-8n-6}{n^3}}{\frac{4n^2+2n}{n^3}} = \lim\limits_{n\rightarrow\infty} \frac{-3 + \frac{4}{n} - \frac{8}{n^2} - \frac{6}{n^3}}{\frac{4}{n} + \frac{2}{n^2}}$

Вычислим предел числителя, вычисляя предел каждого слагаемого:

- $\lim\limits_{n\rightarrow\infty} (-3 + \frac{4}{n} - \frac{8}{n^2} - \frac{6}{n^3})$
   - $\lim\limits_{n\rightarrow\infty} (-3) = 3$
   - $\lim\limits_{n\rightarrow\infty}\frac{4}{n} = 0$
   - $\lim\limits_{n\rightarrow\infty}(- \frac{8}{n^2}) = 0$
   - $\lim\limits_{n\rightarrow\infty}(- \frac{6}{n^3}) = 0$

Следовательно:
$\lim\limits_{n\rightarrow\infty} (-3 + \frac{4}{n} - \frac{8}{n^2} - \frac{6}{n^3}) = - 3 + 0 + 0 + 0 = -3$

Аналогично для знаменателя:
$\lim\limits_{n\rightarrow\infty}(\frac{4}{n} + \frac{2}{n^2}) = 0$

<p style="text-align: justify;">Таким образом, предел числителя равен $-3$, а предел знаменателя равен $0$. Отношение сходящейтся последовательности к бесконечно малой является бесконечно большой, причем в данном случае знаменатель всегда положителен, а предел числителя отрицателен, поэтому предел будет равен $-\infty$: </p>

$\lim\limits_{n\rightarrow\infty}\frac{-3n^3+4n^2-8n-6}{4n^2+2n} = -\infty$

Ответ: $-\infty$

#### Программное решение

<p></p>

```python
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def sequence(n):
    return (-3*n**3 + 4*n**2 - 8*n - 6) / (4*n**2 + 2*n)

def plot_points(m):
    x = np.arange(1, m+1)
    y = sequence(x)

    # (k, 0) - blue colour
    plt.plot(x, np.zeros_like(x), 'bo', label='$(k, 0)$')

    # (0, x_k) - green color
    plt.plot(np.zeros_like(x), y, 'go', label='$(0, x_k)$')

    # (k, x_k) - red color
    plt.plot(x, y, 'ro', label='$(k, x_k)$')

    plt.xlabel('$k$')
    plt.ylabel('$x_k$')
    plt.legend()
    plt.grid()
    plt.show()

m = 20  # number of points
plot_points(m)

n = Symbol("n")  
a = limit((-3*n**3+4*n**2-8*n-6)/(4*n**2+2*n), n, oo)  
print(a) 
```
<pre>

</pre>

#### Иллюстрация решения

![](image_1.png)
<p style="text-align: center;">Рис. 1. Иллюстрация решения задачи.</p>

![](image_2.png)
<p style="text-align: center;">Рис. 2. Вывод программы в терминале.</p>
