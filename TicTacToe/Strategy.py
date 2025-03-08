from abc import ABC, abstractmethod

# Move Validation Strategy
class MoveStrategy(ABC):
    @abstractmethod
    def isValidMove(self, board, x, y):
        pass

# Win Condition Strategy
class WinStrategy(ABC):
    @abstractmethod
    def checkWinner(self, board, symbol):
        pass

# Default Move Validation: Check if cell is empty
class DefaultMoveStrategy(MoveStrategy):
    def isValidMove(self, board, x, y):
        return board.getCell(x, y) == " "   # Empty cell check

class DefaultWinStrategy(WinStrategy):
    def checkWinner(self, board, symbol):
        return (
            self.checkRows(board, symbol) or
            self.checkColumns(board, symbol) or
            self.checkDiagonals(board, symbol)
        )

    def checkRows(self, board, symbol):
        for row in board.board:
            if all(cell == symbol for cell in row):
                return True
        return False
    
    def checkColumns(self, board, symbol):
        for col in range(3):
            if all(board.getCell(row, col) == symbol for row in range(3)):
                return True
        return False

    def checkDiagonals(self, board, symbol):
        return (
            all(board.getCell(i, i) == symbol for i in range(3)) or
            all(board.getCell(i, 2 - i) == symbol for i in range(3)) 
        )