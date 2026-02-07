from Main_Game.m_player import Player, Bot

class Console:
    def __init__(self, game_object):
        self.game_object = game_object

    # Welcome text
    @staticmethod
    def welcome_txt(self):
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
            self.game_object.players.append(Player(player_name = player_name, game_object = self.game_object))
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
                while not level_bot in ("1", "2", "3", "4"):
                    level_bot = input(
                        f"{level_bot} is not valid. Select a level for Bot {bots_num + 1} (careful: 1 / medium: 2 / risky: 3): ")
                level_bot = int(level_bot)
                self.game_object.bots.append(Bot(bot_name = f"Bot {bots_num + 1}", level = level_bot, game_object = self.game_object))

    # Current round
    def tell_round(self):
        print()
        print("****************************************")
        print(f"*               Round: {(self.game_object.rounds + 1)}               *")
        print("****************************************")

    # Tell the played cards
    def tell_played_cards(self):
        print()
        print("Played Cards: ", end="")
        for played_card in self.game_object.cards.played_cards:
            print(played_card, end=" ")
        print()

    def tell_new_card(self):
        print()
        print(f"The drawn card was a {self.game_object.cards.new_card}")
        print()

    # Output depending on drawn card
    def second_trap(self):
        print()
        print(f"Oh no! It's the second {self.game_object.cards.new_card}")
        print("All the players inside lose their diamonds!")
        if self.game_object.rounds == 5 - 1:
            print()
            print("_____________________________________________________________")

    def first_trap_or_treasure_card_or_relics(self):
        print("_____________________________________________________________")
        print()
        print(self.tell_probability())
        print()

    # Tell situation
    def tell_probability(self):
        return f"The probability of dying in the next move is {self.game_object.dying_prob * 100:.1f}%"

    def tell_relics_on_way(self):
        if self.game_object.relics_on_way != 0:
            print(f"There are relics worth {self.game_object.relics_on_way} diamonds on the way")

    # Present Player's diamonds
    def tell_p_diamonds(self, player):
        print(f"You have {player.pocket} diamond(s) in your pocket")
        print(f"There is/are {self.game_object.diamonds_on_way} diamond(s) on the way home")
        print(f"The expected value is {self.game_object.calc_ev_next(player):.2f}")
        print("_____________________________________________________________")

    def ask_player(self, player):
        self.tell_p_diamonds(player)
        decision = input(f"{player.player_name}: Do you want to go home? (Y/N) ").upper()
        while not decision.isalpha():
            decision = input(f"{player.player_name}: {decision} is not valid. Do you want to go home? (Y/N) ").upper()
        print("_____________________________________________________________")
        if decision == "Y" or decision == "YES":
            return "leave"
        else:
            return "stay"

    # Bot goes home
    def bot_goes_home(self, bot):
        print(f"{bot.bot_name} goes home and saves his diamond(s)")
        print("_____________________________________________________________")

    # Bot stays inside
    def bot_stays_inside(self, bot):
        print(f"{bot.bot_name} stays inside")
        print("_____________________________________________________________")

    # Present Bot's diamonds
    def tell_b_diamonds(self, bot):
        print(f"{bot.bot_name} has {bot.pocket} diamond(s) in his pocket")
        print(f"There is/are {self.game_object.diamonds_on_way} diamond(s) on the way home")
        print("_____________________________________________________________")

    # Present the result
    def tell_result(self):
        print()
        print("_____________________________________________________________")
        self.game_object.identify_game_winner()
        for explorer in self.game_object.explorers:
            print(f"{explorer.player_name} collected {explorer.chest} Diamonds")
        print("_____________________________________________________________")
        print()
        print("*************************************************************")
        if len(self.game_object.final_winners) == 1:
            print(f"The winner is: {self.game_object.final_winners[0].player_name}")
        else:
            print(f"The winners are: ", end = "")
            for winner in self.game_object.final_winners:
                if winner == self.game_object.final_winners[-1]:
                    print("& " + winner.player_name)
                elif winner == self.game_object.final_winners[-2]:
                    print(winner.player_name, end=" ")
                else:
                    print(winner.player_name, end=", ")
        print("*************************************************************")
        print()

    # Ask about playing again
    def ask_again(self):
        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again == "Y" or play_again == "YES":
            self.game_object.reset_game()
        else:
            print()
            print("Thanks for playing!")
            self.game_object.is_running = False