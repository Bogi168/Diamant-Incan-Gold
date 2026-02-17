from Main_Game.m_probability_and_ev import calc_future_diamonds, calc_guaranteed_diamonds, calc_ev_next, calc_current_diamonds


# Class Player
class Player:
    def __init__(self, player_name, game_object, is_bot = False):
        self.player_name = player_name
        self.game_object = game_object
        self.is_bot = is_bot

        # Player variables
        self.inside = True
        self.pocket = 0
        self.chest = 0
        self.die_counter = 0

    # Properties
    @property
    def future_diamonds(self):
        return calc_future_diamonds(game_object = self.game_object, cards_object = self.game_object.cards, current_player = self)

    @property
    def guaranteed_diamonds(self):
        return calc_guaranteed_diamonds(game_object = self.game_object, current_player = self)

    @property
    def current_diamonds(self):
        return calc_current_diamonds(game_object = self.game_object, current_player = self)

    @property
    def ev_next(self):
        return calc_ev_next(game_object = self.game_object, current_player = self)

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
        self.die_counter += 1

# Class Bot
class Bot(Player):
    def __init__(self, bot_name, level, game_object):
        # Bot variables
        super().__init__(player_name = bot_name, game_object=game_object, is_bot = True)
        self.level = level
        self.bot_name = bot_name
        self.game_winning_count = 0
        self.round_winning_count = 0
        self.prev_round_chest = 0
        self.diamond_count = 0
        self.collected_diamonds = []
        self.max_diamonds = 0