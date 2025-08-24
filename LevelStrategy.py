from abc import ABC, abstractmethod

class LevelStrategy(ABC):
    def __init__(self, current_bot, diamonds_on_way, relics_on_way, probability, e_go_home_now, highest_diamonds):
        self.current_bot = current_bot
        self.diamonds_on_way = diamonds_on_way
        self.relics_on_way = relics_on_way
        self.probability = probability
        self.e_go_home_now = e_go_home_now
        self.highest_diamonds = highest_diamonds

    @abstractmethod
    def action(self):
        pass


class Level_1(LevelStrategy):
    def action(self):
        if self.probability > 0.1 and (self.diamonds_on_way + self.relics_on_way + self.current_bot.pocket) != 0:
            self.current_bot.bot_goes_home(self.e_go_home_now)
        else:
            self.current_bot.bot_stays_inside()

class Level_2(LevelStrategy):
    def action(self):
        if self.probability > 0.17 and (self.diamonds_on_way + self.relics_on_way + self.current_bot.pocket) != 0:
            self.current_bot.bot_goes_home(self.e_go_home_now)
        else:
            self.current_bot.bot_stays_inside()

class Level_3(LevelStrategy):
    def action(self):
        if self.probability > 0.25 and (self.diamonds_on_way + self.relics_on_way + self.current_bot.pocket) != 0:
                self.current_bot.bot_goes_home(self.e_go_home_now)
        else:
                self.current_bot.bot_stays_inside()

class Level_Last_Round(LevelStrategy):
    def action(self):
        if (self.highest_diamonds - 20) <= self.current_bot.diamonds < self.highest_diamonds:
            self.current_bot.bot_stays_inside()
        elif self.current_bot.diamonds == self.highest_diamonds:
            self.current_bot.level = 2
        elif self.current_bot.diamonds < (self.highest_diamonds - 20):
            self.current_bot.level = 3