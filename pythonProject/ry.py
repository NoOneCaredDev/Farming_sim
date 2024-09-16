class Animal:
    def __init__(self, age: int, food_level: int, water_level: int):
        self.age = age
        self.food_level = food_level
        self.water_level = water_level

    def eat(self, food_amount: int):
        pass

    def drink(self, water_amount: int):
        pass

    def sleep(self):
        pass


class Sheep(Animal):
    def shear(self):
        pass


class Dog(Animal):
    def herd_sheep(self):
        pass


class Cow(Animal):
    def give_milk(self):
        pass


class Pig(Animal):
    def roll_in_mud(self):
        pass


class Chicken(Animal):
    def lay_eggs(self):
        pass


class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        pass

    def run_day(self):
        while True:
            pass

    def close_farm(self):
        pass
