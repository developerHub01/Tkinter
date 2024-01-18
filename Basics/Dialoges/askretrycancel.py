import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askretrycancel

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Askretrycancel')
    self.geometry('420x550')
    
    tk.Button(self, text="Connect to database", command=self.connect_db).pack(expand=True)

  def connect_db(self):
    options = {
      "title":"Connections issue",
      "message":"Server may unreachable want to retry for connection."
    }
    ans = askretrycancel(**options)
    if ans:
      self.connect_db()

if __name__ == '__main__':
  app = App()
  app.mainloop()