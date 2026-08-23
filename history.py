# history.py

import json
import os
from datetime import datetime


class GameHistory:

    def __init__(self, filename="game_history.json"):

        self.filename = filename
        self.history = []

        self.load_history()

    # ==================================================
    # LOAD HISTORY
    # ==================================================

    def load_history(self):

        if not os.path.exists(self.filename):

            self.history = []

            return

        try:

            with open(
                self.filename,
                "r",
                encoding="utf-8"
            ) as file:

                self.history = json.load(file)

        except (json.JSONDecodeError, OSError):

            self.history = []

    # ==================================================
    # SAVE HISTORY
    # ==================================================

    def save_history(self):

        try:

            with open(
                self.filename,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.history,
                    file,
                    indent=4
                )

        except OSError:

            pass

    # ==================================================
    # ADD GAME
    # ==================================================

    def add_game(
        self,
        result,
        difficulty,
        theme
    ):

        game_record = {

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "result": result,

            "difficulty": difficulty,

            "theme": theme
        }

        self.history.append(game_record)

        self.save_history()

    # ==================================================
    # GET HISTORY
    # ==================================================

    def get_history(self):

        return self.history

    # ==================================================
    # CLEAR HISTORY
    # ==================================================

    def clear_history(self):

        self.history = []

        self.save_history()

    # ==================================================
    # GET TOTAL GAMES
    # ==================================================

    def get_total_games(self):

        return len(self.history)