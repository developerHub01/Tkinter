import tkinter as tk
from tkinter import ttk
import random

## Notebook or tabs

window = tk.Tk()
window.title('Progress Bar')
window.geometry('420x550')

tabs = ttk.Notebook(window)
tabs.pack(fill="both", expand=True)

tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)

for i in [tab1,  tab2, tab3]:
  i.pack(fill="both", expand=True)
  
for i in [(tab1, "Tab 1"), (tab2, "Tab 2"), (tab3, "Tab 3")]:
  tabs.add(i[0], text=i[1])
  
tabs_data = [
  {
    "tab": tab1,
    "tab_content":"Tab 1 data"
  },
  {
    "tab": tab2,
    "tab_content":"Tab 2 data"
  },
  {
    "tab": tab3,
    "tab_content":"Tab 3 data"
  },
]

theme = [
  {
    "bg": "#283618",
    "fg": "#fefae0",
  },
  {
    "bg": "#1d3557",
    "fg": "#f1faee",
  },
  {
    "bg": "#0d1b2a",
    "fg": "#f7ede2",
  },
]

for i in tabs_data:
  selected_theme = random.choice(theme)
  label = ttk.Label(i["tab"], text=i["tab_content"], font=("Poppins", 20), anchor="center", background=selected_theme["bg"], foreground=selected_theme["fg"])
  label.pack(fill="both", expand=True)
  

window.mainloop()