import random

class Cards:
    def __init__(self, game_object):
        self.game_object = game_object
        # Define cards
        self.snakes = ["🐍"] * 3
        self.spiders = ["🕷"] * 3
        self.fires = ["🔥"] * 3
        self.avalanches = ["🌑"] * 3
        self.mummies = ["👤"] * 3
        self.treasure_cards = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
        self.relics = [5.01, 7.01, 8.01, 10.01, 12.01]
        self.traps = self.snakes + self.spiders + self.fires + self.avalanches + self.mummies
        self.full_deck = self.traps + self.treasure_cards

        # Define card lists
        self.deck = []
        self.new_card = None
        self.played_cards = []
        self.p_relics = self.relics.copy()

    # Reset played cards
    def reset_played_cards(self):
        self.played_cards.clear()
        self.deck = self.full_deck.copy()

    # Draw cards
    def draw_card(self):
        self.new_card = random.choice(self.deck)
        self.deck.remove(self.new_card)

    # Add relics
    def add_relics(self):
        relic = self.p_relics[self.game_object.rounds]
        self.full_deck.append(relic)
        self.deck = self.full_deck.copy()
