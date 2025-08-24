# Classes Player and Bot
from _player import Player, Bot
from _cards import Cards

# Game
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

        # Define Game variables
        self.is_running = True
        self.rounds = 0
        self.p_inside = True
        self.diamonds_on_way = 0
        self.relics_on_way = 0
        self.amount_current_winner = 0
        self.amount_final_winner = 0


        # Create cards object
        self.cards = Cards()


    # Welcome text
    @staticmethod
    def welcome_txt():
        print()
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
            self.players.append(Player(player_name))
            print("________________________________________")


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
            for bots_num in range(bots_amount):
                level_bot = input(f"Select a level for Bot {bots_num + 1} (careful: 1 / medium: 2 / risky: 3): ")
                while not level_bot == "1" and not level_bot == "2" and not level_bot == "3":
                    level_bot = input(
                        f"{level_bot} is not valid. Select a level for Bot {bots_num + 1} (careful: 1 / medium: 2 / risky: 3): ")
                level_bot = int(level_bot)
                if level_bot == 1:
                    self.bots.append(Bot(f"Bot {bots_num + 1}", level_bot))
                elif level_bot == 2:
                    self.bots.append(Bot(f"Bot {bots_num + 1}", level_bot))
                elif level_bot == 3:
                    self.bots.append(Bot(f"Bot {bots_num + 1}", level_bot))

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

    # Reset previous round and add relics
    def reset_round(self):
        self.players_inside.clear()
        for p in self.explorers:
            p.inside = True
        self.players_inside = [p for p in self.explorers if p.inside]
        self.diamonds_on_way = 0
        self.relics_on_way = 0
        self.cards.reset_played_cards()
        self.cards.add_relics(self.rounds)

    # Start Round
    def start_round(self):
        self.reset_round()
        self.tell_round()
        self.p_inside = True

    # Check whether players inside
    def no_players_inside(self):
        if len(self.players_inside) == 0:
            self.p_inside = False
            return True
        else:
            return False

    # Check whether it is the second trap
    def check_second_trap(self):
        if self.cards.new_card in self.cards.traps and self.cards.new_card in self.cards.played_cards:
            return True
        else:
            return False

    # Second trap
    def sec_trap(self):
        if self.check_second_trap():
            print()
            print(f"Oh no! It's the second {self.cards.new_card}")
            print("All the players inside lose their diamonds!")
            if self.rounds == 5 - 1:
                print()
                print("_____________________________________________________________")
            self.cards.full_deck.remove(self.cards.new_card)
            for p in self.players_inside:
                p.die()
            self.p_inside = False
            return True
        else:
            return False

    # Calculate probability of dying on the next move
    def calc_prob(self):
        killing_traps = 0
        probability = 0
        self.cards.played_cards.append(self.cards.new_card)
        for card in self.cards.played_cards:
            if card in self.cards.traps:
                traps_in_game = self.cards.deck.count(card)
                killing_traps += traps_in_game
        probability += killing_traps / len(self.cards.deck)
        self.cards.played_cards.pop(-1)
        return probability

    # Tell situation
    def tell_new_card(self):
        print()
        print(f"The drawn card was a {self.cards.new_card}")
        print()

    def tell_probability(self):
        return f"The probability of dying in the next move is {self.calc_prob()*100:.1f}%"

    def tell_relics_on_way(self):
        if self.relics_on_way != 0:
            print(f"There are relics worth {self.relics_on_way} diamonds on the way")

    # Identify diamonds of current winner
    def identify_highest_diamonds(self):
        self.amount_current_winner = 0
        for c in self.explorers:
            c_diamonds = c.chest + c.pocket + (self.diamonds_on_way // len(self.players_inside))
            if self.amount_current_winner <= c_diamonds:
                self.amount_current_winner = c_diamonds

    # First trap
    def new_in_traps(self):
        if self.cards.new_card in self.cards.traps:
            print("_____________________________________________________________")
            print()
            print(self.tell_probability())
            print()
            self.tell_relics_on_way()

    # Put remainder of treasure card on the way
    def add_treasure_card_remainder_to_way(self):
        if self.cards.new_card in self.cards.treasure_cards:
            self.diamonds_on_way += self.cards.new_card % len(self.players_inside)

    # Put share of treasure card in pocket
    def new_in_treasure_cards(self, i):
        if self.cards.new_card in self.cards.treasure_cards:
            print("_____________________________________________________________")
            self.players_inside[i].pocket += self.cards.new_card // len(self.players_inside)
            print()
            print(self.tell_probability())
            print()
            self.tell_relics_on_way()

    # Put relics on the way
    def add_relics_to_relics_on_way(self):
        if self.cards.new_card in self.cards.relics:
            self.relics_on_way += int(self.cards.new_card)
            self.cards.full_deck.remove(self.cards.new_card)

    # Tell the amount of relics on the way
    def new_in_relics(self):
        if self.cards.new_card in self.cards.relics:
            print("_____________________________________________________________")
            print()
            print(self.tell_probability())
            print()
            self.tell_relics_on_way()

    # Ask the player / bot what he wants to do
    def ask_explorer(self, i):
        if not self.players_inside[i].is_bot:
            self.players_inside[i].ask_player(self.diamonds_on_way, self.go_home_now)
        elif len(self.bots) != 0 and self.players_inside[i].is_bot:
            self.players_inside[i].ask_bot(self.diamonds_on_way, self.players_inside, self.rounds, self.amount_current_winner,
                                           self.relics_on_way, self.calc_prob(), self.go_home_now)

    # Take action based on the drawn card
    def act_on_card(self):
        self.add_treasure_card_remainder_to_way()
        self.add_relics_to_relics_on_way()
        self.identify_highest_diamonds()
        for i in range(len(self.players_inside)):
            self.new_in_traps()
            self.new_in_treasure_cards(i)
            self.new_in_relics()
            self.ask_explorer(i)

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
        for played_card in self.cards.played_cards:
            print(played_card, end=" ")
        print()

    # Card is not the second trap
    def not_sec_traps(self):
        if not self.check_second_trap():
            self.tell_new_card()
            self.act_on_card()
            self.split_diamonds_on_way()
            self.earn_relics()
            self.go_home_now.clear()
            self.players_inside = [p for p in self.explorers if p.inside]
            self.cards.played_cards.append(self.cards.new_card)
            self.tell_played_cards()

    # Still players inside
    def still_players_inside(self):
        if not self.no_players_inside():
            self.cards.draw_card()
            self.sec_trap()
            self.not_sec_traps()

    def identify_final_winner(self):
        for s in self.explorers:
            if self.amount_final_winner < s.chest:
                self.amount_final_winner = s.chest
                self.final_winners.clear()
                self.final_winners.append(s)
            elif self.amount_final_winner == s.chest:
                self.final_winners.append(s)


    # Present the result
    def tell_result(self):
        print()
        print("_____________________________________________________________")
        self.identify_final_winner()
        for e in self.explorers:
            print(f"{e.player_name} collected {e.chest} Diamonds")
        print("_____________________________________________________________")
        print()
        print("*************************************************************")
        if len(self.final_winners) == 1:
            print(f"The winner is: {self.final_winners[0].player_name}")
        else:
            print(f"The winners are: ", end = "")
            for winner in self.final_winners:
                if winner == self.final_winners[-1]:
                    print("& " + winner.player_name)
                elif winner == self.final_winners[-2]:
                    print(winner.player_name, end=" ")
                else:
                    print(winner.player_name, end=", ")
        print("*************************************************************")
        print()

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

    # Ask about playing again
    def ask_again(self):
        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again == "Y":
            self.reset_game()
        else:
            print()
            print("Thanks for playing!")
            self.is_running = False

    # Play 5 rounds and ask about playing again
    def play_rounds(self):
        for self.rounds in range(5):
            self.start_round()
            while self.p_inside:
                self.no_players_inside()
                self.still_players_inside()
        self.tell_result()
        self.ask_again()

    # Main method
    def main(self):
        Game.welcome_txt()
        self.create_explorers()
        while self.is_running:
            self.play_rounds()
