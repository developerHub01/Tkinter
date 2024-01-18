import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('')
    self.geometry('420x550')
    self.configure(background="#ffffff")
    
    tk.Button(self, text="Choose color", command=self.handle_choose_color).pack(expand=True)
    
    
  def handle_choose_color(self):
    color = askcolor(
      title="Choose color"
    )
    self.configure(background=color[1])


if __name__ == '__main__':
  app = App()
  app.mainloop()