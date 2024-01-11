import tkinter as tk 
from tkinter import ttk, scrolledtext

window = tk.Tk()
window.title('Scrolled text')
window.geometry('420x350')


tk.Label(window, text="Scrolled Text").pack()

scrolledText1 = scrolledtext.ScrolledText(window, width=50, height=5)
scrolledText1.pack()


window.mainloop()