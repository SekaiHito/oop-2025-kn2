import tkinter as tk
from tkinter import ttk
from rental_system import RentalSystem
from ui.car_widgets import AddCarWindow, RemoveCarWindow
from ui.request_widgets import CreateRequestWindow


class CarRentalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система оренди автомобілів")
        self.geometry("700x500")

        # Лише бізнес-логіка
        self.system = RentalSystem()

        self._build_layout()
        self.show_cars()

    def _build_layout(self):
        # Панель кнопок
        frame = tk.Frame(self)
        frame.pack(pady=10)

        tk.Button(frame, text="Додати авто",
                  command=lambda: AddCarWindow(self, self.system, self.show_cars)).grid(row=0, column=0, padx=5)

        tk.Button(frame, text="Видалити авто",
                  command=lambda: RemoveCarWindow(self, self.system, self.show_cars)).grid(row=0, column=1, padx=5)

        tk.Button(frame, text="Заявка на оренду",
                  command=lambda: CreateRequestWindow(self, self.system, self.show_cars)).grid(row=0, column=2, padx=5)

        tk.Button(frame, text="Оновити список", command=self.show_cars).grid(row=0, column=3, padx=5)

        # Таблиця авто
        columns = ("ID", "Марка", "Модель", "Рік", "Статус")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_cars(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for car in self.system.list_cars():
            status = "Вільний" if car.available else "Зайнятий"
            self.tree.insert("", tk.END, values=(
                car.car_id, car.brand, car.model, car.year, status))
