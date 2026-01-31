from card import Card

class Player:
    def __init__(self, dir):
        # Initialize the players hand to seven cards
        self.hand = [Card() for _ in range (7)]
        self.dir = dir

    def draw(self):
        # Add card to hand
        self.hand.append(Card)
        
        # return -1 because drawing skips turn
        return -1
    
    def drawMultiple(self, count):
        for i in range(count):
            self.draw()

    def canPlay(self, curr = Card):
        for card in self.hand:
            # Card can be played if it is matching color, a wild card, or the same number
            if (card.color == curr.color):
                return True
            elif (card.color == 5):
                return True
            elif (card.value == curr.value):
                return True
        return False

    def play(self):
        # return 1 because player successfully played
        return 1 # Card

    def turn(self, curr = Card):
        if self.canPlay(curr):
            return self.play()
        else:
            return self.draw()