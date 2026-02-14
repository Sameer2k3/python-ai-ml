#docstring used to siaply the working of a function it is same as comment , but it can be printed by calling i, by __.doc__
def add(a,b):
    '''takes two values and
      return their sumation'''
   
    c=a+b
    print(c)

add(5,15)
print(add.__doc__)