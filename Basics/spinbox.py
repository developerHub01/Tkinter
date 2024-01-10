import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title("Spin box")
window.resizable(False, False)
window.geometry('300x500')


""" 
Syntax:
ttk.Spinbox(master, from_, to, textvariable, wrap)
"""
spin_var1 = tk.StringVar();
spinBox1 = ttk.Spinbox(
    window, 
    from_=0, 
    to=5, 
    textvariable=spin_var1, 
    font='Poppins 13'
  )
spinBox1.pack(fill=tk.X, padx=10, pady=10)
""" 
wrap is a boolean value if True then it enable rotating number changes
that means if we click upward and reach max value then next upword click will redirect to the min value
"""
spin_var2 = tk.StringVar();
spinBox2 = ttk.Spinbox(
    window, 
    from_=0, 
    to=5, 
    textvariable=spin_var2, 
    wrap=True, 
    font='Poppins 13', 
    command=lambda: (
      print(spin_var2.get()),
      print(spinBox2.get())
    )
  )
spinBox2.pack(fill=tk.X, padx=10, pady=10)

spin_var3 = tk.StringVar(value=0)
spinBox3 = tk.Spinbox(
    window, 
    from_=0, 
    to=50, 
    textvariable=spin_var3, 
    values=(0, 10, 20, 30, 40, 50), 
    wrap=True, 
    font='Poppins 13'
  )
spinBox3.pack(fill=tk.X, padx=10, pady=10)


spin_var4 = tk.StringVar()
spinBox4 = tk.Spinbox(
    window, 
    from_="0", 
    to="7",  
    justify="left", 
    textvariable=spin_var4, 
    values=("A", "B", "C", "D", "E", "F", "G", "H"), 
    wrap=True, 
    font='Poppins 13'
  )
spinBox4.pack(fill=tk.X, padx=10, pady=10)

spin_var5 = tk.StringVar()
spinBox5 = tk.Spinbox(
    window, 
    from_="0", 
    to="7",  
    justify="center", 
    textvariable=spin_var5, 
    values=('H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'), 
    wrap=True, 
    font='Poppins 13'
  )
spinBox5.pack(fill=tk.X, padx=10, pady=10)


spin_var6 = tk.StringVar()
spinBox6 = tk.Spinbox(
    window, 
    from_="0", 
    to="7",  
    justify="right", 
    textvariable=spin_var6, 
    values=("Apple", "Banana", "Orange", "Grapes", "Strawberry"), wrap=True, font='Poppins 13'
  )
spinBox6.pack(fill=tk.X, padx=10, pady=10)
# steops number (increment)
spin_var7 = tk.StringVar();
spinBox7 = ttk.Spinbox(
    window, 
    from_=0, 
    to=50, 
    increment=5, 
    justify="center",
    textvariable=spin_var7, 
    wrap=True, 
    font='Poppins 13'
  )
spinBox7.pack(fill=tk.X, padx=10, pady=10)
spinBox7['justify'] = 'center'
spinBox7.pack(fill=tk.X, padx=10, pady=10)
""" 
we also can set values from outside like 

spinBox6["values"] = ("Apple", "Banana", "Orange", "Grapes", "Strawberry")


**************************
from_ ===>> start value
to ======>> end value
wrap ===>> enable rotating of values when got to start or end point
increment ===>> used to determine increment or decrement steps
justify ===>> ['left', 'center', 'center'] any of them to determine alignment of values
values ===>> you can pass values of the spin to sequntial to as an touple Example: values=("Apple", "Banana", "Orange", "Grapes", "Strawberry")


We can also update or pass them after creating the widget like

widget['property_name'] = property_value

Events ==========================
<<Increment>>
<<Decrement>>

"""

spinBox7.bind('<<Increment>>', lambda e: print("up"))
spinBox7.bind('<<Decrement>>', lambda e: print(e))

button1 = tk.Button(
    window, 
    text="Change spin 1 into 3", 
    command=lambda: spin_var1.set(3)
  )
button2 = tk.Button(
    window, 
    text="Change spin 2 into 5", 
    command=lambda: spinBox2.set(5)
  )
button1.pack(fill=tk.X, padx=10, pady=10)
button2.pack(fill=tk.X, padx=10, pady=10)

""" 
get and set current values 

# get
  print(spin_var2.get())
  print(spinBox2.get())
  
# set 
  spin_var2.set("4")
  spinBox2.set(4)
"""

window.mainloop()