from Main_Game.m_player import Player, Bot
from Main_Game.m_text import *

def render_welcome_txt(game_object):
    game_object.renderer.render_system(self = game_object, message = welcome_txt())

# Create players
def render_create_players(game_object):
    players_amount = game_object.renderer.ask_players_amount(self = game_object.renderer)
    while not players_amount.isdigit() or int(players_amount) <= 0:
        players_amount = game_object.renderer.re_ask_players_amount(self = game_object.renderer)
    players_amount = int(players_amount)
    game_object.renderer.render_game(self = game_object.renderer, message = dashes_1())
    for player_num in range(players_amount):
        player_name = game_object.renderer.ask_player_name(self = game_object.renderer, player_num = player_num)
        game_object.players.append(Player(player_name = player_name, game_object = game_object))
        game_object.renderer.render_game(self = game_object.renderer, message=dashes_2())

# Create bots
def render_create_bots(game_object):
    bots_amount = game_object.renderer.ask_bots_amount(self = game_object.renderer)
    while not bots_amount.isdigit() or int(bots_amount) < 0:
        bots_amount = game_object.renderer.re_ask_bots_amount(self = game_object.renderer)
    bots_amount = int(bots_amount)
    if bots_amount != 0:
        for bot_num in range(bots_amount):
            game_object.renderer.render_game(self = game_object.renderer, message=dashes_3())
            level_bot = game_object.renderer.ask_bot_level(self = game_object.renderer, bot_num = bot_num)
            while not level_bot in ("1", "2", "3", "4"):
                level_bot = game_object.renderer.re_ask_bot_level(self = game_object.renderer, bot_num = bot_num)
            level_bot = int(level_bot)
            game_object.bots.append(Bot(bot_name = f"Bot {bot_num + 1}", level = level_bot, game_object = game_object))
            game_object.renderer.render_game(self = game_object.renderer, message=dashes_4())

# Current round
def render_tell_round(game_object):
    game_object.renderer.render_game(self = game_object.renderer, message=tell_round(rounds = game_object.rounds))

# Tell the played cards
def render_tell_played_cards(game_object, cards_object):
    game_object.renderer.render_game(self = game_object.renderer, message=played_cards_text(cards_object = cards_object))

def render_tell_new_card(game_object, cards_object):
    game_object.renderer.render_game(self = game_object.renderer, message=tell_new_card(cards_object.new_card))

# Output depending on drawn card
def render_second_trap(game_object, cards_object):
    game_object.renderer.render_game(self = game_object.renderer, message=second_trap(cards_object.new_card))
    if game_object.rounds == 5 - 1:
        game_object.renderer.render_game(self = game_object.renderer, message=dashes_5())


# Tell situation
def render_tell_probability(game_object):
    game_object.renderer.render_game(self = game_object.renderer, message=tell_probability(game_object = game_object))

def render_tell_relics_on_way(game_object):
    if game_object.relics_on_way != 0:
        game_object.renderer.render_game(self = game_object.renderer, message=tell_relics_on_way(game_object = game_object))

def render_ask_player(game_object, current_player):
    game_object.renderer.render_game(self = game_object.renderer, message=tell_p_diamonds(game_object = game_object, current_player = current_player))
    decision = game_object.renderer.ask_continue_or_leave(self = game_object.renderer, player_name = current_player.player_name)
    while not decision.isalpha():
        decision = game_object.renderer.re_ask_continue_or_leave(self = game_object.renderer, player_name = current_player.player_name)
    game_object.renderer.render_game(self = game_object.renderer, message=dashes_6())
    if decision in ("Y", "YES"):
        return "leave"
    else:
        return "stay"

# Bot goes home
def render_bot_goes_home(game_object, current_bot):
    game_object.renderer.render_game(self = game_object.renderer, message=bot_goes_home(current_bot = current_bot))

# Bot stays inside
def render_bot_stays_inside(game_object, current_bot):
    game_object.renderer.render_game(self = game_object.renderer, message=bot_stays_inside(current_bot = current_bot))

# Present Bot's diamonds
def render_tell_b_diamonds(game_object, current_bot):
    game_object.renderer.render_game(self = game_object.renderer, message=tell_b_diamonds(game_object = game_object, current_bot = current_bot))

# Present the result
def render_tell_result(game_object):
    game_object.renderer.render_system(self = game_object.renderer, message=dashes_5())
    game_object.identify_game_winner()
    for explorer in game_object.explorers:
        game_object.renderer.render_system(self = game_object.renderer, message=tell_collected_diamonds(player_name = explorer.player_name, chest = explorer.chest))
    game_object.renderer.render_system(self = game_object.renderer, message=stars_1())
    game_object.renderer.render_system(self = game_object.renderer, message=tell_winners(game_object = game_object))
    game_object.renderer.render_system(self = game_object.renderer, message=stars_2())

# Ask about playing again
def render_ask_again(game_object):
    play_again = game_object.renderer.ask_again(self = game_object.renderer)
    if play_again == "Y" or play_again == "YES":
        game_object.renderer.render_system(self=game_object.renderer, message=new_line())
        game_object.reset_game()
    else:
        game_object.renderer.render_system(self = game_object.renderer, message=end_of_game())
        game_object.is_running = False
