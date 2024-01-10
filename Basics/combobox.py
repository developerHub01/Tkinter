import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime


window = tk.Tk()
window.title('Combobox')
window.geometry('400x400')
window.resizable(False, False)

current_var = tk.StringVar()
combobox = ttk.Combobox(window, textvariable=current_var)
combobox['values'] = ('one', 'two', 'three', 'four')
combobox['state'] = 'readonly' # determine that is typing is permited or not
combobox.pack()

# combobox.bind("<<ComboboxSelected>>", lambda e: print(e))

""" 
get and set value in combobox two ways:
1. set("value")
  set ===>> combobox.set("abc")
  get ===>> combobox.get()
            print(combobox.get())

2.combobox.current(0)
  get ===>> combobox.current()
            print(combobox.current())
  set ===>> combobox.current(index)
"""


# combobox.set("abc")
# print(combobox.current())
# combobox.set("three")
# print(combobox.current())
# combobox.current(0)
# combobox.current(1)
# combobox.current(2)
# combobox.current(3)
button = tk.Button(window, text="Button", command=lambda: print(current_var.get()))
button.pack()


label = ttk.Label(text='Please select a month')
label.pack(fill=tk.X, padx=5, pady=5)

selected_month = tk.StringVar()
month_combobox = ttk.Combobox(window, textvariable=selected_month)
month_name = list(month_name)
month_name.pop(0)
month_combobox['values']= [month_name[i][:3] for i in range(0, 12)]
# month_combobox.configure(values= [month_name[i][:3] for i in range(0, 12)])
month_combobox.pack(fill=tk.X, padx=5, pady=5)
month_combobox['state'] = 'normal' # allow to type in combo box
month_combobox['state'] = 'readonly' # don't allow to type in combo box

def handle_change(e):
  showinfo(
    title="Selected month",
    message=f"{month_combobox.get()}",
  )
month_combobox.bind('<<ComboboxSelected>>', handle_change)

month_combobox.set(month_name[datetime.now().month-1][:3])

window.mainloop()