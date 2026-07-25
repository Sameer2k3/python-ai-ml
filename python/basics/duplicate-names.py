# take names of students and remove the duplicate names while preserving the first occurance

names=input().split()

unique_names=[]
for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)
