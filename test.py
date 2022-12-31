import unittest

from minesweeper import game

class TestGame(unittest.TestCase):
    def test_menu(self):
        """
        Test the main menu
        """
        result = game.menu()
        self.assertEqual(result, "Minesweeper")

if __name__ == '__main__':
    unittest.main()
