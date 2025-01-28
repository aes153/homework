class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.set_sides(*sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14159)   # Длина окружности = 2 * π * r

    def get_square(self):
        return 3.14159 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)


    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Формула Герона


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self._Figure__sides = [new_sides[0]] * self.sides_count
        elif len(new_sides) == self.sides_count:
            self._Figure__sides = list(new_sides)
        # else:
        #     self.__sides = self.__sides[0] * self.sides_count

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle = Circle((200, 200, 100), 10)
triangle = Triangle((255, 0, 80), (20, 8, 10))
cube = Cube((222, 35, 130), 8)

# Изменение цвета:
circle.set_color(55, 66, 77)
print(circle.get_color())

triangle.set_color(45, 0, 55)
print(triangle.get_color())

cube.set_color(300, 70, 15)
print(cube.get_color())

# Изменение сторон:
cube.set_sides(4)
print(cube.get_sides())

circle.set_sides(15)
print(circle.get_sides())

triangle.set_sides(25, 12, 17)
print(triangle.get_sides())

# Периметр/длина круга:
print(len(cube))
print(len(circle))
print(len(triangle))

# Объём куба:
print(cube.get_volume())
