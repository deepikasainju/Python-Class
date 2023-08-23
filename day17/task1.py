class Department:
    def __init__(self, name, no_of_students):
        self.name=name
        self.no_of_students=no_of_students
        
    def total_students(self,other):
        return f"total no of students in department {self.name} is {self.no_of_students+other.no_of_students}"
    
    def __add__(self,other):
        return self.no_of_students+other.no_of_students
    
d1=Department("CSIT", 24)
d2=Department("CSIT", 24)
print(d1.total_students(d2)) # two objects as arguments

result=d1+d2  # d1 self ma janxa d2 other ma janxa
print(result)