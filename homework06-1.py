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

    def horse_powers(self):
        return 100


class Nissan(Car):
    price = 2000000

    def horse_powers(self):
        return 120


class Kia(Car):
    price = 3000000

    def horse_powers(self):
        return 150


car_ = Car()
print(f'Мощность автомобиля {car_.__class__.__name__} {car_.horse_powers()} л.с.')

nissan_ = Nissan()
print(f'Мощность автомобиля {nissan_.__class__.__name__} {nissan_.horse_powers()} л.с.')

kia_ = Kia()
print(f'Мощность автомобиля {kia_.__class__.__name__} {kia_.horse_powers()} л.с.')
