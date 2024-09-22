from unittest import TestCase
from src.game import Game
from src.ui import UI


class TestController(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.UI = UI(Game())

    def setUp(self):
        self.game = Game()

    def test_advance_year(self):
        self.assertEqual(self.game.advance_year(0, 0, 0), "STARVE ENDING")
        self.assertNotEqual(self.game.advance_year(0, 0, 0), "CONTINUE")

    def test_game_over(self):
        self.assertEqual(self.UI.game_over(True), None)
        self.assertEqual(self.UI.game_over(False), None)














