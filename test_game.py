from game import Game


def test_cut_card():
    g = Game(num_decks=8, shuffle_threshold=0.33)
    original_len = len(g.deck)
    counter = 0
    while g.deck.draw() != Game.cut_card:
        counter += 1
    assert 0.66 < (counter / original_len) < 0.67
