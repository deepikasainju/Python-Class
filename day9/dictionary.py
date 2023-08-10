# dictionary are mutable in python in key-value pair format

#creating empty dictionary
a=dict()
print(a)
a={}
print(a)

# creating non empty dictionary 
student={"name":"Ram", "age":35,"address":"KTM"}
print(student)

student=dict(name="Ram",age=35,address="KTM")
print(student)

data={"phone no":8347893}
# data=dict(phone no=3748239) yesari mildaina
data=dict(phone_no=623379)

data=dict({"name":"Ram", "age":35,"address":"KTM"}) #yesari hgarda ni milxa tara yesari garirakhna pardaina 
# becuz dict narakhe ni tyo dictionary nai ho
print(data)

