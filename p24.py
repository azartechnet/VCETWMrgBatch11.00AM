from tkinter import *
def sample():
    sample="You selected the option"+str(radio.get())
    label.config(text=sample)


t1=Tk()
t1.geometry("300x150")
radio=IntVar()
lbl=Label(text="Your Programming language")
lbl.pack()
r1=Radiobutton(t1,text="c",variable=radio,value=1,command=sample)
r1.pack(anchor=W)
r2=Radiobutton(t1,text="java",variable=radio,value=2,command=sample)
r2.pack(anchor=W)
r3=Radiobutton(t1,text="j2ee",variable=radio,value=3,command=sample)
r3.pack(anchor=W)

label=Label(t1)
label.pack()
t1.mainloop()
