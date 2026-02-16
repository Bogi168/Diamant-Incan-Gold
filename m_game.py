# Classes Player and Bot
from Main_Game.m_cards import Cards
from Main_Game.m_NewCardEvent import Draw_Card
from Main_Game.m_LevelStrategy import Act_On_Card
from Main_Game.m_console import *

# Main_Game
class Game:
    def __init__(self):
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
        self.undiscovered_diamonds = 0
        self.dying_prob = 0
        self.surviving_prob = 0
        self.ev_next = 0
        self.amount_current_winner = 0
        self.amount_final_winner = 0

        # Create cards object
        self.cards = Cards(self)

    # Create explorers
    def create_explorers(self):
        console_create_players(game_object = self)
        console_create_bots(game_object = self)
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
        console_tell_round(game_object = self)
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
        self.amount_current_winner = 0
        for explorer in self.explorers:
            e_diamonds = explorer.chest + explorer.pocket + (self.diamonds_on_way // len(self.players_inside))
            if self.amount_current_winner <= e_diamonds:
                self.amount_current_winner = e_diamonds

    # Ask the player / bot what he wants to do
    def ask_explorer(self, current_player):
        console_tell_relics_on_way(game_object = self)
        if not current_player.is_bot:
            decision = console_ask_player(game_object = self, cards_object = self.cards, current_player = current_player)
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
        for s in self.explorers:
            if self.amount_final_winner < s.chest:
                self.amount_final_winner = s.chest
                self.final_winners.clear()
                self.final_winners.append(s)
            elif self.amount_final_winner == s.chest:
                self.final_winners.append(s)

    # Reset the game
    def reset_game(self):
        self.cards.full_deck = self.cards.traps + self.cards.treasure_cards
        self.bots.clear()
        self.level_bots.clear()
        self.players.clear()
        self.explorers.clear()
        self.final_winners.clear()
        print()
        self.create_explorers()

    # Play 5 rounds and ask about playing again
    def play_rounds(self):
        for self.rounds in range(5):
            self.start_round()
            while self.p_inside:
                self.no_players_inside()
                self.still_players_inside()
        console_tell_result(game_object = self)
        console_ask_again(game_object = self)

    # Main method
    def main(self):
        console_welcome_txt()
        self.create_explorers()
        while self.is_running:
            self.play_rounds()
