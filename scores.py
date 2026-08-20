# scores.py


class ScoreManager:

    def __init__(self):
        self.reset_scores()

    def reset_scores(self):
        """Reset all game statistics."""

        self.scores = {
            "X": 0,
            "O": 0,
            "Draws": 0
        }

    def add_win(self, player):
        """Add a win for X or O."""

        if player in ("X", "O"):
            self.scores[player] += 1

    def add_draw(self):
        """Add a draw."""

        self.scores["Draws"] += 1

    def get_total_games(self):
        """Return total number of completed games."""

        return (
            self.scores["X"]
            + self.scores["O"]
            + self.scores["Draws"]
        )

    def get_player_win_rate(self):
        """Return Player X win percentage."""

        total_games = self.get_total_games()

        if total_games == 0:
            return 0.0

        return (
            self.scores["X"] / total_games
        ) * 100

    def get_statistics(self):
        """Return all game statistics."""

        total_games = self.get_total_games()

        return {
            "player_wins": self.scores["X"],
            "computer_wins": self.scores["O"],
            "draws": self.scores["Draws"],
            "total_games": total_games,
            "win_rate": self.get_player_win_rate()
        }