f = open("marks.txt", "r")   # open file in read mode
i = 0
while True:
   i = i + 1
   line = f.readline()       # read one line
   if not line:              # if line is empty → end of file
     break
   
   # split line into parts
   m1 = int(line.split(",")[0])   # first number → maths
   m2 = int(line.split(",")[1])   # second number → gk
   m3 = int(line.split(",")[2])   # third number → sst
   
   # printing
   print(f"marks of the student {i} in the maths is {m1}")
   print(f"marks of the student {i} in the gk is {m2}")
   print(f"marks of the student {i} in the sst is {m3}")
   print(line)
