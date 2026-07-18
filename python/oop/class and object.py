class person:
    name="sameer"
    occupation="berojgaar"
    networth=0
    def info(self):  # self indicates that the data extracted should be extracted from the current class it is written
        print(f"{self.name} is a {self.occupation}")


a=person()
print(a.name)
a.name="harry"  #used ot change the data in the class
print(a.name)

b=person()
b.name="shreya"
b.occupation="whore"
b.networth=6000

a.info()
b.info()

# A class serves as a blueprint or a template for creating objects. It defines the structure and behavior that objects of that class will possess. In simpler terms, it's a user-defined data type that encapsulates data (attributes) and functions (methods) into a single unit.

# An object is an instance of a class. It is a concrete realization of the blueprint defined by the class, meaning it has its own unique set of attribute values and can execute the methods defined in its class. You can create multiple objects from a single class, each with its own distinct state.