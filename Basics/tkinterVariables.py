# we can get and set any daynamic tkinter variables

import tkinter as tk
from tkinter import ttk

def handle_button():
  print(string_var.get())
  string_var.set("Test click")

window = tk.Tk()
window.title('Tkinter variableds')

string_var = tk.StringVar(
    value="hello"
  )

label = ttk.Label(
    master=window, text='label', 
    textvariable=string_var
  )
label.pack()
entry = ttk.Entry(
    master=window, 
    textvariable=string_var
  )
entry.pack()
button = ttk.Button(
    master=window, text='button', 
    command=handle_button
  )
button.pack()

# ===================================================

exercise_var = tk.StringVar(value = 'test')

entry1 = ttk.Entry(master=window, textvariable=exercise_var)
entry1.pack()
entry2 = ttk.Entry(master=window, textvariable=exercise_var)
entry2.pack()
exercise_lable = ttk.Label(master=window, text="lable", textvariable=exercise_var)
exercise_lable.pack()


window.mainloop()