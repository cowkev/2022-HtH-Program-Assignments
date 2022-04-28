import random
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

user_action = ("Enter a choice (rock, paper, scissors):")

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

