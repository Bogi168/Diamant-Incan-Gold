import random

class Card:
    def __init__(self, card_type, name, value = 0):
        self.card_type = card_type
        self.name = name
        self.value = value

    def __repr__(self):
        return self.name

class Cards:
    def __init__(self, game_object):
        self.game_object = game_object
        # Define cards
        self.traps = [Card("trap","🐍"),
                      Card("trap", "🕷"),
                      Card("trap", "🔥"),
                      Card("trap", "🌑"),
                      Card("trap", "👤")] * 3
        self.treasure_cards = [Card("treasure_card", str(v), v)
                            for v in [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]]
        self.relics = [Card("relic", f"Relic ({r})", r)
                       for r in [5, 7, 8, 10, 12]]
        self.full_deck = self.traps + self.treasure_cards

        # Define card lists
        self.deck = []
        self.new_card = None
        self.played_cards = []

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
        relic = self.relics[self.game_object.rounds]
        self.full_deck.append(relic)
        self.deck = self.full_deck.copy()
