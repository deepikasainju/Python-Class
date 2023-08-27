import json
filename="students.json"

def read_student(student_id):
    with open(filename,"r") as fp:
        students=json.loads(fp.read())
    
    # for x in students:
    #     if x['id']==student_id:
    #         print(x)

    student=list(filter(lambda x:x['id']==student_id , students))
    if student:
        student=student[0]
        print(student)
    else:
        print("no student of this id.")

    repeat=input("Do you want to continue? (y/n):")
    return True if repeat.lower()=='y' else False
