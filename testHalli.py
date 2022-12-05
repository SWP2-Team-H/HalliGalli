import unittest

from game import *


class TestHalli(unittest.TestCase):

    def setUp(self):
        self.p_list = [Player('a'), Player('b')]

    def tearDown(self):
        pass

    def test_hg_check(self):
        self.p_list[0].suit = "goldkiwi"
        self.p_list[0].num = 3
        self.p_list[1].suit = "goldkiwi"
        self.p_list[1].num = 2
        self.assertEqual(hg_check(self.p_list), 2)
        self.p_list[0].suit = "strawberry"
        self.p_list[0].num = 5
        self.p_list[1].suit = "strawberry"
        self.p_list[1].num = 1
        self.assertEqual(hg_check(self.p_list), 0)
        self.p_list[0].suit = "goldkiwi"
        self.p_list[0].num = 3
        self.p_list[1].suit = "blueberry"
        self.p_list[1].num = 2
        self.assertEqual(hg_check(self.p_list), 0)
        self.p_list[0].suit = "banana"
        self.p_list[0].num = 4
        self.p_list[1].suit = "banana"
        self.p_list[1].num = 1
        self.assertEqual(hg_check(self.p_list), 1)

    def test_win_player(self):
        self.p_list[0].score = 20
        self.p_list[1].score = 10
        self.assertEqual(win_player(self.p_list), "a 승리!")
        self.p_list[0].score = 10
        self.p_list[1].score = 20
        self.assertEqual(win_player(self.p_list), "b 승리!")
        self.p_list[0].score = 20
        self.p_list[1].score = 20
        self.assertEqual(win_player(self.p_list), " 비김!")
        self.p_list[0].score = -10
        self.p_list[1].score = 0
        self.assertEqual(win_player(self.p_list), "b 승리!")


if __name__ == '__main__':
    unittest.main()
