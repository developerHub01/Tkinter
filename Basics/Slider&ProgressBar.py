import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.geometry('500x500')
window.title('Slider')
window.resizable(False, False)

""" 
syntax:
ttk.Scale(container, from_, to)
ttk.Progressbar(container, orient, length, mode)
"""

def handleSlider(slider, slider_label):
  slider_label["text"] = f"{slider.get():.2f}"


slider1_var = tk.DoubleVar()

progress1 = ttk.Progressbar(window, orient="horizontal", mode="indeterminate", length=200, variable=slider1_var)
progress1.pack()

slider1 = ttk.Scale(window, from_=0, to=100, orient='horizontal', variable=slider1_var, command=lambda e: handleSlider(slider1, slider1_label))
slider1.pack()

slider1_label = tk.Label(window, text="First slider")
slider1_label.pack()


slider2_var = tk.DoubleVar()
progress2 = ttk.Progressbar(window, orient="vertical", mode="determinate", length=200, variable=slider2_var)
progress2.pack()
slider2 = ttk.Scale(window, from_=0, to=100, orient='vertical', command=lambda e: handleSlider(slider2, slider2_label), variable=slider2_var)
slider2.pack()

slider2_label = tk.Label(window, text="Second slider")
slider2_label.pack()


slider3 = ttk.Scale(window, from_=0, to=100, orient='horizontal', command=lambda e: handleSlider(slider3, slider3_label))
slider3['state'] = 'disabled'
slider3.pack()

slider3_label = tk.Label(window, text="Third slider")
slider3_label.pack()

""" 
get value:
slider.get()

set value:
slider.set()

set state:
slider['state'] = 'disabled'
slider['state'] = 'normal'
"""


window.mainloop()