from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Rabbit): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._roster = Roster()
        self._console = Console()
        self._board = Board()
        self._number_of_players = 2
        self._game_running = True
        self.last_guess = "none"
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()

        while self._game_running:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for x in range(self._number_of_players):
            name = self._console.read("Enter a name for player " + str(x + 1) + ": ")
            new_player = Player(name)
            new_player.set_move(Move("----"))

            self._roster.add_player(new_player)

 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means getting current visual state from the board.

        Args:
            self (Director): An instance of Director.
        """
        self._console.write("\n" + self._board.to_string(self._roster._players))

    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        current_player = self._roster.get_current()

        self._console.write(current_player.get_name() + "'s turn:")
        self.last_guess = self._console.read("What is your guess? ")

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the stored move in the current player, applying 
        changes to board, and checking if the game is over.

        Args:
            self (Director): An instance of Director.
        """
        current_player = self._roster.get_current()

        move = Move(self.last_guess)
        current_player.set_move(move)
        self._board.apply(move, self._roster._current)

        if self._board.check_win():
            self._game_running = False
            self._console.write("\n" + current_player.get_name() + " wins!")

        self._roster.next_player()


     
       