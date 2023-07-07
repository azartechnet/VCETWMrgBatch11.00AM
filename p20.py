from tkinter import*
top=Tk()

def home():
    print("Home")
def addProduct():
    print("addProduct")
def viewProduct():
    print("ViewProduct")

#Create a toplevel menu

menubar=Menu()
menubar.add_command(label="Home",command=home)
menubar.add_command(label="AddProduct",command=addProduct)
menubar.add_command(label="ViewProduct",command=viewProduct)


#display the menu
top.config(menu=menubar)

top.mainloop()
