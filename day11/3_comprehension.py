# list comprehension
square=[]
for i in range(1,6):
    square.append(i**2)
print(square)

square=[i**2 for i in range(1,6)]
print(square)

# didtionary comprehension
square_dict={}
square_dict={k:k**2 for k in range(1,6)}
print(square_dict)

student_list=[("name","jane"),("age",25),("address","KTM")]
stuent=dict(student_list)

student={k:a for k,a in student_list}
print(student)

