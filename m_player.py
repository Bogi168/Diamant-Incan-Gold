# Class Player
class Player:
    def __init__(self, player_name, game_object, is_bot = False):
        # Player variables
        self.player_name = player_name
        self.game_object = game_object
        self.inside = True
        self.pocket = 0
        self.chest = 0
        self.guaranteed_diamonds = 0
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

# Class Bot
class Bot(Player):
    def __init__(self, bot_name, level, game_object):
        # Bot variables
        super().__init__(player_name = bot_name, game_object=game_object, is_bot = True)
        self.level = level
        self.bot_name = bot_name
        self.diamonds = 0
