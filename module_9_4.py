first = 'Пыхтит как пышка'
second = 'Пухлый мишка'

result = list(map(lambda f, s: f == s, first, second))
print(result)



def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Такой пример', ['У', 'медведя', 10, 'песен', 'и', 'все', 'про', 'мед'])



from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Вверх', 'Вниз', 'Направо', 'Налево')

print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())