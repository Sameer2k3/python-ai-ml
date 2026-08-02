#try ,except,else
#try,except,finally

try:
    a=int(input())
except ValueError:
    print("invalid input")
finally:
    print("Program finished")