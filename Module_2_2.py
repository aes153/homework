# name = input('Введите Ваше имя: ')
# if name == 'Urban':
#     print("Здравствуйте, администратор")
# if name == "Анна":
#     print('Здравствуй, ученик')
# if name != 'Urban' and name != "Анна":
#     print('Привет,', name)

# number = int(input('Введите число: '))
# if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print('Число не подходит')

first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second == third:
    print(3)
elif first != second and first != third and second != third:
    print(0)
else:
    print(2)


