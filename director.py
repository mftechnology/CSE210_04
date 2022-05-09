from Cards import Cards

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
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
        """
        print("-----------------THE PLAY´S BEGIN ---------------------------")
        print()

        while not self.is_stoping:
            self.showResult()
            self.guess_hi_or_lo()
            self.stopGame()

    def showResult(self):
      
        print(f"The card sorted is: {self.cardnum1}")
           

    def guess_hi_or_lo(self):
        print("------------------------")
        print()
        choice = input("Higher or lower? You must enter 'h' or 'l' ").lower()
        

        if(choice == "l"):
            if(self.cardnum2 < self.cardnum1):
                self.score += 100
                print("You guessed!")
            else:
                self.score -= 75
                print("You didn't guess!")
            
        elif(choice == "h"):
            if(self.cardnum2 > self.cardnum1):
                self.score += 100
                print("You guessed!")
            else:
                self.score -= 75
                print("You didn't guess!")

        
      #  self.total_score += self.score
        print(f"Card sort: {self.cardnum1}")
        print(f"The next card was: {self.cardnum2}")
        print(f"teste guess_hi_or_lo: Score is: {self.score}")
        print()
        print("------------------------")
        
      #  print(f"teste guess_hi_or_lo: Total Score is: {self.total_score}")
    def stopGame(self):
        tryagain = input("teste stopGame: Did you play again? [y or n]: ")
        if tryagain == "n" or tryagain == "N":
            self.is_stoping = True
            print()
            print("-----------------END GAME ---------------------------")
        else:
            newcard1 = Cards()
            self.cardnum1 =  newcard1.cardnumber
            newcard2 = Cards()
            self.cardnum2 =  newcard2.cardnumber