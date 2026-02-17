from Main_Game.m_Level_Strategy import *
from Main_Game.m_probability_and_ev import calc_ev_next_without_dia_on_way

class s_Level_1(LevelStrategy):
    def action(self):
        if self.game_object.dying_prob > 0.08 and self.bool_diamonds_available():
            self.current_bot.go_home()

class s_Level_2(LevelStrategy):
    def action(self):
        if self.game_object.dying_prob > 0.17 and self.bool_diamonds_available():
            self.current_bot.go_home()

class s_Level_3(LevelStrategy):
    def action(self):
        if self.game_object.dying_prob > 0.25 and self.bool_diamonds_available():
                self.current_bot.go_home()

class s_Level_4(LevelStrategy):
    def action(self):
        if ((self.current_bot.ev_next - self.current_bot.guaranteed_diamonds) < 0
                and self.bool_diamonds_available()):
            self.current_bot.go_home()

class s_Level_5(LevelStrategy):
    def action(self):
        if (calc_ev_next_without_dia_on_way(game_object = self.game_object, current_player = self.current_bot)
            - self.current_bot.pocket) < 0 and self.bool_diamonds_available():
            self.current_bot.go_home()

class s_Level_6(LevelStrategy):
    def action(self):
        if self.game_object.undiscovered_diamonds < 85:
            self.current_bot.go_home()

class s_Level_7(LevelStrategy):
    def action(self):
        if self.game_object.undiscovered_diamonds < 100:
            self.current_bot.go_home()

class s_Level_8(LevelStrategy):
    def action(self):
        if self.current_bot.guaranteed_diamonds > 5 and self.game_object.dying_prob > 0:
            self.current_bot.go_home()

class s_Level_9(LevelStrategy):
    def action(self):
        if self.current_bot.guaranteed_diamonds > 8 and self.game_object.dying_prob > 0:
            self.current_bot.go_home()

class s_Level_10(LevelStrategy): # bester Bot
    def action(self):
        if self.current_bot.guaranteed_diamonds > 12 and self.game_object.dying_prob > 0:
            self.current_bot.go_home()

class s_Level_11(LevelStrategy):
    def action(self):
        if self.current_bot.guaranteed_diamonds > 5 and self.game_object.dying_prob > 0.08:
            self.current_bot.go_home()

class s_Level_12(LevelStrategy): # Top 3 Bot, wahrscheinlich zweitbester
    def action(self):
        if self.current_bot.guaranteed_diamonds > 8 and self.game_object.dying_prob > 0.08:
            self.current_bot.go_home()

class s_Level_13(LevelStrategy): # Top 3 Bot
    def action(self):
        if self.current_bot.guaranteed_diamonds > 12 and self.game_object.dying_prob > 0.08:
            self.current_bot.go_home()

class s_Act_On_Card(Act_On_Card):
    def __init__(self, current_bot, game_object):
        super().__init__(current_bot, game_object)
    def ask_bot(self):
        if self.current_bot.level == 1:
            level_1 = s_Level_1(self.current_bot, self.game_object)
            level_1.action()
        elif self.current_bot.level == 2:
            level_2 = s_Level_2(self.current_bot, self.game_object)
            level_2.action()
        elif self.current_bot.level == 3:
            level_3 = s_Level_3(self.current_bot, self.game_object)
            level_3.action()
        elif self.current_bot.level == 4:
            level_4 = s_Level_4(self.current_bot, self.game_object)
            level_4.action()
        elif self.current_bot.level == 5:
            level_5 = s_Level_5(self.current_bot, self.game_object)
            level_5.action()
        elif self.current_bot.level == 6:
            level_6 = s_Level_6(self.current_bot, self.game_object)
            level_6.action()
        elif self.current_bot.level == 7:
            level_7 = s_Level_7(self.current_bot, self.game_object)
            level_7.action()
        elif self.current_bot.level == 8:
            level_8 = s_Level_8(self.current_bot, self.game_object)
            level_8.action()
        elif self.current_bot.level == 9:
            level_9 = s_Level_9(self.current_bot, self.game_object)
            level_9.action()
        elif self.current_bot.level == 10:
            level_10 = s_Level_10(self.current_bot, self.game_object)
            level_10.action()
        elif self.current_bot.level == 11:
            level_11 = s_Level_11(self.current_bot, self.game_object)
            level_11.action()
        elif self.current_bot.level == 12:
            level_12 = s_Level_12(self.current_bot, self.game_object)
            level_12.action()
        elif self.current_bot.level == 13:
            level_13 = s_Level_13(self.current_bot, self.game_object)
            level_13.action()
