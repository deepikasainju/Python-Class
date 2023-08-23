# create a circle with an attribute radius. 
# create 2 objects of circle c1 and c2 .add the radius of circle and print
# do above using method and then magic method

class Circle:
    def __init__(self, radius):
        self.radius=radius
    
    def add_radius(self,other):
        return self.radius+other.radius
    
    def __add__(self,other):
        return self.radius+other.radius
    
    def __gt__(self,other): # gt is for comaprison means greater than
        return self.radius>other.radius
        # if self.radius>other.radius:
        #     return f"circle with radius {self.radius} is greater"
        # elif self.radius<other.radius: 
        #     return f"circle with radius {other.radius} is greater"
        # else:
        #     return f"both circle are same size"
    
c1=Circle(2)
c2=Circle(6)
print(c1.add_radius(c2))

result=c1+c2
print(result)

result=c1>c2
print(result) # False
