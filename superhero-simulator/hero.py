
from ability import Ability
from armor import Armor
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

    self.armory = []
    self.abilities = []
  

  def add_ability(self, ability):
    self.abilities.append (ability)
    return self.abilities

  def attack(self):
    attack_value = 0
    for ability in self.abilities:
      attack_value += ability.attack()
    return attack_value

  def add_armor(self, armor):
    self.armory.append (armor)
    return self.armory
  
  def defend(self):
    defense_value = 0
    for armor in self.armory:
      defense_value = armor.block()
    return defense_value

  def take_damage(self, taking_damage):
    damage = taking_damage - self.defend()
    if damage > 0:
      self.current_health -= damage


  def battle(self, opponent):
    '''
    current hero will take turns fighting the oponent hero passed in.
    '''
    if self.abilities == opponent.abilities:
      print (f"{hero1} and {hero2} have same or no abilities. There is a draw.")
    
         
   
   
    hero_names = []
    hero_names.append (self.name)
    hero_names.append(opponent.name)

    winner =random.choice(hero_names)
    
    for hero in hero_names:
      if hero != winner:
        loser = hero

    print(f'{winner} has killed {loser}')

    return winner

hero1 = Hero("Kika")
hero2 = Hero()

hero1.battle(hero2)

ability1 = Ability("super strength", 150)
ability2 = Ability("super poke", 9)
ability3 = Ability("rotten breath", 99)

hero1.add_ability(ability1)
hero1.add_ability(ability2)
hero1.add_ability(ability3)



armor1 = Armor("backpack", 150)
armor2 = Armor("pan", 120)

hero1.add_armor(armor1)
hero1.add_armor(armor2)

print(f"the amror has blocked {hero1.defend()} damage")

print(f"The abilities have dealt {hero1.attack()} dmaage.")







