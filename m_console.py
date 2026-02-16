from Main_Game.m_player import Player, Bot
from Main_Game.m_probability_and_ev import calc_ev_next_dia_on_way

# Welcome text
def console_welcome_txt():
    print("\n" + "*" * 40 +
          "\n* Welcome to Incan Gold - Bogi Edition *  \n" +
          "*" * 40 + "\n")

# Create players
def console_create_players(game_object):
    players_amount = input("How many players? ")
    while not players_amount.isdigit() or int(players_amount) <= 0:
        players_amount = input("That's not a valid number. How many players? ")
    players_amount = int(players_amount)
    print("\n" + "_"*40)
    for player_num in range(players_amount):
        player_name = input(f"Enter player number {player_num + 1}'s name: ").capitalize()
        game_object.players.append(Player(player_name = player_name, game_object = game_object))
        print("_"*40)

# Create bots
def console_create_bots(game_object):
    bots_amount = input("\nHow many bots? ")
    while not bots_amount.isdigit() or int(bots_amount) < 0:
        bots_amount = input("That's not a valid number. How many bots? ")
    bots_amount = int(bots_amount)
    if bots_amount != 0:
        for bots_num in range(bots_amount):
            print("\n" + "_" * 70)
            level_bot = input(f"Select a level for Bot {bots_num + 1} (careful: 1 / medium: 2 / risky: 3): ")
            while not level_bot in ("1", "2", "3", "4"):
                level_bot = input(
                    f"{level_bot} is not valid. Select a level for Bot {bots_num + 1} (careful: 1 / medium: 2 / risky: 3): ")
            level_bot = int(level_bot)
            game_object.bots.append(Bot(bot_name = f"Bot {bots_num + 1}", level = level_bot, game_object = game_object))
            print("_" * 70)

# Current round
def console_tell_round(game_object):
    print("\n" + "*" * 40 + "\n" +
          f"*               Round: {(game_object.rounds + 1)}               * \n" +
          "*" * 40)

# Tell the played cards
def console_tell_played_cards(cards_object):
    print("\n" + "Played Cards: ", end="")
    for played_card in cards_object.played_cards:
        if played_card == cards_object.played_cards[-1]:
            print(played_card)
        else:
            print(played_card, end=", ")

def console_tell_new_card(cards_object):
    print("\n" + f"The drawn card was a {cards_object.new_card} \n")

# Output depending on drawn card
def console_second_trap(game_object, cards_object):
    print("\n" +
          f"Oh no! It's the second {cards_object.new_card} \n" +
          "All the players inside lose their diamonds!")
    if game_object.rounds == 5 - 1:
        print("\n" + "_" * 61)

def console_no_second_trap(game_object):
    print("_" * 61)
    print(console_tell_probability(game_object = game_object) + "\n")

# Tell situation
def console_tell_probability(game_object):
    return f"The probability of dying in the next move is {game_object.dying_prob * 100:.1f}%"

def console_tell_relics_on_way(game_object):
    if game_object.relics_on_way != 0:
        print(f"There are relics worth {game_object.relics_on_way} diamonds on the way")

# Present Player's diamonds
def console_tell_p_diamonds(game_object, cards_object, current_player):
    print(f"You have {current_player.pocket} diamond(s) in your pocket \n" +
          f"There is/are {game_object.diamonds_on_way} diamond(s) on the way home \n" +
          f"The expected value is {calc_ev_next_dia_on_way(game_object = game_object, cards_object = cards_object, current_player = current_player):.2f} \n" +
          "_"*61 + "\n")

def console_ask_player(game_object, cards_object, current_player):
    console_tell_p_diamonds(game_object = game_object, cards_object = cards_object, current_player = current_player)
    decision = input(f"{current_player.player_name}: Do you want to go home? (Y/N) ").upper()
    while not decision.isalpha():
        decision = input(f"{current_player.player_name}: {decision} is not valid. Do you want to go home? (Y/N) ").upper()
    print("_"*61)
    if decision == "Y" or decision == "YES":
        return "leave"
    else:
        return "stay"

# Bot goes home
def console_bot_goes_home(current_bot):
    print(f"{current_bot.bot_name} goes home and saves his diamond(s) \n" +
          "_" * 61)

# Bot stays inside
def console_bot_stays_inside(current_bot):
    print(f"{current_bot.bot_name} stays inside \n" +
          "_" * 61)

# Present Bot's diamonds
def console_tell_b_diamonds(game_object, current_bot):
    print(f"{current_bot.bot_name} has {current_bot.pocket} diamond(s) in his pocket \n" +
          f"There is/are {game_object.diamonds_on_way} diamond(s) on the way home \n" +
          "_" * 61)

# Present the result
def console_tell_result(game_object):
    print("\n" + "_"*61)
    game_object.identify_game_winner()
    for explorer in game_object.explorers:
        print(f"{explorer.player_name} collected {explorer.chest} Diamonds")
    print("_" * 61 + "\n"*2 + "*" * 61)
    if len(game_object.final_winners) == 1:
        print(f"The winner is: {game_object.final_winners[0].player_name}")
    else:
        print(f"The winners are: ", end = "")
        for winner in game_object.final_winners:
            if winner == game_object.final_winners[-1]:
                print("& " + winner.player_name)
            elif winner == game_object.final_winners[-2]:
                print(winner.player_name, end=" ")
            else:
                print(winner.player_name, end=", ")
    print("*"*61 + "\n")

# Ask about playing again
def console_ask_again(game_object):
    play_again = input("Do you want to play again? (Y/N) ").upper()
    if play_again == "Y" or play_again == "YES":
        game_object.reset_game()
    else:
        print("\nThanks for playing!")
        game_object.is_running = False
