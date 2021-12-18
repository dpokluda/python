from Card import MyCard
import random


class MyBoard:
    def __init__(self, cards):
        self.cards = cards
        self.positions = [None] * len(cards) * 2
        self.finished = False
        self.shuffle()
        random.seed()

    def shuffle(self):
        # reset positions
        card_index = 0
        available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        while len(available) > 0:
            index = random.choice(available)
            available.remove(index)
            self.positions[index] = card_index // 2
            card_index += 1
        self.finished = False

    def guess(self, first, second):
        if 0 <= first < len(self.positions) and 0 <= second < len(self.positions) and first != second:
            if self.positions[first] == self.positions[second]:
                # good guess -> mark as finished
                self.cards[self.positions[first]].guessed = True
                # check whether the whole board is now finished
                is_game_over = True
                for card in self.cards:
                    if not card.guessed:
                        is_game_over = False
                if is_game_over:
                    self.finished = True
                return True
            else:
                # wrong guess
                return False
        else:
            # invalid input
            return None

    def __repr__(self):
        string = "["
        for position in self.positions:
            if self.cards[position].guessed:
                string += " " + self.cards[position].color + " "
            else:
                string += " ??? "
        string += ']'
        return string
