# Class Player
class Player:
    def __init__(self, player_name, inside = True, pocket = 0, chest = 0, is_bot = False):
        # Player variables
        self.player_name = player_name
        self.inside = inside
        self.pocket = pocket
        self.chest = chest
        self.is_bot = is_bot

    # Player goes home
    def go_home(self, e_go_home_now):
        self.chest += self.pocket
        self.pocket = 0
        e_go_home_now.append(self)
        self.inside = False
        return e_go_home_now

    # Player dies
    def die(self):
        self.pocket = 0
        self.inside = False

    # Present Player's diamonds
    def tell_p_diamonds(self, diamonds_on_way):
        print(f"You have {self.pocket} diamond(s) in your pocket")
        print(f"There is/are {diamonds_on_way} diamond(s) on the way home")
        print("_____________________________________________________________")

    # Ask player what he wants to do
    def ask_player(self, diamonds_on_way, e_go_home_now):
        self.tell_p_diamonds(diamonds_on_way)
        question = input(f"{self.player_name}: Do you want to go home? (Y/N) ").upper()
        while not question.isalpha():
            question = input(f"{self.player_name}: {question} is not valid. Do you want to go home? (Y/N) ").upper()
        print("_____________________________________________________________")
        if question == "Y":
            self.go_home(e_go_home_now)

    # empty method for Bot
    def ask_bot(self, diamonds_on_way, relics_on_way, probability, e_go_home_now):
        pass

# Class Bot
class Bot(Player):
    def __init__(self, bot_name, level):
        # Bot variables
        super().__init__(player_name = bot_name, is_bot = True)
        self.level = level
        self.bot_name = bot_name

    # Present Bot's diamonds
    def tell_b_diamonds(self, diamonds_on_way):
        print(f"{self.bot_name} has {self.pocket} diamond(s) in his pocket")
        print(f"There is/are {diamonds_on_way} diamond(s) on the way home")
        print("_____________________________________________________________")

    # Bot goes home
    def bot_goes_home(self, e_go_home_now):
        self.go_home(e_go_home_now)
        print(f"{self.bot_name} goes home and saves his diamond(s)")
        print("_____________________________________________________________")

    # Bot stays inside
    def bot_stays_inside(self):
        print(f"{self.bot_name} stays inside")
        print("_____________________________________________________________")

    # Bot level 1
    def bot_lvl1(self, diamonds_on_way, relics_on_way, probability, e_go_home_now):
        if self.level == 1:
            if probability > 0.1 and (diamonds_on_way + relics_on_way + self.pocket) != 0:
                self.bot_goes_home(e_go_home_now)
            else:
                self.bot_stays_inside()

    # Bot level 2
    def bot_lvl2(self, diamonds_on_way, relics_on_way, probability, e_go_home_now):
        if self.level == 2:
            if probability > 0.17 and (diamonds_on_way + relics_on_way + self.pocket) != 0:
                self.bot_goes_home(e_go_home_now)
            else:
                self.bot_stays_inside()

    # Bot level 3
    def bot_lvl3(self, diamonds_on_way, relics_on_way, probability, e_go_home_now):
        if self.level == 3:
            if probability > 0.25 and (diamonds_on_way + relics_on_way + self.pocket) != 0:
                self.bot_goes_home(e_go_home_now)
            else:
                self.bot_stays_inside()

    # Ask bot what he wants to do
    def ask_bot(self, diamonds_on_way, relics_on_way, probability, e_go_home_now):
        self.tell_b_diamonds(diamonds_on_way)
        self.bot_lvl1(diamonds_on_way, relics_on_way, probability, e_go_home_now)
        self.bot_lvl2(diamonds_on_way, relics_on_way, probability, e_go_home_now)
        self.bot_lvl3(diamonds_on_way, relics_on_way, probability, e_go_home_now)
