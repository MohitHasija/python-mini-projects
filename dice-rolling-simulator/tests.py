__author__ = 'Mohit'


import unittest
from main import Die, Player

class DieAndPlayerTests(unittest.TestCase):
    def setUp(self):
        self.die = Die()
        self.player = Player(self.die.run())


    def test_die_run(self):

        random_number = self.die.run()
        self.assertTrue( random_number >= self.die.min and random_number <= self.die.max)

    def test_die_min_setter(self):
        with self.assertRaises(TypeError):
            self.die.min = 0


    def test_die_max_setter(self):
        with self.assertRaises(TypeError):
            self.die.max = 100


    def test_player_add_die(self):
        random_number_1 = self.die.run()
        self.player.score += random_number_1
        self.assertEqual(self.player.score, random_number_1)

        random_number_2 = self.die.run()
        self.player.score += random_number_2

        self.assertEqual(self.player.score, random_number_2 + random_number_1)



if __name__ == '__main__':
    unittest.main()
