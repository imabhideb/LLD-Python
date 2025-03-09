from abc import ABC, abstractmethod
import random

# Strategy Interface
class DiceStrategy(ABC):
    @abstractmethod
    def rollDice(self):
        pass

# Normal Dice: Roll a fair die (1-6)
class NormalDice(DiceStrategy):
    def rollDice(self):
        return random.randint(1, 6)

# Special dice: Biased towards higher number (4-6)
class SpecialDice(DiceStrategy):
    def rollDice(self):
        return random.randint(4, 6)