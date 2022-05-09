import random

class Cards():

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cardnumber = self.sortedCards()

    def sortedCards(self):
        
        cardsList = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        return random.choice(cardsList)
