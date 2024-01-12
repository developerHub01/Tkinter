import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title('Complex Layout 1')
window.geometry('600x450')
window.minsize(600, 400)

main_frame = ttk.Frame(window)
main_frame.pack(expand=True, fill="both", padx=10, pady=10)
main_frame.columnconfigure(0, weight=1, uniform="a")
main_frame.columnconfigure(1, weight=2, uniform="a")
main_frame.rowconfigure(0, weight=1)

left_frame = ttk.Frame(main_frame)
right_frame = ttk.Frame(main_frame)
left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=0, column=1, sticky="nsew")

# left side
frame_left_top = tk.Frame(left_frame)
frame_left_middle = tk.Frame(left_frame)
frame_left_bottom = tk.Frame(left_frame)
left_frame.columnconfigure(0, weight=1, uniform="a")
left_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="a")

frame_left_top.grid(column=0, row=0, rowspan=2, sticky="nsew")
frame_left_middle.grid(column=0, row=2, rowspan=3, sticky="nsew", padx=10)
frame_left_bottom.grid(column=0, row=5, sticky="nsew")

# left top
frame_left_top.columnconfigure((0, 1, 2, 3, 5), weight=1, uniform="a")
frame_left_top.rowconfigure((0, 1), weight=1, uniform="a")

left_top_button1 = ttk.Button(frame_left_top, text="Left Top Button1")
left_top_button2 = ttk.Button(frame_left_top, text="Left Top Button2")
left_top_button3 = ttk.Button(frame_left_top, text="Left Top Button3")
left_top_button1.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
left_top_button2.grid(row=0, column=3, columnspan=2, sticky="nsew", padx=5, pady=5)
left_top_button3.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)


# left middle
left_middle_scale1 = ttk.Scale(
  frame_left_middle,
  from_=0,
  to=100,
  orient="vertical",
  length=200
  )
left_middle_scale2 = ttk.Scale(
  frame_left_middle,
  from_=0,
  to=100,
  orient="vertical",
  length=200
  )

left_middle_scale1.pack(side="left", padx=10, pady=5)
left_middle_scale2.pack(side="right", padx=10, pady=5)


# left bottom
left_bottom_top_frame = ttk.Frame(frame_left_bottom)
left_bottom_top_frame.pack()
left_bottom_check1 = ttk.Checkbutton(left_bottom_top_frame, text="check1")
left_bottom_check2 = ttk.Checkbutton(left_bottom_top_frame, text="check2")
left_bottom_check1.pack(side="right", padx=5)
left_bottom_check2.pack(side="left", padx=5)
left_bottom_entry = ttk.Entry(frame_left_bottom)
left_bottom_entry.pack(fill="x", expand=True)

# right side
right_label1 = tk.Label(right_frame, text="Label 1", background="red")
right_label2 = tk.Label(right_frame, text="Label 2", background="green")
right_button1 = tk.Button(right_frame, text="Button 1")
right_button2 = tk.Button(right_frame, text="Button 2")
right_frame.columnconfigure((0, 1), weight=1, uniform="a")
right_frame.rowconfigure((0, 1), weight=1, uniform="a")

right_label1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
right_button1.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
right_button2.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
right_label2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

window.mainloop()