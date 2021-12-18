from Card import MyCard
from Board import MyBoard


class MyPexeso:
    def __init__(self):
        cards = [MyCard("red"), MyCard("orange"), MyCard("yellow"), MyCard("green"), MyCard("blue"), MyCard("purple")]
        self.board = MyBoard(cards)

    def start_new_game(self):
        # shuffle cards
        self.board.shuffle()

        # start the game
        while not self.board.finished:
            print(self.board)
            try:
                guesses = [int(x) for x in input("Enter your next guess: ").split()]
                first = guesses[0]
                second = guesses[1]

                result = self.board.guess(first, second)
                if result:
                    print("Good guess.")
                else:
                    print(f"Cards: {self.board.cards[self.board.positions[first]]}, " +
                          f"{self.board.cards[self.board.positions[second]]}. Try again.")
            except IndexError:
                print("This wasn't a valid game input. Enter two integer values from 0 to 11.")

        # game over
        print(self.board)
        print("Woo-hoo, game over. :-)")



