go_home_now = []
class Player:
    def __init__(self, player_name, inside = True, pocket = 0, chest = 0, is_bot = False):
        self.player_name = player_name
        self.inside = inside
        self.pocket = pocket
        self.chest = chest
        self.is_bot = is_bot

    def go_home(self):
        self.chest += self.pocket
        self.pocket = 0
        go_home_now.append(self)
        self.inside = False

    def die(self):
        self.pocket = 0
        self.inside = False

    def tell_p_pocket(self):
        print(f"You have {self.pocket} diamond(s) in your pocket")

    def ask_player(self, diamonds_on_way):
        self.tell_p_pocket()
        print(f"There is/are {diamonds_on_way} diamond(s) on the way home")
        print("_____________________________________________________________")
        question = input(f"{self.player_name}: Do you want to go home? (Y/N) ").upper()
        while not question.isalpha():
            question = input(f"{self.player_name}: {question} is not valid. Do you want to go home? (Y/N) ").upper()
        print("_____________________________________________________________")
        if question == "Y":
            self.go_home()

    def ask_bot(self, diamonds_on_way, probability):
        pass

class Bot(Player):
    def __init__(self, bot_name, level):
        super().__init__(player_name = bot_name, is_bot = True)
        self.level = level
        self.bot_name = bot_name

    def tell_b_pocket(self):
        print(f"{self.bot_name} has {self.pocket} diamond(s) in his pocket")

    def ask_bot(self, diamonds_on_way, probability):
        self.tell_b_pocket()
        print(f"There is/are {diamonds_on_way} diamond(s) on the way home")
        print("_____________________________________________________________")
        if self.level == 1:
            if probability > 0.1:
                self.go_home()
                print(f"{self.bot_name} goes home and saves his diamond(s)")
                print("_____________________________________________________________")
            else:
                print(f"{self.bot_name} stays inside")
                print("_____________________________________________________________")
        elif self.level == 2:
            if probability > 0.17:
                self.go_home()
                print(f"{self.bot_name} goes home and saves his diamond(s)")
                print("_____________________________________________________________")
            else:
                print(f"{self.bot_name} stays inside")
                print("_____________________________________________________________")
        elif self.level == 3:
            if probability > 0.25:
                self.go_home()
                print(f"{self.bot_name} goes home and saves his diamond(s)")
                print("_____________________________________________________________")
            else:
                print(f"{self.bot_name} stays inside")
                print("_____________________________________________________________")
