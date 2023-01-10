from blackjack.card import Card

# Card lists for testing
h = []
h2 = [Card(Card.NUM_2)]
h23 = [Card(Card.NUM_2), Card(Card.NUM_3)]
A = [Card(Card.ACE)]
AA = [Card(Card.ACE), Card(Card.ACE)]
h67 = [Card(Card.NUM_6), Card(Card.NUM_7)]
AAAJ = [Card(Card.ACE), Card(Card.JACK), Card(Card.ACE),
        Card(Card.ACE)]
AAA = [Card(Card.ACE), Card(Card.ACE), Card(Card.ACE)]
AA64 = [Card(Card.NUM_6), Card(Card.NUM_4),
        Card(Card.ACE), Card(Card.ACE)]
AA3 = [Card(Card.NUM_3), Card(Card.ACE), Card(Card.ACE)]
A6 = [Card(Card.ACE), Card(Card.NUM_6)]
h8352 = [Card(Card.NUM_8), Card(Card.NUM_3), Card(Card.NUM_5),
         Card(Card.NUM_2)]
A45 = [Card(Card.ACE), Card(Card.NUM_4), Card(Card.NUM_5)]
K28 = [Card(Card.NUM_2), Card(Card.KING), Card(Card.NUM_8)]
AK = [Card(Card.ACE), Card(Card.KING)]
Q75 = [Card(Card.NUM_5), Card(Card.NUM_7), Card(Card.QUEEN)]
JQK5A = [Card(Card.KING), Card(Card.JACK),
         Card(Card.QUEEN), Card(Card.NUM_5), Card(Card.ACE)]

# Collect them together
handlists = [h, h2, h23, A, AA, h67, AAAJ, AAA, AA64, AA3, A6, h8352, A45,
             K28, AK, Q75, JQK5A]
