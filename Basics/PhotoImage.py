import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title('Display Image')
window.geometry('400x400')

photo = tk.PhotoImage(file='./assets/selenium.png')
photoLabel = ttk.Label(window, image=photo)
photoLabel.pack()

window.mainloop()