# Домашнее задание по теме "Наследование классов"
# Создайте новый проект или продолжите работу в текущем проекте
#
# Ваша задача:
# Создайте родительский(базовый) класс Car, который имеет свойство
# price = 1000000 и функцию def horse_powers, которая возвращает
# количество лошидиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство
# price, а также переопределите функцию horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса
# Car и переопределите также свойство price,
# а также переопределите функцию horse_powers

class Car:
    price = 1000000
    power = 100

    def horse_powers(self):
        print(self.__class__.__name__, f'Мощность автомобиля {self.power} л.с.')


class Nissan(Car):
    price = 2000000
    power = 120

    def horse_powers(self):
        print(self.__class__.__name__, f'Мощность автомобиля марки Nissan {self.power} л.с.')


class Kia(Car):
    price = 3000000
    power = 150

    def horse_powers(self):
        print(self.__class__.__name__, f'Мощность автомобиля марки Kia {self.power} л.с.')


car_ = Car()
car_.horse_powers()

nissan_ = Nissan()
nissan_.horse_powers()

kia_ = Kia()
kia_.horse_powers()
