class Figure:
    sides_count = 0

    def __init__(self, color):
        self.__sides = []
        self.__color = color
        self.filled = False

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides) == 1:
            self.__sides = [sides[0]]
        else:
            self.__sides = [1]

        self.__radius = self.__sides[0] / (2 * 3.14159)  # Длина окружности = 2 * pi * radius

    def get_square(self):
        return 3.14159 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides) == 3:
            self.__sides = list(sides)
        else:
            self.__sides = [1, 1, 1]

        # Рассчет высоты методом Герона с использованием сторон
        semi_perimeter = self.__len() / 2
        area = (semi_perimeter *
                 (semi_perimeter - self.__sides[0]) *
                 (semi_perimeter - self.__sides[1]) *
                 (semi_perimeter - self.__sides[2])) ** 0.5
        self.__height = (2 * area) / self.__sides[0]  # Берем первую сторону как основание

    def get_square(self):
        return (self.__sides[0] * self.__height) / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides) == 1:
            self.__sides = [sides[0]] * 12
        else:
            self.__sides = [1] * 12

    def get_volume(self):
        return self.__sides[0] ** 3  # Объем куба = a^3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume()) 