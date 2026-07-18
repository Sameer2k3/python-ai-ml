a=int(input("give nuber between 1 to 5 "))
if(a<1 or a>5):
    raise ValueError("value is not between 1 to 5")
else:
 print("you entered correct value")


print("now raising error for the string")

b=str(input("enter your name \n"))
if(b=="sameer"):
   print("correct name")

else:
   raise ValueError("that not your name")