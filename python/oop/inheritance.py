#Inheritance allows a child class to use properties and methods of a parent class.
# It helps in code reusability and makes programs more structured.
 
class employee:
    def __init__(self,name,id):
        self.name= name
        self.id= id
    
    def showdetails(self):
        print(f"the name of the employe {self.id} is  {self.name}")


e1=employee("sameer",420)
e1.showdetails()

#suppose agar koi ab kahe ki class ka name employee se change krke ab programmer krdo toh pura code me hume employee ki jagah programmer likhna padega , so there we use the inheritance 


# from line 21 ek new class ban gya who has all the data of the employee class as well as the data which is being going to be givern in the programmer, it is like programmer is the son and employee is the father class

class programmer(employee):
    def showlanguage(self):
        print(f"the language of {self.name} is the python")

e2=programmer("rohan",78)
e2.showlanguage()