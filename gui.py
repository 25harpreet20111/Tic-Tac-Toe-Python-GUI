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

        # Game objects
        self.game = TicTacToe()
        self.ai = TicTacToeAI("easy")
        self.score_manager = ScoreManager()

        # Store buttons
        self.buttons = []

        # Current theme
        self.current_theme = "Light"

        # Theme colors
        self.light_theme = {
            "BACKGROUND": "#EAF2F8",
            "HEADER_BG": "#2E8B57",
            "BUTTON_BG": "#A9CCE3",
            "BUTTON_ACTIVE": "#AED6F1",
            "TEXT_COLOR": "#1B4F72",
            "WHITE": "#FFFFFF",
            "RESET_BG": "#27AE60",
            "SECONDARY_BG": "#E67E22",
            "X_COLOR": "#2C3E50",
            "O_COLOR": "#C0392B",
            "WIN_COLOR": "#82E0AA",
            "FOOTER": "#5D6D7E"
        }

        self.dark_theme = {
            "BACKGROUND": "#17202A",
            "HEADER_BG": "#145A32",
            "BUTTON_BG": "#34495E",
            "BUTTON_ACTIVE": "#2E86C1",
            "TEXT_COLOR": "#ECF0F1",
            "WHITE": "#FFFFFF",
            "RESET_BG": "#239B56",
            "SECONDARY_BG": "#D35400",
            "X_COLOR": "#F4F6F7",
            "O_COLOR": "#FF6B6B",
            "WIN_COLOR": "#229954",
            "FOOTER": "#AAB7B8"
        }

        self.colors = self.light_theme.copy()

        # Window
        self.root.title(config.WINDOW_TITLE)

        self.root.geometry(
            f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}"
        )

        self.root.resizable(False, False)

        self.root.config(
            bg=self.colors["BACKGROUND"]
        )

        # Create UI
        self.create_header()
        self.create_scoreboard()
        self.create_difficulty_selector()
        self.create_theme_selector()
        self.create_board()
        self.create_status()
        self.create_controls()
        self.create_footer()

    # ==================================================
    # HEADER
    # ==================================================

    def create_header(self):

        self.header = tk.Frame(
            self.root,
            bg=self.colors["HEADER_BG"],
            relief="raised",
            bd=4
        )

        self.header.pack(fill="x")

        self.title_label = tk.Label(
            self.header,
            text="🎮 TIC TAC TOE 🎮",
            font=config.TITLE_FONT,
            bg=self.colors["HEADER_BG"],
            fg=self.colors["WHITE"]
        )

        self.title_label.pack(pady=10)

    # ==================================================
    # SCOREBOARD
    # ==================================================

    def create_scoreboard(self):

        self.score_frame = tk.Frame(
            self.root,
            bg=self.colors["BACKGROUND"]
        )

        self.score_frame.pack(pady=8)

        self.score_label = tk.Label(
            self.score_frame,
            text=self.get_score_text(),
            font=("Arial", 12, "bold"),
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
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

    # ==================================================
    # DIFFICULTY SELECTOR
    # ==================================================

    def create_difficulty_selector(self):

        self.difficulty_frame = tk.Frame(
            self.root,
            bg=self.colors["BACKGROUND"]
        )

        self.difficulty_frame.pack(pady=5)

        self.difficulty_label = tk.Label(
            self.difficulty_frame,
            text="🤖 AI Difficulty:",
            font=("Arial", 11, "bold"),
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        )

        self.difficulty_label.pack(
            side="left",
            padx=5
        )

        self.difficulty_var = tk.StringVar(
            value="Easy"
        )

        self.difficulty_menu = tk.OptionMenu(
            self.difficulty_frame,
            self.difficulty_var,
            "Easy",
            "Medium",
            "Hard",
            command=self.change_difficulty
        )

        self.difficulty_menu.config(
            font=("Arial", 10, "bold"),
            width=10,
            bg=self.colors["BUTTON_BG"],
            fg=self.colors["TEXT_COLOR"],
            activebackground=self.colors["BUTTON_ACTIVE"]
        )

        self.difficulty_menu["menu"].config(
            font=("Arial", 10)
        )

        self.difficulty_menu.pack(
            side="left"
        )

    # ==================================================
    # CHANGE DIFFICULTY
    # ==================================================

    def change_difficulty(self, difficulty):

        difficulty = difficulty.lower()

        # Compatible with your current AI class
        if hasattr(self.ai, "set_difficulty"):
            self.ai.set_difficulty(difficulty)
        else:
            self.ai.difficulty = difficulty

        self.reset_game()

        self.status_label.config(
            text=f"🤖 AI Difficulty: {difficulty.title()} 🤖"
        )

    # ==================================================
    # THEME SELECTOR
    # ==================================================

    def create_theme_selector(self):

        self.theme_frame = tk.Frame(
            self.root,
            bg=self.colors["BACKGROUND"]
        )

        self.theme_frame.pack(pady=5)

        self.theme_label = tk.Label(
            self.theme_frame,
            text="🎨 Theme:",
            font=("Arial", 11, "bold"),
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        )

        self.theme_label.pack(
            side="left",
            padx=5
        )

        self.theme_var = tk.StringVar(
            value="Light"
        )

        self.theme_menu = tk.OptionMenu(
            self.theme_frame,
            self.theme_var,
            "Light",
            "Dark",
            command=self.change_theme
        )

        self.theme_menu.config(
            font=("Arial", 10, "bold"),
            width=10,
            bg=self.colors["BUTTON_BG"],
            fg=self.colors["TEXT_COLOR"],
            activebackground=self.colors["BUTTON_ACTIVE"]
        )

        self.theme_menu["menu"].config(
            font=("Arial", 10)
        )

        self.theme_menu.pack(
            side="left"
        )

    # ==================================================
    # CHANGE THEME
    # ==================================================

    def change_theme(self, theme):

        self.current_theme = theme

        if theme == "Dark":
            self.colors = self.dark_theme.copy()
        else:
            self.colors = self.light_theme.copy()

        self.apply_theme()

    # ==================================================
    # APPLY THEME
    # ==================================================

    def apply_theme(self):

        # Main window
        self.root.config(
            bg=self.colors["BACKGROUND"]
        )

        # Header
        self.header.config(
            bg=self.colors["HEADER_BG"]
        )

        self.title_label.config(
            bg=self.colors["HEADER_BG"],
            fg=self.colors["WHITE"]
        )

        # Scoreboard
        self.score_frame.config(
            bg=self.colors["BACKGROUND"]
        )

        self.score_label.config(
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        )

        # Difficulty
        self.difficulty_frame.config(
            bg=self.colors["BACKGROUND"]
        )

        self.difficulty_label.config(
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        )

        self.difficulty_menu.config(
            bg=self.colors["BUTTON_BG"],
            fg=self.colors["TEXT_COLOR"],
            activebackground=self.colors["BUTTON_ACTIVE"]
        )

        # Theme
        self.theme_frame.config(
            bg=self.colors["BACKGROUND"]
        )

        self.theme_label.config(
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        )

        self.theme_menu.config(
            bg=self.colors["BUTTON_BG"],
            fg=self.colors["TEXT_COLOR"],
            activebackground=self.colors["BUTTON_ACTIVE"]
        )

        # Board buttons
        for row in range(3):

            for col in range(3):

                button = self.buttons[row][col]

                button.config(
                    bg=self.colors["BUTTON_BG"],
                    activebackground=self.colors["BUTTON_ACTIVE"],
                    highlightbackground=self.colors["HEADER_BG"]
                )

                player = self.game.board[row][col]

                if player == "X":
                    button.config(
                        fg=self.colors["X_COLOR"],
                        disabledforeground=self.colors["X_COLOR"]
                    )

                elif player == "O":
                    button.config(
                        fg=self.colors["O_COLOR"],
                        disabledforeground=self.colors["O_COLOR"]
                    )

        # Status
        self.status_label.config(
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        )

        # Controls
        self.control_frame.config(
            bg=self.colors["BACKGROUND"]
        )

        self.restart_button.config(
            bg=self.colors["RESET_BG"],
            fg=self.colors["WHITE"]
        )

        self.reset_score_button.config(
            bg=self.colors["SECONDARY_BG"],
            fg=self.colors["WHITE"]
        )

        # Footer
        self.footer.config(
            bg=self.colors["BACKGROUND"],
            fg=self.colors["FOOTER"]
        )

    # ==================================================
    # GAME BOARD
    # ==================================================

    def create_board(self):

        self.board_frame = tk.Frame(
            self.root,
            bg=self.colors["BACKGROUND"]
        )

        self.board_frame.pack(
            pady=15
        )

        for row in range(3):

            button_row = []

            for col in range(3):

                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=config.BUTTON_FONT,
                    width=4,
                    height=1,
                    bg=self.colors["BUTTON_BG"],
                    activebackground=self.colors["BUTTON_ACTIVE"],
                    relief="flat",
                    bd=5,
                    highlightthickness=2,
                    highlightbackground=self.colors["HEADER_BG"],
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

    # ==================================================
    # STATUS
    # ==================================================

    def create_status(self):

        self.status_label = tk.Label(
            self.root,
            text="✨ Player X's Turn ✨",
            font=config.STATUS_FONT,
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        )

        self.status_label.pack(
            pady=10
        )

    # ==================================================
    # CONTROLS
    # ==================================================

    def create_controls(self):

        self.control_frame = tk.Frame(
            self.root,
            bg=self.colors["BACKGROUND"]
        )

        self.control_frame.pack(
            pady=5
        )

        self.restart_button = tk.Button(
            self.control_frame,
            text="🔄 Restart Game",
            command=self.reset_game,
            bg=self.colors["RESET_BG"],
            fg=self.colors["WHITE"],
            font=config.RESET_FONT,
            relief="raised",
            bd=3,
            width=18
        )

        self.restart_button.pack(
            pady=5
        )

        self.reset_score_button = tk.Button(
            self.control_frame,
            text="🗑️ Reset Scores",
            command=self.reset_scores,
            bg=self.colors["SECONDARY_BG"],
            fg=self.colors["WHITE"],
            font=("Arial", 11, "bold"),
            width=18
        )

        self.reset_score_button.pack(
            pady=5
        )

    # ==================================================
    # FOOTER
    # ==================================================

    def create_footer(self):

        self.footer = tk.Label(
            self.root,
            text="Developed by Harpreet Kaur 💻",
            bg=self.colors["BACKGROUND"],
            fg=self.colors["FOOTER"],
            font=config.FOOTER_FONT
        )

        self.footer.pack(
            side="bottom",
            pady=10
        )

    # ==================================================
    # PLAYER MOVE
    # ==================================================

    def player_move(self, row, col):

        if self.game.game_over:
            return

        if self.game.current_player != "X":
            return

        if not self.game.make_move(row, col):
            return

        self.update_button(
            row,
            col
        )

        self.check_game_status()

        if not self.game.game_over:

            self.status_label.config(
                text="🤖 Computer's Turn (O) 🤖"
            )

            self.root.after(
                400,
                self.computer_move
            )

    # ==================================================
    # COMPUTER MOVE
    # ==================================================

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

        self.game.make_move(
            row,
            col
        )

        self.update_button(
            row,
            col
        )

        self.check_game_status()

    # ==================================================
    # UPDATE BUTTON
    # ==================================================

    def update_button(self, row, col):

        player = self.game.board[row][col]

        if player == "X":
            color = self.colors["X_COLOR"]
        else:
            color = self.colors["O_COLOR"]

        self.buttons[row][col].config(
            text=player,
            fg=color,
            disabledforeground=color,
            state="disabled"
        )

    # ==================================================
    # CHECK GAME STATUS
    # ==================================================

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

    # ==================================================
    # WINNER HIGHLIGHT
    # ==================================================

    def highlight_winner(self, player):

        winning_cells = self.game.get_winning_cells(
            player
        )

        for row, col in winning_cells:

            self.buttons[row][col].config(
                bg=self.colors["WIN_COLOR"]
            )

    # ==================================================
    # END GAME
    # ==================================================

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

    # ==================================================
    # RESET GAME
    # ==================================================

    def reset_game(self):

        self.game.reset()

        for row in range(3):

            for col in range(3):

                self.buttons[row][col].config(
                    text="",
                    bg=self.colors["BUTTON_BG"],
                    state="normal"
                )

        self.status_label.config(
            text="✨ Your Turn (X) ✨"
        )

    # ==================================================
    # RESET SCORES
    # ==================================================

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