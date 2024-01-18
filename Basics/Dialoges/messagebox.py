import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror

window = tk.Tk()
window.title('Messagebox')
window.geometry('400x400')

options = {
  "expand":True, "fill":"x", "padx":20, "pady":10
}

button_info = ttk.Button(window, command=lambda: showinfo(
    title="Success",
    message="Show Info Dialoges"
  ), text="Show Info").pack(**options)
button_warning = ttk.Button(window, command=lambda: showwarning(
    title="Warning",
    message="Show Warning Dialoges"
  ), text="Show Warning").pack(**options)
button_error = ttk.Button(window, command=lambda: showerror(
    title="Error",
    message="Show Error Dialoges"
  ), text="Show Error").pack(**options)


window.mainloop()