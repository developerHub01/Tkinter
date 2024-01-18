import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Open File')
    self.geometry('420x550')
    
    tk.Button(self, text="Open File", command=self.handle_open_file).pack(expand=True, padx=10, pady=10)
    tk.Button(self, text="Open Files", command=self.handle_open_files).pack(expand=True, padx=10, pady=10)

  def handle_open_file(self):
    file_types = [
      ('text file', '*.txt'),
      ('Javascript file', '*.js'),
      ('Python file', '*.py'),
      ('All file', '*.*'),
   ]
    
    file_name = fd.askopenfilename(
      title="Open a file",
      initialdir='/',
      filetypes = file_types
    )
    if file_name: 
      showinfo(
          title='Selected File',
          message=file_name
      )

  def handle_open_files(self):
    file_types = [
      ('text files', '*.txt'),
      ('Javascript files', '*.js'),
      ('Python files', '*.py'),
      ('All files', '*.*'),
    ]
    
    file_name = fd.askopenfilenames(
      title="Open a files",
      initialdir='/',
      filetypes = file_types
    )
    if file_name:
      showinfo(
          title='Selected File',
          message=file_name
      )

if __name__ == '__main__':
  app = App()
  app.mainloop()