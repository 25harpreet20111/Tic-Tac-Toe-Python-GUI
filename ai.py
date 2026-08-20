# ai.py

import random


class TicTacToeAI:

    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty.lower()

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty.lower()

    def get_move(self, board):
        empty_cells = self.get_empty_cells(board)

        if not empty_cells:
            return None

        # Easy: completely random move
        if self.difficulty == "easy":
            return random.choice(empty_cells)

        # Medium: try to win, block player, otherwise random
        if self.difficulty == "medium":
            return self.medium_move(board)

        # Hard: optimal Minimax move
        if self.difficulty == "hard":
            return self.best_move(board)

        return random.choice(empty_cells)

    # --------------------------------------------------
    # MEDIUM AI
    # --------------------------------------------------

    def medium_move(self, board):

        empty_cells = self.get_empty_cells(board)

        # 1. Check whether computer can win
        for row, col in empty_cells:
            board[row][col] = "O"

            if self.check_winner(board, "O"):
                board[row][col] = ""
                return row, col

            board[row][col] = ""

        # 2. Block the player from winning
        for row, col in empty_cells:
            board[row][col] = "X"

            if self.check_winner(board, "X"):
                board[row][col] = ""
                return row, col

            board[row][col] = ""

        # 3. Take center if available
        if board[1][1] == "":
            return 1, 1

        # 4. Take a corner
        corners = [
            (0, 0),
            (0, 2),
            (2, 0),
            (2, 2)
        ]

        available_corners = [
            corner
            for corner in corners
            if board[corner[0]][corner[1]] == ""
        ]

        if available_corners:
            return random.choice(available_corners)

        # 5. Otherwise choose randomly
        return random.choice(empty_cells)

    # --------------------------------------------------
    # HARD AI - MINIMAX
    # --------------------------------------------------

    def best_move(self, board):

        best_score = float("-inf")
        move = None

        for row, col in self.get_empty_cells(board):

            board[row][col] = "O"

            score = self.minimax(board, False)

            board[row][col] = ""

            if score > best_score:
                best_score = score
                move = (row, col)

        return move

    def minimax(self, board, maximizing):

        # Computer wins
        if self.check_winner(board, "O"):
            return 1

        # Player wins
        if self.check_winner(board, "X"):
            return -1

        # Draw
        if self.is_full(board):
            return 0

        # Computer's turn
        if maximizing:

            best_score = float("-inf")

            for row, col in self.get_empty_cells(board):

                board[row][col] = "O"

                score = self.minimax(board, False)

                board[row][col] = ""

                best_score = max(best_score, score)

            return best_score

        # Player's turn
        best_score = float("inf")

        for row, col in self.get_empty_cells(board):

            board[row][col] = "X"

            score = self.minimax(board, True)

            board[row][col] = ""

            best_score = min(best_score, score)

        return best_score

    # --------------------------------------------------
    # HELPER METHODS
    # --------------------------------------------------

    def get_empty_cells(self, board):

        return [
            (row, col)
            for row in range(3)
            for col in range(3)
            if board[row][col] == ""
        ]

    def is_full(self, board):

        return all(
            board[row][col] != ""
            for row in range(3)
            for col in range(3)
        )

    def check_winner(self, board, player):

        # Rows
        for row in board:
            if all(cell == player for cell in row):
                return True

        # Columns
        for col in range(3):
            if all(
                board[row][col] == player
                for row in range(3)
            ):
                return True

        # Main diagonal
        if all(
            board[i][i] == player
            for i in range(3)
        ):
            return True

        # Anti-diagonal
        if all(
            board[i][2 - i] == player
            for i in range(3)
        ):
            return True

        return False