import random
def generate_password(n):
    result = ""

    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += str(i) + str(j)
    return result
n = random.randint(3,20)
print('Случайное число: ', n)
arbit = generate_password(n)
print('Шифр: ', arbit)
