from Main_Game.Game import Game
from Main_Game.Renderer import ConsoleRenderer

if __name__ == "__main__":
    game = Game(ConsoleRenderer)
    game.main()