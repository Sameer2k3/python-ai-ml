# truncate method limits the byte of the file , like in the below code we can only write 4 bytes that is hell , agaar sample.txt me pahle se koi text hai toh wo 4 byte tak limit ho jaayegi but agar wah pahle se hi 4 byte se kam hai toh required no. of byte hello world se le lega

with open("sample.txt","a") as f:
    f.write("hello world")
    f.truncate(4)
    