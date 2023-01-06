from tkinter import Text
from tkinter import *

root = Tk()
root.title("Text Box / GUI Frame")
root.geometry("300x300")
root.resizable(height=False,width=False)
root['bg']= 'blue'


edit = Text(root, height=5,width=10)
edit.pack(padx=5,pady=5)
edit.place(x=115,y=100)
edit.insert(END, "")

btn = Button(root, fg="red",text="submit",padx=5,pady=3)
btn.pack(padx=5,pady=3)
btn.place(x=110,y=200)

root.mainloop()