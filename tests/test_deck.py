from unittest import TestCase
from deck import Deck
from unittest.mock import patch


class TestDeck(TestCase):

    def setUp(self):
        pass

    @patch('deck.Deck._show_deck')
    def test_create_empty_equipment_list(self, mock_show):
        d = Deck()
        self.assertEqual(0, len(d._create_equipment_list()))

    @patch('deck.Deck._show_deck')
    def test_create_all_equipment_list(self, mock_show):
        d = Deck(dumbbells=True, kettle_bell=True, trx=True, jump_rope=True)
        self.assertEqual(4, len(d._create_equipment_list()))
