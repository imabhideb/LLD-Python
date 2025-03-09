# Observer Interface
class Observer:
    def update(self, message: str):
        pass

# Player class implementing Observer
class Player(Observer):
    def __init__(self, name: str):
        self.name = name
        self.position = 0
    
    def getName(self):
        return self.name
    
    def getPosition(self):
        return self.position

    def setPosition(self, position: int):
        self.position = position
    
    def update(self, message):
        print(f"{self.name}: {message}")

# Game class managing players and turns
class Game:
    def __init__(self):
        self.players = []
        self.currPlayerInd = 0
    
    def addPlayer(self, player: Player):
        self.players.append(player)
    
    def notifyPlayer(self, message: str):
        for player in self.players:
            player.update(message)
    
    def getCurrPlayer(self):
        return self.players[self.currPlayerInd]
    
    def nextTurn(self):
        self.currPlayerInd = (self.currPlayerInd + 1) % len(self.players)