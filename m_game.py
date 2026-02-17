# Classes Player and Bot
from Main_Game.m_cards import Cards
from Main_Game.m_New_Card_Event import Draw_Card
from Main_Game.m_Level_Strategy import Act_On_Card
from Main_Game.m_renders import *
from Main_Game.m_probability_and_ev import calc_dying_prob, calc_undiscovered_diamonds


# Main_Game
class Game:
    def __init__(self, renderer):
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

        # Create renderer
        self.renderer = renderer

    @property
    def dying_prob(self):
        return calc_dying_prob(cards_object = self.cards)

    @property
    def undiscovered_diamonds(self):
        return calc_undiscovered_diamonds(cards_object = self.cards)

    @property
    def amount_current_winner(self):
        return self.identify_highest_diamonds()


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
        for p in self.explorers:
            p.inside = True
        self.players_inside = [p for p in self.explorers]
        self.diamonds_on_way = 0
        self.relics_on_way = 0
        self.cards.reset_played_cards()
        self.cards.add_relics()

    # Start Round
    def start_round(self):
        self.reset_round()
        render_tell_round(game_object = self)
        self.p_inside = True

    # Check whether players inside
    def no_players_inside(self):
        if len(self.players_inside) == 0:
            self.p_inside = False
            return True
        else:
            return False

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
            act_on_card = Act_On_Card(self, current_player)
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

    # Still players inside
    def still_players_inside(self):
        if not self.no_players_inside():
            drawcard = Draw_Card(self)
            drawcard.draw_card()

    def identify_game_winner(self):
        amount_final_winner = 0
        for explorer in self.explorers:
            if amount_final_winner < explorer.chest:
                amount_final_winner = explorer.chest
                self.final_winners.clear()
                self.final_winners.append(explorer)
            elif amount_final_winner == explorer.chest:
                self.final_winners.append(explorer)

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
            self.start_round()
            while self.p_inside:
                self.no_players_inside()
                self.still_players_inside()
        render_tell_result(game_object = self)
        render_ask_again(game_object = self)

    # Main method
    def main(self):
        render_welcome_txt(game_object = self)
        self.create_explorers()
        while self.is_running:
            self.play_rounds()
