from tkinter import *
from Card import MyCard
from Board import MyBoard


class MyPexeso:
    def __init__(self):
        # define cards we play with
        cards = [MyCard("red"), MyCard("orange"), MyCard("yellow"), MyCard("green"), MyCard("blue"), MyCard("purple")]

        # initialize graphics canvas
        self.root = Tk()
        self.root.geometry('900x750')
        self.root.title("Pexeso")
        self.main_canvas = Canvas(self.root, height=750, width=900, bg="LightBlue2")
        self.message = self.main_canvas.create_text(400, 690, text="Start by clicking on a card.", font="Aerial 20 bold italic", justify="center")
        self.main_canvas.grid()
        self.card_boundaries = [None] * len(cards) * 2
        self.current_guesses = []

        # create board of cards
        self.board = MyBoard(cards)

    def start_new_game(self):
        # shuffle cards
        self.board.shuffle()

        # start the game
        self._draw_board()
        # register callback when mouse button is clicked on our main canvas
        self.main_canvas.bind("<Button-1>", self._on_click)

        # main graphics loop
        self.root.mainloop()

    def _on_click(self, event):
        # find the card index
        for index in range(0, len(self.board.positions)):
            if self.card_boundaries[index][0] < event.x < self.card_boundaries[index][2] and \
                    self.card_boundaries[index][1] < event.y < self.card_boundaries[index][3]:
                if len(self.current_guesses) == 0 or index not in self.current_guesses and \
                        not self.board.cards[self.board.positions[index]].guessed:
                    # add the guess to the list of current guesses
                    self.current_guesses.append(index)
        # if we clicked on two cards then try the guess
        if len(self.current_guesses) == 2:
            is_good_guess = self.board.guess(self.current_guesses[0], self.current_guesses[1])
            if self.board.finished:
                # we are finished
                self.main_canvas.itemconfigure(self.message, text="You won. Game over.")
            elif is_good_guess:
                # good guess
                self.main_canvas.itemconfigure(self.message, text="Good guess. Try to guess another pair of cards.")
            else:
                # bad guess
                self.main_canvas.itemconfigure(self.message, text="Bad guess. Try to guess another pair of cards.")
        else:
            # click on a second card to guess a pair
            self.main_canvas.itemconfigure(self.message, text="Click on another card to guess a pair.")
        # redraw (update) board of cards
        self._draw_board()

    def _draw_board(self):
        # draw board of cards
        for index in range(0, len(self.board.positions)):
            # for each card figure out where to place it in our grid of cards
            row = index // 4
            col = index % 4
            # define card coordinates
            self.card_boundaries[index] = [
                20 + col * 200 + col * 20, 20 + row * 200 + row * 20,
                20 + (col + 1) * 200 + col * 20, 20 + (row + 1) * 200 + row * 20]
            # draw the card
            self.main_canvas.create_rectangle(
                self.card_boundaries[index][0], self.card_boundaries[index][1],
                self.card_boundaries[index][2], self.card_boundaries[index][3],
                outline='black',
                fill=self.board.cards[self.board.positions[index]].color if self.board.cards[self.board.positions[index]].guessed or index in self.current_guesses else 'gray')
        # when we clicked two cards already (it means a guess), clear the guesses so that we can start another guess
        if not self.board.finished:
            if len(self.current_guesses) == 2:
                self.current_guesses = []
