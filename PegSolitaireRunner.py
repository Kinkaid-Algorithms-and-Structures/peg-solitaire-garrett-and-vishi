import logging, datetime
from KinkaidDecorators import log_start_stop_method
from game import Game

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]

class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing.")
        # add any code you want to set up variables for the game.
        self.game = Game()

    @log_start_stop_method
    def play_game(self):  # note: this is complaining (grey underline) that it could be static because it doesn't use
        # any variables or methods from "self." Once you do, it will stop pestering you about it.
        logging.info("Starting game.")
        self.game.start_game()
        while not self.game.is_won() and not self.game.is_lost():
            self.game.player.make_move()
        logging.info("Game ended")


if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()
