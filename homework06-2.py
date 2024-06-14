# -*- coding: utf-8 -*-
# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
# Задача "Изменять нельзя получать":
# В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так
# поменять цвет, мощность двигателя и прочие свойства, т.к. в реальной жизни это чаще
# всего делается не владельцем, а в специальных сервисах. Да, узнать значения этих
# свойств мы сможем, но вот изменить - нет.
#
# Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт,
# а Sedan(седан) - наследник класса Vehicle.

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner: str, model: str, color='white', engine_power=1000):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(),
              f'Владелец: {self.owner}', sep='\n', end='\n\n')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'\033[91mНельзя сменить цвет на {new_color}\033[0m')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()