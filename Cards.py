import random

class Cards():

    def __init__(self):
        """Constructs a new Cards.
        
        Args:
            self (cardnumber): an instance of Cards.
        """
        self.cardnumber = self.sortedCards()

    def sortedCards(self):
        """
        Sorted Cards create a cardsList and
        use random to select a number

        """
        
        cardsList = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        return random.choice(cardsList)
