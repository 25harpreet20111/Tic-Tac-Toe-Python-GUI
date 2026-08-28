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
    # CLEAR HISTORY
    # ==================================================

    def clear_history(self):

        self.history = []
        self.save_history()