# In Python, a constructor is a special method that gets called automatically when an object of a class is created.

# 👉 The constructor method is always written as __init__.

class person:
    def __init__(self,n,o):    #__init__ is used for constructor
        print("hey i am a person")
        self.name=n
        self.occupation=o

    def info(self):
        print(f"{self.name} is a {self.occupation}")



a=person("sameer","developer")  #haary and developer will be stored in the n and o
b=person("shreya","doctor")   #same here

a.info()
b.info()