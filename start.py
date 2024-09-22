from src.game import Game
from src.ui import UI

if __name__ == "__main__":
    game = Game()
    ui = UI(game)
    ui.run_ui()
