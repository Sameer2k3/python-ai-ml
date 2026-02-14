# lmbda is used in place of definig  a function
# use lambda when the function defining is in simple one line , avoid if taking multiple input and performing heavy calculatuions else this will make crowd in the code

cube=lambda x:x*x*x   #it will take x as input and return the cube of the x
avg=lambda x,y:(x+y)/2  #it will take xa nd y andf  return the average of it

print(cube(5))   #125
print(avg(8,4))   #6