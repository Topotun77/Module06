# Домашнее задание по теме "Множественное наследование"
# Создайте новый проект или продолжите работу в текущем проекте
#
# Ваша задача:
# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000
# и функцию def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price
# и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle:
    def __init__(self):
        self.vehicle_type = 'none'

class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return 100

class Nissan (Vehicle, Car):
    def __init__(self):
        self.vehicle_type = 'автомобиль'
        self.price = 2000000

    def __str__(self):
        return f'Тип ТС: {self.vehicle_type}, цена {self.price}'

    def horse_powers(self):
        return 200


nissan_ = Nissan()
print(nissan_)