class student:
    def __init__(self,name):
        self.name=name

    def change_name(self,newname):
        self.name=newname

s1=student("sameer")
print(s1.name)
s1.change_name("raj")
print(s1.name)
