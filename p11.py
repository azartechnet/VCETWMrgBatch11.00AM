class Product():
    def addProduct(self,pid,pname):
         print("This is the addProduct modules")
         self.pid=pid
         self.pname=pname
         
    def viewDetails(self):
         print("Your data is::",self.pid,"",self.pname)
s1=Product()
s1.addProduct(1001,"apple")
s1.viewDetails()
