from abc import ABC, abstractmethod
from Main_Game.m_renders import render_bot_goes_home, render_bot_stays_inside, render_tell_b_diamonds
from Main_Game.m_probability_and_ev import calc_ev_next_without_dia_on_way


class LevelStrategy(ABC):
    def __init__(self, current_bot, game_object):
        self.current_bot = current_bot
        self.game_object = game_object

    @property
    def amount_available_diamonds(self):
        return self.game_object.diamonds_on_way + self.game_object.relics_on_way + self.current_bot.pocket

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
        if self.game_object.dying_prob > 0.08 and self.bool_diamonds_available():
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_2(LevelStrategy):
    def action(self):
        if self.game_object.dying_prob > 0.17 and self.bool_diamonds_available():
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_3(LevelStrategy):
    def action(self):
        if self.game_object.dying_prob > 0.25 and self.bool_diamonds_available():
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_4(LevelStrategy):
    def action(self):
        if ((self.current_bot.ev_next - self.current_bot.guaranteed_diamonds) < 0
                and self.bool_diamonds_available()):
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_5(LevelStrategy):
    def action(self):
        if (calc_ev_next_without_dia_on_way(game_object=self.game_object, current_player=self.current_bot)
            - self.current_bot.pocket) < 0 and self.bool_diamonds_available():
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_6(LevelStrategy):
    def action(self):
        if self.game_object.undiscovered_diamonds < 85:
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_7(LevelStrategy):
    def action(self):
        if self.game_object.undiscovered_diamonds < 100:
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_8(LevelStrategy):
    def action(self):
        if self.current_bot.guaranteed_diamonds > 5 and self.game_object.dying_prob > 0:
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_9(LevelStrategy):
    def action(self):
        if self.current_bot.guaranteed_diamonds > 8 and self.game_object.dying_prob > 0:
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_10(LevelStrategy):  # best bot
    def action(self):
        if self.current_bot.guaranteed_diamonds > 12 and self.game_object.dying_prob > 0:
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_11(LevelStrategy):
    def action(self):
        if self.current_bot.guaranteed_diamonds > 5 and self.game_object.dying_prob > 0.08:
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_12(LevelStrategy):  # Top 3 bot, probably second best
    def action(self):
        if self.current_bot.guaranteed_diamonds > 8 and self.game_object.dying_prob > 0.08:
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_13(LevelStrategy):  # Top 3 bot
    def action(self):
        if self.current_bot.guaranteed_diamonds > 12 and self.game_object.dying_prob > 0.08:
            render_bot_goes_home(game_object=self.game_object, current_bot=self.current_bot)
            self.current_bot.go_home()
        else:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)


class Level_999(LevelStrategy):
    def action(self):
        if (self.game_object.amount_current_winner - 20) <= self.current_bot.current_diamonds < self.game_object.amount_current_winner:
            render_bot_stays_inside(game_object=self.game_object, current_bot=self.current_bot)
        elif self.current_bot.current_diamonds == self.game_object.amount_current_winner:
            self.current_bot.level = 2
        elif self.current_bot.current_diamonds < (self.game_object.amount_current_winner - 20):
            self.current_bot.level = 3


class Act_On_Card:
    def __init__(self, game_object, current_bot):
        self.game_object = game_object
        self.current_bot = current_bot

    def adjust_risk_last_round(self):
        amount_current_winner = self.game_object.amount_current_winner
        current_diamonds = self.current_bot.current_diamonds
        if self.game_object.rounds == 4 and amount_current_winner == 0:
            pass
        elif self.game_object.rounds == 4 and (amount_current_winner - 20) <= current_diamonds < amount_current_winner:
            self.current_bot.level = 999
        elif self.game_object.rounds == 4 and current_diamonds == amount_current_winner:
            self.current_bot.level = 2
        elif self.game_object.rounds == 4 and current_diamonds < (amount_current_winner - 20):
            self.current_bot.level = 3

    # Bot takes action, depending on Level
    def ask_bot(self):
        render_tell_b_diamonds(game_object = self.game_object, current_bot = self.current_bot)
        if self.game_object.bool_adjust_risk_last_round:
            self.adjust_risk_last_round()
        if self.current_bot.level == 999:
            level_last_round = Level_999(self.current_bot, self.game_object)
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
        elif self.current_bot.level == 5:
            level_5 = Level_5(self.current_bot, self.game_object)
            level_5.action()
        elif self.current_bot.level == 6:
            level_6 = Level_6(self.current_bot, self.game_object)
            level_6.action()
        elif self.current_bot.level == 7:
            level_7 = Level_7(self.current_bot, self.game_object)
            level_7.action()
        elif self.current_bot.level == 8:
            level_8 = Level_8(self.current_bot, self.game_object)
            level_8.action()
        elif self.current_bot.level == 9:
            level_9 = Level_9(self.current_bot, self.game_object)
            level_9.action()
        elif self.current_bot.level == 10:
            level_10 = Level_10(self.current_bot, self.game_object)
            level_10.action()
        elif self.current_bot.level == 11:
            level_11 = Level_11(self.current_bot, self.game_object)
            level_11.action()
        elif self.current_bot.level == 12:
            level_12 = Level_12(self.current_bot, self.game_object)
            level_12.action()
        elif self.current_bot.level == 13:
            level_13 = Level_13(self.current_bot, self.game_object)
            level_13.action()