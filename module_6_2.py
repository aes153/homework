class Vehicle:
    __COLOR_VARIANTS = ['red', 'white', 'brown', 'blue', 'black']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'Модель: {self.__model}\n Мощность: {self.__engine_power}\n Цвет: {self.__color}\n Владелец: {self.owner}\n')

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass

vehicle1 = Sedan('Mary', 'Mercedes-Benz EQE', 408, 'blue')
vehicle1.print_info()

vehicle1.set_color('Yellow')
vehicle1.set_color('Red')
vehicle1.owner = 'Oleg'

vehicle1.print_info()





