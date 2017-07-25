"""
    Class(es) that represent a deck of playing cards
"""

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades hearts diamonds clubs'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    @staticmethod
    def rank_value(card):
        """ Gets a rank of a card:
            first by rank: aces is the highest rank
            second by suit: suit_values
        """
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(FrenchDeck.suit_values) + FrenchDeck.suit_values[card.suit]

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def get_random_card(self):
        return choice(self)


def ttest_basic():
    """ basic tests """
    print("a card:", Card('7', 'diamonds'))
    deck = FrenchDeck()
    print("Deck len:", len(deck))
    print("First card:", deck[0], "absolute rank:", deck.rank_value(deck[0]))
    print("Last card:", deck[-1], "absolute rank:", deck.rank_value(deck[-1]))
    print("top 3 cards:", deck[:3])
    print("Random card [1]:", deck.get_random_card())
    print("Random card [2]:", deck.get_random_card())
    print("Random card [3]:", deck.get_random_card())
    print("Highest ranks cards:")
    i = 0
    for card in sorted(deck, key=FrenchDeck.rank_value, reverse=True):
        if i > 2:
            break
        print(card, "absolute rank:", FrenchDeck.rank_value(card))
        i += 1


if __name__ == "__main__":
    ttest_basic()