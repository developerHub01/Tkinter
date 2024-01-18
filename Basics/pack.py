import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('')
    self.geometry('420x400')
    self.top_frame()
    self.middle_frame()
    self.bottom_frame()
    # frame1 = tk.Frame(self)
    # tk.Label(frame1, text="hello", bg="red").pack(expand=True, fill='both')
    # frame1.pack(expand=True, fill='both')
    
  def top_frame(self):
    frame = ttk.Frame(self)
    ttk.Label(frame, text="Top", background="red").pack(expand=True, fill='both', side='left')
    ttk.Label(frame, text="Top", background="yellow").pack(expand=True, fill='both', side='left')
    frame.pack(expand=True, fill='both')

  def middle_frame(self):
    frame = ttk.Frame(self)
    tk.Label(frame, text="Middle Label", background="green").pack(expand=True, fill='both')
    frame.pack(fill='both', expand=True)
  
  def bottom_frame(self):
    frame = tk.Frame(self)
    tk.Button(frame, text="1", background="red").pack(fill='both', expand=True, side='left')
    tk.Button(frame, text="1", background="yellow").pack(fill='both', expand=True, side='left')
    tk.Button(frame, text="1", background="blue").pack(fill='both', expand=True, side='left')
    frame.pack(expand=True, fill='both')
    
if __name__ == '__main__':
  app = App()
  app.mainloop()