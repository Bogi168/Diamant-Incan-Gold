class Probability_and_EV:
    def __init__(self, game_object):
        self.game_object = game_object

    # Calculate probability of dying on the next move
    def calc_dying_prob(self):
        killing_traps = 0
        probability = 0
        self.game_object.cards.played_cards.append(self.game_object.cards.new_card)
        for card in self.game_object.cards.played_cards:
            if card in self.game_object.cards.traps:
                traps_in_game = self.game_object.cards.deck.count(card)
                killing_traps += traps_in_game
        probability += killing_traps / len(self.game_object.cards.deck)
        self.game_object.cards.played_cards.pop(-1)
        self.game_object.dying_prob = probability

    # Calculate amount of undiscovered diamonds
    def calc_undiscovered_diamonds(self):
        self.game_object.undiscovered_diamonds = 0
        self.game_object.cards.played_cards.append(self.game_object.cards.new_card)
        for card in self.game_object.cards.deck:
            if card.card_type == "treasure_card":
                self.game_object.undiscovered_diamonds += card.value
        self.game_object.cards.played_cards.pop(-1)

    def calc_guaranteed_diamonds(self, player):
        player.guaranteed_diamonds = player.pocket + self.game_object.diamonds_on_way // len(self.game_object.players_inside)
        if len(self.game_object.players_inside) == 1:
            player.guaranteed_diamonds += self.game_object.relics_on_way

    def calc_ev_next(self, player):
        self.calc_dying_prob()
        self.game_object.surviving_prob = (1 - self.game_object.dying_prob)
        self.calc_undiscovered_diamonds()
        future_diamonds = (self.game_object.undiscovered_diamonds / (len(self.game_object.cards.deck) * len(self.game_object.players_inside))
                           + player.pocket) #+ self.diamonds_on_way // len(self.players_inside))
        ev_next = self.game_object.surviving_prob * future_diamonds - self.game_object.dying_prob * (player.pocket) #+ self.diamonds_on_way // len(self.players_inside))
        return ev_next

    def calc_ev_next_dia_on_way(self, player):
        self.calc_dying_prob()
        self.game_object.surviving_prob = (1 - self.game_object.dying_prob)
        self.calc_undiscovered_diamonds()
        self.calc_guaranteed_diamonds(player)
        future_diamonds = self.game_object.undiscovered_diamonds / (len(self.game_object.cards.deck) * len(self.game_object.players_inside)) + player.guaranteed_diamonds
        ev_next = self.game_object.surviving_prob * future_diamonds - self.game_object.dying_prob * player.guaranteed_diamonds
        return ev_next