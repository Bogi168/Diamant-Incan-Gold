# Levels
from LevelStrategy import Level_1, Level_2, Level_3, Level_Last_Round

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
    def ask_bot(self, diamonds_on_way, players_inside, cur_round, highest_diamonds, relics_on_way, probability, e_go_home_now):
        pass

# Class Bot
class Bot(Player):
    def __init__(self, bot_name, level):
        # Bot variables
        super().__init__(player_name = bot_name, is_bot = True)
        self.level = level
        self.bot_name = bot_name
        self.diamonds = 0

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

    def last_round_risk(self, diamonds_on_way, players_inside, cur_round, highest_diamonds):
        self.diamonds = self.chest + self.pocket + (diamonds_on_way // len(players_inside))
        if cur_round == 4 and highest_diamonds == 0:
            pass
        elif cur_round == 4 and (highest_diamonds - 20) <= self.diamonds < highest_diamonds:
            self.level = 10
        elif cur_round == 4 and self.diamonds == highest_diamonds:
            self.level = 2
        elif cur_round == 4 and self.diamonds < (highest_diamonds - 20):
            self.level = 3

    # Bot takes action, depending on Level
    def act_based_on_level(self, diamonds_on_way, relics_on_way, probability, e_go_home_now, highest_diamonds):
        if self.level == 10:
            level_last_round = Level_Last_Round(self, diamonds_on_way, relics_on_way, probability, e_go_home_now, highest_diamonds)
            level_last_round.action()
        if self.level == 1:
            level_1 = Level_1(self, diamonds_on_way, relics_on_way, probability, e_go_home_now, highest_diamonds)
            level_1.action()
        elif self.level == 2:
            level_2 = Level_2(self, diamonds_on_way, relics_on_way, probability, e_go_home_now, highest_diamonds)
            level_2.action()
        elif self.level == 3:
            level_3 = Level_3(self, diamonds_on_way, relics_on_way, probability, e_go_home_now, highest_diamonds)
            level_3.action()

    # Ask bot what he wants to do
    def ask_bot(self, diamonds_on_way, players_inside, cur_round, highest_diamonds, relics_on_way, probability, e_go_home_now):
        self.tell_b_diamonds(diamonds_on_way)
        self.last_round_risk(diamonds_on_way, players_inside, cur_round, highest_diamonds)
        self.act_based_on_level(diamonds_on_way, relics_on_way, probability, e_go_home_now, highest_diamonds)
