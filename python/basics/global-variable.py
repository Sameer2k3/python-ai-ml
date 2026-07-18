def myfunction():
    global x
    x=78 #global variable
    # global y=78
    y=798 #local variable
    print("hello")

myfunction()
print(x) #although x is decalred in the function but it is treated as the global variable because we have said global x in line 2, pehle decalre kro fir value assign kro but dono saath na kro like in line 4 other wise it is a error
