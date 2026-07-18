def fun(a):
  print(f"multiplication table of {a} is")
 
  try:   
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
        return 1
  except:
    print("invalid input")
    return 0
  finally:
    print("this line runs everytime")

a=input("input the number: ")
fun(a)

#agar  try run hua toh 1 milega and finally bhi run hoga 
#agar try run nhi hua toh  except run hoga but finally bhi run hoga 
# finally run hoga jo bhi ho jaaye
