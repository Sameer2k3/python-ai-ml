f=open("file.txt","r")
while True:
    line=f.readline()     #readline reads one line at a time 
    print(line)
    if not line:
        print(line)
        print(type(line))
        break
   
    