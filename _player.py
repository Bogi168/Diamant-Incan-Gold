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

    def ask_question(self):
        self.tell_pocket()
        question = input(f"{self.player_name}: Do you want to go home? (Y/N) ").upper()
        while not question.isalpha():
            question = input(f"{self.player_name}: {question} is not valid. Do you want to go home? (Y/N) ").upper()
        if question == "Y":
            self.go_home()

#Test

players = []
players_amount = input("How many players? ")
while not players_amount.isdigit() or int(players_amount) <= 0:
    players_amount = input("That's not a valid number. How many players? ")
players_amount= int(players_amount)

for player_num in range(players_amount):
    player_name = input(f"Enter player number {player_num+1}'s name: ").capitalize()
    players.append(player_name)
players = [Player(players[i]) for i in range(len(players))]

#print(players[0].player_name)
#print(players[1].player_name)
#print(players[0].pocket)
#print(players[1].chest)
#print(type(players[0]))


#Eingabe Namen der Spieler

#players = []

#players_amount = input("How many players? ")
#while not players_amount.isdigit():
#    players_amount = input("That's not a number. How many players? ")
#players_amount= int(players_amount)

#for player_num in range(players_amount):
#    player_name = input(f"Enter player number {player_num+1}'s name: ")
#    players.append(player_name)
#    print(f"Hi {player_name}!")
#print(players)


