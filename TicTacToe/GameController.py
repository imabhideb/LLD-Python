class GameController:
    _instance = None    # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameController, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, board=None, moveStrategy=None, winStrategy=None, players=None):
        if not self._initialized:
            self.board = board
            self.moveStrategy = moveStrategy
            self.winStrategy = winStrategy
            self.players = players
            self.currPlayer = 0
            self._initialized = True
            print("Game controller initialized")
    
    @classmethod
    def getInstance(cls, board=None, moveStrategy=None, winStrategy=None, players=None):
        """Singleton access method to get the instance."""
        return cls._instance