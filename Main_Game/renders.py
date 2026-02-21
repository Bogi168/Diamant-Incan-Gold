from Main_Game.Player import Player, Bot
from Main_Game.text import *
from Simulation.stat_saver import *

def render_welcome_txt(game_object):
    game_object.renderer.render_game(message = welcome_txt())

# Create players
def render_create_players(game_object):
    players_amount = game_object.renderer.ask_players_amount()
    while players_amount != None and not (players_amount.isdigit() or int(players_amount) <= 0):
        players_amount = game_object.renderer.re_ask_players_amount()
    if players_amount == None:
        players_amount = 0
    players_amount = int(players_amount)
    game_object.players_amount = players_amount
    game_object.renderer.render_game(message = dashes_1())
    for player_num in range(players_amount):
        player_name = game_object.renderer.ask_player_name(player_num = player_num)
        game_object.list_players.append(Player(player_name = player_name, game_object = game_object))
        game_object.renderer.render_game(message=dashes_2())

# Create bots
def render_select_bots_amount(game_object):
    bots_amount = game_object.renderer.ask_bots_amount()
    if game_object.players_amount == 0:
        while not bots_amount.isdigit() or int(bots_amount) <= 0:
            bots_amount = game_object.renderer.re_ask_bots_amount()
    else:
        while not bots_amount.isdigit() or int(bots_amount) < 0:
            bots_amount = game_object.renderer.re_ask_bots_amount()
    bots_amount = int(bots_amount)
    game_object.bots_amount = bots_amount

def render_select_bot_level(game_object):
    if game_object.bots_amount != 0:
        for bot_num in range(game_object.bots_amount):
            game_object.renderer.render_game(message=dashes_3())
            level_bot = game_object.renderer.ask_bot_level(bot_num = bot_num)
            while not level_bot in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"):
                level_bot = game_object.renderer.re_ask_bot_level(bot_num = bot_num)
            level_bot = int(level_bot)
            game_object.list_level_bots.append(level_bot)
            game_object.list_bots.append(Bot(bot_name =f"Bot {bot_num + 1}", level = level_bot, game_object = game_object))
            game_object.renderer.render_game(message=dashes_4())

def render_create_bots(game_object):
    render_select_bots_amount(game_object = game_object)
    render_select_bot_level(game_object = game_object)


# Current round
def render_tell_round(game_object):
    game_object.renderer.render_game(message=tell_round(rounds = game_object.rounds))

# Tell the played cards
def render_tell_played_cards(game_object, cards_object):
    game_object.renderer.render_game(message=played_cards_text(cards_object = cards_object))

def render_tell_new_card(game_object, cards_object):
    game_object.renderer.render_game(message=tell_new_card(cards_object.new_card))

# Output depending on drawn card
def render_second_trap(game_object, cards_object):
    game_object.renderer.render_game(message=second_trap(cards_object.new_card))
    if game_object.rounds == 5 - 1:
        game_object.renderer.render_game(message=dashes_5())


# Tell situation
def render_tell_probability(game_object):
    game_object.renderer.render_game(message=tell_probability(game_object = game_object))

def render_tell_relics_on_way(game_object):
    if game_object.relics_on_way != 0:
        game_object.renderer.render_game(message=tell_relics_on_way(game_object = game_object))

def render_ask_player(game_object, current_player):
    game_object.renderer.render_game(message=tell_p_diamonds(game_object = game_object, current_player = current_player))
    decision = game_object.renderer.ask_continue_or_leave(player_name = current_player.player_name)
    while not decision.isalpha():
        decision = game_object.renderer.re_ask_continue_or_leave(player_name = current_player.player_name)
    game_object.renderer.render_game(message=dashes_6())
    if decision in ("Y", "YES"):
        return "leave"
    else:
        return "stay"

# Bot goes home
def render_bot_goes_home(game_object, current_bot):
    game_object.renderer.render_game(message=bot_goes_home(current_bot = current_bot))

# Bot stays inside
def render_bot_stays_inside(game_object, current_bot):
    game_object.renderer.render_game(message=bot_stays_inside(current_bot = current_bot))

# Present Bot's diamonds
def render_tell_b_diamonds(game_object, current_bot):
    game_object.renderer.render_game(message=tell_b_diamonds(game_object = game_object, current_bot = current_bot))

# Present the result
def render_tell_result(game_object):
    game_object.renderer.render_game(message=dashes_5())
    for explorer in game_object.list_explorers:
        game_object.renderer.render_game(message=tell_collected_diamonds(player_name = explorer.player_name, chest = explorer.chest))
    game_object.renderer.render_game(message=stars_1())
    game_object.renderer.render_game(message=tell_winners(game_object = game_object))
    game_object.renderer.render_game(message=stars_2())

# Ask about playing again
def render_ask_again(game_object):
    play_again = game_object.renderer.ask_again()
    return play_again

def render_new_line(game_object):
    game_object.renderer.render_game(message=new_line())

def render_end_of_game(game_object):
    game_object.renderer.render_game(message=end_of_game())

# Simulation
def render_select_games_amount(game_object):
    games_amount = game_object.renderer.ask_games_amount()
    while not games_amount.isdigit() or int(games_amount) <= 0:
        games_amount = game_object.renderer.re_ask_games_amount()
    game_object.games_amount = int(games_amount)

def render_tell_stats(game_object):
    game_object.get_max_diamonds()
    for explorer in game_object.list_explorers:
        game_object.renderer.render_system(message = tell_stats(game_object = game_object, explorer = explorer))

def render_ask_for_save(game_object, file_path):
    save_answer = game_object.renderer.ask_for_save()
    if save_answer in ("Y", "YES"):
        save_statistics(game_object = game_object, file_path = file_path)
        game_object.renderer.render_system(message = save_stats(file_path = file_path))
    else:
        game_object.renderer.render_system(message = delete_stats())