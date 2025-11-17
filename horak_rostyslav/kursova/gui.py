import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager
        self.build_ui()
        self.refresh_ui()

    def build_ui(self):
        # лівий фрейм: список техніки
        left = ttk.Frame(self.root, padding=10)
        left.grid(row=0, column=0, sticky="nsew")
        ttk.Label(left, text="Одиниці техніки:").pack(anchor="w")
        self.eq_listbox = tk.Listbox(left, width=40, height=15)
        self.eq_listbox.pack(fill="both", expand=True)
        btn_frame = ttk.Frame(left)
        btn_frame.pack(fill="x", pady=5)
        self.add_btn = ttk.Button(btn_frame, text="Додати техніку")
        self.add_btn.pack(side="left", padx=2)
        self.remove_btn = ttk.Button(btn_frame, text="Видалити техніку")
        self.remove_btn.pack(side="left", padx=2)

        # правий фрейм: заявки
        right = ttk.Frame(self.root, padding=10)
        right.grid(row=0, column=1, sticky="nsew")
        ttk.Label(right, text="Заявки на оренду:").pack(anchor="w")
        cols = ("ID","Техніка","Клієнт","Початок","Кінець")
        self.tree = ttk.Treeview(right, columns=cols, show="headings", height=10)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=120)
        self.tree.pack(fill="both", expand=True)
        rent_btns = ttk.Frame(right)
        rent_btns.pack(fill="x", pady=5)
        self.create_btn = ttk.Button(rent_btns, text="Створити заявку")
        self.create_btn.pack(side="left", padx=2)
        self.delete_btn = ttk.Button(rent_btns, text="Видалити заявку")
        self.delete_btn.pack(side="left", padx=2)
        self.refresh_btn = ttk.Button(rent_btns, text="Оновити")
        self.refresh_btn.pack(side="left", padx=2)

        # статус
        self.status = ttk.Label(self.root, text="", relief="sunken", anchor="w")
        self.status.grid(row=1, column=0, columnspan=2, sticky="we")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(0, weight=1)

    def refresh_ui(self):
        # список техніки
        self.eq_listbox.delete(0, tk.END)
        for e in self.manager.equipments:
            self.eq_listbox.insert(tk.END, f"{e.id}: {e.name} ({e.type})")
        # таблиця заявок
        for i in self.tree.get_children():
            self.tree.delete(i)
        for r in self.manager.rentals:
            equip_name = next((e.name for e in self.manager.equipments if e.id == r.equipment_id), "—")
            start = r.start.replace("T"," ")
            end = r.end.replace("T"," ")
            self.tree.insert("", tk.END, values=(r.id, equip_name, r.client, start, end))
        self.status.config(text=f"Техніки: {len(self.manager.equipments)} | Заявок: {len(self.manager.rentals)}")
