class Demo():
    def input(self):
        self.pid=int(input("Enter the value is::"))
    def disp(self):
        print("Your value is::",self.pid)
    def __init__(self):
        print("This is default method")
    
f1=Demo()
f1.input()
f1.disp()
