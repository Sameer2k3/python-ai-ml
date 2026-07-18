s1={1,2,5,6}
s2={3,6,7}
s2.add(8)   #adds elemts in the set
s2.remove(8)  #removes a element
s2.pop()   #pop removes any one elemnet randomly
print(s1.union(s2))   #gives union
print(s1,s2)
s1.update(s2)  #puts the items of s2 in s1
print(s1)

city1={"a","b","c","d"}
city2={"a","b","e","f","g"}
city3=city1.symmetric_difference(city2)  #gives all the elemnts which are only in one set
print(city3)
print(city1.intersection(city2))  #gives intersection
city1.intersection_update(city2)  #puts all intersected value in city1 and deletes the old ones
print(city1)
city3.clear()  #clears all the elements in the set and make it empty set
print(city3)
del city3  #del deletes a set completley
print(city3)

#some more methods
 # isdisjoint()
 #issuperset()
 #issubset()
 