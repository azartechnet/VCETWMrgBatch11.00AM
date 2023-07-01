def fun1():
    try:
        p=int(input("Enter the p value is::"))
        a=p/0;
        print("Your value is::",a)
        fun2()
    except ZeroDivisionError:
        print("Please check the number")
    fun2()
def fun2():
    print("Your function")
fun1()
    
