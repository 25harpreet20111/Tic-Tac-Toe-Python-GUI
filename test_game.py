# test_game.py

import unittest

from game import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_initial_board(self):
        game = TicTacToe()

        self.assertEqual(
            game.board,
            [
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
            ]
        )

    def test_valid_move(self):
        game = TicTacToe()

        result = game.make_move(0, 0)

        self.assertTrue(result)
        self.assertEqual(game.board[0][0], "X")

    def test_invalid_move(self):
        game = TicTacToe()

        game.make_move(0, 0)

        result = game.make_move(0, 0)

        self.assertFalse(result)

    def test_x_wins(self):
        game = TicTacToe()

        game.board = [
            ["X", "X", "X"],
            ["O", "O", ""],
            ["", "", ""]
        ]

        self.assertTrue(game.check_winner("X"))

    def test_draw(self):
        game = TicTacToe()

        game.board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]

        self.assertTrue(game.is_draw())


if __name__ == "__main__":
    unittest.main()