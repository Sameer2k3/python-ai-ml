ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.update(ep2)   #update ep1 with ep2 items
print(ep1)
# ep1.clear()  #clears the ep1
# print(ep1)
empt={}  #empty dictionary created
ep1.pop(122)  #pop removes the key and its value
print(ep1)
ep1.popitem()   #removes the laast item from the dictionary
# del ep1   #delets the dictonary entirely
#del ep1[122]   deletes the 122 key and its value from the dictionary, but don nont deletes the whole dictionary
