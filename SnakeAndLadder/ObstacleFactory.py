class ObstacleFactory:

    @staticmethod
    def createSnakes(board, snakes):
        for mouth, tail in snakes:
            board.addSnake(mouth, tail)
    
    @staticmethod
    def createLadder(board, ladders):
        for top, bottom in ladders:
            board.addLadder(bottom, top)