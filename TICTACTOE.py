import tkinter as tk
from tkinter import messagebox

def on_click(row, col):
    global current_player, board, game_over

    if board[row][col] == "" and not game_over:
        board[row][col] = current_player

        buttons[row][col].config(
            text=current_player,
            fg="#2C3E50" if current_player == "X" else "#C0392B",
            disabledforeground="#2C3E50" if current_player == "X" else "#C0392B",
            state="disabled"
        )

        if check_winner(current_player):
            highlight_winner(current_player)
            messagebox.showinfo("🏆 Game Over", f"Player {current_player} Wins!")
            end_game()

        elif is_draw():
            messagebox.showinfo("😐 Game Over", "It's a Draw!")
            end_game()

        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"✨ Player {current_player}'s Turn ✨")

def check_winner(player):
    for i in range(3):
       
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    if (board[0][0] == board[1][1] == board[2][2] == player) or \
       (board[0][2] == board[1][1] == board[2][0] == player):
        return True

    return False
def highlight_winner(player):
    for i in range(3):
        # Row highlight
        if all(board[i][j] == player for j in range(3)):
            for j in range(3):
                buttons[i][j].config(bg="#82E0AA")

        if all(board[j][i] == player for j in range(3)):
            for j in range(3):
                buttons[j][i].config(bg="#82E0AA")

    if board[0][0] == board[1][1] == board[2][2] == player:
        for i in range(3):
            buttons[i][i].config(bg="#82E0AA")

    if board[0][2] == board[1][1] == board[2][0] == player:
        buttons[0][2].config(bg="#82E0AA")
        buttons[1][1].config(bg="#82E0AA")
        buttons[2][0].config(bg="#82E0AA")

def is_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def end_game():
    global game_over
    game_over = True

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

def reset_game():
    global board, current_player, game_over

    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="#A9CCE3", state="normal")

    status_label.config(text=f"✨ Player {current_player}'s Turn ✨")
root = tk.Tk()
root.title("🎮 Tic Tac Toe - Modern Edition")
root.geometry("420x550")
root.config(bg="#EAF2F8")

header = tk.Frame(root, bg="#5DADE2", relief="raised", bd=4)
header.pack(fill="x")

title_label = tk.Label(
    header,
    text="🎮 TIC TAC TOE 🎮",
    font=("Comic Sans MS", 22, "bold"),
    bg="#5DADE2",
    fg="white",
)
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#EAF2F8")
frame.pack(pady=20)
buttons = []
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            frame,
            text="",
            font=("Comic Sans MS", 26, "bold"),
            width=4,
            height=1,
            bg="#A9CCE3",
            activebackground="#AED6F1",
            relief="flat",
            bd=5,
            highlightthickness=2,
            highlightbackground="#5DADE2",
            command=lambda r=i, c=j: on_click(r, c),
        )
        btn.grid(row=i, column=j, padx=10, pady=10)
        row.append(btn)
    buttons.append(row)
status_label = tk.Label(
    root,
    text=f"✨ Player {current_player}'s Turn ✨",
    font=("Comic Sans MS", 14, "bold"),
    bg="#EAF2F8",
    fg="#1B4F72",
)
status_label.pack(pady=15)
reset_btn = tk.Button(
    root,
    text="🔄 Restart Game",
    command=reset_game,
    bg="#58D68D",
    fg="white",
    font=("Comic Sans MS", 13, "bold"),
    relief="raised",
    bd=3,
    width=18,
)
reset_btn.pack(pady=15)

footer = tk.Label(
    root,
    text="Developed by Harpreet Kaur 💻",
    bg="#EAF2F8",
    fg="#5D6D7E",
    font=("Arial", 10, "italic"),
)
footer.pack(side="bottom", pady=10)
root.mainloop()