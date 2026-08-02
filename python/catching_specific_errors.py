# try:
#     n=int(input("enter the number: "))
#     print((100/n))
# except Exception as e:
#     print(e)

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)
    a=[1,2]
    print(a[3])
except ValueError:
    print("Invalid input. Enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("some error has occured")