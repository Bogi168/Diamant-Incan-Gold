from s_player import s_Bot
from s_stat_saver import *

def console_select_bots_amount(game_object):
    bots_amount = input("\nHow many bots? ")
    while not bots_amount.isdigit() or int(bots_amount) <= 0:
        bots_amount = input("That's not a valid number. How many bots? ")
    game_object.bots_amount = int(bots_amount)

def console_select_bots_level(game_object):
    for bots_num in range(game_object.bots_amount):
        level_bot = input(f"Select a level for Bot {bots_num + 1} (1-13): ")
        while not level_bot in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"):
            level_bot = input(
                f"{level_bot} is not valid. Select a level for Bot {bots_num + 1} (1-13): ")
        level_bot = int(level_bot)
        game_object.explorers.append(s_Bot(bot_name=f"Bot {bots_num + 1}", level=level_bot, game_object = game_object))

def console_select_games_amount(game_object):
    games_amount = input("How many games? ")
    while not games_amount.isdigit() or int(games_amount) <= 0:
        games_amount = input("That's not a valid number. How many games?: ")
    game_object.games_amount = int(games_amount)

def console_tell_stats(game_object):
    game_object.get_max_diamonds()
    for explorer in game_object.explorers:
        print("\n" + "*" * 62 + "\n" +
              f"{explorer.bot_name} (Level: {explorer.level}) won {explorer.round_winning_count} rounds \n" +
              f"{explorer.bot_name} won {explorer.game_winning_count} games \n" +
              f"That's a win rate of {explorer.game_winning_count / game_object.games_amount * 100:.1f}% \n" +
              f"{explorer.bot_name} collected {explorer.diamond_count} diamonds \n" +
              f"That's {((explorer.diamond_count / 5) / game_object.games_amount):.1f} diamonds per round \n" +
              f"{explorer.bot_name} collected {explorer.max_diamonds} diamonds in his best round \n" +
              f"But he died in {explorer.die_counter} rounds \n" +
              f"That's {(explorer.die_counter / (game_object.games_amount * 5)) * 100:.2f}% of the rounds \n" +
              "*" * 62 + "\n")

def console_ask_for_save(game_object):
    file_path = "s_stats.txt"
    save_answer = input("Do you want to save the game statistics? (Y/N): ").lower()
    if save_answer in ("y", "yes"):
        save_statistics(game_object, file_path = file_path)
        print("\n" + f"The stats were saved in {file_path} \n")
    else:
        print("\n" + "The stats were not saved. \n")
