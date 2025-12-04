import tkinter as tk
from tkinter import messagebox
from datetime import date
from rental_request import RentalRequest


class CreateRequestWindow(tk.Toplevel):
    def __init__(self, parent, system, refresh_callback):
        super().__init__(parent)
        self.system = system
        self.refresh_callback = refresh_callback

        self.title("Створити заявку на оренду")

        tk.Label(self, text="ID заявки:").grid(row=0, column=0)
        tk.Label(self, text="ID авто:").grid(row=1, column=0)
        tk.Label(self, text="Початок (YYYY-MM-DD):").grid(row=2, column=0)
        tk.Label(self, text="Кінець (YYYY-MM-DD):").grid(row=3, column=0)

        self.req_id = tk.Entry(self)
        self.car_id = tk.Entry(self)
        self.start = tk.Entry(self)
        self.end = tk.Entry(self)

        self.req_id.grid(row=0, column=1)
        self.car_id.grid(row=1, column=1)
        self.start.grid(row=2, column=1)
        self.end.grid(row=3, column=1)

        tk.Button(self, text="Зберегти", command=self.save).grid(row=4, column=0, columnspan=2, pady=10)

    def save(self):
        try:
            req = RentalRequest(
                self.req_id.get(),
                self.car_id.get(),
                date.fromisoformat(self.start.get()),
                date.fromisoformat(self.end.get())
            )
            if self.system.create_request(req):
                self.refresh_callback()

            self.destroy()
        except ValueError:
            messagebox.showerror("Помилка", "Невірний формат дати!")
