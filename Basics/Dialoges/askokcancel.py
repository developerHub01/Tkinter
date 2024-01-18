import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Askokcancel')
    self.geometry('420x550')
    self.options = {
      "expand":True, "padx":20, "pady":10
    }
    tk.Button(self, text="Close", command=self.handle_close).pack(**self.options)

  def handle_close(self):
    ans = askokcancel(
      title="Confirm",
      message="Are you sure to cancel download"
    )
    if ans:
      showinfo(
        title="Success",
        message="Download canceled"
      )
      

if __name__ == '__main__':
  app = App()
  app.mainloop()