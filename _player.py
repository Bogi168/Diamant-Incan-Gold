# Class Player
class Player:
    def __init__(self, player_name, game_object, is_bot = False):
        # Player variables
        self.player_name = player_name
        self.game_object = game_object
        self.inside = True
        self.pocket = 0
        self.chest = 0
        self.is_bot = is_bot

    # Player goes home
    def go_home(self):
        self.chest += self.pocket
        self.pocket = 0
        self.game_object.go_home_now.append(self)
        self.inside = False

    # Player dies
    def die(self):
        self.pocket = 0
        self.inside = False

    # Present Player's diamonds
    def tell_p_diamonds(self):
        print(f"You have {self.pocket} diamond(s) in your pocket")
        print(f"There is/are {self.game_object.diamonds_on_way} diamond(s) on the way home")
        print(f"The expected value is {self.game_object.calc_ev_next(self):.2f}")
        print("_____________________________________________________________")

    # Ask player what he wants to do
    def ask_player(self):
        self.tell_p_diamonds()
        decision = input(f"{self.player_name}: Do you want to go home? (Y/N) ").upper()
        while not decision.isalpha():
            decision = input(f"{self.player_name}: {decision} is not valid. Do you want to go home? (Y/N) ").upper()
        print("_____________________________________________________________")
        if decision == "Y" or decision == "YES":
            self.go_home()

# Class Bot
class Bot(Player):
    def __init__(self, bot_name, level, game_object):
        # Bot variables
        super().__init__(player_name = bot_name, game_object=game_object, is_bot = True)
        self.level = level
        self.bot_name = bot_name
        self.diamonds = 0


    # Bot goes home
    def bot_goes_home(self):
        self.go_home()
        print(f"{self.bot_name} goes home and saves his diamond(s)")
        print("_____________________________________________________________")

    # Bot stays inside
    def bot_stays_inside(self):
        print(f"{self.bot_name} stays inside")
        print("_____________________________________________________________")
