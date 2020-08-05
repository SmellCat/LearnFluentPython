# -*- coding:utf-8 -*-

__author__ = "Atituset"

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position): # 关于__getitem__ ,可以参考 https://stackoverflow.com/questions/43627405/understanding-getitem-method
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    # Since Python2.6, nametuple can be used to build classed of objects that are
    # just bundles of attributes with no custom methods, like a database record
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])

    # get random item
    print(choice(deck))

    # Just by implementing the __getitem__ special method, our deck is alse iterable
    for card in deck:
        print(card)

    print('*' * 100)

    for card in sorted(deck, key=spades_high):
        print(card)
