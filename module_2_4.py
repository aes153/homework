numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []                  # простые числа
not_primes = []              # не простые числа

for i in numbers:            # i - число из списка
    if i == 1:
      continue
    is_prime = True
    for j in range(2, i):    # j - делитель
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print("Простые числа:", primes)
print("Составные числа:", not_primes)