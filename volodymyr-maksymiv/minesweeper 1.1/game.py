from tkinter import *
from tkinter import messagebox
from cell import Cell
from grid import Grid
from window import Window
from game_logic import GameLogic 

class Minesweeper:
    def __init__(self):

        self.logic = GameLogic()
        
        Window.window_settings()
        Window.top_frames()
        self.left_frame = Window.left_frames()
        self.centre_frame = Window.centre_frames()
        
        self.timer_label = None
        self.high_score_label = None
        
        self.create_control_buttons() 
        self.create_info_labels()
        
        self.start_new_game(self.logic.current_difficulty)

    @property
    def game_over(self):
        return self.logic.game_over
    
    @game_over.setter
    def game_over(self, value):
        self.logic.game_over = value

    @property
    def first_click(self):
        return self.logic.first_click
    
    # --- Методи UI ---

    def create_control_buttons(self):
        difficulty_frame = Frame(self.left_frame, bg='black')
        difficulty_frame.pack(pady=10)

        # Беремо рівні складності з логіки
        for level in self.logic.difficulty_levels.keys():
            btn = Button(
                difficulty_frame,
                text=level,
                width=10,
                command=lambda lvl=level: self.start_new_game(lvl)
            )
            btn.pack(pady=5)
    
    def on_restart_click(self):
        self.start_new_game(self.logic.current_difficulty)

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
        self.logic.reset_state(difficulty)
        self.clear_game_ui()
        
        settings = self.logic.get_current_settings()
        grid_size = settings['grid_size']
        
        Cell.all.clear() 
        Cell.cell_count = 0 

        Grid.Grid_generate(self.centre_frame, grid_size, self) 
        Grid.create_cell_count_label(self.left_frame)
        Cell.cell_count_label_object.pack(pady=20) 
        
        self.update_high_score_display()
        self.timer_label.configure(text="Час: 0.0s")
    
    def initialize_mines(self, first_clicked_cell):
        self.logic.first_click = False 
        
        mines_count, total_cells = self.logic.calculate_mines_count()

        Cell.cell_count = total_cells - mines_count
        Cell.cell_count_label_object.configure(
            text=f"Cells left:{Cell.cell_count}"
        )
        
        Grid.randomize_mines(mines_count, first_clicked_cell)

        self.logic.start_timer()
        self.update_timer()

    def update_timer(self):
        if self.logic.game_over:
            return 
        
        if self.logic.start_time is None:
            return

        elapsed = self.logic.get_elapsed_time()
        self.timer_label.configure(text=f"Час: {elapsed:.1f}s")
        Window.root.after(100, self.update_timer)

    def game_over_lose(self):
        self.logic.game_over = True
        
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
        self.logic.game_over = True
        elapsed_time = self.logic.get_elapsed_time()
        
        self.logic.save_score(elapsed_time)
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
        # Делегуємо запит до логіки
        return self.logic.load_scores()
            
    def save_score(self, new_time):
        # Делегуємо запит до логіки
        self.logic.save_score(new_time)
                
    def update_high_score_display(self):
        best_time = self.logic.get_best_score()
        
        if best_time:
            self.high_score_label.configure(
                text=f"Рекорд ({self.logic.current_difficulty}):\n{best_time:.2f}с"
            )
        else:
            self.high_score_label.configure(
                text=f"Рекорд ({self.logic.current_difficulty}):\nN/A"
            )

    def run(self):
        Window.root.mainloop()