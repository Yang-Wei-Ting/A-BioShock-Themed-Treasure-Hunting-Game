import math
import random
from . import gui, cipher


class GameObject:
    def __init__(self, x, y):
        "Initializes the coordinate of self."
        self.x, self.y = x, y
        gui.update_label(self)

    def move_to(self, x, y):
        "Moves self to the given coordinate."
        self.x, self.y = x, y
        gui.update_label(self)

    def move(self, x, y):
        "Moves the coordinate of self."
        self.x += x
        self.y += y
        gui.update_label(self)

    def __repr__(self):
        "Returns the coordinate of self as a string."
        return str((self.x, self.y))

    def distance_between(self, other):
        "Returns the distance between self and other as a float."
        return math.dist((self.x, self.y), (other.x, other.y))


class Player(GameObject):
    color = "Blue"
    health = 5
    mobility = 3

    def __init__(self, x, y):
        super().__init__(x, y)

    def is_drowned(self):
        "Returns True if the coordinate of self exceeds the boundary, else False."
        return abs(self.x) > 5 or abs(self.y) > 5


class BadGuy(GameObject):
    color = "Red"
    weapon_range = 3
    weapon_damage = 0.5

    def __init__(self, x, y):
        super().__init__(x, y)

    def random_move(self):
        "Moves self randomly."
        while True:
            dx, dy = random.randint(-3, 3), random.randint(-3, 3)
            if abs(self.x + dx) > 5 or abs(self.y + dy) > 5:
                continue
            break
        self.move(dx, dy)

    def weapon_upgrade(self):
        "Upgrades self's weapon."
        self.weapon_range += 0.4
        self.weapon_damage += 0.25


class Item(GameObject):
    def __init__(self):
        "Randomly initializes the coordinate of self."
        while True:
            self.x, self.y = random.randint(-5, 5), random.randint(-5, 5)
            if self.x + self.y > -8:
                break


class Cheat:
    @property
    def code_1(self):
        return cipher.decrypt("Errnhu"), cipher.decrypt("Fdwfk!")

    @property
    def code_2(self):
        return cipher.decrypt("D"), cipher.decrypt("Whdu!")

    @property
    def code_3(self):
        return cipher.decrypt("Oljkw"), cipher.decrypt("Krxvh")
