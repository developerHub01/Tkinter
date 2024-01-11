import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title('Progress Bar')
window.geometry('420x550')

progress1 = ttk.Progressbar(
  window,
  orient="horizontal",
  mode="indeterminate",
  length=400
)
progress1.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

start_btn1 = ttk.Button(
  window,
  text="START",
  command=progress1.start,
)
start_btn1.grid(column=0, row=1, padx=10, pady=10)

stop_btn1 = ttk.Button(
  window,
  text="STOP",
  command=progress1.stop
)
stop_btn1.grid(column=1, row=1, padx=10, pady=10)




progress2 = ttk.Progressbar(
  window,
  maximum=100,
  orient="horizontal",
  mode="determinate",
  length=400
)

progress2.grid(column=0, row=2, columnspan=2, padx=10, pady=20)

start_btn2 = ttk.Button(
  window,
  text="START",
  command=progress2.start,
)
start_btn2.grid(column=0, row=3, padx=10, pady=10)

stop_btn2 = ttk.Button(
  window,
  text="STOP",
  command=progress2.stop
)
stop_btn2.grid(column=1, row=3, padx=10, pady=10)


def startProgress():
  if progress3['value'] < 100:
    progress3['value'] += 20
    progress3_label['text'] = f'Downlaod progress {progress3['value']}%'
  else:
    progress3_label['text'] = f'Downlaod completed'
    progress3.stop()
    return
    
def endProgress():
  progress3.stop()

progress3 = ttk.Progressbar(
  window,
  orient="horizontal",
  mode="determinate",
  length=400
)
progress3.grid(column=0, row=4, columnspan=2, padx=10, pady=20)

progress3_label = tk.Label(window, text="", font=('Poppins', 10))
progress3_label.grid(column=0, row=5, columnspan=2, padx=10, pady=0)

start_btn3 = ttk.Button(
  window,
  text="START",
  # command=(startProgress, progress3.start(100)),
  command=startProgress,
)
start_btn3.grid(column=0, row=6, padx=10, pady=10)

stop_btn3 = ttk.Button(
  window,
  text="STOP",
  command=endProgress
)
stop_btn3.grid(column=1, row=6, padx=10, pady=10)


progress4_var = tk.DoubleVar()
progress4_slider = tk.Scale(
  window,
  from_=0,
  to=100,
  length=400,
  orient="horizontal",
  variable=progress4_var,
)
progress4_slider.grid(
  column=0, 
  row=7, 
  columnspan=2, 
  padx=10, 
  pady=10
  )

progress4 = ttk.Progressbar(
  window,
  orient="horizontal",
  mode="determinate",
  maximum=100,
  variable=progress4_var,
  length=400,
)
progress4.grid(
  column=0, 
  row=8, 
  columnspan=2, 
  padx=10, 
  pady=10
  )
progress4_label = ttk.Label(
  window, 
  text="Downloading 0%",
  textvariable=progress4_var
  )
progress4_label.grid(
  column=0, 
  row=9,
  columnspan=2, 
  padx=10, 
  pady=10
  )

def handleProgressStart():
  progress4.start()
  progress4_label['text'] = f"{progress4_var} E"

progress4_start_btn = ttk.Button(
  window,
  text="Start",
  command=handleProgressStart
  )
progress4_start_btn.grid(column=0, row=10, columnspan=2)


window.mainloop()