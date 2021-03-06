__author__ = "Natalie Gaston"
__copyright__ = "Copyright 2020"

__version__ = "1.0.0"
__email__ = "nmgaston@gmail.com"

import random
import tkinter.font as tkFont
from tkinter import Tk, Label, Button
from typing import List

from card import Card, FaceCards
from constants import DIAMONDS, HEARTS, SPADES, CLUBS
from exercise import Exercise, Equipment


class Deck(object):
    """Represents a deck of cards used as an exercise.

    @param dumbbells: True if dumbbells are available for the workout; otherwise, false.
    @param kettle_bell: True if a kettle bell is available for the workout; otherwise, false.
    @param trx: True if a TRX is available for the workout; otherwise, false.
    @param jump_rope: True if a jump rope is available for the workout; otherwise, false.
    """
    def __init__(self, dumbbells: bool = False, kettle_bell: bool = False,
                 trx: bool = False, jump_rope: bool = False, equipment_only: bool = False) -> None:
        self._kettle_bell = kettle_bell
        self._dumbbells = dumbbells
        self._jump_rope = jump_rope
        self._equipment_only = equipment_only

        self._trx = trx
        self._deck = []
        self._create_deck()
        random.shuffle(self._deck)

        self._gui = Tk()
        self._gui.title("Deck of Cards Workout")
        self._gui.geometry("800x300")
        self._font_style = tkFont.Font(family="Lucida Grande", size=20)
        self._count = 0
        self._exercise_count = Label(self._gui, text="Exercise #{}".format(self._count + 1), font=self._font_style)
        self._exercise = Label(self._gui, text=self._deck[self._count].show(), font=self._font_style)

        self._show_deck()

    def _create_equipment_list(self) -> List[Equipment]:
        eq = []
        if self._kettle_bell:
            eq.append(Equipment.kettle_bell)
        if self._dumbbells:
            eq.append(Equipment.dumbbells)
        if self._trx:
            eq.append(Equipment.trx)
        if self._jump_rope:
            eq.append(Equipment.jump_rope)
        return eq

    def _create_deck(self) -> None:
        ex = Exercise(self._create_equipment_list(), self._equipment_only)

        for s, e in [(DIAMONDS, ex.get_upper_body_exercise()), (CLUBS, ex.get_lower_body_exercise()),
                     (HEARTS, ex.get_core_exercise()), (SPADES, ex.get_total_body_exercise())]:
            for v in range(2, 11):
                self._deck.append(Card(s, v, e))

        cardio = ex.get_cardio_exercises()
        for s, e in [(DIAMONDS, cardio[0]), (CLUBS, cardio[1]), (HEARTS, cardio[2]), (SPADES, cardio[3])]:
            for v in FaceCards:
                self._deck.append(Card(s, v.value, e))

        self._deck.append(Card('Joker', 14, '1 minute rest'))
        self._deck.append(Card('Joker', 14, '1 minute rest'))

    def _show_deck(self) -> None:
        Label(self._gui, text="").pack()
        self._exercise_count.pack()
        Label(self._gui, text="").pack()
        self._exercise.pack()
        Label(self._gui, text="").pack()

        Button(self._gui, text="Next", command=self._next_exercise, font=self._font_style).pack()
        self._gui.mainloop()

    def _next_exercise(self) -> None:
        self._count = self._count + 1
        if self._count < len(self._deck):
            self._exercise_count['text'] = "Exercise #{}".format(self._count + 1)
            self._exercise['text'] = self._deck[self._count].show()
        else:
            self._exercise_count['text'] = "ALL DONE!".format(self._count + 1)
            self._exercise['text'] = ""
