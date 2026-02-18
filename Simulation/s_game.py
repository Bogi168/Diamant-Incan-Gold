from Main_Game.m_game import Game
from Simulation.s_renders import *
from Main_Game.Renderer import SimulationRenderer

class s_Game(Game):
    def __init__(self):
        super().__init__(renderer = SimulationRenderer, bool_adjust_risk_last_round = False)

    def create_explorers(self):
        render_create_bots(game_object = self)
        self.players_inside = [p for p in self.explorers if p.inside]
        render_select_games_amount(game_object = self)

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
