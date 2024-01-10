import tkinter as tk


# create a window
window = tk.Tk()
window.title('Window and widgets')
window.geometry('800x500')


# create widgets
textarea = tk.Text(master=window, font='Poppins 16')
textarea.pack()

# run 
window.mainloop()