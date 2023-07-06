from tkinter import*
p=Tk()
redbutton=Button(p,text="Red",fg="red")
redbutton.pack(side=LEFT)
greebutton=Button(p,text="Green",fg="green")
greebutton.pack(side=RIGHT)
bluebutton=Button(p,text="Blue",fg="blue")
bluebutton.pack(side=TOP)
p.mainloop()
