import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, askquestion

window = tk.Tk()
window.title('Treeview')
window.geometry('600x500')
window.resizable(False, False)

columns = ('first_name', 'last_name', 'email')

tree = ttk.Treeview(window, columns=columns, show='headings')
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

tree.column("first_name", width='200', anchor='center')
tree.column("last_name", width='200', anchor='center')
tree.column("email", anchor='center')

userData = []
for i in range (1, 201):
  userData.append((f'first name {i}', f'last name {i}', f'email{i}@gamil.com'))

for data in userData:
  tree.insert(parent='', index=tk.END, values=data)

tree.pack(fill='both', expand=True)

def delete_items():
  selected_data = tree.selection();
  if not selected_data:
    return;
  
  response = askquestion(
    title="Are you sure?",
    message= "Are you sure to remove them from list?"
  )
  if response == "no":
    return;
  
  for single_data in tree.selection():
    tree.delete(single_data)

# delete operations =====================
tree.bind('<Delete>', lambda e: delete_items())

window.mainloop()