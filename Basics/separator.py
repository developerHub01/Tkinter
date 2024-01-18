import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title('Progress Bar')
window.geometry('420x550')

ttk.Label(window, text="Label 1").pack()
ttk.Separator(window, orient='horizontal').pack(fill='x')
ttk.Label(window, text="Label 2").pack()

window.mainloop()