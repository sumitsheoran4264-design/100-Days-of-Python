"""
Simple hill climbing game with a graphical interface.

Use the arrow buttons or keyboard arrows to move left and right.
Reach the top without stepping on a dangerous tile.
"""

import random
import tkinter as tk
from tkinter import messagebox

WIDTH = 9
HEIGHT = 10
SAFE = "O"
DANGEROUS = "X"
PLAYER = "P"
EMPTY = " "
CELL_SIZE = 42
CELL_FONT = ("Courier", 16, "bold")


def generate_hill(width, height, difficulty=0.25):
    hill = []
    for row in range(height):
        line = []
        for col in range(width):
            if row == height - 1:
                line.append(SAFE)
            else:
                line.append(SAFE if random.random() > difficulty else DANGEROUS)
        hill.append(line)
    return hill


def move_player(player_x, direction):
    if direction == "l":
        return max(0, player_x - 1)
    if direction == "r":
        return min(WIDTH - 1, player_x + 1)
    return player_x


class HillClimbingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hill Climbing Game")
        self.resizable(False, False)
        self.bind("<Left>", lambda event: self.handle_move("l"))
        self.bind("<Right>", lambda event: self.handle_move("r"))
        self.bind("<q>", lambda event: self.quit())

        self.hill = generate_hill(WIDTH, HEIGHT)
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT - 1

        self.status_label = tk.Label(self, text="Reach the top of the hill!", font=("Arial", 12))
        self.status_label.grid(row=0, column=0, columnspan=WIDTH, pady=(10, 0))

        self.grid_frame = tk.Frame(self, padx=10, pady=10)
        self.grid_frame.grid(row=1, column=0, columnspan=WIDTH)

        self.cell_labels = []
        for y in range(HEIGHT):
            row_labels = []
            for x in range(WIDTH):
                label = tk.Label(self.grid_frame, text=" ", width=2, height=1, font=CELL_FONT, borderwidth=2, relief="ridge")
                label.grid(row=y, column=x, padx=1, pady=1)
                row_labels.append(label)
            self.cell_labels.append(row_labels)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(row=2, column=0, columnspan=WIDTH, pady=(0, 10))

        left_button = tk.Button(self.buttons_frame, text="Move Left", width=12, command=lambda: self.handle_move("l"))
        left_button.grid(row=0, column=0, padx=5)

        right_button = tk.Button(self.buttons_frame, text="Move Right", width=12, command=lambda: self.handle_move("r"))
        right_button.grid(row=0, column=1, padx=5)

        restart_button = tk.Button(self.buttons_frame, text="Restart", width=12, command=self.reset_game)
        restart_button.grid(row=0, column=2, padx=5)

        quit_button = tk.Button(self.buttons_frame, text="Quit", width=12, command=self.quit)
        quit_button.grid(row=0, column=3, padx=5)

        self.draw_hill()

    def draw_hill(self):
        for y, row in enumerate(self.hill):
            for x, tile in enumerate(row):
                text = PLAYER if (x == self.player_x and y == self.player_y) else tile
                fg = "blue" if text == PLAYER else ("green" if tile == SAFE else "red")
                self.cell_labels[y][x].config(text=text, fg=fg, bg="white")

        self.status_label.config(text="Use arrow keys or buttons. Top row is the goal.")

    def handle_move(self, direction):
        if self.player_y == 0:
            messagebox.showinfo("Victory", "You already reached the top!")
            return

        new_x = move_player(self.player_x, direction)
        new_y = self.player_y - 1

        if self.hill[new_y][new_x] == DANGEROUS:
            messagebox.showwarning("Danger!", "You stepped on a dangerous patch and slid back down.")
            self.reset_game(new_message="A new hill appears. Try again!")
            return

        self.player_x = new_x
        self.player_y = new_y
        self.draw_hill()

        if self.player_y == 0:
            self.status_label.config(text="Congratulations! You reached the top!")
            messagebox.showinfo("Victory", "You reached the top of the hill!")

    def reset_game(self, new_message=None):
        self.hill = generate_hill(WIDTH, HEIGHT)
        self.player_x = WIDTH // 2
        self.player_y = HEIGHT - 1
        self.draw_hill()
        if new_message:
            self.status_label.config(text=new_message)
        else:
            self.status_label.config(text="New hill generated. Use arrow keys or buttons.")


def main():
    app = HillClimbingGame()
    app.mainloop()


if __name__ == "__main__":
    main()
