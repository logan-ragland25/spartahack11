import random

class Card:
    def __init__(self):
        rand = random.randint(1,108)

        if rand <= 8:
            # Wilds
            self.color = 5
            #13 is wild 
            #14 is draw 4
            self.value = random.randint(13,14)

        elif rand <= (24 + 8):
            # Action cards
            self.color = random.randint(1,4)
            #10 is draw 2
            #11 is reverse
            #12 is skip
            self.value = random.randint(10,12)

        else:
            # Number cards
            self.color = random.randint(1,4)
            self.value = random.randint(0,9)

