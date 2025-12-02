import tkinter as tk
from tkinter import messagebox
from car import Car


class AddCarWindow(tk.Toplevel):
    def __init__(self, parent, system, refresh_callback):
        super().__init__(parent)
        self.system = system
        self.refresh_callback = refresh_callback

        self.title("Додати автомобіль")

        tk.Label(self, text="ID:").grid(row=0, column=0)
        tk.Label(self, text="Марка:").grid(row=1, column=0)
        tk.Label(self, text="Модель:").grid(row=2, column=0)
        tk.Label(self, text="Рік:").grid(row=3, column=0)

        self.id = tk.Entry(self)
        self.brand = tk.Entry(self)
        self.model = tk.Entry(self)
        self.year = tk.Entry(self)

        self.id.grid(row=0, column=1)
        self.brand.grid(row=1, column=1)
        self.model.grid(row=2, column=1)
        self.year.grid(row=3, column=1)

        tk.Button(self, text="Зберегти", command=self.save).grid(row=4, column=0, columnspan=2, pady=10)

    def save(self):
        try:
            car = Car(self.id.get(), self.brand.get(), self.model.get(), int(self.year.get()))
            self.system.add_car(car)
            self.refresh_callback()
            self.destroy()
        except ValueError:
            messagebox.showerror("Помилка", "Невірний формат року!")


class RemoveCarWindow(tk.Toplevel):
    def __init__(self, parent, system, refresh_callback):
        super().__init__(parent)
        self.system = system
        self.refresh_callback = refresh_callback

        self.title("Видалити автомобіль")

        tk.Label(self, text="ID авто:").grid(row=0, column=0)
        self.id = tk.Entry(self)
        self.id.grid(row=0, column=1)

        tk.Button(self, text="Видалити", command=self.remove).grid(row=1, column=0, columnspan=2, pady=10)

    def remove(self):
        self.system.remove_car(self.id.get())
        self.refresh_callback()
        self.destroy()
