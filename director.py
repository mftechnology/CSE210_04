from Cards import Cards

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cardnum1 and cardnum2 are objects of the classe Cards()
        is_stoping (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        card1 = Cards()
        self.cardnum1 =  card1.cardnumber
        card2 = Cards()
        self.cardnum2 =  card2.cardnumber
        self.is_stoping = False
        self.score = 300
    

        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
            self show result : show the card selected from random on the Card class
            self guess_hi_or_lo : calculate score e show on the screen
            self stopGame: Boolean True stop de game or score zero
        """
        print("-----------------THE PLAY´S BEGIN ---------------------------")
        print()

        while not self.is_stoping:
            self.showResult()
            self.guess_hi_or_lo()
            self.stopGame(self.score)

    def showResult(self):
      
        print(f"The card number: {self.cardnum1}")
           

    def guess_hi_or_lo(self):
    #Calculate the score if the user guess obtain 100 points
    #if didn´t guessed lost 75 point

        print("------------------------")
        print()
        choice = input("The next cards will be Higher or lower? You must enter 'h' or 'l' ").lower()
        

        if(choice == "l"):
            if(self.cardnum2 <= self.cardnum1):
                self.score += 100
                print("You guessed!")
            else:
                self.score -= 75
                print("You didn't guess!")
            
        elif(choice == "h"):
            if(self.cardnum2 >= self.cardnum1):
                self.score += 100
                print("You guessed!")
            else:
                self.score -= 75
                print("You didn't guess!")

        
        print(f"Card number: {self.cardnum1}")
        print(f"The next card number was: {self.cardnum2}")
        print(f"teste guess_hi_or_lo: Score is: {self.score}")
        print()
        print("------------------------")
        
    def stopGame(self,score):
        """Tratament to exit if score were zero
        or if user insert N 

        Tratament while to continue and to generate
        object card again  
    """
        tryagain = input("Did you play again? [y or n]: ")

        if tryagain == "n" or tryagain == "N" or score == 0:
            self.is_stoping = True
            print("Thanks for played!")
            print()
            print("-----------------END GAME ---------------------------")
        else:
            
            newcard1 = Cards()
            self.cardnum1 =  newcard1.cardnumber
            newcard2 = Cards()
            self.cardnum2 =  newcard2.cardnumber