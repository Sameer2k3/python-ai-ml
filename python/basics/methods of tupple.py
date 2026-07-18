#tuple se list banao then list ko modify kro then usey tuple banao
countries=("india","china","france")
a=countries.count("india")
print(a)

temp=list(countries)

temp.append("russia")  #add items

temp.pop(2)   #remove items

temp[2]="finland"    #change items

countries=tuple(temp)

print(countries)
