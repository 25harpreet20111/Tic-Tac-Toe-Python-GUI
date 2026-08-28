# test_history.py

import unittest
import os
import json

from history import GameHistory


class TestGameHistory(unittest.TestCase):

    TEST_FILE = "test_game_history.json"

    def setUp(self):
        """Prepare a clean test environment."""

        self.original_file = GameHistory.FILE_NAME
        GameHistory.FILE_NAME = self.TEST_FILE

        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

        self.history = GameHistory()

    def tearDown(self):
        """Clean up the test file after each test."""

        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

        GameHistory.FILE_NAME = self.original_file

    # ==================================================
    # INITIAL HISTORY
    # ==================================================

    def test_initial_history_is_empty(self):
        self.assertEqual(
            self.history.get_history(),
            []
        )

    # ==================================================
    # ADD GAME
    # ==================================================

    def test_add_game(self):
        self.history.add_game(
            "X",
            "Easy",
            "LIGHT"
        )

        records = self.history.get_history()

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["result"], "X")
        self.assertEqual(records[0]["difficulty"], "Easy")
        self.assertEqual(records[0]["theme"], "LIGHT")
        self.assertIn("date", records[0])

    def test_multiple_games(self):
        self.history.add_game(
            "X",
            "Easy",
            "LIGHT"
        )

        self.history.add_game(
            "O",
            "Hard",
            "DARK"
        )

        self.history.add_game(
            "Draw",
            "Medium",
            "LIGHT"
        )

        records = self.history.get_history()

        self.assertEqual(len(records), 3)
        self.assertEqual(records[1]["result"], "O")
        self.assertEqual(records[2]["result"], "Draw")

    # ==================================================
    # FILE STORAGE
    # ==================================================

    def test_history_is_saved_to_file(self):
        self.history.add_game(
            "X",
            "Easy",
            "LIGHT"
        )

        self.assertTrue(
            os.path.exists(self.TEST_FILE)
        )

        with open(
            self.TEST_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["result"], "X")

    def test_history_persists_after_reload(self):
        self.history.add_game(
            "X",
            "Easy",
            "LIGHT"
        )

        new_history = GameHistory()

        records = new_history.get_history()

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["result"], "X")
        self.assertEqual(
            records[0]["difficulty"],
            "Easy"
        )
        self.assertEqual(
            records[0]["theme"],
            "LIGHT"
        )

    # ==================================================
    # CLEAR HISTORY
    # ==================================================

    def test_clear_history(self):
        self.history.add_game(
            "X",
            "Easy",
            "LIGHT"
        )

        self.history.add_game(
            "O",
            "Hard",
            "DARK"
        )

        self.history.clear_history()

        self.assertEqual(
            self.history.get_history(),
            []
        )

    # ==================================================
    # INVALID HISTORY
    # ==================================================

    def test_invalid_history_format(self):
        with open(
            self.TEST_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                {"invalid": "format"},
                file
            )

        history = GameHistory()

        self.assertEqual(
            history.get_history(),
            []
        )

    # ==================================================
    # STATISTICS
    # ==================================================

    def test_get_statistics(self):
        """Test game history statistics."""

        self.history.add_game(
            "X",
            "Easy",
            "Light"
        )

        self.history.add_game(
            "O",
            "Hard",
            "Dark"
        )

        self.history.add_game(
            "Draw",
            "Medium",
            "Light"
        )

        self.history.add_game(
            "X",
            "Easy",
            "Dark"
        )

        statistics = self.history.get_statistics()

        self.assertEqual(
            statistics["total_games"],
            4
        )

        self.assertEqual(
            statistics["x_wins"],
            2
        )

        self.assertEqual(
            statistics["o_wins"],
            1
        )

        self.assertEqual(
            statistics["draws"],
            1
        )

    # ==================================================
    # FILTER BY RESULT
    # ==================================================

    def test_get_games_by_result(self):
        """Test filtering games by result."""

        self.history.add_game(
            "X",
            "Easy",
            "Light"
        )

        self.history.add_game(
            "O",
            "Hard",
            "Dark"
        )

        self.history.add_game(
            "X",
            "Medium",
            "Light"
        )

        self.history.add_game(
            "Draw",
            "Easy",
            "Dark"
        )

        x_games = self.history.get_games_by_result("X")
        o_games = self.history.get_games_by_result("O")
        draw_games = self.history.get_games_by_result("Draw")

        self.assertEqual(
            len(x_games),
            2
        )

        self.assertEqual(
            len(o_games),
            1
        )

        self.assertEqual(
            len(draw_games),
            1
        )

        self.assertEqual(
            x_games[0]["result"],
            "X"
        )

        self.assertEqual(
            x_games[1]["result"],
            "X"
        )

    # ==================================================
    # FILTER BY DIFFICULTY
    # ==================================================

    def test_get_games_by_difficulty(self):
        """Test filtering games by difficulty."""

        self.history.add_game(
            "X",
            "Easy",
            "Light"
        )

        self.history.add_game(
            "O",
            "Hard",
            "Dark"
        )

        self.history.add_game(
            "X",
            "Easy",
            "Light"
        )

        self.history.add_game(
            "Draw",
            "Medium",
            "Dark"
        )

        easy_games = self.history.get_games_by_difficulty(
            "Easy"
        )

        hard_games = self.history.get_games_by_difficulty(
            "Hard"
        )

        medium_games = self.history.get_games_by_difficulty(
            "Medium"
        )

        self.assertEqual(
            len(easy_games),
            2
        )

        self.assertEqual(
            len(hard_games),
            1
        )

        self.assertEqual(
            len(medium_games),
            1
        )

        self.assertEqual(
            easy_games[0]["difficulty"],
            "Easy"
        )

        self.assertEqual(
            easy_games[1]["difficulty"],
            "Easy"
        )
    # ==================================================
    # FILTER GAMES BY THEME
    # ==================================================

    def test_get_games_by_theme(self):
        """Test filtering games by theme."""

        self.history.add_game(
            "X",
            "Easy",
            "Light"
        )

        self.history.add_game(
            "O",
            "Hard",
            "Dark"
        )

        self.history.add_game(
            "X",
            "Medium",
            "Light"
        )

        self.history.add_game(
            "Draw",
            "Easy",
            "Dark"
        )

        light_games = self.history.get_games_by_theme("Light")
        dark_games = self.history.get_games_by_theme("Dark")

        self.assertEqual(
            len(light_games),
            2
        )

        self.assertEqual(
            len(dark_games),
            2
        )

        self.assertEqual(
            light_games[0]["theme"],
            "Light"
        )

        self.assertEqual(
            light_games[1]["theme"],
            "Light"
        )

        self.assertEqual(
            dark_games[0]["theme"],
            "Dark"
        )

        self.assertEqual(
            dark_games[1]["theme"],
            "Dark"
        )

    def test_get_difficulty_statistics(self):
        """Test difficulty-based game statistics."""

        self.history.add_game("X", "Easy", "Light")
        self.history.add_game("O", "Hard", "Dark")
        self.history.add_game("X", "Easy", "Light")
        self.history.add_game("Draw", "Medium", "Dark")
        self.history.add_game("O", "Hard", "Light")

        statistics = self.history.get_difficulty_statistics()

        self.assertEqual(statistics["Easy"], 2)
        self.assertEqual(statistics["Medium"], 1)
        self.assertEqual(statistics["Hard"], 2)
if __name__ == "__main__":
    unittest.main()