from tkinter import Button, Label, messagebox, SUNKEN
import random

class Cell:
    all = []
    cell_count_label_object = None
    cell_count = 0
    
    def __init__(self, x, y, game, is_mine=False): 
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.game = game 
        
        Cell.all.append(self)

    def create_btn_oblect(self, location):
        btn = Button(
            location,
            width=5,
            height=3,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn
    
    
    def left_click_actions(self, event):
        
        if self.game.first_click:
            self.game.initialize_mines(self)

        if self.is_opened or self.is_mine_candidate or self.game.game_over:
            return 

        if self.is_mine:
            self.game.game_over_lose() 
        else:
            self.show_cell() 
            
            if Cell.cell_count == 0:
                self.game.game_over_win()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x -1, self.y -1),
            self.get_cell_by_axis(self.x -1, self.y),
            self.get_cell_by_axis(self.x -1, self.y +1),
            self.get_cell_by_axis(self.x, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y +1),
            self.get_cell_by_axis(self.x +1, self.y),
            self.get_cell_by_axis(self.x, self.y +1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_lens(self):
        counter =0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if self.is_opened:
            return

        self.is_opened = True
        Cell.cell_count -= 1
        
        mines_nearby = self.surrounded_cells_mines_lens
        self.cell_btn_object.configure(text=str(mines_nearby) if mines_nearby > 0 else "")
        
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(
                text = f"Cells left:{Cell.cell_count}"
            )
        
        default_bg = Button().cget("background")
        self.cell_btn_object.configure(bg=default_bg, relief=SUNKEN) 

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

        if mines_nearby == 0:
            for cell in self.surrounded_cells:
                if not cell.is_opened and not cell.is_mine_candidate:
                    cell.show_cell()

    def right_click_actions(self, event):
        if self.is_opened or self.game.game_over:
            return

        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg = 'orange'
            )
            self.is_mine_candidate = True
        else:
            default_bg = Button().cget("background")
            self.cell_btn_object.configure(bg=default_bg)
            self.is_mine_candidate = False

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"