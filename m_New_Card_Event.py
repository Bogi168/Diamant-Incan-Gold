from abc import ABC, abstractmethod
from Main_Game.m_probability_and_ev import calc_dying_prob
from Main_Game.m_console import console_tell_played_cards, console_tell_new_card, console_second_trap, console_no_second_trap

class New_Card(ABC):
    def __init__(self, game_object):
        self.game_object = game_object

    @abstractmethod
    def act_on_card(self):
        pass

class Second_Trap(New_Card):
    def act_on_card(self):
        console_second_trap(game_object = self.game_object, cards_object = self.game_object.cards)
        self.game_object.cards.full_deck.remove(self.game_object.cards.new_card)
        for player in self.game_object.players_inside:
            player.die()
        self.game_object.p_inside = False

class First_Trap(New_Card):
    def act_on_card(self):
        self.game_object.identify_highest_diamonds()
        for player in self.game_object.players_inside:
            console_no_second_trap(game_object = self.game_object)
            self.game_object.ask_explorer(player)

class Treasure_Card(New_Card):
    def act_on_card(self):
        self.game_object.diamonds_on_way += self.game_object.cards.new_card.value % len(self.game_object.players_inside)
        self.game_object.identify_highest_diamonds()
        for player in self.game_object.players_inside:
            console_no_second_trap(game_object = self.game_object)
            player.pocket += self.game_object.cards.new_card.value // len(self.game_object.players_inside)
            self.game_object.ask_explorer(player)


class Relics(New_Card):
    def act_on_card(self):
        self.game_object.relics_on_way += self.game_object.cards.new_card.value
        self.game_object.cards.full_deck.remove(self.game_object.cards.new_card)
        self.game_object.identify_highest_diamonds()
        for player in self.game_object.players_inside:
            console_no_second_trap(game_object = self.game_object)
            self.game_object.ask_explorer(player)

class Draw_Card:
    def __init__(self, game_object):
        self.game_object = game_object

    def check_second_trap(self):
        if (self.game_object.cards.new_card.card_type == "trap" and
                self.game_object.cards.new_card in self.game_object.cards.played_cards):
            return True
        else:
            return False

    def draw_card(self):
        self.game_object.cards.draw_card()
        calc_dying_prob(game_object = self.game_object, cards_object = self.game_object.cards)
        if self.check_second_trap():
            drawn_card = Second_Trap(self.game_object)
            drawn_card.act_on_card()
        else:
            console_tell_new_card(cards_object = self.game_object.cards)
            if self.game_object.cards.new_card.card_type == "treasure_card":
                drawn_card = Treasure_Card(self.game_object)
                drawn_card.act_on_card()

            elif self.game_object.cards.new_card.card_type == "trap":
                drawn_card = First_Trap(self.game_object)
                drawn_card.act_on_card()

            elif self.game_object.cards.new_card.card_type == "relic":
                drawn_card = Relics(self.game_object)
                drawn_card.act_on_card()

            self.game_object.split_diamonds_on_way()
            self.game_object.earn_relics()
            self.game_object.go_home_now.clear()
            self.game_object.players_inside = [p for p in self.game_object.explorers if p.inside]
            self.game_object.cards.played_cards.append(self.game_object.cards.new_card)
            console_tell_played_cards(cards_object = self.game_object.cards)
