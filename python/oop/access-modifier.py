#in Python, access specifiers (also called access modifiers) define how accessible class attributes (variables) and methods are from outside the class.
# Unlike languages such as Java or C++, Python doesn’t have strict keywords like private or protected. Instead, it follows naming conventions (with underscores) to indicate the level of access.

class employee:
    def __init__(self):
        self.__name="sameer"  #private  (cant be accessed outside the class)
        self._age=47  #protected (can be accessed in same class or subclass)

a=employee()

print(a._age)
# print(a.__name)  #cant  be accesed directly because of name mangling
print(a._employee__name)   # but can be accessed indirectly
