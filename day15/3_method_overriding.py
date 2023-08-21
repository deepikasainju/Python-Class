class Vehicle:
    def __init__(self,color,doors):
        self.color=color
        self.doors=doors
    
    def get_details(self):
        return f"color is {self.color} and no of doors is {self.doors}"
    
class Bike(Vehicle):
    def __init__(self, color, doors, milage, company): # parent ko init lai child ley override gareko xa
        super().__init__(color,doors) #child bata parent lai call garna parda super use garxam
        # yesto garda Vehicle object banayera inherit gareko jasto hunxa
        self.milage=milage
        self.company=company

    def get_details(self):
        print(super().get_details()) # inherit the get_details method of Vehicle (parent class)
        return f"milage is {self.milage} and company is {self.company}" 


b1=Bike("red", 3, 45,"yamaha")
print(b1.get_details())

# overriding ko help ley extra details ni thapna milxa