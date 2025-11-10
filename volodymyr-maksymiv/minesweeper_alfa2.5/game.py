from tkinter import *
from cell import Cell
from grid import Grid
from window import Window
import math

class Minesweeper:

    difficulty_levels = {
        'Легко': {'grid_size': 6, 'mine_percentage': 0.20},  
        'Середньо': {'grid_size': 7, 'mine_percentage': 0.30}, 
        'Складно': {'grid_size': 9, 'mine_percentage': 0.40}  
    }

    def __init__(self):
        Window.window_settings()
        Window.top_frames()
        self.left_frame = Window.left_frames()
        self.centre_frame = Window.centre_frames()
        self.create_difficulty_buttons()
        self.start_new_game('Легко')
    
    def create_difficulty_buttons(self):
        btn_frame = Frame(self.left_frame, bg='black')
        btn_frame.pack(pady=10)

        for level in self.difficulty_levels.keys():
            btn = Button(
                btn_frame,
                text=level,
                width=10,
                command=lambda lvl=level: self.start_new_game(lvl)
            )
            btn.pack(pady=5)

    def clear_game_ui(self):
        for widget in self.centre_frame.winfo_children():
            widget.destroy()
        
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.destroy()
            Cell.cell_count_label_object = None
    
    def start_new_game(self, difficulty):
        self.clear_game_ui()

        new_settings = self.difficulty_levels[difficulty]
        grid_size = new_settings['grid_size']
        mine_percentage = new_settings['mine_percentage']
        total_cells = grid_size ** 2
        mines_count = math.ceil(total_cells * mine_percentage) 
        
        if mines_count >= total_cells:
            mines_count = total_cells - 1

        Cell.all.clear() 
        Cell.cell_count = total_cells - mines_count 

        Grid.Grid_generate(self.centre_frame, grid_size)
        Grid.create_cell_count_label(self.left_frame)
        Cell.cell_count_label_object.pack(pady=20) 
        Grid.randomize_mines(mines_count)
    
    def run(self):
        Window.root.mainloop()