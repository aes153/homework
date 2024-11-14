class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        # self.new_floor = (1, new_floor)
        # print(f'Введите номер этажа: {new_floor}')
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
h1 = House('ЖК Молодежный', 5)
h2 = House('ЖК Самолет', 16)
h3 = House('ЖК Изумрудный', 2)

h1.go_to(7)
h2.go_to(4)
h3.go_to(0)