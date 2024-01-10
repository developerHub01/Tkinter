import tkinter as tk 
from tkinter import ttk

'''
Button 
CheckButton 
RadioButton

to use them we need tkinter variables
'''

window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')


'''
def button_fun(text):
  print(text) 
## with lamda function
button = ttk.Button(window, text='A Single Button', command=lambda: print('hello'))


## pass a argument using lamda function
button = ttk.Button(window, text='A Single 
Button', command=lambda: button_fun('hello'))

'''

# button ==========================================
def button_fun():
  print(button_string.get()) 
  print(check_var.get())
  print(radio_var.get())
  
button_string = tk.StringVar(value='A Single Button with string var')
button = ttk.Button(window, text= 'A Single Button', textvariable=button_string, command=button_fun)
button.pack()

# checkbox ==========================================
def check_fun():
  pass

# for check box
# check_var = tk.StringVar() # output as 0/1
# check_var = tk.BooleanVar() # Output as True/False
# check_var = tk.DoubleVar() # Ouput as 0.0/1.0
check_var = tk.IntVar() # output as 0/1
check = ttk.Checkbutton(window, text='Check Box 1', command=lambda: print(check_var.get()), variable=check_var)
check.pack()


'''
As well as we can use onvalue and offvalue to fixed any value for on or off
'''

check_var2 = tk.IntVar()
check2 = ttk.Checkbutton(window, text='Check Box 2', command=lambda: print(check_var2.get()), variable=check_var2, onvalue=10, offvalue=5)
check2.pack()

check_var3 = tk.StringVar()
check3 = ttk.Checkbutton(window, text='Check Box 3', command=lambda: print(check_var3.get()), variable=check_var3, onvalue="on", offvalue="off")
check3.pack()

check_var4 = tk.BooleanVar()
check4 = ttk.Checkbutton(window, text='Check Box 4', command=lambda: print(check_var4.get()), variable=check_var4, onvalue=True, offvalue=False)
check4.pack()


# radio buttons ==========================================
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window, 
    text='radio 1',
    value='option 1',
    variable=radio_var,
    command=lambda: print(radio_var.get())
  )
radio2 = ttk.Radiobutton(
    window, 
    text='radio 2',
    value='option 2',
    variable=radio_var,
    command=lambda: print(radio_var.get())
  )
radio3 = ttk.Radiobutton(
    window, 
    text='radio 3',
    value='option 3',
    variable=radio_var,
    command=lambda: print(radio_var.get())
  )
radio1.pack()
radio2.pack()
radio3.pack()




# exercise ===================================
result_label = tk.Label(window, text="Result")
result_label.pack()
exCheck_var = tk.BooleanVar(value=False)
exCheck = tk.Checkbutton(window, text="Check Button 1", command=lambda: result_label.configure(text = exradio_var.get()), variable=exCheck_var)
exCheck.pack()
exradio_var = tk.IntVar()
exradio1 = tk.Radiobutton(window, text="radio 1",value=1, variable=exradio_var, command=lambda: (exCheck_var.set(0), result_label.configure(text="")))
exradio1.pack()
exradio2 = tk.Radiobutton(window, text="radio 2",value=2, variable=exradio_var, command=lambda: (exCheck_var.set(0), result_label.configure(text="")))
exradio2.pack()
exradio3 = tk.Radiobutton(window, text="radio 3",value=3, variable=exradio_var, command=lambda: (exCheck_var.set(0), result_label.configure(text="")))
exradio3.pack()
window.mainloop()