# Дополнительное практическое задание по модулю: "Наследование классов."
# Задание "Они все так похожи":
# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут
# обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированы и для них должны быть написаны
# интерфейсы взаимодействия (методы) - геттеры и сеттеры.

import math

class Figure:
    def __init__(self, sides, color=(255, 255, 255), filled=True, sides_count = 0):
        self.sides_count = sides_count
        if sides_count != len(sides) or not self.__is_valid_sides(*sides, new=True):
            sides = [1] * sides_count
            print('\033[91mСтороны введены с ошибкой, меняем на единичные значения\033[0m')
        self.__sides = sides
        if len(color) != 3 or not self.__is_valid_color(*color):
            color = (255, 255, 255)
            print('\033[91mЦвет введен с ошибкой, меняем на белый\033[0m')
        self.__color = color
        self.filled = filled

    def __str__(self):
        list_ = list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', self.__dict__.keys(),
                         self.__dict__.values()))
        return f'Атрибуты объекта: {self.__class__.__name__}\n' + ' '.join(list_)

    def __len__(self):
        """
        Метод __len__ должен возвращать периметр фигуры.
        :return: периметр фигуры
        """
        return sum(list(self.__sides))

    def get_color(self):
        """
        возвращает список RGB цветов.
        :return: список RGB цветов.
        """
        return list(self.__color)

    def get_sides(self):
        """
        возвращает список сторон.
        :return: список сторон.
        """
        return self.__sides


    def __is_valid_color(self, r, g, b):
        """
        Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет
        корректность переданных значений перед установкой нового цвета. Корректным цвет:
        все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        :param r: красный
        :param g: зеленый
        :param b: синий
        :return: boolean - корректно или нет введены цвета
        """
        return True if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255) else False

    def set_color(self, r=None, g=None, b=None):
        """
        Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color
        на соответствующие значения, предварительно проверив их на корректность.
        Если введены некорректные данные, то цвет остаётся прежним.
        :param r: красный
        :param g: зеленый
        :param b: синий
        :return: boolean - корректно или нет введены цвета
        """
        if b != None and self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            return True
        else:
            print('\033[91mЦвет введен с ошибкой. Цвет останется прежним.\033[0m')
            return False

    def __is_valid_sides(self, *sides, new = False):
        """
        Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
        возвращает True если все стороны целые положительные числа и кол-во новых
        сторон совпадает с текущим, False - во всех остальных случаях.
        :param sides: список сторон
        :return: boolean - корректно или нет введены стороны
        """
        if not new and len(sides) != len(self.__sides):
            return False
        for i in sides:
            if i <= 0:
                return False
        return True

    def set_sides(self, *sides):
        """
        Метод set_sides принимает неограниченное кол-во сторон, проверяет корректность
        переданных данных, если данные корректны, то меняет __sides на новый список,
        если нет, то оставляет прежние.
        :param sides: список кторон
        :return: boolean - корректно или нет введены стороны
        """
        if not self.__is_valid_sides(*sides):
            print('\033[91mСтороны введены с ошибкой. Изменение сторон не было произведено.\033[0m')
            return False
        self.__sides = list(sides)
        return True


class Circle(Figure):
    def __init__(self, color, *sides, filled=True):
        super().__init__(list(sides), color, filled, sides_count = 1)
        self.__radius = self._Figure__sides[0] / (2 * math.pi)

    def get_square(self):
        """
        Метод get_square возращает площадь круга (можно рассчитать как через длину,
        так и через радиус).
        :return: площадь круга
        """
        return math.pi * self.__radius ** 2

    def set_sides(self, *sides):
        """
        Переопределено из родительского класса
        :param sides: стороны
        :return: boolean - корректно или нет введены стороны
        """
        super().set_sides(*sides)
        self.__radius = self._Figure__sides[0] / (2 * math.pi)

class Triangle(Figure):

    def __init__(self, color, *sides, filled=True):
        if len(sides) == 3 and (sides[0] + sides[1] < sides[2] or sides[0] + sides[2] < sides[1]
                                or sides[2] + sides[1] < sides[0]):
            print(f'\033[91mНевозможно построить треугольника с такими сторонами {sides}. Меняем стороны на единичные.\033[0m')
            sides = [1]*3

        super().__init__(list(sides), color, filled, sides_count = 3)
        self.__height = 2 * self.get_square() / self._Figure__sides[0]

    def get_square(self):
        """
        Метод get_square возращает площадь треугольника.
        :return: площадь треугольника
        """
        a, b, c = self._Figure__sides
        if a + b < c or a + c < b or c + b < a:
            return (f'\033[91mПлощадь расчитать невозмодно, т.к. треугольника с такими сторонами'
                    f'({a}, {b}, {c}) не существует\033[0m')
        p = sum(self._Figure__sides) / 2
        return math.sqrt(p * (p - a) * (p - b) *
                         (p - c))

    def set_sides(self, *sides):
        """
        Переопределено из родительского класса
        :param sides: стороны
        :return: boolean - корректно или нет введены стороны
        """
        super().set_sides(*sides)
        self.__height = 2 * self.get_square() / self._Figure__sides[0]


class Cube(Figure):
    def __init__(self, color, *sides, filled=True):
        sides = list(sides)*12
        super().__init__(sides, color, filled, sides_count = 12)

    def get_volume(self):
        """
        Метод get_volume, возвращает объём куба.
        :return: объём куба
        """
        return (len(self) / 12) ** 3

    def set_sides(self, *sides):
        """
        Переопределено из родительского класса
        :param sides: стороны
        :return: boolean - корректно или нет введены стороны
        """
        sides = list(sides) * 12
        super().set_sides(*sides)



if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    cube1.set_color(300, 70, 15) # Не изменится
    print(circle1.get_color())
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    circle1.set_sides(15) # Изменится
    print(cube1.get_sides())
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # ===============================================================
    print('\n\033[93mДополнительные проверки: \033[0m\n')
    print(circle1, '\n', cube1)
    print(f'Площадь круга: {circle1.get_square()}, периметр круга: {len(circle1)}')
    print(f'Объем куба: {cube1.get_volume()}, периметр всех граней куба: {len(cube1)}\n')

    triangle1 = Triangle((50, 50, 350), 6, filled=False)
    print(triangle1)
    triangle1 = Triangle((100, 150, 150), 6, 7, 20, filled=False)
    print(triangle1)
    print(f'Площадь треугольника: {triangle1.get_square()}, периметр треугольника: {len(triangle1)}\n')


    triangle1 = Triangle((50, 50, 50), 6, 5, 8, filled=False)
    print(triangle1)
    print(f'Площадь треугольника: {triangle1.get_square()}, периметр треугольника: {len(triangle1)}\n')

    print(f'Площадь круга: {circle1.get_square()}')

    choice_dic = {
        0: 'Завершить работу,',
        1: 'Задать круг,',
        2: 'Вывести площадь круга,',
        3: 'Задать треугольник,',
        4: 'Вывести площадь треугольника,',
        5: 'Задать куб,',
        6: 'Вывести объем куба,',
        7: 'Вывести цвет,',
        8: 'Изменить цвет,',
        9: 'Вывести стороны,',
        10: 'Изменить стороны,',
        11: 'Вывести периметр фигуры',
        'Любой другой ввод': 'Вывести атрибуты фигуры.'
    }
    choice_ = 1
    figure_ = Circle((255, 255, 255), 1)
    while choice_:
        choice_ = input('\n\033[93mВыберете одно из следующих действий:\n' +
                        ''.join(list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', choice_dic.keys(),
                                         choice_dic.values()))) + '\033[0m')
        choice_ = int(choice_) if choice_.isnumeric() else 20
        if choice_ == 0:
            exit()
        if choice_ == 1:
            # list_ = list(map(int, input('Введите цвет (3 числа в диапазоне от 0 до 255 через пробел): ').split()))
            # print(*list_)
            figure_ = Circle(tuple(map(int, input('Введите цвет (3 числа в диапазоне '
                                                  'от 0 до 255 через пробел): ').split())),
                             *list(map(int, input('Введите длину окружности: ').split())))
        elif choice_ == 2:
            if isinstance(figure_, Circle):
                print(f'Площадь круга: {figure_.get_square()}')
            else:
                print(f'\033[91mОшибка запроса! Последняя введенная фигура {figure_.__class__.__name__}\033[0m')
        elif choice_ == 3:
            figure_ = Triangle(tuple(map(int, input('Введите цвет (3 числа в диапазоне '
                                                    'от 0 до 255 через пробел): ').split())),
                             *list(map(int, input('Введите 3 стороны через пробел: ').split())))
        elif choice_ == 4:
            if isinstance(figure_, Triangle):
                print(f'Площадь треугольника: {figure_.get_square()}')
            else:
                print(f'\033[91mОшибка запроса! Последняя введенная фигура {figure_.__class__.__name__}\033[0m')
        elif choice_ == 5:
            figure_ = Cube(tuple(map(int, input('Введите цвет (3 числа в диапазоне '
                                                  'от 0 до 255 через пробел): ').split())),
                             *list(map(int, input('Введите длину стороны куба: ').split())))
        elif choice_ == 6:
            if isinstance(figure_, Cube):
                print(f'Объем куба: {figure_.get_volume()}')
            else:
                print(f'\033[91mОшибка запроса! Последняя введенная фигура {figure_.__class__.__name__}\033[0m')
        elif choice_ == 7:
            print(f'Цвет: {figure_.get_color()}')
        elif choice_ == 8:
            figure_.set_color(*tuple(map(int, input('Введите цвет (3 числа в диапазоне '
                                                    'от 0 до 255 через пробел): ').split())))
        elif choice_ == 9:
            print(f'Стороны: {figure_.get_sides()}')
        elif choice_ == 10:
            figure_.set_sides(*tuple(map(int, input(f'Введите стороны для {figure_.__class__.__name__} '
                                                    f'через пробел): ').split())))
        elif choice_ == 11:
            print(f'Периметр фигуры {figure_.__class__.__name__}: {len(figure_)}')
        else:
            print(figure_)