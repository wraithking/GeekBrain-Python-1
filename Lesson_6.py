# Павел Грез  (Pavels Grjozs)
# Легкий уровень сложности (Easy)

# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
class TownCar():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # Методы
    def type(self):
        print('Это городская машина\n')

    #используем print для вывода результата в консоль.

    def go(self):
        print('Начало движения')

    def stop(self):
        print('Остановка движения')

    def turn(self):
        direction = input('Куда повернули\n')
        print("Поворот -", direction)



class SportCar():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def type(self):
        print('Это спортивная машина\n')

    def go(self):
        print('Начало движения')

    def stop(self):
        print('Остановка движения')

    def turn(self):
        direction = input('Куда повернули\n')
        print('Поворот -', direction)




class WorkCar():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def type(self):
        print('Это рабочая машина\n')

    def go(self):
        print('Начало движения')

    def stop(self):
        print('Остановка движения')

    def turn(self):
        direction = input('Куда повернули\n')
        print('Поворот -', direction)


class PoliceCar():

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def type(self):
        print('Это городская машина\n')

    def go(self):
        print('Начало движения')

    def stop(self):
        print('Остановка движения')

    def turn(self):
        direction = input('Куда повернули\n')
        print('Поворот -', direction)



# Данные для тестов:
# MyFirstCar = SportCar(200, "красный", "Ferrari 488 Pista", False)
#
# MySecondCar = WorkCar(160, "зеленый", "Jaguar F-Pace", False)
#
# MyThirdCar = TownCar(140, "черный", "BMW i3", False)
#
# print('Моя первая машина называется ', MySecondCar.name, 'и она раскраски:',MySecondCar.color)
#
# print('Поуправляем машиной ', MySecondCar.name)
#
# MySecondCar.go()
#
# MySecondCar.turn()



# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:

    #Конструктор класса машина
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    #Методы
    def go(self):
        return 'Начало движения'

    def stop(self):
        return 'Остановка движения'

    def turn(self):
        direction = input('Куда повернули\n')
        print('Поворот -', direction)



class TownCar(Car):

    def type(self):
        print('Это городская машина\n')


class SportCar(Car):

    def type(self):
        print('Это спортивная машина\n')


class WorkCar(Car):

    def type(self):
        print('Это городская машина\n')


class PoliceCar(Car):

    def type(self):
        print('Это городская машина\n')


# Проверки:
# MyFirstCar = SportCar(200, "red", "Ferrari 488 Pista", False)
#
# MySecondCar = WorkCar(160, "red", "Jaguar F-Pace", False)
#
# MyThirdCar = TownCar(140, "red", "BMW i3", False)
#
#
# MyFirstCar.type()
#
# MyFirstCar.turn()
#
# print(MyThirdCar.name)