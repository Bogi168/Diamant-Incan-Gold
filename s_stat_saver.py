file_path = "s_stats.txt"

def save_statistics(game_object):
    with open(file_path,"a") as file:
        game_object.get_max_diamonds()
        for e in game_object.explorers:
            file.write("\n" + "*"*46 + "\n"
                       f"Stats for Bot Level {e.level}: \n"
                       f"The Bot collects {((e.diamond_count / 5) / game_object.games_amount):.1f} diamonds per round \n"
                       f"He collected {e.max_diamonds} diamonds in his best round \n" +
                       "*"*46 + "\n")