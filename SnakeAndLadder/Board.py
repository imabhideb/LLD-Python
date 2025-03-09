class Board:
    _instance = None

    def __new__(cls, size):
        if cls._instance is None:
            cls._instance = super(Board, cls).__new__(cls)
            cls._instance.size = size
            cls._instance.snakes = {}
            cls._instance.ladders = {}
        return cls._instance

    def getSize(self):
        return self.size

    def getSnakes(self):
        return self.snakes
    
    def getLadders(self):
        return self.ladders
    
    def addSnake(self, mouth, tail):
        self.snakes[mouth] = tail
    
    def addLadder(self, bottom, top):
        self.ladders[bottom] = top