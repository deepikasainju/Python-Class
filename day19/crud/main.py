from day19.crud.create import create_student
from day19.crud.read import read_student
from day19.crud.update import update_student
from day19.crud.delete import delete_student

def inquiry():
    selection=input("enter your choice c/r/u/d/e:")
    selection=selection.lower()

    def exit_message():
        print("thank you. byeeeeeee!!!!!")

    if selection=="c":
        create_student()

    if selection=="r":
        read_student()

    if selection=="u":
        update_student()

    if selection=="d":
        delete_student()

    else:
        exit_message()


if __name__=="__main__":
    inquiry()