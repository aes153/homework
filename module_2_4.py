# list_ = ['one', 'two', 'three']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
# print(list_)

# for i in range(5):
#     print(i)
# print(list_)

# for i in range(len(list_)):
#     print(list_[i])
# print(list_)

# for i in range(len(list_)):
#     list_[i] = ':)'
# print(list_)

# list_2 = [1, 2, 3, 4, 5]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
# print(sum_)

# for i in range(1,11,2): #список от 1до 10 через 1
#     print(i)

# for i in range(1,11):
#     for j in range(1, 11):
#         print(i,end=' ')

# for i in range(1, 11):           # таблица умножения
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i*j}')

dict_ = {'a': 1, 'b': 2, 'c': 3}
# print(dict_)

# for i in dict_:          # вывод значения по ключу
#     print(i, dict_[i])

# for i, k in dict_.items():          #
#     print(i, k)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numbers.remove(1)
# for i in numbers:
#     print(i)

    # Исходный список чисел
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # Создаем пустые списки для простых и непростых чисел
    primes = []
    not_primes = []

    # Перебираем список numbers
    for number in numbers:
        if number <= 1:
            # Пропускаем числа 1 и меньше
            continue

        is_prime = True  # Предполагаем, что число простое

        # Проверяем делители от 2 до number (не включая number)
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False  # Если нашли делитель, число не простое
                break  # Прерываем проверку, так как число уже не простое

        # Добавляем число в соответствующий список
        if is_prime:
            primes.append(number)
        else:
            not_primes.append(number)

    # Выводим списки на экран
    print("Простые числа:", primes)
    print("Непростые числа:", not_primes)