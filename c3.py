from tkinter import*
p=Tk()
name=Label(p,text="Name").grid(row=0,column=0)
e1=Entry(p).grid(row=0,column=1)
password=Label(p,text="Password").grid(row=1,column=0)
e2=Entry(p).grid(row=1,column=1)

submit=Button(p,text="Submit").grid(row=4,column=0)

Reset=Button(p,text="Reset").grid(row=4,column=1)

p.mainloop()
