# seek functions moves the pointer by n bytes
#  whereas tell function tells us where the pointeer or cusor is

with open("file1.txt","r") as f:
    print(type(f))

    # move toh the 10th byte of the file
    f.seek(10)
    print(f.tell())  #this tells us wehre the pointer is currently placed
    

    # read next 5 bytes
    data=f.read(5)
   
    print(data)