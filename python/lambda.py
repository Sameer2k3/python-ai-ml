# lambda dunction-->>anonymouse function
sq=lambda x:x*x
print(sq(5))

# sum of two int
sum=lambda x,y:x+y
print(sum(6,7))

# max of two numbers
max=lambda x,y:x if x>y else y
print(max(5,9))

# even odd checking
check=lambda x:"Even" if x%2==0 else "Odd"
print(check(8))

# function to return the last character of a string
last=lambda s:s[-1]
print(last("sameer"))