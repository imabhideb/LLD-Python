class Board:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.players = []    # List of players
    
    def addPlayer(self, player):
        self.players.append(player)
    
    def notifyPlayers(self):
        for player in self.players:
            player.update(self)
    
    def updateBoard(self, x, y, symbol):
        if self.board[x][y] == " ":
            self.board[x][y] = symbol
            self.notifyPlayers()
        else:
            print("Invalid move! Cell already occupied.")
    
    def getCell(self, x, y):
        return self.board[x][y]
    
    def display(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)  # Just a random number to create a border