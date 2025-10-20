from tkinter import *
import utils
import settings

class Window:
    root = None  

    @staticmethod
    def window_settings():
        Window.root = Tk()
        Window.root.configure(bg="black")
        Window.root.geometry(f'{settings.WIDTH}x{settings.HEIGTH}')
        Window.root.title("Сапер")
        Window.root.resizable(False, False)

    @staticmethod
    def Top_frame():
        top_frame = Frame(
            Window.root,
            bg='black',
            width=settings.WIDTH,
            height=utils.height_prct(25)
        )
        top_frame.place(x=0, y=0)

        game_title = Label(
            top_frame,
            bg='black',
            fg='white',
            text='Minesweeper Game',
            font=('', 48)
        )
        game_title.place(
            x=utils.width_prct(25),
            y=0
        )

    @staticmethod
    def Left_frame():
        left_frame = Frame(
            Window.root,
            bg='black',
            width=utils.width_prct(25),
            height=utils.height_prct(75)
        )
        left_frame.place(x=0, y=utils.height_prct(25))
        return left_frame

    @staticmethod
    def Centre_frame():
        centre_frame = Frame(
            Window.root,
            bg='black',
            width=utils.width_prct(75),
            height=utils.height_prct(75)
        )
        centre_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))
        return centre_frame
