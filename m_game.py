# Classes Player and Bot
from Main_Game.m_cards import Cards
from Main_Game.m_NewCardEvent import Draw_Card
from Main_Game.m_LevelStrategy import Act_On_Card
from Main_Game.m_console import Console

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

        # Create console object
        self.console = Console(self)


    # Create explorers
    def create_explorers(self):
        self.console.create_players()
        self.console.create_bots()
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
        self.console.tell_round()
        self.p_inside = True

    # Check whether players inside
    def no_players_inside(self):
        if len(self.players_inside) == 0:
            self.p_inside = False
            return True
        else:
            return False

    # Calculate probability of dying on the next move
    def calc_dying_prob(self):
        killing_traps = 0
        probability = 0
        self.cards.played_cards.append(self.cards.new_card)
        for card in self.cards.played_cards:
            if card in self.cards.traps:
                traps_in_game = self.cards.deck.count(card)
                killing_traps += traps_in_game
        probability += killing_traps / len(self.cards.deck)
        self.cards.played_cards.pop(-1)
        self.dying_prob = probability
        return probability

    # Calculate amount of undiscovered diamonds
    def calc_undiscovered_diamonds(self):
        self.undiscovered_diamonds = 0
        self.cards.played_cards.append(self.cards.new_card)
        for card in self.cards.deck:
            if card in self.cards.treasure_cards:
                self.undiscovered_diamonds += card
        self.cards.played_cards.pop(-1)

    def calc_guaranteed_diamonds(self, player):
        player.guaranteed_diamonds = player.pocket + self.diamonds_on_way // len(self.players_inside)
        if len(self.players_inside) == 1:
            player.guaranteed_diamonds += self.relics_on_way

    def calc_ev_next(self, player):
        self.calc_dying_prob()
        self.surviving_prob = (1 - self.dying_prob)
        self.calc_undiscovered_diamonds()
        future_diamonds = (self.undiscovered_diamonds / (len(self.cards.deck) * len(self.players_inside))
                           + player.pocket) #+ self.diamonds_on_way // len(self.players_inside))
        ev_next = self.surviving_prob * future_diamonds - self.dying_prob * (player.pocket) #+ self.diamonds_on_way // len(self.players_inside))
        return ev_next

    def calc_ev_next_dia_on_way(self, player):
        self.calc_dying_prob()
        self.surviving_prob = (1 - self.dying_prob)
        self.calc_undiscovered_diamonds()
        self.calc_guaranteed_diamonds(player)
        future_diamonds = self.undiscovered_diamonds / (len(self.cards.deck) * len(self.players_inside)) + player.guaranteed_diamonds
        ev_next = self.surviving_prob * future_diamonds - self.dying_prob * player.guaranteed_diamonds
        return ev_next

    # Identify diamonds of current winner
    def identify_highest_diamonds(self):
        self.amount_current_winner = 0
        for explorer in self.explorers:
            e_diamonds = explorer.chest + explorer.pocket + (self.diamonds_on_way // len(self.players_inside))
            if self.amount_current_winner <= e_diamonds:
                self.amount_current_winner = e_diamonds

    # Ask the player / bot what he wants to do
    def ask_explorer(self, player):
        self.console.tell_relics_on_way()
        if not player.is_bot:
            decision = self.console.ask_player(player)
            if decision == "leave":
                player.go_home()
        elif len(self.bots) != 0 and player.is_bot:
            act_on_card = Act_On_Card(self, player)
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
        self.cards.traps = self.cards.snakes + self.cards.spiders + self.cards.fires + self.cards.avalanches + self.cards.mummies
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
        self.console.tell_result()
        self.console.ask_again()

    # Main method
    def main(self):
        Console.welcome_txt(self)
        self.create_explorers()
        while self.is_running:
            self.play_rounds()
