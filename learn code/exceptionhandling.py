a=input("input the number: ")
print(f"multiplication table of {a} is")
 
try:   
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except:
    print("invalid input")

print("code end")

#summary
# agar try k andar ka code sahi hai toh run ho jaaye otherwise except want code run hoga aur saath me uske baad ki bhi line run hogi
# this  is used so that we can move forward agar koi wrong code mil jaye