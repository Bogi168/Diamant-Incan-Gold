from abc import ABC, abstractmethod

class LevelStrategy(ABC):
    def __init__(self, current_bot, game_object):
        self.current_bot = current_bot
        self.game_object = game_object
        self.amount_available_diamonds = self.game_object.diamonds_on_way + self.game_object.relics_on_way + self.current_bot.pocket

    @abstractmethod
    def action(self):
        pass

    def bool_diamonds_available(self):
        if self.amount_available_diamonds != 0:
            return True
        else:
            return False


class Level_1(LevelStrategy):
    def action(self):
#        if self.game_object.probability > 0.1 and self.bool_diamonds_available():
#            self.current_bot.bot_goes_home()
#        else:
#            self.current_bot.bot_stays_inside()
        if (self.game_object.calc_ev_next(self.current_bot) - self.current_bot.pocket) < 0 and self.bool_diamonds_available():
            self.current_bot.bot_goes_home()
        else:
            self.current_bot.bot_stays_inside()

class Level_2(LevelStrategy):
    def action(self):
        if self.game_object.probability > 0.17 and self.bool_diamonds_available():
            self.current_bot.bot_goes_home()
        else:
            self.current_bot.bot_stays_inside()

class Level_3(LevelStrategy):
    def action(self):
        if self.game_object.probability > 0.25 and self.bool_diamonds_available():
                self.current_bot.bot_goes_home()
        else:
                self.current_bot.bot_stays_inside()

class Level_4(LevelStrategy):
    def action(self):
        if self.game_object.probability > 0.20 and self.bool_diamonds_available():
                self.current_bot.bot_goes_home()

        elif self.amount_available_diamonds / len(self.game_object.players_inside) > 10 :
            self.current_bot.bot_goes_home()

        else:
                self.current_bot.bot_stays_inside()

class Level_Last_Round(LevelStrategy):
    def action(self):
        if (self.game_object.amount_current_winner - 20) <= self.current_bot.diamonds < self.game_object.amount_current_winner:
            self.current_bot.bot_stays_inside()
        elif self.current_bot.diamonds == self.game_object.amount_current_winner:
            self.current_bot.level = 2
        elif self.current_bot.diamonds < (self.game_object.amount_current_winner - 20):
            self.current_bot.level = 3

class Act_On_Card:
    def __init__(self, game_object, current_bot):
        self.game_object = game_object
        self.current_bot = current_bot


    # Present Bot's diamonds
    def tell_b_diamonds(self):
        print(f"{self.current_bot.bot_name} has {self.current_bot.pocket} diamond(s) in his pocket")
        print(f"There is/are {self.game_object.diamonds_on_way} diamond(s) on the way home")
        print("_____________________________________________________________")

    def last_round_risk(self):
        self.current_bot.diamonds = self.current_bot.chest + self.current_bot.pocket + (self.game_object.diamonds_on_way // len(self.game_object.players_inside))
        if self.game_object.rounds == 4 and self.game_object.amount_current_winner == 0:
            pass
        elif self.game_object.rounds == 4 and (self.game_object.amount_current_winner - 20) <= self.current_bot.diamonds < self.game_object.amount_current_winner:
            self.current_bot.level = 10
        elif self.game_object.rounds == 4 and self.current_bot.diamonds == self.game_object.amount_current_winner:
            self.current_bot.level = 2
        elif self.game_object.rounds == 4 and self.current_bot.diamonds < (self.game_object.amount_current_winner - 20):
            self.current_bot.level = 3

    # Bot takes action, depending on Level
    def ask_bot(self):
        self.tell_b_diamonds()
        self.last_round_risk()
        if self.current_bot.level == 10:
            level_last_round = Level_Last_Round(self.current_bot, self.game_object)
            level_last_round.action()
        if self.current_bot.level == 1:
            level_1 = Level_1(self.current_bot, self.game_object)
            level_1.action()
        elif self.current_bot.level == 2:
            level_2 = Level_2(self.current_bot, self.game_object)
            level_2.action()
        elif self.current_bot.level == 3:
            level_3 = Level_3(self.current_bot, self.game_object)
            level_3.action()
        elif self.current_bot.level == 4:
            level_4 = Level_4(self.current_bot, self.game_object)
            level_4.action()
