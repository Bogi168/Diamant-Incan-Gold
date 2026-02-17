from Main_Game.m_game import Game
from Main_Game.m_Renderer import ConsoleRenderer

if __name__ == "__main__":
    game = Game(ConsoleRenderer)
    game.main()
