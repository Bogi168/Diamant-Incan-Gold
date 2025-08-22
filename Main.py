#Random module
import random

#Classes Player and Bot
import _player

#Game
class Game:
    def __init__(self):
        # Define cards
        self.snakes = ["🐍"] * 3
        self.spiders = ["🕷"] * 3
        self.fires = ["🔥"] * 3
        self.avalanches = ["🌑"] * 3
        self.mummys = ["👤"] * 3
        self.treasure_cards = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
        self.relics = [5.01, 7.01, 8.01, 10.01, 12.01]
        self.traps = self.snakes + self.spiders + self.fires + self.avalanches + self.mummys
        self.cards = self.traps + self.treasure_cards

        # Define players
        self.players = []
        self.level_bots = []
        self.bots = []
        self.explorers = []

        # Define Game variables
        self.is_running = True
        self.rounds = 0
        self.p_inside = True
        self.diamonds_on_way = 0
        self.relics_on_way = 0

        # Define card lists
        self.played_cards = []
        self.players_inside = []
        self.p_relics = self.relics.copy()
        self.go_home_now = []
        self.winners = []

    # Welcome text
    def start_game(self):
        print("****************************************")
        print("* Welcome to Incan Gold - Bogi Edition *")
        print("****************************************")
        print()

    # Create players
    def create_players(self):
        players_amount = input("How many players? ")
        while not players_amount.isdigit() or int(players_amount) <= 0:
            players_amount = input("That's not a valid number. How many players? ")
        print()
        print("________________________________________")
        players_amount = int(players_amount)
        for player_num in range(players_amount):
            player_name = input(f"Enter player number {player_num + 1}'s name: ").capitalize()
            self.players.append(player_name)
            print("________________________________________")
        self.players = [_player.Player(self.players[i]) for i in range(len(self.players))]

    # Create bots
    def create_bots(self):
        print()
        bots_amount = input("How many bots? ")
        while not bots_amount.isdigit() or int(bots_amount) < 0:
            bots_amount = input("That's not a valid number. How many bots? ")
        print()
        print("________________________________________")
        bots_amount = int(bots_amount)
        if bots_amount != 0:
            for l in range(bots_amount):
                level_bot = input(f"Select a level for Bot {l + 1} (careful: 1 / medium: 2 / risky: 3): ")
                while not level_bot == "1" and not level_bot == "2" and not level_bot == "3":
                    level_bot = input(
                        f"{level_bot} is not valid. Select a level for Bot {l + 1} (careful: 1 / medium: 2 / risky: 3): ")
                level_bot = int(level_bot)
                self.level_bots.append(level_bot)
            for bots_num in range(bots_amount):
                self.bots.append(f"Bot {bots_num + 1}")
            self.bots = [_player.Bot(self.bots[i], self.level_bots[i]) for i in range(len(self.bots))]

    # Create explorers
    def create_explorers(self):
        self.create_players()
        self.create_bots()
        if len(self.bots) == 0:
            self.explorers = self.players
        else:
            self.explorers = self.players + self.bots
        self.players_inside = [p for p in self.explorers if p.inside]

    # Current round
    def tell_round(self):
        print()
        print("****************************************")
        print(f"*               Round: {(self.rounds + 1)}               *")
        print("****************************************")

    # Draw cards
    def draw_card(self):
        drawn = random.choice(self.deck)
        self.deck.remove(drawn)
        return drawn

    # Second trap
    def sec_trap(self):
        print()
        print(f"Oh no! It's the second {self.new_card}")
        print("All the players inside lose their diamonds!")
        if self.rounds == 5 - 1:
            print()
            print("_____________________________________________________________")
        self.cards.remove(self.new_card)
        for p in self.players_inside:
            p.die()
        self.p_inside = False

    # Calculate probability of dying on the next move
    def calc_prob(self):
        killing_traps = 0
        probability = 0
        self.played_cards.append(self.new_card)
        for card in self.played_cards:
            if card in self.traps:
                traps_in_game = self.deck.count(card)
                killing_traps += traps_in_game
        probability += killing_traps / len(self.deck)
        self.played_cards.pop(-1)
        return probability

    # Tell situation
    def tell_new_card(self):
        print()
        print(f"The drawn card was a {self.new_card}")
        print()

    def tell_probability(self):
        return f"The probability of dying in the next move is {self.calc_prob()*100:.1f}%"

    def tell_relics_on_way(self):
        if self.relics_on_way != 0:
            print(f"There are relics worth {self.relics_on_way} diamonds on the way")

    # First trap
    def new_in_traps(self):
        if self.new_card in self.traps:
            print("_____________________________________________________________")
            print()
            print(self.tell_probability())
            print()
            self.tell_relics_on_way()

    # Put remainder of treasure card on the way
    def new_in_treasure_cards_1(self):
        if self.new_card in self.treasure_cards and len(self.players_inside) != 0:
            self.diamonds_on_way += self.new_card % len(self.players_inside)

    # Put share of treasure card in pocket
    def new_in_treasure_cards_2(self, i):
        if self.new_card in self.treasure_cards:
            print("_____________________________________________________________")
            self.players_inside[i].pocket += self.new_card // len(self.players_inside)
            print()
            print(self.tell_probability())
            print()
            self.tell_relics_on_way()

    # Put relics on the way
    def new_in_relics_1(self):
        if self.new_card in self.relics:
            self.relics_on_way += int(self.new_card)
            self.cards.remove(self.new_card)

    # Tell the amount of relics on the way
    def new_in_relics_2(self):
        if self.new_card in self.relics:
            print("_____________________________________________________________")
            print()
            print(self.tell_probability())
            print()
            self.tell_relics_on_way()

    # Take action based on the drawn card
    def act_on_card(self):
        self.new_in_treasure_cards_1()
        self.new_in_relics_1()
        for i in range(len(self.players_inside)):
            self.new_in_traps()
            self.new_in_treasure_cards_2(i)
            self.new_in_relics_2()
            self.ask_explorer(i)

    # Ask the player / bot what he wants to do
    def ask_explorer(self, i):
        if not self.players_inside[i].is_bot:
            self.players_inside[i].ask_player(self.diamonds_on_way, self.go_home_now)
        elif len(self.bots) != 0 and self.players_inside[i].is_bot:
            self.players_inside[i].ask_bot(self.diamonds_on_way, self.relics_on_way, self.calc_prob(), self.go_home_now)

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

    # Tell the played cards
    def tell_played_cards(self):
        print()
        print("Played Cards: ", end="")
        for played_card in self.played_cards:
            print(played_card, end=" ")
        print()

    # Prepare next round
    def reset_round(self):
        self.played_cards.clear()
        self.players_inside.clear()
        for p in self.explorers:
            p.inside = True
        self.players_inside = [p for p in self.explorers if p.inside]
        self.diamonds_on_way = 0
        self.relics_on_way = 0
        self.deck = self.cards.copy()

    # Find the winner
    def identify_winner(self):
        d_winner = 0
        print()
        print("_____________________________________________________________")
        for s in self.explorers:
            print(f"{s.player_name} collected {s.chest} Diamonds")
            if d_winner < s.chest:
                d_winner = s.chest
                self.winners.clear()
                self.winners.append(s)
            elif d_winner == s.chest:
                self.winners.append(s)
        print("_____________________________________________________________")
        print()

    # Present the result
    def tell_result(self):
        self.identify_winner()
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

    # Reset the cards
    def reset_game(self):
        self.traps = self.snakes + self.spiders + self.fires + self.avalanches + self.mummys
        self.cards = self.traps + self.treasure_cards

    # Ask about playing again
    def ask_again(self):
        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again == "Y":
            self.reset_game()
            for e in self.explorers:
                e.chest = 0
        else:
            self.is_running = False

    def main(self):
        self.start_game()
        self.create_explorers()
        while self.is_running:
            for self.rounds in range(5):
                #Add relics
                card = self.p_relics[self.rounds]
                self.cards.append(card)
                self.deck = self.cards.copy()
                #Start Round
                self.tell_round()
                self.p_inside = True
                while self.p_inside:
                    #No players inside
                    if len(self.players_inside) == 0:
                        self.p_inside = False

                    else:
                        self.new_card = self.draw_card()
                        if self.new_card in self.traps and self.new_card in self.played_cards:
                            self.sec_trap()
                            continue
                        self.tell_new_card()
                        self.act_on_card()
                        self.split_diamonds_on_way()
                        self.earn_relics()
                        self.go_home_now.clear()
                        self.players_inside = [p for p in self.explorers if p.inside]
                        self.played_cards.append(self.new_card)
                        self.tell_played_cards()

                self.reset_round()

            self.tell_result()
            self.ask_again()

if __name__ == "__main__":
    game = Game()
    game.main()
