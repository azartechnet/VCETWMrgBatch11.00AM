from tkinter import Toplevel,Button,Tk,Menu

top=Tk()

menubar=Menu(top)

file=Menu(menubar,tearoff=0)

file.add_command(label="New")

file.add_command(label="Open")

file.add_command(label="Save")

file.add_separator()

file.add_command(label="Exit",command=top.quit)

menubar.add_cascade(label="File",menu=file)

top.config(menu=menubar)

top.mainloop()
