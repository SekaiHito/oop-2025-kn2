import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date
from car import Car
from rental_request import RentalRequest
from rental_system import RentalSystem


class CarRentalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система оренди автомобілів")
        self.geometry("700x500")
        self.system = RentalSystem()
        self.create_widgets()

    def create_widgets(self):
        # === Меню кнопок ===
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Button(frame, text="Додати авто", command=self.add_car_window).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Видалити авто", command=self.remove_car_window).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Заявка на оренду", command=self.create_request_window).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Оновити список", command=self.show_cars).grid(row=0, column=3, padx=5)

        # === Таблиця автомобілів ===
        columns = ("ID", "Марка", "Модель", "Рік", "Статус")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        self.show_cars()

    def show_cars(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for c in self.system.list_cars():
            status = "Вільний" if c.available else "Зайнятий"
            self.tree.insert("", tk.END, values=(c.car_id, c.brand, c.model, c.year, status))

    def add_car_window(self):
        win = tk.Toplevel(self)
        win.title("Додати автомобіль")

        tk.Label(win, text="ID:").grid(row=0, column=0)
        tk.Label(win, text="Марка:").grid(row=1, column=0)
        tk.Label(win, text="Модель:").grid(row=2, column=0)
        tk.Label(win, text="Рік:").grid(row=3, column=0)

        id_entry = tk.Entry(win)
        brand_entry = tk.Entry(win)
        model_entry = tk.Entry(win)
        year_entry = tk.Entry(win)

        id_entry.grid(row=0, column=1)
        brand_entry.grid(row=1, column=1)
        model_entry.grid(row=2, column=1)
        year_entry.grid(row=3, column=1)

        def save_car():
            try:
                car = Car(id_entry.get(), brand_entry.get(), model_entry.get(), int(year_entry.get()))
                self.system.add_car(car)
                self.show_cars()
                win.destroy()
            except ValueError:
                messagebox.showerror("Помилка", "Неправильний формат року!")

        tk.Button(win, text="Зберегти", command=save_car).grid(row=4, column=0, columnspan=2, pady=10)

    def remove_car_window(self):
        win = tk.Toplevel(self)
        win.title("Видалити автомобіль")

        tk.Label(win, text="ID авто:").grid(row=0, column=0)
        id_entry = tk.Entry(win)
        id_entry.grid(row=0, column=1)

        def remove():
            car_id = id_entry.get()
            self.system.remove_car(car_id)
            self.show_cars()
            win.destroy()

        tk.Button(win, text="Видалити", command=remove).grid(row=1, column=0, columnspan=2, pady=10)

    def create_request_window(self):
        win = tk.Toplevel(self)
        win.title("Створити заявку на оренду")

        tk.Label(win, text="ID заявки:").grid(row=0, column=0)
        tk.Label(win, text="ID авто:").grid(row=1, column=0)
        tk.Label(win, text="Початок (YYYY-MM-DD):").grid(row=2, column=0)
        tk.Label(win, text="Кінець (YYYY-MM-DD):").grid(row=3, column=0)

        id_req = tk.Entry(win)
        id_car = tk.Entry(win)
        start_entry = tk.Entry(win)
        end_entry = tk.Entry(win)

        id_req.grid(row=0, column=1)
        id_car.grid(row=1, column=1)
        start_entry.grid(row=2, column=1)
        end_entry.grid(row=3, column=1)

        def save_request():
            try:
                req = RentalRequest(
                    id_req.get(),
                    id_car.get(),
                    date.fromisoformat(start_entry.get()),
                    date.fromisoformat(end_entry.get())
                )
                if self.system.create_request(req):
                    self.show_cars()
                win.destroy()
            except ValueError:
                messagebox.showerror("Помилка", "Невірний формат дати!")

        tk.Button(win, text="Зберегти", command=save_request).grid(row=4, column=0, columnspan=2, pady=10)
