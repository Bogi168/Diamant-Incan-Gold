from Simulation.s_stat_saver import save_statistics
from Simulation.s_renders import render_select_games_amount
from Main_Game.player import Bot
from Simulation.s_game import s_Game

file_path = "s_auto_simulation"

class s_Auto_Game(s_Game):
    def __init__(self):
        super().__init__()
        self.level_bot = 0

    def create_bot(self):
        self.explorers.append(
            Bot(bot_name=f"Bot {self.level_bot}", level = self.level_bot, game_object = self))

    def main(self):
        render_select_games_amount(game_object = self)
        for self.level_bot in range(1, 14):
            self.explorers.clear()
            self.create_bot()
            self.players_inside = [p for p in self.explorers if p.inside]
            for game_num in range(self.games_amount):
                self.play_rounds()
                self.reset_game()
            save_statistics(game_object = self, file_path = file_path)

if __name__ == "__main__":
    game = s_Auto_Game()
    game.main()