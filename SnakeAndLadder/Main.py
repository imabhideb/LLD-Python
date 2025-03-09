from Board import Board
from ObstacleFactory import ObstacleFactory
from Observer import Game, Player
from Dice import NormalDice, SpecialDice
from Game import MoveCommand

def main():
    # Initialize board
    board = Board(100)

    # Create snakes and ladders
    ObstacleFactory.createSnakes(
        board, 
        [(16, 6), (48, 26), (49, 11)]
    )

    ObstacleFactory.createLadder(
        board,
        [(1, 38), (4, 14), (9, 31)]
    )

    # Initialize game and player
    game = Game()
    player1 = Player("Abhijit")
    player2 = Player("Deb")

    game.addPlayer(player1)
    game.addPlayer(player2)

    # Use normal/special dice strategy
    # dice = NormalDice()
    dice = SpecialDice()

    # Play game
    while True:
        currPlayer = game.getCurrPlayer()
        diceRoll = dice.rollDice()

        moveCommand = MoveCommand(currPlayer, diceRoll, board)
        moveCommand.execute()

        game.notifyPlayer(f"{currPlayer.getName()} rolled a {diceRoll} and moved to {currPlayer.getPosition()}")

        if currPlayer.getPosition() == board.getSize():
            game.notifyPlayer(f"{currPlayer.getName()} wins!")
            break

        game.nextTurn()

if __name__ == "__main__":
    main()