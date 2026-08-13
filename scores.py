# scores.py

import json
import os

SCORE_FILE = "scores.json"


class ScoreManager:

    def __init__(self):
        self.scores = {
            "X": 0,
            "O": 0,
            "Draws": 0
        }

        self.load_scores()

    def load_scores(self):
        if os.path.exists(SCORE_FILE):
            try:
                with open(SCORE_FILE, "r") as file:
                    self.scores = json.load(file)
            except (json.JSONDecodeError, OSError):
                pass

    def add_win(self, player):
        if player in self.scores:
            self.scores[player] += 1

        self.save_scores()

    def add_draw(self):
        self.scores["Draws"] += 1
        self.save_scores()

    def save_scores(self):
        with open(SCORE_FILE, "w") as file:
            json.dump(self.scores, file, indent=4)

    def reset_scores(self):
        self.scores = {
            "X": 0,
            "O": 0,
            "Draws": 0
        }

        self.save_scores()