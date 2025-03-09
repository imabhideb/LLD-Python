from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Move Command Class
class MoveCommand(Command):
    def __init__(self, player, steps, board):
        self.player = player
        self.steps = steps
        self.board = board
    
    def execute(self):
        newPosition = self.player.getPosition() + self.steps

        # Ensure the player in within board boundary
        if newPosition > self.board.getSize():
            newPosition = self.board.getSize()
        
        # Check for snake or ladder
        snakes = self.board.getSnakes()
        ladders = self.board.getLadders()

        if newPosition in snakes:
            newPosition = snakes[newPosition]
        elif newPosition in ladders:
            newPosition = ladders[newPosition]
        
        self.player.setPosition(newPosition)