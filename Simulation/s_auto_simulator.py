from Simulation.s_renders import render_select_games_amount, render_ask_for_save
from Main_Game.player import Bot
from Simulation.s_game import s_Game

class s_Auto_Game(s_Game):
    def __init__(self):
        super().__init__()
        self.level_bot = 0

    def create_bot(self):
        self.list_bots.clear()
        self.list_bots.append(Bot(bot_name=f"Bot {self.level_bot}", level = self.level_bot, game_object = self))
        self.list_explorers = self.list_bots.copy()

    def main(self):
        render_select_games_amount(game_object = self)
        for self.level_bot in range(1, 14):
            self.create_bot()
            for game_num in range(self.games_amount):
                self.play_rounds()
                self.reset_game()
            file_path = "s_auto_simulation"
            render_ask_for_save(game_object = self, file_path = file_path)

if __name__ == "__main__":
    game = s_Auto_Game()
    game.main()
