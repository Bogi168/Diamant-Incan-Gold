def tell_stats(game_object, explorer):
    return ("\n" + "*" * 62 + "\n" +
            f"{explorer.bot_name} (Level: {explorer.level}) won {explorer.round_winning_count} rounds \n" +
            f"{explorer.bot_name} won {explorer.game_winning_count} games \n" +
            f"That's a win rate of {explorer.game_winning_count / game_object.games_amount * 100:.1f}% \n" +
            f"{explorer.bot_name} collected {explorer.diamond_count} diamonds \n" +
            f"That's {((explorer.diamond_count / 5) / game_object.games_amount):.1f} diamonds per round \n" +
            f"{explorer.bot_name} collected {explorer.max_diamonds} diamonds in his best round \n" +
            f"But he died in {explorer.die_counter} rounds \n" +
            f"That's {(explorer.die_counter / (game_object.games_amount * 5)) * 100:.2f}% of the rounds \n" +
            "*" * 62 + "\n")

def save_stats(file_path):
    return "\n" + f"The stats were saved in {file_path} \n"

def delete_stats():
    return "\n" + "The stats were not saved. \n"