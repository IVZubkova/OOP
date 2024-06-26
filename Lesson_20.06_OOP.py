#первый урок по ООП
import random


class Car:
    def __init__(self, brand, model, year=2000, color=(0, 0, 255)):
        """
        Инициализация объекта класса
        self - внутренняя переменная
        brand, model - обяз параметры
        year, color - опциональные
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color #синий цвет
        self.condition = {'tyres': 100, 'engine': 100, 'fuel':100, 'glass':100}

    def change_color(self, new_color):
        """
        перекрасить
        внутри класс между методами расстояние - 1 строчка
        :param new_color:
        :return:
        """
        self.color = new_color

    def change_condition(self, part, value):
        if part in self.condition.keys():
            self.condition[part] = value
        else:
            print('Invalid part', part)

    def crash(self, level):
        if level == 'low':
            self.condition['fuel'] -= random.randint(5, 25)
            self.condition['glass'] -= random.randint(10, 40)
        elif level == 'middle':
            self.condition['fuel'] -= random.randint(25, 55)
            self.condition['glass'] -= random.randint(40, 80)
        elif level == 'high':
            self.condition['fuel'] -= random.randint(55, 95)
            self.condition['glass'] -= random.randint(80, 95)
            self.condition['engine'] -= random.randint(70, 95)

    def show_condition(self):
        for part in self.condition.keys():
            print(f'{part}: {self.condition[part]}')

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}, color:{self.color}'


class Kia(Car):
    def __init__(self, model, year, color):
        super().__init__('Kia', model, year, color)


class KiaRio(Kia):
    def __init__(self, year=2000, color=(0, 255, 0)):
        super().__init__('Rio', year, color)


class Mammal:
    def __init__(self, name, role, viviparous=True):
        self.name = name
        self.role = role
        self.viviparous = viviparous

    def __str__(self):
        return f'{self.name} {self.role} {self.viviparous}'


class Human(Mammal):
    def __init__(self, name):
        super().__init__(name, role='omnivorous')


class Dog(Mammal):
    def __init__(self, name, breed, colour):
        super().__init__(name, role='predator')
        self.breed = breed
        self.colour = colour



if __name__ == '__main__':

    just_man = Human(name='Vasya')
    print(just_man)
    ford = Car(brand='Kia', model='Sorrento', year=2005)
    print(ford)
    # ford.change_color((255, 0, 0))
    # print(ford)
    # ford.crash(random.choice(['low','middle','high']))
    # ford.show_condition()
    # kia = Kia(model='Picanto', year=2010,color=(251, 0, 0))
    # print(kia)
    # kia.crash(random.choice(['low', 'middle', 'high']))
    # kia.show_condition()
    # kia_rio = KiaRio()
    # print(kia_rio)
    # print(issubclass(KiaRio, Kia))
    # print(issubclass(KiaRio, Car))#KiaRio является потомком Car?
    # print('=======')
    # print(isinstance(kia_rio, KiaRio))#является ли этот объект kia_rio объектом этого класса

