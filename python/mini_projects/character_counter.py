# write a program to count the frequnecy of the letters in a string, also display the max repeating character

s="python is the most popular prooooogramming for the ml"

freq={}

for c in s:
    if c not in freq:
        freq[c]=1
    else:
        freq[c]+=1

print(freq)

max_value=0
max_key=0

for k,v in freq.items():
    if v>max_value:
        max_value=v
        max_key=k

print(max_key, max_value)