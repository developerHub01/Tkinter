import tkinter
import pyshorteners

root = tkinter.Tk()
root.title('URL SHortener')
root.geometry('300x150')

frame = tkinter.Frame(root)

def short_url():
  input_url = longurl_entry.get()
  shortener = pyshorteners.Shortener()
  shorturl_entry.insert(0, shortener.tinyurl.short(input_url))

longurl_label = tkinter.Label(frame, text="Enter long URL")
longurl_entry = tkinter.Entry(frame)

shorturl_label = tkinter.Label(frame, text='Output short URL')
shorturl_entry = tkinter.Entry(frame)

shorten_button = tkinter.Button(frame, text="Short", command=short_url)

frame.pack()
longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()


root.mainloop()