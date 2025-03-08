from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol    # Stores plater symbol ("X" or "O")
    
    def getSymbol(self):
        return self.symbol

    @abstractmethod
    def update(self, board):
        pass    # To be implemented by subclasses

# Concrete Human player class
class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    # Implementation for making a move

    def update(self, board):
        pass    # Implementation to update player with board state

# Factory class to create players
class PlayerFactory:
    @staticmethod
    def createPlayer(symbol):
        return HumanPlayer(symbol)