##Function
def add(a,b):
    return a+b
print(add(1,2))


##Method
class Student:
    def age_after_ten_years(self,current_age):
        return current_age +10
    
s=Student()
age_after_ten_years=s.age_after_ten_years(10)
print(age_after_ten_years)
#age_after_ten_years() is amthod of class Student which can be called using object s 

