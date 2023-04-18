# На 5
import matplotlib.pyplot as plt
import numpy as np

# Коэффициенты параболы
a = 1
b = 2
c = 1

# Диапазон значений x
x_start = -5
x_stop = 5
x_step = 0.1

# Значения функции
x = np.arange(x_start, x_stop + x_step, x_step)
y = a*x**2 + b*x + c

# График
plt.plot(x, y)

# Добавляем заголовок и подписи к осям
plt.title("График параболы")
plt.xlabel("Ось x")
plt.ylabel("Ось y")

# Координатную сетку
plt.grid()

# Вывод графика на экран
plt.show()