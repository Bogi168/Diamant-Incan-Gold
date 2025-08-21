import random
#Spieler
import _player

#Karten
snakes = ["🐍", "🐍", "🐍"]
spiders = ["🕷", "🕷", "🕷"]
fires = ["🔥", "🔥", "🔥"]
avalanches = ["🌑", "🌑", "🌑"]
mummys = ["👤", "👤", "👤"]
treasure_cards = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
relics = [5.01, 7.01, 8.01, 10.01, 12.01]
traps = []
cards = []
players = []

def create_deck():
    for snake in snakes:
        card = snake
        traps.append(card)
    for spider in spiders:
        card = spider
        traps.append(card)
    for fire in fires:
        card = fire
        traps.append(card)
    for avalanche in avalanches:
        card = avalanche
        traps.append(card)
    for mummy in mummys:
        card = mummy
        traps.append(card)

    for snake in snakes:
        card = snake
        cards.append(card)
    for spider in spiders:
        card = spider
        cards.append(card)
    for fire in fires:
        card = fire
        cards.append(card)
    for avalanche in avalanches:
        card = avalanche
        cards.append(card)
    for mummy in mummys:
        card = mummy
        cards.append(card)
    for treasure in treasure_cards:
        card = treasure
        cards.append(card)

def start_game():
    print("****************************************")
    print("* Welcome to Incan Gold - Bogi Edition *")
    print("****************************************")
    print()

def create_players():
    players_amount = input("How many players? ")
    while not players_amount.isdigit() or int(players_amount) <= 0:
        players_amount = input("That's not a valid number. How many players? ")
    print()
    print("________________________________________")
    players_amount = int(players_amount)
    c_players = []
    for player_num in range(players_amount):
        player_name = input(f"Enter player number {player_num + 1}'s name: ").capitalize()
        c_players.append(player_name)
        print("________________________________________")
    c_players = [_player.Player(c_players[i]) for i in range(len(c_players))]
    return c_players

class Game:
    def __init__(self):
        # Spiel
        self.is_running = True
        self.rounds = 0
        self.p_inside = True
        self.played_cards = []
        self.diamonds_on_way = 0
        self.relics_on_way = 0
        self.players_inside = [p for p in players if p.inside]
        self.p_relics = relics.copy()
        self.winners = []

    def tell_round(self):
        print()
        print("****************************************")
        print(f"*               Round: {(self.rounds + 1)}               *")
        print("****************************************")

    def draw_card(self):
        drawn = random.choice(self.p_cards)
        self.p_cards.remove(drawn)
        return drawn

    def sec_trap(self):
        print()
        print(f"Oh no! It's the second {self.new_card}")
        print("All the players inside lose their diamonds!")
        if self.rounds == 5 - 1:
            print()
            print("_____________________________________________________________")
        cards.remove(self.new_card)
        for p in self.players_inside:
            p.die()
        self.p_inside = False

    def tell_new_card(self):
        print()
        print(f"The drawn card was a {self.new_card}")
        print()

    def split_diamonds_on_way(self):
        if len(_player.go_home_now) != 0:
            for homer in _player.go_home_now:
                homer.chest += self.diamonds_on_way // len(_player.go_home_now)
            self.diamonds_on_way %= len(_player.go_home_now)

    def tell_result(self):
        d_winner = 0
        for s in players:
            print(f"{s.player_name} collected {s.chest} Diamonds")
            if d_winner < s.chest:
                d_winner = s.chest
                self.winners.clear()
                self.winners.append(s)
            elif d_winner == s.chest:
                self.winners.append(s)
        print("_____________________________________________________________")
        print()
        print("*************************************************************")
        if len(self.winners) == 1:
            print(f"The winner is: {self.winners[0].player_name}")
        else:
            print(f"The winners are: ", end = "")
            for winner in self.winners:
                if winner == self.winners[-1]:
                    print("& " + winner.player_name)
                elif winner == self.winners[-2]:
                    print(winner.player_name, end=" ")
                else:
                    print(winner.player_name, end=", ")
        print("*************************************************************")
        print()

    def tell_played_cards(self):
        print()
        print("Played Cards: ", end="")
        for played_card in self.played_cards:
            print(played_card, end=" ")
        print()

    def act_on_card(self):
        if self.new_card in treasure_cards and len(self.players_inside) != 0:
            self.diamonds_on_way += self.new_card % len(self.players_inside)
        if self.new_card in relics:
            self.relics_on_way += int(self.new_card)
            cards.remove(self.new_card)
        for i in range(len(self.players_inside)):
            if self.new_card in traps:
                print("_____________________________________________________________")
                if self.relics_on_way != 0:
                    print(f"There are relics worth {self.relics_on_way} diamonds on the way")
                self.players_inside[i].ask_question(self.diamonds_on_way)

            elif self.new_card in treasure_cards:
                print("_____________________________________________________________")
                self.players_inside[i].pocket += self.new_card // len(self.players_inside)
                if self.relics_on_way != 0:
                    print(f"There are relics worth {self.relics_on_way} diamonds on the way")
                self.players_inside[i].ask_question(self.diamonds_on_way)

            elif self.new_card in relics:
                print("_____________________________________________________________")
                print(f"There are relics worth {self.relics_on_way} diamonds on the way")
                self.players_inside[i].ask_question(self.diamonds_on_way)
    def earn_relics(self):
        if self.relics_on_way != 0 and len(_player.go_home_now) == 1:
            _player.go_home_now[0].chest += self.relics_on_way
            self.relics_on_way = 0

    def reset_round(self):
        self.played_cards.clear()
        self.players_inside.clear()
        for p in players:
            p.inside = True
        self.players_inside = [p for p in players if p.inside]
        self.diamonds_on_way = 0
        self.relics_on_way = 0
        self.p_cards = cards.copy()
        
    def ask_again(self):
        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again != "Y":
            self.is_running = False

    def main(self):
        while self.is_running:
            for self.rounds in range(5):
                card = self.p_relics[self.rounds]
                cards.append(card)
                self.p_cards = cards.copy()
                self.tell_round()
                self.p_inside = True
                while self.p_inside:

                    if len(self.players_inside) == 0:
                        self.p_inside = False

                    else:
                        self.new_card = self.draw_card()
                        if self.new_card in traps and self.new_card in self.played_cards:
                            self.sec_trap()
                            continue
                        self.tell_new_card()
                        self.act_on_card()
                        self.split_diamonds_on_way()
                        self.earn_relics()
                        _player.go_home_now.clear()
                        self.players_inside = [p for p in players if p.inside]
                        self.played_cards.append(self.new_card)
                        self.tell_played_cards()

                self.reset_round()

            self.tell_result()
            self.ask_again()

if __name__ == "__main__":
    create_deck()
    start_game()
    players = create_players()
    game = Game()
    game.main()
