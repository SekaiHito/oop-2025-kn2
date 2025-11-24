import math
import time
import json
import os

class GameLogic:
    difficulty_levels = {
        'Легко': {'grid_size': 7, 'mine_percentage': 0.20},  
        'Середньо': {'grid_size': 9, 'mine_percentage': 0.25}, 
        'Складно': {'grid_size': 12, 'mine_percentage': 0.30}  
    }
    SCORES_FILE = 'scores.json'

    def __init__(self):
        self.current_difficulty = 'Легко'
        self.start_time = None
        self.game_over = False
        self.first_click = True

    def reset_state(self, difficulty):
        self.current_difficulty = difficulty
        self.game_over = False
        self.first_click = True
        self.start_time = None

    def start_timer(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time

    def get_current_settings(self):
        return self.difficulty_levels[self.current_difficulty]

    def calculate_mines_count(self):
        settings = self.get_current_settings()
        total_cells = settings['grid_size'] ** 2
        mines_count = math.ceil(total_cells * settings['mine_percentage'])
        
        if mines_count >= total_cells:
            mines_count = total_cells - 1
        return mines_count, total_cells

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

    def get_best_score(self):
        scores = self.load_scores()
        return scores.get(self.current_difficulty)