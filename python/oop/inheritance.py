# inheritance is the property of aquiring all the property of  the parent class

class person:
    def __init__(self,first_name,last_name):
        self.firstname=first_name
        self.lastname=last_name

    def showname(self):
        print(self.firstname,self.lastname)

p1=person("sameer","yadav")
p1.showname()

class student(person):
    college="iit madras"

s1=student("ram","kumar")
s1.showname()
print(s1.college)