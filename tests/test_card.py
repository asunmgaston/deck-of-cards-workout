from unittest import TestCase
from card import Card
from constants import *


class TestCard(TestCase):

    def test_show_correct_ace_card(self):
        c = Card(DIAMONDS, 1, 'Burpees')
        self.assertEqual(c.show(), 'Ace of Diamonds -> 30 Burpees')

    def test_show_correct_jack_card(self):
        c = Card(DIAMONDS, 11, 'Burpees')
        self.assertEqual(c.show(), 'Jack of Diamonds -> 10 Burpees')

    def test_show_correct_queen_card(self):
        c = Card(DIAMONDS, 12, 'Burpees')
        self.assertEqual(c.show(), 'Queen of Diamonds -> 15 Burpees')

    def test_show_correct_king_card(self):
        c = Card(DIAMONDS, 13, 'Burpees')
        self.assertEqual(c.show(), 'King of Diamonds -> 20 Burpees')

    def test_show_correct_joker_card(self):
        c = Card(DIAMONDS, 14, None)
        self.assertEqual(c.show(), 'Joker -> 1 minute rest')

    def test_show_correct_number_card(self):
        c = Card(CLUBS, 5, 'Squats')
        self.assertEqual(c.show(), '5 of Clubs -> 5 Squats')
