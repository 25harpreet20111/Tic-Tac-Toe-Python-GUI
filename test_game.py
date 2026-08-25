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

        self.assertEqual(game.current_player, "X")
        self.assertIsNone(game.winner)
        self.assertFalse(game.game_over)

    def test_valid_move(self):
        game = TicTacToe()

        result = game.make_move(0, 0)

        self.assertTrue(result)
        self.assertEqual(game.board[0][0], "X")
        self.assertEqual(game.current_player, "O")

    def test_invalid_move(self):
        game = TicTacToe()

        game.make_move(0, 0)

        result = game.make_move(0, 0)

        self.assertFalse(result)
        self.assertEqual(game.board[0][0], "X")

    def test_x_wins(self):
        game = TicTacToe()

        game.board = [
            ["X", "X", "X"],
            ["O", "O", ""],
            ["", "", ""]
        ]

        self.assertTrue(game.check_winner("X"))

    def test_o_wins(self):
        game = TicTacToe()

        game.board = [
            ["O", "X", ""],
            ["O", "X", ""],
            ["O", "", ""]
        ]

        self.assertTrue(game.check_winner("O"))

    def test_diagonal_win(self):
        game = TicTacToe()

        game.board = [
            ["X", "O", ""],
            ["O", "X", ""],
            ["", "", "X"]
        ]

        self.assertTrue(game.check_winner("X"))

    def test_no_winner(self):
        game = TicTacToe()

        game.board = [
            ["X", "O", "X"],
            ["X", "O", ""],
            ["", "", ""]
        ]

        self.assertFalse(game.check_winner("X"))
        self.assertFalse(game.check_winner("O"))

    def test_draw(self):
        game = TicTacToe()

        game.board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]

        self.assertTrue(game.is_draw())

    def test_board_not_full(self):
        game = TicTacToe()

        game.board = [
            ["X", "O", "X"],
            ["X", "O", ""],
            ["O", "X", "X"]
        ]

        self.assertFalse(game.is_board_full())
        self.assertFalse(game.is_draw())

    def test_reset(self):
        game = TicTacToe()

        game.make_move(0, 0)
        game.reset()

        self.assertEqual(
            game.board,
            [
                ["", "", ""],
                ["", "", ""],
                ["", "", ""]
            ]
        )

        self.assertEqual(game.current_player, "X")
        self.assertIsNone(game.winner)
        self.assertFalse(game.game_over)

    def test_winning_cells(self):
        game = TicTacToe()

        game.board = [
            ["X", "X", "X"],
            ["O", "O", ""],
            ["", "", ""]
        ]

        expected = [
            (0, 0),
            (0, 1),
            (0, 2)
        ]

        self.assertEqual(
            game.get_winning_cells("X"),
            expected
        )

    def test_game_over_after_win(self):
        game = TicTacToe()

        game.board = [
            ["X", "X", ""],
            ["O", "O", ""],
            ["", "", ""]
        ]

        game.current_player = "X"

        game.make_move(0, 2)

        self.assertEqual(game.winner, "X")
        self.assertTrue(game.game_over)

        # No additional move should be allowed
        self.assertFalse(game.make_move(2, 2))
    def test_out_of_bounds_move(self):
        game = TicTacToe()

        self.assertFalse(game.make_move(-1, 0))
        self.assertFalse(game.make_move(3, 0))
        self.assertFalse(game.make_move(0, 3))
        self.assertFalse(game.make_move(0, -1))

if __name__ == "__main__":
    unittest.main()