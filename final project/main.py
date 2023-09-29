import tkinter
from tkinter import ttk
from tkinter import messagebox

from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base

Base=declarative_base()

class Entry_Form(Base):
    __tablename__="Form"
    id=Column("ID",Integer,primary_key=True)
    first_name=Column("First Name", String)
    last_name=Column("Last Name", String)
    title=Column("Title", String)
    age=Column("Age", Integer)
    nationality=Column("Nationality",String)
    num_courses=Column("No of Completed Courses",String)
    num_semesters=Column("No of Semester", String)
    registration_status=Column("Registration Status", String)

    def __init__(self,id,first_name,last_name,title,age,nationality,num_courses,num_semesters,registration_status):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.title=title
        self.age=age
        self.nationality=nationality
        self.num_courses=num_courses
        self.num_semesters=num_semesters
        self.registration_status=registration_status

engine=create_engine("sqlite:///entry_form.db", echo=True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()
print("Connection Established!!")



def submit_data():
    status = terms_check_var.get()
    if status == "Accepted":
        id=id_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        num_courses = num_courses_spinbox.get()
        num_semesters = num_semesters_spinbox.get()
        registration_status = reg_status_var.get()

        form_object=Entry_Form(id,first_name,last_name,title,age,nationality,num_courses,num_semesters,registration_status)
        session.add(form_object)
        session.commit()


        print(first_name)
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms and conditions")


window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

id_label = tkinter.Label(user_info_frame, text="ID")
id_label.grid(row=2, column=0)
id_entry = tkinter.Entry(user_info_frame)
id_entry.grid(row=3, column=0)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=1)
age_spinbox.grid(row=3, column=1)


nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Nepal", "Singapore", "Japan"])
nationality_label.grid(row=2, column=2)
nationality_combobox.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")

registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

num_courses_label = tkinter.Label(courses_frame, text="# Completed Courses")
num_courses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
num_courses_label.grid(row=0, column=1)
num_courses_spinbox.grid(row=1, column=1)

num_semesters_label = tkinter.Label(courses_frame, text="# Semesters")
num_semesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
num_semesters_label.grid(row=0, column=2)
num_semesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_check_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions",
                                  variable=terms_check_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Submit", command=submit_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()