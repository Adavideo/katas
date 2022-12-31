import unittest

from minesweeper.field import *
from minesweeper.game import *

class TestField(unittest.TestCase):
    def test_createField(self):
        """
        Test the creation of a field
        """
        f = createField(2,2,1)
        self.assertEqual(f, None)

class testmenu(unittest.TestCase):
    def test_menu(self):
        """
        Test the menu
        """
        f = menu()
        self.assertEqual(f, None)
