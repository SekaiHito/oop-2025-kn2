from cell import Cell
from tkinter import Button, Label, messagebox
import random

class Grid:

    @staticmethod
    def Grid_generate(location, grid_size, game): 
        for x in range(grid_size):
            for y in range(grid_size):
                c = Cell(x , y, game) 
                c.create_btn_oblect(location)
                c.cell_btn_object.grid(column=y, row=x)

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Cells left:...", 
            width = 14,
            height= 4,
            font = ("",30)
            
        )
        Cell.cell_count_label_object = lbl
    
    @staticmethod
    def randomize_mines(mines_count, first_clicked_cell):
        
        available_cells = [
            cell for cell in Cell.all if cell != first_clicked_cell
        ]
        
        picked_cells = random.sample(
            available_cells, mines_count
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True