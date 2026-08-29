import tkinter as tk
from tkinter import messagebox

from game import TicTacToe
from ai import TicTacToeAI
from scores import ScoreManager
from history import GameHistory
import config


class TicTacToeGUI:

    def __init__(self, root):

        self.root = root

        self.game = TicTacToe()
        self.ai = TicTacToeAI("easy")
        self.score_manager = ScoreManager()
        self.history_manager = GameHistory()

        self.buttons = []

        # Current theme
        self.theme = config.CURRENT_THEME
        self.colors = self.get_theme()

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
    # THEME
    # ==================================================

    def get_theme(self):

        if self.theme == "DARK":
            return config.DARK_THEME.copy()

        return config.LIGHT_THEME.copy()

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
            value=self.theme.title()
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

    def change_theme(self, theme):

        self.theme = theme.upper()
        self.colors = self.get_theme()

        self.apply_theme()

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

        # Difficulty selector
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

        # Theme selector
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

        # Board
        self.board_frame.config(
            bg=self.colors["BACKGROUND"]
        )

        for row in range(3):

            for col in range(3):

                button = self.buttons[row][col]

                player = self.game.board[row][col]

                button.config(
                    bg=self.colors["BUTTON_BG"],
                    activebackground=self.colors["BUTTON_ACTIVE"],
                    highlightbackground=self.colors["HEADER_BG"]
                )

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
            bg="#E67E22",
            fg=self.colors["WHITE"]
        )

        # Footer
        self.footer.config(
            bg=self.colors["BACKGROUND"],
            fg=self.colors["FOOTER_COLOR"]
        )

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
    # DIFFICULTY
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

    def change_difficulty(self, difficulty):

        difficulty = difficulty.lower()

        self.ai.set_difficulty(difficulty)

        self.reset_game()

        self.status_label.config(
            text=f"🤖 AI Difficulty: {difficulty.title()}"
        )

    # ==================================================
    # BOARD
    # ==================================================

    def create_board(self):

        self.board_frame = tk.Frame(
            self.root,
            bg=self.colors["BACKGROUND"]
        )

        self.board_frame.pack(pady=15)

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

        self.status_label.pack(pady=10)

    # ==================================================
    # CONTROLS
    # ==================================================

    def create_controls(self):

        self.control_frame = tk.Frame(
            self.root,
            bg=self.colors["BACKGROUND"]
        )

        self.control_frame.pack(pady=5)

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

        self.restart_button.pack(pady=5)

        self.reset_score_button = tk.Button(
            self.control_frame,
            text="🗑️ Reset Scores",
            command=self.reset_scores,
            bg="#E67E22",
            fg=self.colors["WHITE"],
            font=("Arial", 11, "bold"),
            width=18
        )

        self.reset_score_button.pack(pady=5)
        self.statistics_button = tk.Button(
            self.control_frame,
            text="📊 Statistics",
            command=self.show_statistics,
            bg=self.colors["BUTTON_BG"],
            fg=self.colors["TEXT_COLOR"],
            font=("Arial", 11, "bold"),
            width=18
        )

        self.statistics_button.pack(pady=5)

    # ==================================================
    # FOOTER
    # ==================================================

    def create_footer(self):

        self.footer = tk.Label(
            self.root,
            text="Developed by Harpreet Kaur 💻",
            bg=self.colors["BACKGROUND"],
            fg=self.colors["FOOTER_COLOR"],
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

        self.game.make_move(row, col)

        self.update_button(row, col)

        self.check_game_status()

    # ==================================================
    # UPDATE BUTTON
    # ==================================================

    def update_button(self, row, col):

        player = self.game.board[row][col]

        color = (
            self.colors["X_COLOR"]
            if player == "X"
            else self.colors["O_COLOR"]
        )

        self.buttons[row][col].config(
            text=player,
            fg=color,
            disabledforeground=color,
            state="disabled"
        )

    # ==================================================
    # GAME STATUS
    # ==================================================

    def check_game_status(self):

        if self.game.winner == "X":

            self.highlight_winner("X")

            self.score_manager.add_win("X")

            try:
                self.history_manager.add_game(
                    "X",
                    self.difficulty_var.get(),
                    self.theme
                )
            except AttributeError:
                pass

            messagebox.showinfo(
                "🏆 Game Over",
                "Player X Wins!"
            )

            self.end_game()

        elif self.game.winner == "O":

            self.highlight_winner("O")

            self.score_manager.add_win("O")

            try:
                self.history_manager.add_game(
                    "O",
                    self.difficulty_var.get(),
                    self.theme
                )
            except AttributeError:
                pass

            messagebox.showinfo(
                "🏆 Game Over",
                "Computer Wins!"
            )

            self.end_game()

        elif self.game.winner == "Draw":

            self.score_manager.add_draw()

            try:
                self.history_manager.add_game(
                    "Draw",
                    self.difficulty_var.get(),
                    self.theme
                )
            except AttributeError:
                pass

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
    # WINNER
    # ==================================================

    def highlight_winner(self, player):

        winning_cells = self.game.get_winning_cells(player)

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
                    activebackground=self.colors["BUTTON_ACTIVE"],
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
        # ==================================================
    # SHOW STATISTICS
    # ==================================================

    def show_statistics(self):

        statistics = self.history_manager.get_statistics()
        win_rates = self.history_manager.get_win_rates()
        difficulty_stats = (
            self.history_manager.get_difficulty_statistics()
        )

        stats_window = tk.Toplevel(self.root)

        stats_window.title("📊 Game Statistics")
        stats_window.geometry("400x500")
        stats_window.resizable(False, False)

        stats_window.config(
            bg=self.colors["BACKGROUND"]
        )

        # ==================================================
        # HEADER
        # ==================================================

        header = tk.Label(
            stats_window,
            text="📊 GAME STATISTICS",
            font=("Arial", 18, "bold"),
            bg=self.colors["HEADER_BG"],
            fg=self.colors["WHITE"]
        )

        header.pack(
            fill="x",
            pady=(0, 15)
        )

        # ==================================================
        # GAME STATISTICS
        # ==================================================

        stats_frame = tk.Frame(
            stats_window,
            bg=self.colors["BACKGROUND"]
        )

        stats_frame.pack(
            fill="x",
            padx=25
        )

        labels = [
            (
                "🎮 Total Games",
                statistics["total_games"]
            ),
            (
                "❌ X Wins",
                statistics["x_wins"]
            ),
            (
                "⭕ O Wins",
                statistics["o_wins"]
            ),
            (
                "🤝 Draws",
                statistics["draws"]
            ),
        ]

        for label, value in labels:

            tk.Label(
                stats_frame,
                text=f"{label}: {value}",
                font=("Arial", 12, "bold"),
                anchor="w",
                bg=self.colors["BACKGROUND"],
                fg=self.colors["TEXT_COLOR"]
            ).pack(
                fill="x",
                pady=5
            )

        # ==================================================
        # WIN RATES
        # ==================================================

        tk.Label(
            stats_window,
            text="🏆 WIN RATES",
            font=("Arial", 14, "bold"),
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        ).pack(pady=(20, 10))

        rate_frame = tk.Frame(
            stats_window,
            bg=self.colors["BACKGROUND"]
        )

        rate_frame.pack(
            fill="x",
            padx=25
        )

        rates = [
            (
                "❌ X Win Rate",
                win_rates["x_win_rate"]
            ),
            (
                "⭕ O Win Rate",
                win_rates["o_win_rate"]
            ),
            (
                "🤝 Draw Rate",
                win_rates["draw_rate"]
            ),
        ]

        for label, value in rates:

            tk.Label(
                rate_frame,
                text=f"{label}: {value:.2f}%",
                font=("Arial", 11, "bold"),
                anchor="w",
                bg=self.colors["BACKGROUND"],
                fg=self.colors["TEXT_COLOR"]
            ).pack(
                fill="x",
                pady=3
            )

        # ==================================================
        # DIFFICULTY STATISTICS
        # ==================================================

        tk.Label(
            stats_window,
            text="🤖 GAMES BY DIFFICULTY",
            font=("Arial", 14, "bold"),
            bg=self.colors["BACKGROUND"],
            fg=self.colors["TEXT_COLOR"]
        ).pack(pady=(20, 10))

        difficulty_frame = tk.Frame(
            stats_window,
            bg=self.colors["BACKGROUND"]
        )

        difficulty_frame.pack(
            fill="x",
            padx=25
        )

        for difficulty in ["Easy", "Medium", "Hard"]:

            count = difficulty_stats.get(
                difficulty,
                0
            )

            tk.Label(
                difficulty_frame,
                text=f"{difficulty}: {count}",
                font=("Arial", 11, "bold"),
                anchor="w",
                bg=self.colors["BACKGROUND"],
                fg=self.colors["TEXT_COLOR"]
            ).pack(
                fill="x",
                pady=2
            )

        # ==================================================
        # CLOSE BUTTON
        # ==================================================

        tk.Button(
            stats_window,
            text="Close",
            command=stats_window.destroy,
            font=("Arial", 11, "bold"),
            width=15,
            bg=self.colors["BUTTON_BG"],
            fg=self.colors["TEXT_COLOR"],
            activebackground=self.colors["BUTTON_ACTIVE"]
        ).pack(
            pady=20
        )