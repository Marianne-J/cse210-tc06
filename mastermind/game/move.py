class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the player's guess
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess: the Player's guess
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Board): an instance of Move
        """
        self._guess = guess

    def get_guess(self):
        """Returns the pile to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return self._guess