from unittest import TestCase
from exercise import Exercise, Equipment

exercises = {'Windmill Pushups': None, 'Diamond Pushups': None, 'Hammer Curls': Equipment.dumbbells,
             'Arnold Presses': Equipment.dumbbells, 'Bent Over Rows': Equipment.dumbbells,
             'Spiderman Pushups': None, 'DB Lateral Raises': Equipment.dumbbells,
             'KB exercise': Equipment.kettle_bell}


class TestCard(TestCase):

    def test_get_exercises_requiring_no_equipment(self):
        e = Exercise()
        self.assertEqual(len(e._get_equipped_exercises(exercises)), 3)

    def test_get_exercises_including_dumbbells(self):
        e = Exercise(Equipment.dumbbells.name)
        self.assertEqual(len(e._get_equipped_exercises(exercises)), 7)

    def test_get_exercises_including_kettlebells(self):
        e = Exercise(Equipment.kettle_bell.name)
        self.assertEqual(len(e._get_equipped_exercises(exercises)), 4)

    def test_get_exercises_including_all_equipment(self):
        e = Exercise([Equipment.kettle_bell.name, Equipment.dumbbells.name])
        self.assertEqual(len(e._get_equipped_exercises(exercises)), 8)
