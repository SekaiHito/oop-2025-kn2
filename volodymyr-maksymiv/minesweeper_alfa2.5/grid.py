from cell import Cell
from tkinter import Button, Label, messagebox
import random

class Grid:

    @staticmethod
    def Grid_generate(location, grid_size):
        for x in range(grid_size):
            for y in range(grid_size):
                c = Cell(x , y)
                c.create_btn_oblect(location)
                c.cell_btn_object.grid(column=y, row=x)

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Cells left:{Cell.cell_count}",
            width = 14,
            height= 4,
            font = ("",30)
            
        )
        Cell.cell_count_label_object = lbl
    
    @staticmethod
    def randomize_mines(mines_count):
        
        picked_cells = random.sample(
            Cell.all, mines_count
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True