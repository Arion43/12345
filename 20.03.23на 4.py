# на 4
a = 1
b = 2
c = 1

# Диапазон значений x
x_start = -5
x_stop = 5
x_step = 1

# Заголовок таблицы
print("{0:10} | {1:10}".format("x", "y"))
print("-" * 25)

# Таблица значений
for x in range(x_start, x_stop + x_step, x_step):
    y = a*x**2 + b*x + c
    print("{0:10} | {1:10}".format(x, y))