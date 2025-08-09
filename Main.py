import random

#Karten
snakes = ["🐍", "🐍", "🐍"]
spiders = ["🕷", "🕷", "🕷"]
fires = ["🔥", "🔥", "🔥"]
avalanches = ["🌑", "🌑", "🌑"]
mummys = ["👤", "👤", "👤"]
treasure_cards = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
relics = [4.01, 6.01, 8.01, 11.01, 14.01]
traps = []

for snake in snakes:
    card = snake
    traps.append(card)
for spider in spiders:
    card = spider
    traps.append(card)
for fire in fires:
    card = fire
    traps.append(card)
for avalanche in avalanches:
    card = avalanche
    traps.append(card)
for mummy in mummys:
    card = mummy
    traps.append(card)

cards = []

for snake in snakes:
    card = snake
    cards.append(card)
for spider in spiders:
    card = spider
    cards.append(card)
for fire in fires:
    card = fire
    cards.append(card)
for avalanche in avalanches:
    card = avalanche
    cards.append(card)
for mummy in mummys:
    card = mummy
    cards.append(card)
for treasure in treasure_cards:
    card = treasure
    cards.append(card)

#Spieler
import _player

# Spiel
is_running = True
p_inside = True
played_cards = []
diamonds_on_way = 0
relics_on_way = 0
players_inside = [p for p in _player.players if p.inside]
p_relics = relics.copy()
d_winner = 0
winners = []

def draw_card():
    drawn = random.choice(p_cards)
    p_cards.remove(drawn)
    return drawn


while is_running:

    for rounds in range(5):
        card = random.choice(p_relics)
        cards.append(card)
        p_relics.remove(card)
        p_cards = cards.copy()
        print()
        print("****************************************")
        print(f"*               Round: {(rounds+1)}               *")
        print("****************************************")
        p_inside = True

        while p_inside:

            if len(players_inside) == 0:
                p_inside = False

            else:
                new_card = draw_card()
                if new_card in traps and new_card in played_cards:
                    print()
                    print(f"Oh no! It's the second {new_card}")
                    print("All the players inside lose their diamonds!")
                    if rounds == 5-1:
                        print()
                        print("_____________________________________________________________")
                    cards.remove(new_card)
                    for p in players_inside:
                        p.die()
                    p_inside = False
                    continue
                print()
                print(f"The drawn card was a {new_card}")
                print()
                if new_card in treasure_cards and len(players_inside) != 0:
                    diamonds_on_way += new_card % len(players_inside)
                if new_card in relics:
                    relics_on_way += int(new_card)
                    cards.remove(new_card)
                for i in range(len(players_inside)):
                    if new_card in traps:
                        print("_____________________________________________________________")
                        if relics_on_way != 0:
                            print(f"There are relics worth {relics_on_way} diamonds on the way")
                        players_inside[i].ask_question(diamonds_on_way)

                    elif new_card in treasure_cards:
                        print("_____________________________________________________________")
                        players_inside[i].pocket += new_card // len(players_inside)
                        if relics_on_way != 0:
                            print(f"There are relics worth {relics_on_way} diamonds on the way")
                        players_inside[i].ask_question(diamonds_on_way)

                    elif new_card in relics:
                        print("_____________________________________________________________")
                        print(f"There are relics worth {relics_on_way} diamonds on the way")
                        players_inside[i].ask_question(diamonds_on_way)
            if len(_player.go_home_now) != 0 and p_inside:
                for homer in _player.go_home_now:
                    homer.chest += diamonds_on_way // len(_player.go_home_now)
                diamonds_on_way = diamonds_on_way % len(_player.go_home_now)
            if relics_on_way != 0 and p_inside:
                if len(_player.go_home_now) == 1:
                    _player.go_home_now[0].chest += relics_on_way
                    relics_on_way = 0
            _player.go_home_now.clear()

            if p_inside:
                players_inside = [p for p in _player.players if p.inside]
                played_cards.append(new_card)


        played_cards.clear()
        players_inside.clear()
        for p in _player.players:
            p.inside = True
        players_inside = [p for p in _player.players if p.inside]
        diamonds_on_way = 0
        relics_on_way = 0
        p_cards = cards.copy()
    for s in _player.players:
        print(f"{s.player_name} collected {s.chest} Diamonds")
        if d_winner < s.chest:
            d_winner = s.chest
            winners.clear()
            winners.append(s)
        elif d_winner == s.chest:
            winners.append(s)
    print("_____________________________________________________________")
    print()
    print("*************************************************************")
    if len(winners) == 1:
        print(f"The winner is: {winners[0].player_name}")
    else:
        print(f"The winners are: ", end = "")
        for winner in winners:
            if winner == winners[-1]:
                print("& " + winner.player_name)
            elif winner == winners[-2]:
                print(winner.player_name, end=" ")
            else:
                print(winner.player_name, end=", ")
    print("*************************************************************")
    is_running = False
