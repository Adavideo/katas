import unittest

from minesweeper import game
from minesweeper.field import *


class TestField(unittest.TestCase):
    def test_createField(self):
        """
        Test the creation of a field
        """
        f = createField(2,2,1) 
        self.assertEqual(len(f), 2)

class testmenu(unittest.TestCase):
    def test_menu(self):
        """
        Test the menu
        """
        f = game.menu()
        self.assertEqual(len(f), 2)
