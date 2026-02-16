# Calculate probability of dying on the next move
def calc_dying_prob(game_object, cards_object):
    killing_traps = 0
    probability = 0
    cards_object.played_cards.append(cards_object.new_card)
    for card in cards_object.played_cards:
        if card.card_type == "trap":
            traps_in_game = cards_object.deck.count(card)
            killing_traps += traps_in_game
    probability += killing_traps / len(cards_object.deck)
    cards_object.played_cards.pop(-1)
    game_object.dying_prob = probability

# Calculate amount of undiscovered diamonds
def calc_undiscovered_diamonds(game_object, cards_object):
    game_object.undiscovered_diamonds = 0
    cards_object.played_cards.append(cards_object.new_card)
    for card in cards_object.deck:
        if card.card_type == "treasure_card":
            game_object.undiscovered_diamonds += card.value
    cards_object.played_cards.pop(-1)

def calc_guaranteed_diamonds(game_object, current_player):
    current_player.guaranteed_diamonds = current_player.pocket + game_object.diamonds_on_way // len(game_object.players_inside)
    if len(game_object.players_inside) == 1:
        current_player.guaranteed_diamonds += game_object.relics_on_way

def calc_ev_next(game_object, cards_object, current_player):
    calc_dying_prob(game_object = game_object, cards_object = cards_object)
    game_object.surviving_prob = (1 - game_object.dying_prob)
    calc_undiscovered_diamonds(game_object = game_object, cards_object = cards_object)
    future_diamonds = (game_object.undiscovered_diamonds / (len(cards_object.deck) * len(game_object.players_inside))
                       + current_player.pocket)
    ev_next = game_object.surviving_prob * future_diamonds - game_object.dying_prob * current_player.pocket
    return ev_next

def calc_ev_next_dia_on_way(game_object, cards_object, current_player):
    calc_dying_prob(game_object = game_object, cards_object = cards_object)
    game_object.surviving_prob = (1 - game_object.dying_prob)
    calc_undiscovered_diamonds(game_object = game_object, cards_object = cards_object)
    calc_guaranteed_diamonds(game_object = game_object, current_player = current_player)
    future_diamonds = game_object.undiscovered_diamonds / (len(game_object.cards.deck) * len(game_object.players_inside)) + current_player.guaranteed_diamonds
    ev_next = game_object.surviving_prob * future_diamonds - game_object.dying_prob * current_player.guaranteed_diamonds
    return ev_next
