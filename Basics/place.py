import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('')
    self.geometry('420x550')
    
    """ 
    x = distance from left in px
    y = distance from top in px
    relx = distance from left between 0 and 1
    rely = distance from top between 0 and 1, they percentage from 0 to 1
    
    width = width in px
    height = height in px
    
    relwidth = width between 0 to 1
    relheight = height between 0 to 1
    """


if __name__ == '__main__':
  app = App()
  app.mainloop()