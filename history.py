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
    # GET WIN RATES
    # ==================================================

    def get_win_rates(self):
        """Return win rates for X, O, and Draw."""

        statistics = self.get_statistics()
        total_games = statistics["total_games"]

        if total_games == 0:
            return {
                "x_win_rate": 0.0,
                "o_win_rate": 0.0,
                "draw_rate": 0.0
            }

        return {
            "x_win_rate": round(
                (statistics["x_wins"] / total_games) * 100, 2
            ),
            "o_win_rate": round(
                (statistics["o_wins"] / total_games) * 100, 2
            ),
            "draw_rate": round(
                (statistics["draws"] / total_games) * 100, 2
            )
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
    # GET DIFFICULTY STATISTICS
    # ==================================================

    def get_difficulty_statistics(self):
        """Return the number of games played at each difficulty."""

        statistics = {
            "Easy": 0,
            "Medium": 0,
            "Hard": 0
        }

        for game in self.history:
            difficulty = game.get("difficulty")

            if difficulty in statistics:
                statistics[difficulty] += 1

        return statistics
    # ==================================================
    # FILTER GAMES BY THEME
    # ==================================================

    def get_games_by_theme(self, theme):
        """Return games played with the specified theme."""

        return [
            game for game in self.history
            if game.get("theme") == theme
        ]
    
    # ==================================================
    # CLEAR HISTORY
    # ==================================================
    def clear_history(self):
        """Clear all game history."""

        self.history = []
        self.save_history()