# ai.py

import random


class TicTacToeAI:

    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty

    def get_move(self, board):
        empty_cells = [
            (row, col)
            for row in range(3)
            for col in range(3)
            if board[row][col] == ""
        ]

        if not empty_cells:
            return None

        if self.difficulty == "easy":
            return random.choice(empty_cells)

        if self.difficulty == "hard":
            return self.best_move(board)

        return random.choice(empty_cells)

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
        if self.check_winner(board, "O"):
            return 1

        if self.check_winner(board, "X"):
            return -1

        if self.is_full(board):
            return 0

        if maximizing:
            best_score = float("-inf")

            for row, col in self.get_empty_cells(board):
                board[row][col] = "O"
                score = self.minimax(board, False)
                board[row][col] = ""
                best_score = max(best_score, score)

            return best_score

        best_score = float("inf")

        for row, col in self.get_empty_cells(board):
            board[row][col] = "X"
            score = self.minimax(board, True)
            board[row][col] = ""
            best_score = min(best_score, score)

        return best_score

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
        for row in board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True

        if all(board[i][i] == player for i in range(3)):
            return True

        if all(board[i][2 - i] == player for i in range(3)):
            return True

        return False