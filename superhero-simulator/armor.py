from multiprocessing.sharedctypes import Value
import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block_value = random.randrange (0, self.max_block)
        return block_value

block1 = Armor("wooden spoon", 40)
block2 = Armor("pan", 30)

print (block1.block())

