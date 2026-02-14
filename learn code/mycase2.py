
   #multiple deafult cases........

x=int(input("enter the number"))
match x:
    case 1:
        print("the number is 1")
    case 2:
        print("the number is 2")
    case _ if x==10:
        print("the numner is 10")
    case _ if x==20:
        print("its 20")
    case _:
        print("the number is",x)
         