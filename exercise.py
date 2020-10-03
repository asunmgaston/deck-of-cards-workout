__author__ = "Natalie Gaston"
__copyright__ = "Copyright 2020"

__version__ = "1.0.0"
__email__ = "nmgaston@gmail.com"

import random
from typing import List


class Exercise(object):
    """Different exercises used for various types of cards.  Contains the list of exercises and randomly selects
    from each list.
    """

    def __init__(self) -> None:
        self._upper_body = ['Windmill Pushups', 'Diamond Pushups', 'Hammer Curls', 'Tricep Dips', 'Chest Press',
                            'Bicep Curls', 'Arnold Presses', 'Bent Over Rows', 'Spiderman Pushups', 'DB Lateral Raises']
        self._lower_body = ['Backwards Lunges', 'Forward Lunges', 'Squats', 'Goblet Squats', 'Tip Toe Squats',
                            'Glute Bridge', 'Jumping Lunges', 'Split Jump Squats']
        self._core = ['V-Ups', 'Bicycle Crunches', 'Flutter Kicks', 'Commandos', 'Situps', 'Russian Twists',
                      'Supermans', 'Bird Dogs', 'Renegade Rows', 'Inch Worms', 'Leg Raises', 'Kickouts', 'Plank Jack']
        self._total_body = ['Burpee', 'Thrusters', 'Pushups']
        self._cardio = ['Jump Squats', 'Jumping Jacks', 'KB Swings', 'Snow Boarders',
                        'Skaters', 'High Knees', 'Mountain Climbers', 'Tuck Jumps', 'Plank Jacks']

    def get_upper_body_exercise(self) -> str:
        """Shuffles the upper body exercises and returns the first one in the queue as the selected exercise.

        @return: selected upper body exercise
        """
        random.shuffle(self._upper_body)
        return self._upper_body[0]

    def get_lower_body_exercise(self) -> str:
        """Shuffles the lower body exercises and returns the first one in the queue as the selected exercise.

        @return: selected lower body exercise
        """
        random.shuffle(self._lower_body)
        return self._lower_body[0]

    def get_core_exercise(self) -> str:
        """Shuffles the core exercises and returns the first one in the queue as the selected exercise.

        @return: selected core exercise
        """
        random.shuffle(self._core)
        return self._core[0]

    def get_total_body_exercise(self) -> str:
        """Shuffles the total body exercises and returns the first one in the queue as the selected exercise.

        @return: selected total body exercise
        """
        random.shuffle(self._total_body)
        return self._total_body[0]

    def get_cardio_exercises(self) -> List[str]:
        """Shuffles the cardio exercises and returns the entire sorted list.

        @return: shuffled cardio list
        """
        random.shuffle(self._cardio)
        return self._cardio
