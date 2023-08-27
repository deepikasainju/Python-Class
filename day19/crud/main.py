from create import create_student
from read import read_student
from update import update_student
from delete import delete_student

def inquiry():
    selection=input("enter your choice c/r/u/d/e:")
    selection=selection.lower()

    def exit_message():
        print("thank you. byeeeeeee!!!!!")

    if selection=="c":
        repeat=create_student()
        inquiry() if repeat else exit_message()

    elif selection=="r":
        student_id=input("enter the student id:")
        repeat=read_student(student_id)
        inquiry() if repeat else exit_message()

    elif selection=="u":
        student_id=input("enter the student id:")
        repeat=update_student(student_id)
        inquiry() if repeat else exit_message()

    elif selection=="d":
        student_id=input("enter the id of data to be deleted:")
        repeat=delete_student(student_id)
        inquiry() if repeat else exit_message()

    else:
        exit_message()


if __name__=="__main__":
    inquiry()