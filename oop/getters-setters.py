# in python getters and settters  is the method used to access and modify the attributes of a class
#use the __init__  method when we know that we must provide value to the each varible , if any varibale is being not giving a value then use  getters and setters kyuki isme agar hum koi ek variobale ko value na bhi de toh bhi chalta hai
#jais ki niche code me hum name ko toh value de rhe hai (line 17) but age ko koi value nhi de rhe hai

class student:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    
    def set_age(self,age):
        self.age=age
    def get_age(self):
        return self.age

s1=student()
s1.set_name("sameer")  #here i have given a value to be stored in the varible name using the setter
print(s1.get_name())  #getter id being called