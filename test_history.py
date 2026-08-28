import unittest
import os
import json
from history import GameHistory


class TestGameHistory(unittest.TestCase):

    TEST_FILE = "test_game_history.json"

    def setUp(self):
        self.original_file = GameHistory.FILE_NAME
        GameHistory.FILE_NAME = self.TEST_FILE

        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

        self.history = GameHistory()

    def tearDown(self):
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

        GameHistory.FILE_NAME = self.original_file

    def test_initial_history_is_empty(self):
        self.assertEqual(self.history.get_history(), [])

    def test_add_game(self):
        self.history.add_game("X", "Easy", "LIGHT")

        records = self.history.get_history()

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["result"], "X")
        self.assertEqual(records[0]["difficulty"], "Easy")
        self.assertEqual(records[0]["theme"], "LIGHT")
        self.assertIn("date", records[0])

    def test_multiple_games(self):
        self.history.add_game("X", "Easy", "LIGHT")
        self.history.add_game("O", "Hard", "DARK")
        self.history.add_game("Draw", "Medium", "LIGHT")

        records = self.history.get_history()

        self.assertEqual(len(records), 3)
        self.assertEqual(records[1]["result"], "O")
        self.assertEqual(records[2]["result"], "Draw")

    def test_history_is_saved_to_file(self):
        self.history.add_game("X", "Easy", "LIGHT")

        self.assertTrue(os.path.exists(self.TEST_FILE))

        with open(self.TEST_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["result"], "X")

    def test_clear_history(self):
        self.history.add_game("X", "Easy", "LIGHT")
        self.history.add_game("O", "Hard", "DARK")

        self.history.clear_history()

        self.assertEqual(self.history.get_history(), [])

    def test_history_persists_after_reload(self):
        self.history.add_game("X", "Easy", "LIGHT")

        new_history = GameHistory()

        records = new_history.get_history()

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["result"], "X")
        self.assertEqual(records[0]["difficulty"], "Easy")
        self.assertEqual(records[0]["theme"], "LIGHT")

def test_invalid_history_format(self):
        with open(self.TEST_FILE, "w", encoding="utf-8") as file:
            json.dump({"invalid": "format"}, file)

        history = GameHistory()

        self.assertEqual(history.get_history(), [])


if __name__ == "__main__":
    unittest.main()