# gui.py

import tkinter as tk
from tkinter import messagebox

from game import TicTacToe
from ai import TicTacToeAI
from scores import ScoreManager
import config


class TicTacToeGUI:

    def __init__(self, root):

        self.root = root

        self.game = TicTacToe()

        self.ai = TicTacToeAI("easy")

        self.score_manager = ScoreManager()

        self.buttons = []

        self.root.title(config.WINDOW_TITLE)

        self.root.geometry(
            f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}"
        )

        self.root.resizable(False, False)

        self.root.config(bg=config.BACKGROUND)

        self.create_header()
        self.create_scoreboard()
        self.create_difficulty_selector()
        self.create_board()
        self.create_status()
        self.create_controls()
        self.create_footer()

    # --------------------------------------------------
    # HEADER
    # --------------------------------------------------

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg=config.HEADER_BG,
            relief="raised",
            bd=4
        )

        header.pack(fill="x")

        title = tk.Label(
            header,
            text="🎮 TIC TAC TOE 🎮",
            font=config.TITLE_FONT,
            bg=config.HEADER_BG,
            fg=config.WHITE
        )

        title.pack(pady=10)

    # --------------------------------------------------
    # SCOREBOARD
    # --------------------------------------------------

    def create_scoreboard(self):

        score_frame = tk.Frame(
            self.root,
            bg=config.BACKGROUND
        )

        score_frame.pack(pady=8)

        self.score_label = tk.Label(
            score_frame,
            text=self.get_score_text(),
            font=("Arial", 12, "bold"),
            bg=config.BACKGROUND,
            fg=config.TEXT_COLOR
        )

        self.score_label.pack()

    def get_score_text(self):

         stats = self.score_manager.get_statistics()

         return (
        f"❌ X: {stats['player_wins']}     "
        f"⭕ O: {stats['computer_wins']}     "
        f"😐 Draws: {stats['draws']}     "
        f"🎮 Games: {stats['total_games']}     "
        f"🏆 Win Rate: {stats['win_rate']:.1f}%"
    )

    # --------------------------------------------------
    # DIFFICULTY SELECTOR
    # --------------------------------------------------

    def create_difficulty_selector(self):

        difficulty_frame = tk.Frame(
            self.root,
            bg=config.BACKGROUND
        )

        difficulty_frame.pack(pady=5)

        label = tk.Label(
            difficulty_frame,
            text="🤖 AI Difficulty:",
            font=("Arial", 11, "bold"),
            bg=config.BACKGROUND,
            fg=config.TEXT_COLOR
        )

        label.pack(side="left", padx=5)

        self.difficulty_var = tk.StringVar(
            value="Easy"
        )

        difficulty_menu = tk.OptionMenu(
            difficulty_frame,
            self.difficulty_var,
            "Easy",
            "Medium",
            "Hard",
            command=self.change_difficulty
        )

        difficulty_menu.config(
            font=("Arial", 10, "bold"),
            width=10,
            bg=config.BUTTON_BG,
            fg=config.TEXT_COLOR,
            activebackground=config.BUTTON_ACTIVE
        )

        difficulty_menu["menu"].config(
            font=("Arial", 10)
        )

        difficulty_menu.pack(side="left")

    def change_difficulty(self, difficulty):

        difficulty = difficulty.lower()

        self.ai.set_difficulty(difficulty)

        self.reset_game()

        self.status_label.config(
            text=f"🤖 AI Difficulty: {difficulty.title()}"
        )

    # --------------------------------------------------
    # GAME BOARD
    # --------------------------------------------------

    def create_board(self):

        frame = tk.Frame(
            self.root,
            bg=config.BACKGROUND
        )

        frame.pack(pady=15)

        for row in range(3):

            button_row = []

            for col in range(3):

                button = tk.Button(
                    frame,
                    text="",
                    font=config.BUTTON_FONT,
                    width=4,
                    height=1,
                    bg=config.BUTTON_BG,
                    activebackground=config.BUTTON_ACTIVE,
                    relief="flat",
                    bd=5,
                    highlightthickness=2,
                    highlightbackground=config.HEADER_BG,
                    command=lambda r=row, c=col:
                    self.player_move(r, c)
                )

                button.grid(
                    row=row,
                    column=col,
                    padx=10,
                    pady=10
                )

                button_row.append(button)

            self.buttons.append(button_row)

    # --------------------------------------------------
    # STATUS
    # --------------------------------------------------

    def create_status(self):

        self.status_label = tk.Label(
            self.root,
            text="✨ Player X's Turn ✨",
            font=config.STATUS_FONT,
            bg=config.BACKGROUND,
            fg=config.TEXT_COLOR
        )

        self.status_label.pack(pady=10)

    # --------------------------------------------------
    # CONTROLS
    # --------------------------------------------------

    def create_controls(self):

        control_frame = tk.Frame(
            self.root,
            bg=config.BACKGROUND
        )

        control_frame.pack(pady=5)

        restart_button = tk.Button(
            control_frame,
            text="🔄 Restart Game",
            command=self.reset_game,
            bg=config.RESET_BG,
            fg=config.WHITE,
            font=config.RESET_FONT,
            relief="raised",
            bd=3,
            width=18
        )

        restart_button.pack(pady=5)

        reset_score_button = tk.Button(
            control_frame,
            text="🗑️ Reset Scores",
            command=self.reset_scores,
            bg="#E67E22",
            fg=config.WHITE,
            font=("Arial", 11, "bold"),
            width=18
        )

        reset_score_button.pack(pady=5)

    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------

    def create_footer(self):

        footer = tk.Label(
            self.root,
            text="Developed by Harpreet Kaur 💻",
            bg=config.BACKGROUND,
            fg="#5D6D7E",
            font=config.FOOTER_FONT
        )

        footer.pack(
            side="bottom",
            pady=10
        )

    # --------------------------------------------------
    # PLAYER MOVE
    # --------------------------------------------------

    def player_move(self, row, col):

        if self.game.game_over:
            return

        if self.game.current_player != "X":
            return

        if not self.game.make_move(row, col):
            return

        self.update_button(row, col)

        self.check_game_status()

        if not self.game.game_over:

            self.status_label.config(
                text="🤖 Computer's Turn (O) 🤖"
            )

            self.root.after(
                400,
                self.computer_move
            )

    # --------------------------------------------------
    # COMPUTER MOVE
    # --------------------------------------------------

    def computer_move(self):

        if self.game.game_over:
            return

        if self.game.current_player != "O":
            return

        move = self.ai.get_move(
            self.game.board
        )

        if move is None:
            return

        row, col = move

        self.game.make_move(row, col)

        self.update_button(row, col)

        self.check_game_status()

    # --------------------------------------------------
    # UPDATE BUTTON
    # --------------------------------------------------

    def update_button(self, row, col):

        player = self.game.board[row][col]

        color = (
            config.X_COLOR
            if player == "X"
            else config.O_COLOR
        )

        self.buttons[row][col].config(
            text=player,
            fg=color,
            disabledforeground=color,
            state="disabled"
        )

    # --------------------------------------------------
    # CHECK GAME STATUS
    # --------------------------------------------------

    def check_game_status(self):

        if self.game.winner == "X":

            self.highlight_winner("X")

            self.score_manager.add_win("X")

            messagebox.showinfo(
                "🏆 Game Over",
                "Player X Wins!"
            )

            self.end_game()

        elif self.game.winner == "O":

            self.highlight_winner("O")

            self.score_manager.add_win("O")

            messagebox.showinfo(
                "🏆 Game Over",
                "Computer Wins!"
            )

            self.end_game()

        elif self.game.winner == "Draw":

            self.score_manager.add_draw()

            messagebox.showinfo(
                "😐 Game Over",
                "It's a Draw!"
            )

            self.end_game()

        else:

            player = self.game.current_player

            if player == "X":

                self.status_label.config(
                    text="✨ Your Turn (X) ✨"
                )

            else:

                self.status_label.config(
                    text="🤖 Computer's Turn (O) 🤖"
                )

    # --------------------------------------------------
    # WINNER HIGHLIGHT
    # --------------------------------------------------

    def highlight_winner(self, player):

        winning_cells = (
            self.game.get_winning_cells(player)
        )

        for row, col in winning_cells:

            self.buttons[row][col].config(
                bg=config.WIN_COLOR
            )

    # --------------------------------------------------
    # END GAME
    # --------------------------------------------------

    def end_game(self):

        self.score_label.config(
            text=self.get_score_text()
        )

        for row in range(3):

            for col in range(3):

                self.buttons[row][col].config(
                    state="disabled"
                )

        self.status_label.config(
            text="🎮 Game Over — Press Restart Game"
        )

    # --------------------------------------------------
    # RESET GAME
    # --------------------------------------------------

    def reset_game(self):

        self.game.reset()

        for row in range(3):

            for col in range(3):

                self.buttons[row][col].config(
                    text="",
                    bg=config.BUTTON_BG,
                    state="normal"
                )

        self.status_label.config(
            text="✨ Your Turn (X) ✨"
        )

    # --------------------------------------------------
    # RESET SCORES
    # --------------------------------------------------

    def reset_scores(self):

        answer = messagebox.askyesno(
            "Reset Scores",
            "Are you sure you want to reset all scores?"
        )

        if answer:

            self.score_manager.reset_scores()

            self.score_label.config(
                text=self.get_score_text()
            )

            messagebox.showinfo(
                "Scores Reset",
                "All scores have been reset."
            )