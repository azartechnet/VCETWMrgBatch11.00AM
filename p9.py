def fun1():
    try:
       p1=int(input("Enter the p value is::"))
       c1=p1/0;
       print("Your value is::",c1)
    except ValueError as e1:
        print("Please check the value error",e1)
    except ZeroDivisionError as e2:
        print("Please check the ZeroDivision Error",e2)
    except Exception:
        print("All type exception")
fun1()  
