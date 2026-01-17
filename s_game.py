from Main_Game._game import Game
from s_player import s_Bot
from s_NewCardEvent import s_Draw_Card
from s_LevelStrategy import s_Act_On_Card


class s_Game(Game):
    def __init__(self):
        super().__init__()
        self.bots_amount = 0
        self.games_amount = 0

    def select_bots_amount(self):
        self.bots_amount = input("How many bots? ")
        while not self.bots_amount.isdigit() or int(self.bots_amount) <= 0:
            self.bots_amount = input("That's not a valid number. How many bots? ")
        self.bots_amount = int(self.bots_amount)

    def select_games_amount(self):
        self.games_amount = input("How many games? ")
        while not self.games_amount.isdigit() or int(self.games_amount) <= 0:
            self.games_amount = input("That's not a valid number. How many games?: ")
        self.games_amount = int(self.games_amount)

    def create_explorers(self):
        self.select_bots_amount()
        self.select_games_amount()
        level_bot = 1
        for bots_num in range(self.bots_amount):
            if level_bot==4:
                level_bot = 1
            if level_bot == 1:
                self.explorers.append(s_Bot(bot_name=f"Bot {bots_num + 1}", level=level_bot, game_object=self))
            elif level_bot == 2:
                self.explorers.append(s_Bot(bot_name=f"Bot {bots_num + 1}", level=level_bot, game_object=self))
            elif level_bot == 3:
                self.explorers.append(s_Bot(bot_name=f"Bot {bots_num + 1}", level=level_bot, game_object=self))
            level_bot += 1
        self.players_inside = [p for p in self.explorers if p.inside]

    def start_round(self):
        self.reset_round()
        self.p_inside = True

    def ask_explorer(self, p):
        if len(self.explorers) != 0:
            act_on_card = s_Act_On_Card(self, p)
            act_on_card.ask_bot()

    def still_players_inside(self):
        if not self.no_players_inside():
            drawcard = s_Draw_Card(self)
            drawcard.draw_card()

    def identify_round_winner(self):
        self.final_winners.clear()
        self.amount_final_winner = 0
        for s in self.explorers:
            if self.amount_final_winner < s.chest:
                self.amount_final_winner = s.chest
                self.final_winners.clear()
                self.final_winners.append(s)
            elif self.amount_final_winner == s.chest:
                self.final_winners.append(s)
            s.diamond_count += s.chest
            s.collected_diamonds.append(s.chest)
        for w in self.final_winners:
            w.round_winning_count += 1

    def identify_game_winner(self):
        self.final_winners.clear()
        self.amount_final_winner = 0
        for s in self.explorers:
            if self.amount_final_winner < s.chest:
                self.amount_final_winner = s.chest
                self.final_winners.clear()
                self.final_winners.append(s)
            elif self.amount_final_winner == s.chest:
                self.final_winners.append(s)
        for w in self.final_winners:
            w.game_winning_count += 1

    def play_rounds(self):
        for self.rounds in range(5):
            self.start_round()
            while self.p_inside:
                self.no_players_inside()
                self.still_players_inside()
            self.identify_round_winner()
        self.identify_game_winner()

    def get_max_diamonds(self):
        for e in self.explorers:
            for c in e.collected_diamonds:
                if c > e.max_diamonds:
                    e.max_diamonds = c

    def reset_game(self):
        self.cards.traps = self.cards.snakes + self.cards.spiders + self.cards.fires + self.cards.avalanches + self.cards.mummies
        self.cards.full_deck = self.cards.traps + self.cards.treasure_cards
        for b in self.explorers:
            b.inside = True
            b.pocket = 0
            b.chest = 0

    def tell_stats(self):
        self.get_max_diamonds()
        for e in self.explorers:
            print()
            print("******************************************************************")
            print(f"{e.bot_name} (Level: {e.level}) won {e.round_winning_count} rounds")
            print(f"{e.bot_name} won {e.game_winning_count} games")
            print(f"That's a win rate of {e.game_winning_count / self.games_amount * 100:.1f}%")
            print(f"{e.bot_name} collected {e.diamond_count} diamonds")
            print(f"That's {((e.diamond_count/5)/self.games_amount):.1f} diamonds per round")
            print(f"{e.bot_name} collected {e.max_diamonds} diamonds in his best round")
            print("******************************************************************")
            print()

    def main(self):
        self.create_explorers()
        for game_num in range(self.games_amount):
            self.play_rounds()
            self.reset_game()
        self.tell_stats()
