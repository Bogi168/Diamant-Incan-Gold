import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

import random

#Karten
snakes = ["🐍", "🐍", "🐍"]
spiders = ["🕷", "🕷", "🕷"]
fires = ["🔥", "🔥", "🔥"]
avalanches = ["🌑", "🌑", "🌑"]
mummys = ["👤", "👤", "👤"]
treasure_cards = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]
relics = [5.01, 7.01, 8.01, 10.01, 12.01]
traps = []

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

cards = []

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

#Player
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


#Wilkommensfenster
class WelcWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Incan Gold")
        self.setGeometry(600,150,800,800)
        self.setWindowIcon(QIcon("Icon.png"))
        dia_image = QLabel(self)
        dia_image.setGeometry(0,0,self.width(),self.height())
        pixmap = QPixmap("Icon.png")
        dia_image.setPixmap(pixmap)
        dia_image.setScaledContents(True)
        welc_txt = QLabel("Welcome to Incan Gold", self)
        welc_txt.setGeometry(0, 30, 800, 60)
        welc_txt.setGeometry((self.width() - welc_txt.width()) // 2,
                            welc_txt.y(),
                            self.width(),
                            welc_txt.height())
        welc_txt.setFont(QFont("Arial", 30))
        welc_txt.setStyleSheet("color: purple;"
                            "background-color: white;"
                            "font-weight: bold;")
        welc_txt.setAlignment(Qt.AlignCenter)

        bogi_edition = QLabel("Bogi Edition", self)
        bogi_edition.setGeometry(0, 0, 800, 50)
        bogi_edition.setGeometry((self.width() - bogi_edition.width()) // 2,
                             welc_txt.height() + welc_txt.y(),
                             self.width(),
                             bogi_edition.height())
        bogi_edition.setFont(QFont("Arial", 20))
        bogi_edition.setStyleSheet("color: purple;"
                               "background-color: white;"
                               "font-weight: bold;")
        bogi_edition.setAlignment(Qt.AlignCenter)

        self.button = QPushButton("Click here to start", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,200,300,100)
        self.button.setGeometry((self.width()-self.button.width())//2,
                                self.height()-self.button.height(),
                                self.button.width(),
                                self.button.height())
        self.button.setFont(QFont("Arial", 20))
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.main_win = MainWindow()
        self.main_win.show()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Incan Gold")
        self.setGeometry(0,0,1910,990)
        self.setWindowIcon(QIcon("Icon.png"))
        self.but_go_home = QPushButton("Go Home", self)
        self.but_stay_in = QPushButton("Stay Inside", self)
        self.initUI()

    def initUI(self):
        self.but_go_home.setGeometry(150, 200, 300, 100)
        self.but_go_home.setFont(QFont("Arial", 20))
        self.but_go_home.clicked.connect(self.go_home())

        self.but_stay_in.setGeometry(150, 200, 300, 100)
        self.but_stay_in.setFont(QFont("Arial", 20))
        self.but_stay_in.clicked.connect(self.stay_in())

    def go_home(self):
        pass

    def stay_in(self):
        pass

#main
def main():
    app = QApplication(sys.argv)
    welc_window = WelcWindow()
    welc_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()