# main.py

import tkinter as tk
from gui import TicTacToeGUI


def main():
    root = tk.Tk()

    TicTacToeGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()