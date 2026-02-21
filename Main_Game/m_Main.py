from Main_Game.Game import Game
from Main_Game.Renderer import ConsoleRenderer

if __name__ == "__main__":
    console_renderer = ConsoleRenderer()
    game = Game(console_renderer)
    game.main()