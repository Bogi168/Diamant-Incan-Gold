from s_stat_saver import save_statistics
from s_console import console_select_games_amount
from s_player import s_Bot
from s_game import s_Game

file_path = "s_auto_simulation"

class s_Auto_Game(s_Game):
    def __init__(self):
        super().__init__()
        self.level_bot = 0

    def create_bot(self):
        self.explorers.append(
            s_Bot(bot_name=f"Bot {self.level_bot}", level = self.level_bot, game_object = self))

    def main(self):
        console_select_games_amount(game_object = self)
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
