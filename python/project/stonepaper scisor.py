import random

def check(comp,user):
    if(computer==user):
        return 0
    if(computer=="stone" and user=="scissor"):
        return -1
    if(computer=="paper" and user=="stone"):
        return -1
    if(computer=="scissor" and user=="paper"):
        return -1
    else:
        return 1
    
 
options = ["stone", "paper", "scissor"]

computer = random.choice(options)
user=input("enter your choice--->>>")
print(f"computer has chosen {computer}")

score=check(computer,user)
if(score==0):
    print("its a draw")
if(score==1):
    print("you won")
if(score==(-1)):
    print("computer won")

