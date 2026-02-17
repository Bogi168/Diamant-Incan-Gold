from Main_Game.m_game import Game
from Simulation.s_New_Card_Event import s_Draw_Card
from Simulation.s_Level_Strategy import s_Act_On_Card
from Simulation.s_renders import *
from Main_Game.m_Renderer import SimulationRenderer


class s_Game(Game):
    def __init__(self):
        super().__init__(renderer = SimulationRenderer)
        self.bots_amount = 0
        self.games_amount = 0

    def create_explorers(self):
        render_create_bots(game_object = self)
        self.players_inside = [p for p in self.explorers if p.inside]
        render_select_games_amount(game_object = self)

    def save_prev_round_chest(self):
        for current_bot in self.explorers:
            current_bot.prev_round_chest = current_bot.chest

    def start_round(self):
        self.reset_round()
        self.p_inside = True
        self.save_prev_round_chest()

    def ask_explorer(self, current_player):
        if len(self.explorers) != 0:
            act_on_card = s_Act_On_Card(self, current_player)
            act_on_card.ask_bot()

    def still_players_inside(self):
        if not self.no_players_inside():
            drawcard = s_Draw_Card(self)
            drawcard.draw_card()

    def identify_round_winner(self):
        round_winners = []
        amount_round_winner = 0
        for explorer in self.explorers:
            booty = explorer.chest - explorer.prev_round_chest
            if amount_round_winner < booty:
                amount_round_winner = booty
                round_winners.clear()
                round_winners.append(explorer)
            elif amount_round_winner == booty:
                round_winners.append(explorer)
            explorer.diamond_count += explorer.chest
            explorer.collected_diamonds.append(explorer.chest)
        for winner in round_winners:
            winner.round_winning_count += 1

    def identify_game_winner(self):
        final_winners = []
        amount_final_winner = 0
        for s in self.explorers:
            if amount_final_winner < s.chest:
                amount_final_winner = s.chest
                final_winners.clear()
                final_winners.append(s)
            elif amount_final_winner == s.chest:
                final_winners.append(s)
        for w in final_winners:
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
        render_tell_stats(game_object = self)
        if self.bots_amount == 1:
            render_ask_for_save(game_object = self)
