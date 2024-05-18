from start_page import StartPage
from game_pole import GamePole
from final_page import FinalPage
import tkinter as tk
from tkinter import ttk


def form_start_page():
    root = tk.Tk()
    app = StartPage(root)
    root.mainloop()
    return app.selected_game_mode, app.selected_difficulty_level

def form_game_pole(game_mode, difficulty_level):
    root = tk.Tk()
    app = GamePole(root, game_mode, difficulty_level)
    root.mainloop()

def form_final_page():
    root = tk.Tk()
    app = FinalPage(root)
    root.mainloop()

if __name__ == "__main__":
    settings = form_start_page()
    form_game_pole(settings[0], settings[1])
    form_final_page()