from Main_Game.m_game import Game
from Simulation.s_console import s_Console
from s_NewCardEvent import s_Draw_Card
from s_LevelStrategy import s_Act_On_Card


class s_Game(Game):
    def __init__(self):
        super().__init__()
        self.bots_amount = 0
        self.games_amount = 0
        self.console = s_Console(self)

    def create_explorers(self):
        self.console.select_bots_amount()
        self.console.select_bots_level()
        self.players_inside = [p for p in self.explorers if p.inside]
        self.console.select_games_amount()

    def start_round(self):
        self.reset_round()
        self.p_inside = True

    def ask_explorer(self, player):
        if len(self.explorers) != 0:
            act_on_card = s_Act_On_Card(self, player)
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
        self.cards.full_deck = self.cards.traps + self.cards.treasure_cards
        for b in self.explorers:
            b.inside = True
            b.pocket = 0
            b.chest = 0

    def main(self):
        self.create_explorers()
        for game_num in range(self.games_amount):
            self.play_rounds()
            self.reset_game()
        self.console.tell_stats()
        if self.bots_amount == 1:
            self.console.ask_for_save()
