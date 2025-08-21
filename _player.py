go_home_now = []
class Player:
    def __init__(self, player_name, inside = True, pocket = 0, chest = 0):
        self.player_name = player_name
        self.inside = inside
        self.pocket = pocket
        self.chest = chest

    def go_home(self):
        self.chest += self.pocket
        self.pocket = 0
        go_home_now.append(self)
        self.inside = False

    def die(self):
        self.pocket = 0
        self.inside = False

    def tell_pocket(self):
        print(f"You have {self.pocket} diamond(s) in your pocket")

    def ask_question(self, diamonds_on_way):
        self.tell_pocket()
        print(f"There is/are {diamonds_on_way} diamond(s) on the way home")
        print("_____________________________________________________________")
        question = input(f"{self.player_name}: Do you want to go home? (Y/N) ").upper()
        while not question.isalpha():
            question = input(f"{self.player_name}: {question} is not valid. Do you want to go home? (Y/N) ").upper()
        print("_____________________________________________________________")
        if question == "Y":
            self.go_home()
