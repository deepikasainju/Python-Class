from main import session, Student

result=session.query(Student).all() #databases ko data list ma aauxa result
print(result)
s1=result[0]
print(s1.name)
for student in result:
    print(student.name)
    print(student.age)

# particular data lai filter garera data print gareko
# filtering particular data from the table
student=list(session.query(Student).filter(Student.id==2)) # ORM
print(student) # list vitra student ko object aauxa veuta row
student=student[0]
print(student.name)
print(student.age)

# updating a data in a row
session.query(Student).filter(Student.id==3).update({"name":"Lara"})
session.commit()

# deleting a row in the table 
session.query(Student).filter(Student.id==3).delete()
session.commit()
print("row3 has been deleted.")

#raw q uery use nagarna ORM use garinxa
