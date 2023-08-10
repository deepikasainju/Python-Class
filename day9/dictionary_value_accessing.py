#accessing elements of dictionary is similar to that of list. 
# we use keys for indexing

student={"name":"Ram", "age":35,"address":"KTM"}
print(student["name"]) #"name is key"

print(student["age"])
print(student["address"])
# print(student["phone"])  ###key error


## we can also access dictionary values using get() method
name=student.get("name")
print(name)

phone=student.get("phone")
print(phone) #no error it gives none due to use of get


#adding key-value pair in dictionary
student={"name":"Ram", "age":35,"address":"KTM"}
student["phone"]="747984982784" #phone no add hunxa student dictionary ma
print(student)

other_info={"email":"ah@gamil.com","roll":12}
student.update(other_info) #other info wala dictionary pani student ma add vayera aauxa
# {'name': 'Ram', 'age': 35, 'address': 'KTM', 'phone': '747984982784', 'email': 'ah@gamil.com', 'roll': 12}
print(student)

#updating
student["name"]="john"
print(student) #name wala ma john vayra print hunxa


#removing key-value pair from a dictionary
student={'name': 'Ram', 'age': 35, 'address': 'KTM', 'phone': '747984982784', 'email': 'ah@gamil.com', 'roll': 12}
email=student.pop("email")
print(student)
print(email)

# school=student.pop("school") ##key error
school=student.pop("school","sm")  
print(school) # sm defaultly aauxa mathi sm rakheko ley

#popitem()
student={'name': 'john', 'age': 35, 'address': 'KTM', 'phone': '747984982784', 'email': 'ah@gamil.com', 'roll': 12}
result=student.popitem() #last ko item delete garxa
print(result)
print(student)


student.clear() #delete whole dictionary elements
print(student)