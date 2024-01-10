import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb

""" 
Event details resource: https://www.pythontutorial.net/tkinter/tkinter-event-binding/
"""

'''
Widget.bind(event, function)
format: modifier-type-detail

Alt-Keypress-a
'''

# window = tk.Tk()
window = ttkb.Window(themename='flatly')
window.geometry('600x500')
window.title('Event Binding')

text = ttkb.Text(window)
text.pack()

entry = ttkb.Entry(window)
entry.pack()

btn = ttkb.Button(window, text='A button')
btn.pack()
""" 
window.bind('<KeyPress>', lambda e: print('Event called'))
window.bind('<Alt-KeyPress>', lambda e: print('Event called'))
window.bind('<KeyPress-a>', lambda e: print('Event called'))
window.bind('<Alt-KeyPress-a>', lambda e: print('Event called'))
 """
window.bind('<Alt-KeyPress-a>', lambda e: print(e))
""" 
<KeyPress event send_event=True state=Mod1|0x20000 keysym=a keycode=65 char='a' x=18 y=73>
"""

# work whenever btn is selected......... :)
btn.bind('<Alt-KeyPress-a>', lambda e: print(e))
btn.bind('<Enter>', lambda e: print(f'x={e.x} y={e.y}'))
btn.bind('<Enter>', lambda e: print(f'IsFocused={e.focus}'), add='+')
"""
To use multiple handle function for same widget and same event we add='+' that enable to handle muliple handler function  
"""
btn.bind('<Leave>', lambda e: print(f'x={e.x} y={e.y}'), add='+')
window.bind('<Motion>', lambda e: print(f'x={e.x} y={e.y}'), add='+')

window.bind('<Control-KeyPress-c>', lambda e: print('Ctrl+c'))
window.bind('<MouseWheel>', lambda e: print(e))
window.bind('<Alt_L>', lambda e: print('Alt+L'))
window.bind_class('Entry', 'Control-V', lambda e: print(e))

# exercise 
text.bind('<Shift-MouseWheel>', lambda e: print('MouseWheel'))

window.mainloop()