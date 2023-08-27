import json
filename="students.json"

def update_student(student_id):
    with open(filename, "r+") as fp:
        students=json.loads(fp.read())
        student=list(filter(lambda x: x['id']==student_id, students))
        if student:
            student=student[0]
            index=students.index(student) # a.index(3)
            print(f"index={index}")

            new_value=input("enter the new value:")
            key=input("enter info you want to update:")
            student[key]=new_value
            students[index]=student # change garne key ma new value haleko
            fp.seek(0)
            fp.write(json.dumps(students, indent=2))
            print("students updates successfully!!")

        else:
            print("no student of this id.")

    repeat=input("Do you want to continue? (y/n):")
    return True if repeat.lower()=='y' else False
