__author__ = "Natalie Gaston"
__copyright__ = "Copyright 2020"

__version__ = "1.0.0"
__email__ = "nmgaston@gmail.com"

import enum


class FaceCards(enum.Enum):
    Ace = 1
    Jack = 11
    Queen = 12
    King = 13


class Card(object):
    """Represents a card in a deck of cards.

    @param suite: suite of the card [diamond, heart, spade, club]
    @param value: 1-13 1=Ace, 11=Jack, 12=Queen, 13=King, 14=Joker
    @param exercise: exercise assigned to the card
    """

    def __init__(self, suite: str, value: int, exercise: str) -> None:
        self._suite = suite
        self._value = value
        self._exercise = exercise

    def show(self) -> str:
        """Shows the output of the card including value, suite, reps, and exercise

        @return: output of card
        """
        if self._value == FaceCards.Ace.value:
            return "Ace of {} -> 30 {}".format(self._suite, self._exercise)
        elif self._value == FaceCards.Jack.value:
            return "Jack of {} -> 10 {}".format(self._suite, self._exercise)
        elif self._value == FaceCards.Queen.value:
            return "Queen of {} -> 15 {}".format(self._suite, self._exercise)
        elif self._value == FaceCards.King.value:
            return "King of {} -> 20 {}".format(self._suite, self._exercise)
        elif self._value == 14:
            return "Joker -> 1 minute rest"
        else:
            return "{} of {} -> {} {}".format(self._value, self._suite, self._value, self._exercise)
