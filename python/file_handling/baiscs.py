# writing a data in a file
file = open ("sample.txt", "w")
file.write("Hello ")
file.write("world\n")
file.write("how are u??")
file.close()

# reading the file
f=open("sample.txt", "r")
data=f.read()
print(data)

data1=f.readlines()
print(data1)
