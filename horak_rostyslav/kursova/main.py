from tkinter import Tk
from manager import RentalManager
from gui import MainApp
from gui_actions import GUIActions

root = Tk()
manager = RentalManager()
app = MainApp(root, manager)
actions = GUIActions(app)

# Прив’язка кнопок
app.add_btn.config(command=actions.add_equipment)
app.remove_btn.config(command=actions.remove_equipment)
app.create_btn.config(command=actions.create_rental)
app.delete_btn.config(command=actions.delete_rental)
app.refresh_btn.config(command=app.refresh_ui)

root.mainloop()
