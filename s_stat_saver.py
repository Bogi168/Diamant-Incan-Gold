def save_statistics(game_object, file_path):
    with open(file_path,"a") as file:
        game_object.get_max_diamonds()
        for explorer in game_object.explorers:
            file.write("\n" + "*" * 60 + "\n"
                       f"Stats for bot level {explorer.level}: \n"
                       f"The bot collects {((explorer.diamond_count / 5) / game_object.games_amount):.1f} diamonds per round \n"
                       f"He collected {explorer.max_diamonds} diamonds in his best round \n"
                       f"The bot died in {(explorer.die_counter / (game_object.games_amount * 5)) * 100:.2f}% of the rounds \n" +
                       "*" * 60 + "\n")
