from Main_Game.m_console import Console

class s_Console(Console):
    def select_bots_amount(self):
        bots_amount = input("How many bots? ")
        while not bots_amount.isdigit() or int(bots_amount) <= 0:
            bots_amount = input("That's not a valid number. How many bots? ")
        self.game_object.bots_amount = int(bots_amount)

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