class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.height*self.width

a=rectangle(5,4)
print(a.area())