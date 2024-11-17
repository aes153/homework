class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

h1 = House('ЖК Молодежный', 5)
h2 = House('ЖК Самолет', 16)
h3 = House('ЖК Изумрудный', 2)

print(h1)
print(h2)
print(h3)

print(len(h1))
print(len(h2))
print(len(h3))

