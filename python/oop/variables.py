#there are 2 variables ---- class variables and instance variables

class student:
    college="iit"
    # college is a class variable
    def __init__(self,name):
        # name is instance variable
        self.name=name


s1=student("sameer")
print(s1.name , s1.college)

s1.college="nit"
print(s1.name , s1.college)
