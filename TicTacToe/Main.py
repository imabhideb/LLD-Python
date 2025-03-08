from GameController import GameController
from Player import PlayerFactory
from Board import Board
from Strategy import DefaultMoveStrategy, DefaultWinStrategy

def isDraw(board):
    for row in board.board:
        if ' ' in row:
            return False
    return True

def switchPlayer(currPlayer, player1, player2):
    return player2 if currPlayer == player1 else player1

def main():
    print("Welcome to Tic-Tac-Toe!")

    # Initialize Board and Strategies
    board = Board()
    moveStrategy = DefaultMoveStrategy()
    winStrategy = DefaultWinStrategy()

    # Create Players using Factory Pattern
    player1 = PlayerFactory.createPlayer('X')
    player2 = PlayerFactory.createPlayer('O')
    board.addPlayer(player1)
    board.addPlayer(player2)

    currPlayer = player1

    # Game loop
    while True:
        board.display()
        print(f"Player {currPlayer.symbol}'s turn")

        # Get Valid move
        while True:
            try:
                x, y = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if moveStrategy.isValidMove(board, x, y):
                    break
                else:
                    print("Invalid move! Cell occupied or out of bounds.")
            except ValueError:
                print("Invalid input! Please enter two numbers (0-2).")
        
        # Update board and notify players
        board.updateBoard(x, y, currPlayer.symbol)

        # Check for win
        if winStrategy.checkWinner(board, currPlayer.symbol):
            board.display()
            print(f"Player {currPlayer.symbol} wins!")
            break
        
        # Check for draw
        if isDraw(board):
            board.display()
            print("It's a draw")
            break
            
        currPlayer = switchPlayer(currPlayer, player1, player2)


if __name__ == "__main__":
    main()