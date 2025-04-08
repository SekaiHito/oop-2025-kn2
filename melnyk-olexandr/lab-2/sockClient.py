import socket

from tkinter import *
from tkinter import messagebox

window = Tk() # створюємо вікно

window.title("Рахівник")  # назва  вікна
window.resizable = False  # робимо так, щоб його не можна було розтягувати
window.geometry("400x200")   # його розміри


placeholder_label = Label(window, text="Введiть речення:", font=("Arial", 18))   # шрифт і розмір "Введiть речення"
placeholder_label.place(relx=0.5, y=65, anchor=CENTER)   # розміри та розташування
tetx_entry = Entry(window, width=22)
tetx_entry.place(relx=0.5, y=93, anchor=CENTER)   


def send_request():   # функція при натисканні на кнопку
    if 2 < len(tetx_entry.get()):    # якщо введено більше 2 символів
        sock.send(tetx_entry.get().encode())    # тоді відправляємо запит серверу

        data = sock.recv(4000)    # отримуємо вже результат (кількість унікал символів)
        messagebox.showinfo(title="Данi", message=data.decode())    # розкодовуємо і показуємо користувачу



btn = Button(window, text="Отримати данi", command=send_request)
btn.place(relx=0.5, y=125, anchor=CENTER)
btn['foreground'] = "green"

sock = socket.socket()    # пробуємо підключитися
sock.connect(('localhost', 50007))  # пробуємо підключитися
window.mainloop()  # якщо все добре, то показуємо форму

