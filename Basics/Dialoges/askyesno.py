import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import askyesno

""" 
Syntax: 
  answer = askyesno(title, message, **options)
"""

# options = {
#   "expand":True, "pady":10
# }

# def handle_close():
#   ans = askyesno(
#     title="Confirmation",
#     message="Are you sure to close."
#   )
#   if ans:
#     window.destroy()

# button_info = ttk.Button(window, command=handle_close, text="Close").pack(**options)

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    
    self.title('Askyesno')
    self.geometry('420x550')
    self.options = {
      "expand":True, "pady":10
    }
    close_button = ttk.Button(self, command=self.handle_close, text="Close")
    close_button.pack(**self.options)
    
  def handle_close(self):
    ans = askyesno(
      title="Confirmation",
      message="Are you sure to close."
    )
    if ans:
      self.destroy()

if __name__ == "__main__":
  app = App()
  app.mainloop()