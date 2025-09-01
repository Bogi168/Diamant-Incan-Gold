from Main_Game.NewCardEvent import *

class s_Second_Trap(Second_Trap):
    def act_on_card(self):
        self.game_object.cards.full_deck.remove(self.game_object.cards.new_card)
        for p in self.game_object.players_inside:
            p.die()
        self.game_object.p_inside = False

class s_First_Trap(First_Trap):
    def act_on_card(self):
        self.game_object.identify_highest_diamonds()
        for p in self.game_object.players_inside:
            self.game_object.ask_explorer(p)

class s_Treasure_Card(Treasure_Card):
    def act_on_card(self):
        self.game_object.diamonds_on_way += self.game_object.cards.new_card % len(self.game_object.players_inside)
        self.game_object.identify_highest_diamonds()
        for p in self.game_object.players_inside:
            p.pocket += self.game_object.cards.new_card // len(self.game_object.players_inside)
            self.game_object.ask_explorer(p)

class s_Relics(Relics):
    def act_on_card(self):
        self.game_object.relics_on_way += int(self.game_object.cards.new_card)
        self.game_object.cards.full_deck.remove(self.game_object.cards.new_card)
        self.game_object.identify_highest_diamonds()
        for p in self.game_object.players_inside:
            self.game_object.ask_explorer(p)

class s_Draw_Card(Draw_Card):
    def draw_card(self):
        self.game_object.cards.draw_card()
        if self.check_second_trap():
            drawn_card = s_Second_Trap(self.game_object)
            drawn_card.act_on_card()
        elif not self.check_second_trap():
            if self.game_object.cards.new_card in self.game_object.cards.treasure_cards:
                drawn_card = s_Treasure_Card(self.game_object)
                drawn_card.act_on_card()

            elif self.game_object.cards.new_card in self.game_object.cards.traps:
                drawn_card = s_First_Trap(self.game_object)
                drawn_card.act_on_card()

            elif self.game_object.cards.new_card in self.game_object.cards.relics:
                drawn_card = s_Relics(self.game_object)
                drawn_card.act_on_card()

            self.game_object.split_diamonds_on_way()
            self.game_object.earn_relics()
            self.game_object.go_home_now.clear()
            self.game_object.players_inside = [p for p in self.game_object.explorers if p.inside]
            self.game_object.cards.played_cards.append(self.game_object.cards.new_card)