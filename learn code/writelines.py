f=open("myfile2.txt","w")
line=["SAMEER\n","rohan\n","aryan\n"]
f.writelines(line)
f.writelines("teri ma bhosda\n kyu re madharchod")
f.close()


# we ca use both line 2 and line 4 to write a line in outer file 
# in first line agar i used "r" instead of "w" the myfile.txt will not be created if it dont exist but i the w mode it get created if dont exist





# readline is used to  read lines line by line  whereas writeline writes a line in the external file