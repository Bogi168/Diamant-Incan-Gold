from Main_Game.LevelStrategy import *

class s_Level_1(Level_1):
    def action(self):
        if self.game_object.calc_prob() > 0.08 and self.bool_diamonds_available():
            self.current_bot.bot_goes_home()

#        if (self.game_object.calc_ev_next(self.current_bot) - self.current_bot.pocket) < 0 and self.bool_diamonds_available():
#            self.current_bot.bot_goes_home()

#        elif self.game_object.calc_undiscovered_diamonds() < 50:
#            self.current_bot.bot_goes_home()

#        elif len(self.game_object.players_inside) != 1:
#            if self.amount_available_diamonds / (len(self.game_object.players_inside) - 1) > 12 and self.game_object.calc_prob() > 0:
#                self.current_bot.bot_goes_home()

class s_Level_2(Level_2):
    def action(self):
#        if self.game_object.calc_prob() > 0.17 and self.bool_diamonds_available():
#            self.current_bot.bot_goes_home()

        if (self.game_object.calc_ev_next(self.current_bot) - self.current_bot.pocket) < 0 and self.bool_diamonds_available():
            self.current_bot.bot_goes_home()

#        elif self.game_object.calc_undiscovered_diamonds() < 70:
#            self.current_bot.bot_goes_home()

#        elif len(self.game_object.players_inside) != 1:
#            if self.amount_available_diamonds / (len(self.game_object.players_inside) - 1) > 16 and self.game_object.calc_prob() > 0.09:
#                self.current_bot.bot_goes_home()

class s_Level_3(Level_3):
    def action(self):
        if self.game_object.calc_prob() > 0.25 and self.bool_diamonds_available():
                self.current_bot.bot_goes_home()

#        if (self.game_object.calc_ev_next(self.current_bot) - self.current_bot.pocket) < 0 and self.bool_diamonds_available():
#            self.current_bot.bot_goes_home()

#        elif self.game_object.calc_undiscovered_diamonds() < 30:
#            self.current_bot.bot_goes_home()

#        elif self.amount_available_diamonds / len(self.game_object.players_inside) > 16 and len(self.game_object.players_inside) != 1 and self.game_object.calc_prob() > 0.15:
#            self.current_bot.bot_goes_home()

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
