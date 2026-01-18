from abc import ABC, abstractmethod

class New_Card(ABC):
    def __init__(self, game_object):
        self.game_object = game_object

    @abstractmethod
    def act_on_card(self):
        pass

class Second_Trap(New_Card):
    def act_on_card(self):
        print()
        print(f"Oh no! It's the second {self.game_object.cards.new_card}")
        print("All the players inside lose their diamonds!")
        if self.game_object.rounds == 5 - 1:
            print()
            print("_____________________________________________________________")
        self.game_object.cards.full_deck.remove(self.game_object.cards.new_card)
        for p in self.game_object.players_inside:
            p.die()
        self.game_object.p_inside = False

class First_Trap(New_Card):
    def act_on_card(self):
        self.game_object.identify_highest_diamonds()
        for p in self.game_object.players_inside:
            print("_____________________________________________________________")
            print()
            print(self.game_object.tell_probability())
            print()
            self.game_object.ask_explorer(p)

class Treasure_Card(New_Card):
    def act_on_card(self):
        self.game_object.diamonds_on_way += self.game_object.cards.new_card % len(self.game_object.players_inside)
        self.game_object.identify_highest_diamonds()
        for p in self.game_object.players_inside:
            print("_____________________________________________________________")
            p.pocket += self.game_object.cards.new_card // len(self.game_object.players_inside)
            print()
            print(self.game_object.tell_probability())
            print()
            self.game_object.ask_explorer(p)


class Relics(New_Card):
    def act_on_card(self):
        self.game_object.relics_on_way += int(self.game_object.cards.new_card)
        self.game_object.cards.full_deck.remove(self.game_object.cards.new_card)
        self.game_object.identify_highest_diamonds()
        for p in self.game_object.players_inside:
            print("_____________________________________________________________")
            print()
            print(self.game_object.tell_probability())
            print()
            self.game_object.ask_explorer(p)

class Draw_Card:
    def __init__(self, game_object):
        self.game_object = game_object

    def check_second_trap(self):
        if (self.game_object.cards.new_card in self.game_object.cards.traps and
                self.game_object.cards.new_card in self.game_object.cards.played_cards):
            return True
        else:
            return False

    def tell_new_card(self):
        print()
        print(f"The drawn card was a {self.game_object.cards.new_card}")
        print()

    def draw_card(self):
        self.game_object.cards.draw_card()
        self.game_object.calc_dying_prob()
        if self.check_second_trap():
            drawn_card = Second_Trap(self.game_object)
            drawn_card.act_on_card()
        elif not self.check_second_trap():
            self.tell_new_card()
            if self.game_object.cards.new_card in self.game_object.cards.treasure_cards:
                drawn_card = Treasure_Card(self.game_object)
                drawn_card.act_on_card()

            elif self.game_object.cards.new_card in self.game_object.cards.traps:
                drawn_card = First_Trap(self.game_object)
                drawn_card.act_on_card()

            elif self.game_object.cards.new_card in self.game_object.cards.relics:
                drawn_card = Relics(self.game_object)
                drawn_card.act_on_card()

            self.game_object.split_diamonds_on_way()
            self.game_object.earn_relics()
            self.game_object.go_home_now.clear()
            self.game_object.players_inside = [p for p in self.game_object.explorers if p.inside]
            self.game_object.cards.played_cards.append(self.game_object.cards.new_card)
            self.game_object.tell_played_cards()
