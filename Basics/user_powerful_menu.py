import tkinter as tk
from tkinter import ttk, Menu
from tkinter.messagebox import askyesno

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Menu')
    self.geometry('420x450')
    
    self.menubar = Menu(self)
    self.config(menu=self.menubar)

    self.foramt_var = tk.IntVar(value=1)
    self.statusbar_var = tk.IntVar(value=1)
    
    """ 
    This is a reuseable menu. just call the method and pass the list of menu items. 
    """
    
    menu_list = [
      {
        "label": "File",
        "children":[
          {
            "label": "New File",
            "accelerator": "Ctrl+N",
            "command": self.handle_new_file,
          },
          {
            "label": "New Window",
            "accelerator": "Ctrl+Shift+N",
            "command": self.handle_new_window
          },
          {
            "label": "Open...",
            "accelerator": "Ctrl+O",
          },
          {
            "label": "Save",
            "accelerator": "Ctrl+S",
          },
          {
            "label": "Save As...",
            "accelerator": "Ctrl+Shift+S",
          },
          None,
          {
            "label": "Page Setup...",
            "accelerator": None,
          },
          {
            "label": "Print...",
            "accelerator": "Ctrl+P",
          },
          None,
          {
            "label": "Exit",
            "command": self.handle_exit
          },
        ]
      },
      {
        "label": "Edit",
        "children":[
          {
            "label": "Undo",
            "accelerator": "Ctrl+Z",
            "command": self.handle_undo,
          },
          None,
          {
            "label": "Cut",
            "accelerator": "Ctrl+X",
          },
          {
            "label": "Copy",
            "accelerator": "Ctrl+C",
          },
          {
            "label": "Past",
            "accelerator": "Ctrl+V",
          },
          {
            "label": "Delete",
            "accelerator": "Del",
          },
          None,
          {
            "label": "Search with Bing...",
            "accelerator": "Ctrl+E",
          },
          {
            "label": "Find..",
            "accelerator": "Ctrl+F",
          },
          {
            "label": "Find Next",
            "accelerator": "F3",
          },
          {
            "label": "Find Previous",
            "accelerator": "Shift+F3",
          },
          {
            "label": "Replace..",
            "accelerator": "Ctrl+H",
          },
          {
            "label": "Got To...",
            "accelerator": "Ctrl+G",
          },
          {
            "label": "Got To...",
            "accelerator": "Ctrl+G",
          },
          None,
          {
            "label": "Select All",
            "accelerator": "Ctrl+A",
          },
          {
            "label": "Time/Date",
            "accelerator": "F5",
          },
        ]
      },
      {
        "label": "Format",
        "children":[
          {
            "label": "Word Wrap",
            "type": "checkbutton"
          },
          {
            "label": "Font...",
          },
        ]
      },
      {
        "label": "View",
        "children":[
          {
            "label": "Zoom",
            "command": None,
            "children":[
                {
                  "label": "Zoom In",
                  "accelerator": "Ctrl+Plus",
                  "command": lambda: print("Zoom in"),
                },
                {
                  "label": "Zoom Out",
                  "accelerator": "Ctrl+Minus",
                  "command": lambda: print("Zoom out"),
                },
                {
                  "label": "Restore Default Zoom",
                  "accelerator": "Ctrl+0",
                  "command": lambda: print("Default Zoom"),
                },
              ]
          },
          {
            "label": "Status Bar",
            "type": "checkbutton"
          },
        ]
      },
      {
        "label": "Help",
        "children":[
          {
            "label": "View Help",
          },
          {
            "label": "Send Feedback",
          },
          {
            "label": "About Notepad",
            "children":[
              {
                "label": "View Help",
              },
              {
                "label": "Send Feedback",
              },
              {
                "label": "About Notepad",
                  "children":[
                    {
                      "label": "View Help",
                    },
                    {
                      "label": "Send Feedback",
                    },
                    {
                      "label": "About Notepad",
                    },
                  ]
              },
            ]
          },
        ]
      },
    ]
    self.generate_menu(self.menubar, menu_list)
  
  def get_dict_value(self, dict, key):
    value = None
    try:
      value = dict[key]
    except:pass
    return value
  
  def generate_menu(self, parent, menu_list):
    for item in menu_list:
      label = self.get_dict_value(item, "label")
      accelerator = self.get_dict_value(item, "accelerator")
      children = self.get_dict_value(item, "children")
      command = self.get_dict_value(item, "command")
      type = self.get_dict_value(item, "type")
      
      menu = Menu(
          parent,
          tearoff=0
      )
      
      if children:
        self.generate_menu(menu, children)
        parent.add_cascade(
            label=label,
            menu=menu
        )
      elif  not item:
        parent.add_separator()
      elif type == "checkbutton":
        parent.add_checkbutton(
          label=label,
          accelerator=accelerator,
          command=command
        )
      elif type == "radiobutton":
        parent.add_radiobutton(
          label=label,
          accelerator=accelerator,
          command=command
        )
      else:
        parent.add_command(
          label=label,
          accelerator=accelerator,
          command=command
        )

  def handle_exit(self):
    response = askyesno(
      title="Confirm",
      message="Are you sure to exit?"
    )
    if response:
      self.destroy()

  def handle_new_window(self):
    App()

  def handle_new_file(self):
    pass

  def handle_undo(self): 
    pass  

if __name__ == '__main__':
  app = App()
  app.mainloop()