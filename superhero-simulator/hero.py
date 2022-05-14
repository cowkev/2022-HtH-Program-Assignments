
import random


# hero.py
class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name = "Capybara", starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''

    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health

  def kill(self, oppenent):
    '''
    current hero will take turns fighting the oponent hero passed in.
    '''
    hero_names = []
    hero_names.append (self.name)
    hero_names.append(oppenent.name)

    winner =random.choice(hero_names)

    for hero in hero_names:
      if hero !=winner:
        loser = hero

    print(f'{winner} has killed {loser}')

    return winner

hero1 = Hero()
hero2 = Hero("Dumbledore")

hero1.kill(hero2)

