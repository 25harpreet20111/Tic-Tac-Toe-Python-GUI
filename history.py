# history.py

import json
import os
from datetime import datetime


class GameHistory:

    FILE_NAME = "game_history.json"

    def __init__(self):
        self.history = []
        self.load_history()

    # ==================================================
    # LOAD HISTORY
    # ==================================================

    def load_history(self):
        """Load saved game history from the JSON file."""

        if not os.path.exists(self.FILE_NAME):
            self.history = []
            return

        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, list):
                self.history = data
            else:
                self.history = []

        except (json.JSONDecodeError, OSError):
            self.history = []

    # ==================================================
    # ADD GAME
    # ==================================================

    def add_game(self, result, difficulty, theme):

        game = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "result": result,
            "difficulty": difficulty,
            "theme": theme
        }

        self.history.append(game)

        self.save_history()

    # ==================================================
    # SAVE HISTORY
    # ==================================================

    def save_history(self):

        try:
            with open(self.FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(
                    self.history,
                    file,
                    indent=4
                )

        except OSError:
            pass

    # ==================================================
    # GET HISTORY
    # ==================================================

    def get_history(self):

        return self.history.copy()

    # ==================================================
    # GET STATISTICS
    # ==================================================

    def get_statistics(self):
        """Return summary statistics for recorded games."""

        total_games = len(self.history)
        x_wins = 0
        o_wins = 0
        draws = 0

        for game in self.history:
            result = game.get("result")

            if result == "X":
                x_wins += 1
            elif result == "O":
                o_wins += 1
            elif result == "Draw":
                draws += 1

        return {
            "total_games": total_games,
            "x_wins": x_wins,
            "o_wins": o_wins,
            "draws": draws
        }
    # ==================================================
    # FILTER GAMES BY RESULT
    # ==================================================

    def get_games_by_result(self, result):
        """Return games matching the specified result."""

        return [
            game for game in self.history
            if game.get("result") == result
        ]
    # ==================================================
    # FILTER GAMES BY DIFFICULTY
    # ==================================================
    def get_games_by_difficulty(self, difficulty):
        """Return games played at the specified difficulty."""

        return [
            game for game in self.history
            if game.get("difficulty") == difficulty
        ]
    # ==================================================
    # CLEAR HISTORY
    # ==================================================
    def clear_history(self):
        """Clear all game history."""

        self.history = []
        self.save_history()