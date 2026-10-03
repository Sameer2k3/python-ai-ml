# map(function, iterable)
# The map() function in Python applies a function to every item in an iterable (such as a list, tuple, or string) and returns a map object (an iterator).

# write a function to return a list of the cube of elements in a list
lst=[1,2,3,4,5]  
cube=list(map(lambda x:x**3,lst)) 
print(cube)

# return a list with increase of 5 in every element from a list
plus5=list(map(lambda x:x+5,lst))
print(plus5)