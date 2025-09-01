from Main_Game._player import Bot

class s_Bot(Bot):
    def __init__(self, bot_name, level, game_object):
        super().__init__(bot_name = bot_name, level = level,  game_object = game_object)
        self.game_winning_count = 0
        self.round_winning_count = 0
        self.diamond_count = 0
        self.collected_diamonds = []
        self.max_diamonds = 0

    def bot_goes_home(self):
        self.go_home()