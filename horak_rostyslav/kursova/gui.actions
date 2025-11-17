from tkinter import simpledialog, messagebox
from datetime import datetime

class GUIActions:
    def __init__(self, app):
        self.app = app

    def add_equipment(self):
        name = simpledialog.askstring("Додати техніку", "Назва техніки:", parent=self.app.root)
        if not name: return
        type_ = simpledialog.askstring("Додати техніку", "Тип (Трактор, Комбайн):", parent=self.app.root)
        if not type_: return
        eq = self.app.manager.add_equipment(name, type_)
        messagebox.showinfo("Додано", f"Додано техніку: {eq.name} (ID {eq.id})", parent=self.app.root)
        self.app.refresh_ui()

    def remove_equipment(self):
        sel = self.app.eq_listbox.curselection()
        if not sel:
            messagebox.showwarning("Помилка", "Оберіть техніку", parent=self.app.root)
            return
        equip_id = int(self.app.eq_listbox.get(sel[0]).split(":")[0])
        self.app.manager.remove_equipment(equip_id)
        self.app.refresh_ui()

    def create_rental(self):
        sel = self.app.eq_listbox.curselection()
        if not sel:
            messagebox.showwarning("Помилка", "Оберіть техніку", parent=self.app.root)
            return
        equip_id = int(self.app.eq_listbox.get(sel[0]).split(":")[0])
        client = simpledialog.askstring("Клієнт", "Ім'я клієнта:", parent=self.app.root)
        if not client: return
        start_str = simpledialog.askstring("Початок оренди", "YYYY-MM-DD HH:MM", parent=self.app.root)
        end_str = simpledialog.askstring("Кінець оренди", "YYYY-MM-DD HH:MM", parent=self.app.root)
        if not start_str or not end_str: return
        try:
            # Використовуємо strptime для безпечного перетворення
            start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
            end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M")
            if end_dt <= start_dt:
                messagebox.showerror("Помилка", "Кінець повинен бути після початку", parent=self.app.root)
                return
            start_iso = start_dt.isoformat()
            end_iso = end_dt.isoformat()
        except ValueError:
            messagebox.showerror("Помилка", "Неправильний формат дати", parent=self.app.root)
            return
        rental = self.app.manager.create_rental(equip_id, client, start_iso, end_iso)
        if rental:
            messagebox.showinfo("Успіх", "Заявку створено", parent=self.app.root)
        else:
            messagebox.showerror("Конфлікт", "Техніка зайнята на цей період", parent=self.app.root)
        self.app.refresh_ui()

    def delete_rental(self):
        sel = self.app.tree.selection()
        if not sel:
            messagebox.showwarning("Помилка", "Оберіть заявку", parent=self.app.root)
            return
        rent_id = int(self.app.tree.item(sel[0], "values")[0])
        self.app.manager.delete_rental(rent_id)
        self.app.refresh_ui()
