import random

class Board:
  
    """ keeps track of board pieces during play. """


    def __init__(self):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._code = ""
        self._guess = ""
        self._player_1_status = []
        self._player_2_status = []
        self._prepare()


    def apply(self):
        """Applies the given move to the playing surface. 
        
        Args:
            self (Board): an instance of Board.
            move (Move): The move to apply.
        """
        guess = move._guess()
        player_1 = move._player_1_status()
        player_2 = move._player_2_status()


    def check_win(self):
        """Determines if a player has guessed the code. It returns True if the player has correctly
        guessed the code; false if otherwise.
        
        Args:
            self (Board): An instance of Board.

        Return:
            Boolean
        """
        if self._guess == self._code:
            check_win = True
        else:
            check_win = False
        
        return check_win


    def to_string(self, players):
        """Converts the board data to its string representation and returns it to the caller.
        
        Args:
            self (Board): An instance of Board.
            players (List): A list of the players currently playing the game.

        Return:
            String
        """
        player_1 = f"Player {players[0]}: {self._player_1_status[0]}, {self._player_1_status[1]}\n"
        player_2 = f"Player {players[1]}: {self._player_2_status[0]}, {self._player_2_status[1]}\n"

        status = player_1 + player_2
        
        current_board = f"\n--------------------\n{status}--------------------\n"
        
        return current_board


    def _prepare(self):
        """Sets up the board with a random code. And adds hint placeholders
        
        Args:
            self (Board): an instance of Board.
        """
        self._code = [format(random.randint(0000,9999), '04d')]
        self._code.append('----')
        self._code.append('****')