from tkinter import Button, Label, messagebox
import random
from window import Window
import sys

class Cell:
    all = []
    cell_count_label_object = None
    cell_count = 0
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        
        Cell.all.append(self)


    def create_btn_oblect(self, location):
        btn = Button(
            location,
            width=8,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn
    
    
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_lens == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
        if Cell.cell_count == settings.MINES_COUNT:
            messagebox.showinfo('Game over!', 'Congratulation!')

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
    
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
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_lens)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f"Cells left:{Cell.cell_count}"
                )
            default_bg = Button().cget("background")
            self.cell_btn_object.configure(bg=default_bg)
        self.is_opened = True

    
    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        messagebox.showinfo('Game over!', 'You clicked on a mine!')
        sys.exit()

    def right_click_actions(self, event):
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

    