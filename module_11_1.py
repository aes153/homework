import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont



# Работа с библиотекой numpy

array = np.arange(1, 15, 3)     # Создание массива чисел, содержащего ряд равномерно распределенных интервалов.

squared_array = np.power(array, 2)      # Вычисление квадрата каждого элемента

mean_value = np.mean(array)     # Вычисление среднего значения массива

sum_value = np.sum(array)       # Вычисление суммы элементов массива

print("Исходный массив:", array)
print("Массив квадратов:", squared_array)
print("Среднее значение:", mean_value)
print("Сумма элементов:", sum_value)



# Работа с библиотекой matplotlib

# Генерация случайных данных
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создание графика
plt.figure(figsize=(8, 4))  # Размер графика
plt.plot(x, y, label='Синус', color='red')  # Построение линии для синуса

# Настройка графика
plt.title('График функции синуса')  # Заголовок
plt.xlabel('x')  # Подпись оси x
plt.ylabel('sin(x)')  # Подпись оси y
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Горизонтальная линия y=0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Вертикальная линия x=0

# Отображение графика
plt.show()



# Работа с библиотекой pillow

image = Image.open('Figure_1.png')      # Открываем изображение

# Изменение размера изображения
new_size = (1000, 600)
resized_image = image.resize(new_size)

# Добавление текста
draw = ImageDraw.Draw(resized_image)
font = ImageFont.truetype("arial.ttf", 48)
text = "Добавили текст"
draw.text((300, 250), text, font=font, fill=0)

# Изменение цвета изображения на черно-белый
grayscale_image = resized_image.convert('L')

# Сохранение изображения в другом формате
grayscale_image.save("new_figure.jpg")

print(f"Изображение успешно обработано и сохранено в {grayscale_image}.")