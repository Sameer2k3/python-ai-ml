# enumerate is used to read or dispaly the index of a list or tupple so that we dont need to do that manually
fruits=["apple","banana","orange","mango","kiwi"]
for index,fruit in enumerate(fruits,start=1):
    print(index, fruit)
    if(index==4):
        print("this is the king of the fruits")
 