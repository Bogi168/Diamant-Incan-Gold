from Main_Game.m_game import Game
from Simulation.s_renders import *
from Main_Game.Renderer import SimulationRenderer

class s_Game(Game):
    def __init__(self):
        super().__init__(renderer = SimulationRenderer, bool_adjust_risk_last_round = False)

    def create_explorers(self):
        render_create_bots(game_object = self)
        render_select_games_amount(game_object = self)