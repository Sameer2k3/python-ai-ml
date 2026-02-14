a="sameer"
print(a.upper())  #uppper
b="SAMEER"
print(b.lower())   #lower
c="sameerllllllll"
print(c.rstrip('l'))   #rstrip

print(a.replace("sameer","harry"))   #replace
d="my name is sameer"
print(d.split())   #split ,,used to make list of all the words in the string

print(a.capitalize())  #capitalize for first letter capital
print(a.center(12))   #center
e="He is a man who is good"
print(e.count('is'))  #count

print(a.endswith('r'))  #endswith
print(a.startswith('s'))  #startwith
print(e.find('man'))  #find
print(e.isalpha())  #isalpha
f="heis849F"
print(f.isalnum())   #isalnum
g="sameer is good boy"
print(g.islower())  #isllower
print(g.isupper())   #isupper
h="he is a god\n"
print(h.isprintable())  #isprintable
print(h.isspace())  #issapce
print(h.istitle())  #istitle
i="This Is The Example Of Title"
print(i.istitle())  #istitle
print(i.startswith('This'))  #startwith
print(i.swapcase())  #swapcase
print(h.capitalize())   #capitalize