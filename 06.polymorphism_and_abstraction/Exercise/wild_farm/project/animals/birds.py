from project.animals.animal import Bird
from project.food import Meat, Vegetable, Seed, Fruit


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def gained_weight(self):
        return 0.25

    @property
    def food_that_can_eat(self):
        return [Meat]


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    @property
    def gained_weight(self):
        return 0.35

    @property
    def food_that_can_eat(self):
        return [Meat, Vegetable, Seed, Fruit]
