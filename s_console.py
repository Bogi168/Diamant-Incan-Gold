from s_player import s_Bot
from Main_Game.m_console import Console
from s_stat_saver import *

class s_Console(Console):
    def select_bots_amount(self):
        bots_amount = input("How many bots? ")
        while not bots_amount.isdigit() or int(bots_amount) <= 0:
            bots_amount = input("That's not a valid number. How many bots? ")
        self.game_object.bots_amount = int(bots_amount)

    def select_bots_level(self):
        for bots_num in range(self.game_object.bots_amount):
            level_bot = input(f"Select a level for Bot {bots_num + 1} (1-13): ")
            while not level_bot in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"):
                level_bot = input(
                    f"{level_bot} is not valid. Select a level for Bot {bots_num + 1} (1-13): ")
            level_bot = int(level_bot)
            self.game_object.explorers.append(s_Bot(bot_name=f"Bot {bots_num + 1}", level=level_bot, game_object=self.game_object))

    def select_games_amount(self):
        games_amount = input("How many games? ")
        while not games_amount.isdigit() or int(games_amount) <= 0:
            games_amount = input("That's not a valid number. How many games?: ")
        self.game_object.games_amount = int(games_amount)

    def tell_stats(self):
        self.game_object.get_max_diamonds()
        for e in self.game_object.explorers:
            print()
            print("******************************************************************")
            print(f"{e.bot_name} (Level: {e.level}) won {e.round_winning_count} rounds")
            print(f"{e.bot_name} won {e.game_winning_count} games")
            print(f"That's a win rate of {e.game_winning_count / self.game_object.games_amount * 100:.1f}%")
            print(f"{e.bot_name} collected {e.diamond_count} diamonds")
            print(f"That's {((e.diamond_count/5)/self.game_object.games_amount):.1f} diamonds per round")
            print(f"{e.bot_name} collected {e.max_diamonds} diamonds in his best round")
            print("******************************************************************")
            print()

    def ask_for_save(self):
        save_answer = input("Do you want to save the game statistics? (Y/N): ").lower()
        if save_answer in ("y", "yes"):
            save_statistics(self.game_object)
            print("\n" + f"The stats were saved in {file_path} \n")
        else:
            print("\n" + "The stats were not saved. \n")
