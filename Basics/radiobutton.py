import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Radio Button')
    self.geometry('420x400')
    
    self.selected_color = tk.StringVar()
    self.selected_color.trace("w", self.menu_item_selected)
    
    self.create_menu_button()
    
  def menu_item_selected(self, *args):
    self.config(bg=self.selected_color.get())
  
  def create_menu_button(self):
    colors = ('red', 'green', 'blue')
    
    menu_button = ttk.Menubutton(
      self,
      text = "Selec a color"
    )
    
    menu = tk.Menu(menu_button, tearoff=0)
    
    for color in colors:
      menu.add_radiobutton(
        label=color,
        value=color,
        variable=self.selected_color,
      )
    menu_button['menu'] = menu
    menu_button.pack(expand=True)


if __name__ == '__main__':
  app = App()
  app.mainloop()