# two way to get data of an widget
# get()

# update==============
# 1. Label.configure(text="Setter text")
# 1. Label['text'] = text="Setter text"

# enable disabled 
# entry['state'] = 'disabled'
# entry.configure(state= 'disabled')


import tkinter as tk
from tkinter import ttk

def change_func():
  # get ============================
  # get the content of the entry
  # but get only works with Entry but not others like Label or Text
  print(entry.get())
  print(textarea.configure())
  
  
  # set =======================
  # label['text'] = 'set text..'
  # label.configure(text='another test text')
  
  label.configure(text = entry.get())
  # label['text'] = entry.get()
  
  button['state'] = 'disabled'
  entry.configure(state= 'disabled')

window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('300x200')

textarea = tk.Text(master=window)
textarea.pack()

label = ttk.Label(master=window, text="Some Text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="Change", command=change_func)
button.pack()

# run
window.mainloop()