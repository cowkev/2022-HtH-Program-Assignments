import random

class Ability:
    #constructor/ initializer
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def __repr__(self):
        return f'Ability({self.name}, {self.max_damage})'

    def attack(self):
        attack_value = random.randrange (0, self.max_damage)
        return attack_value 

ability1 = Ability("super strength", 150)
ability2 = Ability("fly", 10)

print (ability1.attack())


