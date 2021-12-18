"""represents one color twin of cards; each color contains the color, and boolean flag for whether
it was finished being guessed"""


class MyCard:
    def __init__(self, color):
        self.color = color
        self.guessed = False

    def __repr__(self):
        return self.color
