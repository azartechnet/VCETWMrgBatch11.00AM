def fun1():
    try:
        pid=int(input("Enter the value is::"))
        print("Your value is::",pid)
        fun1()
    except NameError:
        print("please check the value")
fun1()
