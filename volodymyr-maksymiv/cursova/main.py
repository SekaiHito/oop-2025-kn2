from tkinter import *
import settings
import utils
from cell import Cell
from window import Window

Window.window_settings()
Window.Top_frame()

centre_frame = Window.Centre_frame()
left_frame = Window.Left_frame()

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x , y)
        c.create_btn_oblect(centre_frame)
        c.cell_btn_object.grid(column=y, row=x)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

Window.root.mainloop()


