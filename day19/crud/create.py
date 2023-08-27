import json
import os

filename="students.json"

def create_student():
    id=input("enter student id:")
    name=input("enter name:")
    age=input("enter age:")

    student=dict(id=id, name=name, age=age)
    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            data=json.dumps([student], indent=2)#list ma halda new data add garda students.json ma overwrite nagari add hunxa
            fp.write(data)
    
    else:
        with open(filename, "r+") as fp:
            students=json.loads(fp.read())
            students.append(student)
            fp.seek(0)
            fp.write(json.dumps(students,indent=2))

    print("student added successfully")
    repeat=input("Do you want to continue? (y/n):")
    return True if repeat.lower()=='y' else False

