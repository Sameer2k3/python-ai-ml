# file handling me mainly 3 mode hote hai "a" for append, "r" for read, w" for write only
# r me sirf file read hoga
# w me sirf write hoag by deletimng the existint data
# a me bhi read write hoga but existinga data delete nhi hota hai , simnply overwrite hota hai
# agar file open kre toh close bhi karna padta hai but we can avoid that by using "with" like in line 36







f=open('text.txt','r')  # r for read only and w for write only
# r mode is default if nothing writeen

text=f.read()
print(text)
f.close()

# agar w mode me humne aisi fileko open kra jo exisst na krti ho to wo  file create ho jayegi

f=open("random.text","w")  # since so file is created by me so random.txt willbe created by the pyhton




# below is method to write in a file

h=open("a.txt","a") # "a" use krne par jab hum file me write karenge toh date a.txt file me add hote jaayega aur pichla data bhi pada rhega
h.write("sameer is learning pythom from the code with harry\n")
h.close()  #close karna jaruri hai


# below id the code if we do not wan to write close() in the code and also append the code

with open("b.txt","a") as j:
    j.write("hello everyone this is sameer from the azamgarh\n")
    # everyone time this code runs it add the above string in the b.txt file