__author__ = "Natalie Gaston"
__copyright__ = "Copyright 2020"

__version__ = "1.0.0"
__email__ = "nmgaston@gmail.com"

import random
from enum import Enum
from typing import List, Dict


class Equipment(Enum):
    dumbbells = 0
    kettle_bell = 1
    trx = 2
    jump_rope = 3


class Exercise(object):
    """Different exercises used for various types of cards.  Contains the list of exercises and randomly selects
    from each list.

    @param equipment: Available equipment
    @param equipment_only: Select only exercises that use available equipment. No body weight exercises.
    """

    def __init__(self, equipment: List[str] = None, equipment_only: bool = False) -> None:
        self._equipment = equipment
        self._equipment_only = equipment_only

        self._upper_body = {'Windmill Pushups': None,
                            'Diamond Pushups': None,
                            'Tricep Dips': None,
                            'Spiderman Pushups': None,
                            'Pike Pushup': None,
                            'Hammer Curls (DB)': Equipment.dumbbells,
                            'Arnold Presses (DB)': Equipment.dumbbells,
                            'Bent Over Rows (DB)': Equipment.dumbbells,
                            'DB Lateral Raises (DB)': Equipment.dumbbells,
                            'Chest Press (DB)': Equipment.dumbbells,
                            'Pec Flys (DB)': Equipment.dumbbells,
                            'Shoulder Press (KB)': Equipment.kettle_bell,
                            'Chest Press (TRX)': Equipment.trx,
                            'Tricep Press (TRX)': Equipment.trx,
                            'Low Row (TRX)': Equipment.trx,
                            'Squat to Row (TRX)': Equipment.trx,
                            'Bicep Curls (TRX)': Equipment.trx,
                            'Y-Deltoid Fly (TR)': Equipment.trx,
                            'Chest Press to Triceps Extension (TRX)': Equipment.trx}

        self._lower_body = {'Backwards Lunges': None,
                            'Forward Lunges': None,
                            'Squats': None,
                            'Curtsy Lunge': None,
                            'Tip Toe Squats': None,
                            'Glute Bridge': None,
                            'Jumping Lunges': None,
                            'Split Jump Squats': None,
                            'Drop Squats': None,
                            'Hamstring Curl (TRX)': Equipment.trx,
                            'Squat (TRX)': Equipment.trx}

        self._core = {'V-Ups': None,
                      'Bicycle Crunches': None,
                      'Flutter Kicks': None,
                      'Commandos': None,
                      'Sit ups': None,
                      'Russian Twists': None,
                      'Supermans': None,
                      'Bird Dogs': None,
                      'Inch Worms': None,
                      'Leg Raises': None,
                      'Kickouts': None,
                      'Plank Jack': None,
                      'Scissors:': None,
                      'Crunches': None,
                      'Cross Crunches': None,
                      'Toe Taps': None,
                      'Knee to Elbow': None,
                      'Renegade Rows (DB)': Equipment.dumbbells,
                      'Pullovers (KB)': Equipment.kettle_bell,
                      'Sit ups (KB)': Equipment.kettle_bell,
                      'Hamstring Curl to Hip Press (TRX)': Equipment.trx,
                      'Crunch (TRX)': Equipment.trx,
                      'Atomic Pushup (TRX)': Equipment.trx}

        self._total_body = {'Burpees': None,
                            'Pushups': None,
                            'Squat Thrusts': None,
                            'Thrusters (DB)': Equipment.dumbbells,
                            'Goblet Squats (KB)': Equipment.kettle_bell,
                            'Pistol Squat (KB)': Equipment.kettle_bell}

        self._cardio = {'Jump Squats': None,
                        'Jumping Jacks': None,
                        'Snow Boarders': None,
                        'Skaters': None,
                        'High Knees': None,
                        'Mountain Climbers': None,
                        'Tuck Jumps': None,
                        'Plank Jacks': None,
                        'KB Swings (KB)': Equipment.kettle_bell,
                        'Basic Jump (JR)': Equipment.jump_rope,
                        'Alternating Foot (JR)': Equipment.jump_rope,
                        'Boxer Step (JR)': Equipment.jump_rope}

    def get_upper_body_exercise(self) -> str:
        """Shuffles the upper body exercises and returns the first one in the queue as the selected exercise.

        @return: selected upper body exercise
        """
        return self._get_equipped_exercise(self._upper_body)

    def get_lower_body_exercise(self) -> str:
        """Shuffles the lower body exercises and returns the first one in the queue as the selected exercise.

        @return: selected lower body exercise
        """
        return self._get_equipped_exercise(self._lower_body)

    def get_core_exercise(self) -> str:
        """Shuffles the core exercises and returns the first one in the queue as the selected exercise.

        @return: selected core exercise
        """
        return self._get_equipped_exercise(self._core)

    def get_total_body_exercise(self) -> str:
        """Shuffles the total body exercises and returns the first one in the queue as the selected exercise.

        @return: selected total body exercise
        """
        return self._get_equipped_exercise(self._total_body)

    def get_cardio_exercises(self) -> List[str]:
        """Shuffles the cardio exercises and returns the entire sorted list.

        @return: shuffled cardio list
        """
        return self._get_equipped_exercises(self._cardio)

    def _get_equipped_exercises(self, exercises: Dict[str, Equipment]) -> List[str]:
        """Randomly picks an exercise that matches the exercise equipment available for the workout

        @param exercises - Dictionary of exercises with exercise name and required equipment.
        @return: List of all exercises matching equipment available.
        """
        equipped_exercises = []

        for ex, eq in exercises.items():
            if eq is None and not self._equipment_only:
                equipped_exercises.append(ex)
                continue
            if self._equipment:
                if Equipment.dumbbells in self._equipment and eq == Equipment.dumbbells:
                    equipped_exercises.append(ex)
                elif Equipment.kettle_bell in self._equipment and eq == Equipment.kettle_bell:
                    equipped_exercises.append(ex)
                elif Equipment.trx in self._equipment and eq == Equipment.trx:
                    equipped_exercises.append(ex)
                elif Equipment.jump_rope in self._equipment and eq == Equipment.jump_rope:
                    equipped_exercises.append(ex)

        random.shuffle(equipped_exercises)
        return equipped_exercises

    def _get_equipped_exercise(self, exercises: Dict[str, Equipment]) -> str:
        """Randomly picks an exercise that matches the exercise equipment available for the workout

        @param exercises - Dictionary of exercises with exercise name and required equipment.
        @return: Exercise that matches equipment available.
        """
        return self._get_equipped_exercises(exercises)[0]
