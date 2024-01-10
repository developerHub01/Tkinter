import tkinter as tk 
from tkinter import ttk

window = tk.Tk()
window.title('button function and args')

'''
Way One ==================
'''
def test_fun1(data):
  print(data)

entry_string = tk.StringVar()
entry = ttk.Entry(window, text='button', textvariable=entry_string)
entry.pack()
button1 = ttk.Button(window, text="button 1", command = lambda: test_fun1(entry_string.get()))
button1.pack()

'''
Way Two ==================
'''

def test_fun2(data):
  def test_fun():
    print(data.get())
  return test_fun

button2 = ttk.Button(window, text="Button 2", command=test_fun2(entry_string))
button2.pack()

window.mainloop()