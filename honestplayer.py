from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate

def estimate_win_rate(first_card, second_card, nb_players):
    hole_card = gen_cards([first_card, second_card])
    community_card = gen_cards([])
    estimate = estimate_hole_card_win_rate(nb_simulation=500, nb_player=nb_players, hole_card=hole_card, community_card=community_card)
    print("Win chance: " + str(estimate))
    return estimate
