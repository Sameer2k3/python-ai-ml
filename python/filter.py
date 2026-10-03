# WRITE A FUNCTION TO FILTER THE EVEN ELEMENTS FROM A LIST
lst=[1,2,3,4,5,6]
even=list(filter(lambda x: x%2==0, lst))
print(even)