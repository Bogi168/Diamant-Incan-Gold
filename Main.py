import random

#Karten
snakes = ["snake", "snake", "snake"]
spiders = ["spider", "spider", "spider"]
fires = ["fire", "fire", "fire"]
avalanches = ["avalanche", "avalanche", "avalanche"]
mummys = ["mummy", "mummy", "mummy"]
treasure_cards = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
relics = [4.01, 8.01, 11.01]
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
for relic in relics:
    card = relic
    cards.append(card)

p_cards = cards.copy()

#Spieler
import _player

# Spiel
is_running = True
p_inside = True
played_cards = []
diamonds_on_way = 0
relics_on_way = 0
players_inside = [p for p in _player.players if p.inside]


def draw_card():
    drawn = random.choice(p_cards)
    p_cards.remove(drawn)
    return drawn


while is_running:

    for rounds in range(5):

        print(f"Round: {rounds+1}")
        p_inside = True

        while p_inside:

            if len(players_inside) == 0:
                p_inside = False

            else:
                new_card = draw_card()
                if new_card in traps:
                    if new_card in played_cards:
                        print(f"Oh no! It's the second {new_card}")
                        print("All players lose their diamonds!")
                        for p in players_inside:
                            p.die()
                        p_inside = False
                        continue
                print(f"The drawn card was a {new_card}")
                if new_card in treasure_cards and len(players_inside) != 0:
                    diamonds_on_way += new_card % len(players_inside)
                if new_card in relics:
                    relics_on_way += int(new_card)
                for i in range(len(players_inside)):
                    if new_card in traps:
                        if relics_on_way != 0:
                            print(f"There are relics worth {relics_on_way} diamonds on the way")
                        players_inside[i].ask_question(diamonds_on_way)

                    elif new_card in treasure_cards:
                        players_inside[i].pocket += new_card // len(players_inside)
                        if relics_on_way != 0:
                            print(f"There are relics worth {relics_on_way} diamonds on the way")
                        players_inside[i].ask_question(diamonds_on_way)

                    elif new_card in relics:
                        print(f"There are relics worth {relics_on_way} diamonds on the way")
                        players_inside[i].ask_question(diamonds_on_way)
            if len(_player.go_home_now) != 0 and p_inside:
                for homer in _player.go_home_now:
                    homer.chest += diamonds_on_way//len(_player.go_home_now)
                diamonds_on_way = diamonds_on_way%len(_player.go_home_now)
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

    is_running = False

