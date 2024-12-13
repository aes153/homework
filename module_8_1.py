#  Вариант 1

def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


# Вариант 2

a = input("Введите первое значение: ")
b = input("Введите второе значение: ")

def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)
try:
    a = float(a)
except ValueError:
    a = a
try:
    b = float(b)
except ValueError:
    b = b

print(add_everything_up(a, b))

