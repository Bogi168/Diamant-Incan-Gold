from Main_Game.player import Bot
from Simulation.s_stat_saver import *
from Main_Game.text import *

def render_select_bots_amount(game_object):
    bots_amount = game_object.renderer.ask_bots_amount(self = game_object.renderer)
    while not bots_amount.isdigit() or int(bots_amount) <= 0:
        bots_amount = game_object.renderer.re_ask_bots_amount(self = game_object.renderer)
    game_object.bots_amount = int(bots_amount)

def render_select_bots_level(game_object):
    for bot_num in range(game_object.bots_amount):
        level_bot = game_object.renderer.ask_bot_level(self = game_object.renderer, bot_num = bot_num)
        while not level_bot in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"):
            level_bot = game_object.renderer.ask_bot_level(self = game_object.renderer, bot_num = bot_num)
        level_bot = int(level_bot)
        game_object.bots.append(Bot(bot_name=f"Bot {bot_num + 1}", level=level_bot, game_object = game_object))
        game_object.explorers = game_object.bots.copy()

def render_create_bots(game_object):
    render_select_bots_amount(game_object = game_object)
    render_select_bots_level(game_object= game_object)

def render_select_games_amount(game_object):
    games_amount = game_object.renderer.ask_games_amount(self = game_object.renderer)
    while not games_amount.isdigit() or int(games_amount) <= 0:
        games_amount = game_object.renderer.re_ask_games_amount(self = game_object.renderer)
    game_object.games_amount = int(games_amount)

def render_tell_stats(game_object):
    game_object.get_max_diamonds()
    for explorer in game_object.explorers:
        game_object.renderer.render_system(self = game_object.renderer, message = tell_stats(game_object = game_object, explorer = explorer))

def render_ask_for_save(game_object):
    file_path = "s_stats.txt"
    save_answer = game_object.renderer.ask_for_save(self= game_object.renderer)
    if save_answer in ("Y", "YES"):
        save_statistics(game_object = game_object, file_path = file_path)
        game_object.renderer.render_system(self = game_object.renderer, message = save_stats(file_path = file_path))
    else:
        game_object.renderer.render_system(self = game_object.renderer, message = delete_stats())