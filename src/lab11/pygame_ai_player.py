""" Create PyGameAIPlayer class here"""
from turn_combat import CombatPlayer
import random 
from lab4.player import Player


class PyGameAIPlayer:
    def selectAction(self,state):
        return random.randint(48,57)
    pass


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        # Implement your own weapon selecting strategy here
        # For example, select a random weapon
        self.weapon = random.randint(0,2)

pass
