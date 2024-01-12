import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title('Progress Bar')
window.geometry('420x550')

""" 
There are an opposite way of each layout method.
place ----> place_forget
grid ----> grid_forget
pack ----> pack_forget
"""

# # Place
# def handle_toggle_label():
#   global toggle_label_show
  
#   toggle_label_show = not toggle_label_show
  
#   if toggle_label_show:
#     toggle_label.place(relx=0.75, rely=0.5, anchor="center")
#   else:
#     toggle_label.place_forget()
    
# toggle_label_show = True
# toggle_button = ttk.Button(window, text="Toggle Place", command=handle_toggle_label)
# toggle_label = ttk.Label(window, text="Place label")
# toggle_button.place(relx=0.25, rely=0.5, anchor="center")
# toggle_label.place(relx=0.75, rely=0.5, anchor="center")

# # grid
# def handle_toggle_label():
#   global toggle_label_show
  
#   toggle_label_show = not toggle_label_show
  
#   if toggle_label_show:
#     toggle_label.grid(row=0, column=1)
#   else:
#     toggle_label.grid_forget()
    
# toggle_label_show = True
# toggle_button = ttk.Button(window, text="Toggle Grid", command=handle_toggle_label)
# toggle_label = ttk.Label(window, text="Place label")
# window.columnconfigure((0, 1), weight=1, uniform="a")
# window.rowconfigure(0, weight=1, uniform="a")
# toggle_button.grid(row=0, column=0)
# toggle_label.grid(row=0, column=1)

# # pack
# def handle_toggle_label():
#   global toggle_label_show
  
#   toggle_label_show = not toggle_label_show
  
#   if toggle_label_show:
#     replaceable_frame.pack_forget()
#     toggle_label.pack(expand=True, before=toggle_button)
#   else:
#     replaceable_frame.pack(expand=True, before=toggle_button)
#     toggle_label.pack_forget()
    
# toggle_label_show = True
# toggle_button = ttk.Button(window, text="Toggle Grid", command=handle_toggle_label)
# toggle_label = ttk.Label(window, text="Place label")
# replaceable_frame = ttk.Frame(window)
# toggle_label.pack(expand=True)
# toggle_button.pack()



window.mainloop()