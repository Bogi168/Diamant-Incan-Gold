# Welcome text
def welcome_txt():
    return ("\n" + "*" * 40 +
            "\n* Welcome to Incan Gold - Bogi Edition *  \n" +
            "*" * 40 + "\n")

def dashes_1():
    return "\n" + "_"*40

def dashes_2():
    return "_"*40

def dashes_3():
    return "\n" + "_" * 70

def dashes_4():
    return "_"*70

def dashes_5():
    return "\n" + "_" * 61

def dashes_6():
    return "_" * 61

def stars_1():
    return  "_" * 61 + "\n"*2 + "*" * 61

def stars_2():
    return "*"*61 + "\n"

# Current round
def tell_round(rounds):
    return ("\n" + "*" * 40 +
          f"\n*               Round: {(rounds + 1)}               * \n" +
          "*" * 40)

# Tell the played cards
def played_cards_text(cards_object):
    cards = ", ".join(str(card) for card in cards_object.played_cards)
    return f"\nPlayed Cards: {cards}"

def tell_new_card(new_card):
    return "\n" + f"The drawn card was a {new_card} \n"

# Output depending on drawn card
def second_trap(new_card):
    return ("\n" +
            f"Oh no! It's the second {new_card} \n" +
            "All the players inside lose their diamonds!")

# Tell situation
def tell_probability(game_object):
    return ("_" * 61 +
            f"\nThe probability of dying in the next move is {game_object.dying_prob * 100:.1f}%")

def tell_relics_on_way(game_object):
    return f"There are relics worth {game_object.relics_on_way} diamonds on the way"

# Present Player's diamonds
def tell_p_diamonds(game_object, current_player):
    return (f"You have {current_player.pocket} diamond(s) in your pocket \n" +
            f"There is/are {game_object.diamonds_on_way} diamond(s) on the way home \n" +
            f"The expected value is {current_player.ev_next:.2f} \n" +
            "_"*61 + "\n")

# Bot goes home
def bot_goes_home(current_bot):
    return (f"{current_bot.bot_name} goes home and saves his diamond(s) \n" +
            "_" * 61)

# Bot stays inside
def bot_stays_inside(current_bot):
    return (f"{current_bot.bot_name} stays inside \n" +
            "_" * 61)

# Present Bot's diamonds
def tell_b_diamonds(game_object, current_bot):
    return (f"{current_bot.bot_name} has {current_bot.pocket} diamond(s) in his pocket \n" +
            f"There is/are {game_object.diamonds_on_way} diamond(s) on the way home \n" +
            "_" * 61)

# Present the result
def tell_collected_diamonds(player_name, chest):
    return f"{player_name} collected {chest} Diamonds"

def tell_winners(game_object):
    names = [winner.player_name for winner in game_object.list_final_winners]
    if len(names) == 1:
        return f"The winner is: {names[0]}"
    elif len(names) == 2:
        return f"The winners are: {names[0]} & {names[1]}"
    else:
        *first_names, last_name = names
        return f"The winners are: {', '.join(first_names)} & {last_name}"

def new_line():
    return ""

def end_of_game():
    return "\nThanks for playing!"

# Simulation output
def tell_stats(game_object, explorer):
    return ("\n" + "*" * 62 + "\n" +
            f"{explorer.player_name} (Level: {explorer.level}) won {explorer.round_winning_count} rounds \n" +
            f"{explorer.player_name} won {explorer.game_winning_count} games \n" +
            f"That's a win rate of {explorer.game_winning_count / game_object.games_amount * 100:.1f}% \n" +
            f"{explorer.player_name} collected {explorer.diamond_count} diamonds \n" +
            f"That's {((explorer.diamond_count / 5) / game_object.games_amount):.1f} diamonds per round \n" +
            f"{explorer.player_name} collected {explorer.max_diamonds} diamonds in his best round \n" +
            f"But he died in {explorer.die_counter} rounds \n" +
            f"That's {(explorer.die_counter / (game_object.games_amount * 5)) * 100:.2f}% of the rounds \n" +
            "*" * 62 + "\n")

def save_stats(file_path):
    return "\n" + f"The stats were saved in {file_path} \n"

def delete_stats():
    return "\n" + "The stats were not saved. \n"
