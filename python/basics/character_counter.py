s=input()
sl=s.lower()

vowels=0
consonant=0
space=0
digits=0

for c in sl:
    if c in "aeiou":
        vowels+=1
    elif c in "bcdfghjklmnpqrstvwxyz":
        consonant+=1
    elif c==" ":
        space+=1
    elif c in "1234567890":
        digits+=1

print("vowels are ",vowels)
print("consonants are ",consonant)
print("digits are ",digits)
print("spaces are ",space)
