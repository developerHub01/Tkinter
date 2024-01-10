import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
  print("Convert....")
  # print(entry.get())
  print(entry_int.get())
  output_string.set(f'{entry_int.get()*1.61} Km')


# window 
window = ttk.Window(themename='darkly')
window.title('Demo')
window.geometry('300x150')


# error label 
error_label = None

# title
title_label = ttk.Label(master=window, text="Miles to kilometers", font='Roboto 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.DoubleVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side='left', padx=10, pady=10)
button.pack(side='right', padx=10, pady=10)
input_frame.pack()

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", textvariable=output_string)
output_label.pack()

# run 
window.mainloop()
