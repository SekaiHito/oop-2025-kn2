from tkinter import *
from tkinter import messagebox
from cell import Cell
from grid import Grid
from window import Window
import math
import time
import json
import os

class Minesweeper:

    difficulty_levels = {
        'Легко': {'grid_size': 7, 'mine_percentage': 0.20},  
        'Середньо': {'grid_size': 9, 'mine_percentage': 0.25}, 
        'Складно': {'grid_size': 12, 'mine_percentage': 0.30}  
    }
    SCORES_FILE = 'scores.json'

    def __init__(self):
        Window.window_settings()
        Window.top_frames()
        self.left_frame = Window.left_frames()
        self.centre_frame = Window.centre_frames()
        
        self.timer_label = None
        self.high_score_label = None
        
        self.create_control_buttons() 
        self.create_info_labels()
        
        self.start_time = None
        self.game_over = False
        self.first_click = True
        self.current_difficulty = 'Легко'
        
        self.start_new_game(self.current_difficulty)
    
    def create_control_buttons(self):
        difficulty_frame = Frame(self.left_frame, bg='black')
        difficulty_frame.pack(pady=10)

        for level in self.difficulty_levels.keys():
            btn = Button(
                difficulty_frame,
                text=level,
                width=10,
                command=lambda lvl=level: self.start_new_game(lvl)
            )
            btn.pack(pady=5)
            
        self.restart_button = Button(
            self.left_frame,
            text="Рестарт",
            width=10,
            command=self.on_restart_click
        )
        self.restart_button.pack(pady=20)

    def on_restart_click(self):
        self.start_new_game(self.current_difficulty)

    def create_info_labels(self):
        self.timer_label = Label(
            self.left_frame, bg='black', fg='white',
            text="Час: 0.0s", font=("", 20)
        )
        self.timer_label.pack(pady=10)
        
        self.high_score_label = Label(
            self.left_frame, bg='black', fg='cyan',
            text="Рекорд: N/A", font=("", 16)
        )
        self.high_score_label.pack(pady=20)

    def clear_game_ui(self):
        for widget in self.centre_frame.winfo_children():
            widget.destroy()
        
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.destroy()
            Cell.cell_count_label_object = None
    
    def start_new_game(self, difficulty):
        self.clear_game_ui()
        self.game_over = False
        self.current_difficulty = difficulty
        self.first_click = True 
        
        new_settings = self.difficulty_levels[difficulty]
        grid_size = new_settings['grid_size']
        
        Cell.all.clear() 
        Cell.cell_count = 0 

        Grid.Grid_generate(self.centre_frame, grid_size, self) 
        Grid.create_cell_count_label(self.left_frame)
        Cell.cell_count_label_object.pack(pady=20) 
        
        self.update_high_score_display()
        
        self.start_time = None 
        self.timer_label.configure(text="Час: 0.0s")
    
    def initialize_mines(self, first_clicked_cell):
        self.first_click = False 
        
        new_settings = self.difficulty_levels[self.current_difficulty]
        grid_size = new_settings['grid_size']
        mine_percentage = new_settings['mine_percentage']
        total_cells = grid_size ** 2
        mines_count = math.ceil(total_cells * mine_percentage) 
        
        if mines_count >= total_cells:
            mines_count = total_cells - 1

        Cell.cell_count = total_cells - mines_count
        Cell.cell_count_label_object.configure(
            text=f"Cells left:{Cell.cell_count}"
        )
        
        Grid.randomize_mines(mines_count, first_clicked_cell)

        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        if self.game_over:
            return 
        
        if self.start_time is None:
            return

        elapsed = time.time() - self.start_time
        self.timer_label.configure(text=f"Час: {elapsed:.1f}s")
        Window.root.after(100, self.update_timer)

    def game_over_lose(self):
        self.game_over = True
        
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_btn_object.configure(bg='red', text='*')
        
        response = messagebox.askquestion(
            'Гра завершена!', 
            'Ви натрапили на міну!\n\nБажаєте зіграти ще раз?'
        )
        
        if response == 'yes':
            self.on_restart_click() 
        else:
            self.game_exit() 

    def game_over_win(self):
        self.game_over = True
        elapsed_time = time.time() - self.start_time
        
        self.save_score(elapsed_time)
        self.update_high_score_display()
        
        response = messagebox.askquestion(
            'Перемога!', 
            f'Вітаємо! Ваш час: {elapsed_time:.2f}с\n\nБажаєте зіграти ще раз?'
        )
        
        if response == 'yes':
            self.on_restart_click()
        else:
            self.game_exit()

    def game_exit(self):
        Window.root.destroy()

    def load_scores(self):
        if not os.path.exists(self.SCORES_FILE):
            return {level: None for level in self.difficulty_levels.keys()}
        
        try:
            with open(self.SCORES_FILE, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {level: None for level in self.difficulty_levels.keys()}
            
    def save_score(self, new_time):
        scores = self.load_scores()
        current_best = scores.get(self.current_difficulty)
        
        if current_best is None or new_time < current_best:
            scores[self.current_difficulty] = new_time
            try:
                with open(self.SCORES_FILE, 'w') as f:
                    json.dump(scores, f)
            except IOError as e:
                print(f"Помилка збереження рекорду: {e}")
                
    def update_high_score_display(self):
        scores = self.load_scores()
        best_time = scores.get(self.current_difficulty)
        
        if best_time:
            self.high_score_label.configure(
                text=f"Рекорд ({self.current_difficulty}):\n{best_time:.2f}с"
            )
        else:
            self.high_score_label.configure(
                text=f"Рекорд ({self.current_difficulty}):\nN/A"
            )

    def run(self):
        Window.root.mainloop()