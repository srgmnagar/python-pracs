class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):    
        return 2*(self.length+self.breadth)

obj1=rectangle(2,6)
print(obj1.area())
print(obj1.perimeter())