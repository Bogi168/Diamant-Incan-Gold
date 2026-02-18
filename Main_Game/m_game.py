# Classes Player and Bot
from Main_Game.cards import Cards
from Main_Game.New_Card_Event import Draw_Card
from Main_Game.Level_Strategy import Act_On_Card
from Main_Game.m_renders import *
from Main_Game.probability_and_ev import calc_dying_prob, calc_undiscovered_diamonds


# Main_Game
class Game:
    def __init__(self, renderer, bool_adjust_risk_last_round = True):
        self.renderer = renderer
        self.bool_adjust_risk_last_round = bool_adjust_risk_last_round

        self.players_amount = 0
        self.bots_amount = 0
        self.games_amount = 0

        # Define explorer lists
        self.players = []
        self.level_bots = []
        self.bots = []
        self.explorers = []
        self.players_inside = []
        self.go_home_now = []
        self.final_winners = []

        # Define Main_Game variables
        self.is_running = True
        self.rounds = 0
        self.p_inside = True
        self.diamonds_on_way = 0
        self.relics_on_way = 0

        # Create cards object
        self.cards = Cards(self)

    @property
    def dying_prob(self):
        return calc_dying_prob(cards_object = self.cards)

    @property
    def undiscovered_diamonds(self):
        return calc_undiscovered_diamonds(cards_object = self.cards)

    @property
    def amount_current_winner(self):
        return self.identify_highest_diamonds()

    # Check whether players inside
    @property
    def check_players_inside(self):
        if len(self.players_inside) == 0:
            return False
        else:
            return True


    # Create explorers
    def create_explorers(self):
        render_create_players(game_object = self)
        render_create_bots(game_object = self)
        if len(self.bots) == 0:
            self.explorers = self.players
        else:
            self.explorers = self.players + self.bots
        self.players_inside = [p for p in self.explorers if p.inside]

    # Reset previous round and add relics
    def reset_round(self):
        self.players_inside.clear()
        for explorer in self.explorers:
            explorer.inside = True
            explorer.prev_round_chest = explorer.chest
        self.players_inside = [p for p in self.explorers]
        self.diamonds_on_way = 0
        self.relics_on_way = 0
        self.cards.reset_played_cards()
        self.cards.add_relics()


    # Identify diamonds of current winner
    def identify_highest_diamonds(self):
        amount_current_winner = 0
        for explorer in self.explorers:
            e_diamonds = explorer.chest + explorer.pocket + (self.diamonds_on_way // len(self.players_inside))
            if amount_current_winner <= e_diamonds:
                amount_current_winner = e_diamonds
        return amount_current_winner

    # Ask the player / bot what he wants to do
    def ask_explorer(self, current_player):
        render_tell_relics_on_way(game_object = self)
        if not current_player.is_bot:
            decision = render_ask_player(game_object = self, current_player = current_player)
            if decision == "leave":
                current_player.go_home()
        elif len(self.bots) != 0 and current_player.is_bot:
            act_on_card = Act_On_Card(game_object = self, current_bot = current_player)
            act_on_card.ask_bot()


    # Put share of diamonds on the way into the home going player's chests
    def split_diamonds_on_way(self):
        if len(self.go_home_now) != 0:
            for homer in self.go_home_now:
                homer.chest += self.diamonds_on_way // len(self.go_home_now)
            self.diamonds_on_way %= len(self.go_home_now)

    # Put the relics in the home going player's chest (only if he's alone)
    def earn_relics(self):
        if self.relics_on_way != 0 and len(self.go_home_now) == 1:
            self.go_home_now[0].chest += self.relics_on_way
            self.relics_on_way = 0

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
            explorer.collected_diamonds.append(booty)
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
        self.final_winners = final_winners
        for winner in final_winners:
            winner.game_winning_count += 1

    def get_max_diamonds(self):
        for explorer in self.explorers:
            for diamonds in explorer.collected_diamonds:
                if diamonds > explorer.max_diamonds:
                    explorer.max_diamonds = diamonds

    # Reset the game
    def reset_game(self):
        self.cards.full_deck = self.cards.traps + self.cards.treasure_cards
        self.bots.clear()
        self.level_bots.clear()
        self.players.clear()
        self.explorers.clear()
        self.final_winners.clear()
        self.create_explorers()

    # Play 5 rounds and ask about playing again
    def play_rounds(self):
        for self.rounds in range(5):
            # Start Round
            self.reset_round()
            render_tell_round(game_object=self)
            self.p_inside = True
            while self.p_inside:
                if self.check_players_inside:
                    drawcard = Draw_Card(self)
                    drawcard.draw_card()
                else:
                    self.p_inside = False
            self.identify_round_winner()
        self.identify_game_winner()
        render_tell_result(game_object = self)
        render_ask_again(game_object = self)

    # Main method
    def main(self):
        render_welcome_txt(game_object = self)
        self.create_explorers()
        while self.is_running:
            self.play_rounds()
