from tkinter import *


class Window:
    root = None  

    @staticmethod
    def window_settings():
        Window.root = Tk()
        Window.root.configure(bg="black")
        Window.root.title("Сапер")
        Window.root.resizable(False, False)
        Window.root.rowconfigure(1, weight=1)
        Window.root.columnconfigure(1, weight=1)

    @staticmethod
    def Top_frame():
        top_frame = Frame(
            Window.root,
            bg='black'
        )
        top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        game_title = Label(
            top_frame,
            bg='black',
            fg='white',
            text='Minesweeper Game',
            font=('', 48)
        )
        game_title.pack(pady=20)

    @staticmethod
    def Left_frame():
        left_frame = Frame(
            Window.root,
            bg='black'
        )
        left_frame.grid(row=1, column=0, sticky="ns")
        return left_frame

    @staticmethod
    def Centre_frame():
        centre_frame = Frame(
            Window.root,
            bg='black',
        )
        centre_frame.grid(row=1, column=1, sticky="nsew")
        return centre_frame
