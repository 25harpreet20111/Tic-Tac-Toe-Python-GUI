# game.py


class TicTacToe:

    def __init__(self):
        self.reset()

    def reset(self):
        """Reset the board and start a new game."""

        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.current_player = "X"
        self.winner = None
        self.game_over = False

    def make_move(self, row, col):
        """Make a move for the current player."""

        # Game already finished
        if self.game_over:
            return False

        # Cell already occupied
        if self.board[row][col] != "":
            return False

        # Place player's mark
        self.board[row][col] = self.current_player

        # Check winner
        if self.check_winner(self.current_player):
            self.winner = self.current_player
            self.game_over = True
            return True

        # Check draw
        if self.is_draw():
            self.winner = "Draw"
            self.game_over = True
            return True

        # Switch player
        self.current_player = (
            "O" if self.current_player == "X" else "X"
        )

        return True

    def check_winner(self, player):
        """Check whether the given player has won."""

        # Rows
        for row in range(3):
            if all(
                self.board[row][col] == player
                for col in range(3)
            ):
                return True

        # Columns
        for col in range(3):
            if all(
                self.board[row][col] == player
                for row in range(3)
            ):
                return True

        # Main diagonal
        if all(
            self.board[i][i] == player
            for i in range(3)
        ):
            return True

        # Other diagonal
        if all(
            self.board[i][2 - i] == player
            for i in range(3)
        ):
            return True

        return False

    def get_winning_cells(self, player):
        """Return the cells that form the winning combination."""

        # Rows
        for row in range(3):
            if all(
                self.board[row][col] == player
                for col in range(3)
            ):
                return [
                    (row, 0),
                    (row, 1),
                    (row, 2)
                ]

        # Columns
        for col in range(3):
            if all(
                self.board[row][col] == player
                for row in range(3)
            ):
                return [
                    (0, col),
                    (1, col),
                    (2, col)
                ]

        # Main diagonal
        if all(
            self.board[i][i] == player
            for i in range(3)
        ):
            return [
                (0, 0),
                (1, 1),
                (2, 2)
            ]

        # Other diagonal
        if all(
            self.board[i][2 - i] == player
            for i in range(3)
        ):
            return [
                (0, 2),
                (1, 1),
                (2, 0)
            ]

        return []

    def is_board_full(self):
        """Check whether all cells are occupied."""

        return all(
            self.board[row][col] != ""
            for row in range(3)
            for col in range(3)
        )

    def is_draw(self):
        """Check whether the current game is a draw."""

        return (
            self.is_board_full()
            and not self.check_winner("X")
            and not self.check_winner("O")
        )