# Calculate probability of dying on the next move
def calc_dying_prob(cards_object):
    killing_traps = 0
    probability = 0
    list_played_cards = cards_object.played_cards.copy()
    list_played_cards.append(cards_object.new_card)
    for card in list_played_cards:
        if card.card_type == "trap":
            traps_in_game = cards_object.deck.count(card)
            killing_traps += traps_in_game
    probability += killing_traps / len(cards_object.deck)
    return probability

# Calculate amount of undiscovered diamonds
def calc_undiscovered_diamonds(cards_object):
    undiscovered_diamonds = 0
    list_played_cards = cards_object.played_cards.copy()
    list_played_cards.append(cards_object.new_card)
    for card in cards_object.deck:
        if card.card_type == "treasure_card":
            undiscovered_diamonds += card.value
    return undiscovered_diamonds

def calc_guaranteed_diamonds(game_object, current_player):
    guaranteed_diamonds = current_player.pocket + game_object.diamonds_on_way // len(game_object.players_inside)
    if len(game_object.players_inside) == 1:
        guaranteed_diamonds += game_object.relics_on_way
    return guaranteed_diamonds

def calc_future_diamonds(game_object, cards_object, current_player):
    guaranteed_diamonds = current_player.guaranteed_diamonds
    future_diamonds =  (game_object.undiscovered_diamonds /
                        (len(cards_object.deck) * len(game_object.players_inside))
                        + guaranteed_diamonds)
    return future_diamonds

def calc_ev_next_without_dia_on_way(game_object, current_player):
    dying_prob = game_object.dying_prob
    surviving_prob = 1 - dying_prob
    future_diamonds = current_player.future_diamonds
    ev_next = surviving_prob * future_diamonds - dying_prob * current_player.pocket
    return ev_next

def calc_ev_next(game_object, current_player):
    dying_prob = game_object.dying_prob
    surviving_prob = 1 - dying_prob
    guaranteed_diamonds = current_player.guaranteed_diamonds
    future_diamonds = current_player.future_diamonds
    ev_next = surviving_prob * future_diamonds - dying_prob * guaranteed_diamonds
    return ev_next
