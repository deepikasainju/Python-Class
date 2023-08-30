import csv

students=[
    {'id': '1', 'name': 'jon', 'age': '20', 'address': 'KTM'},
    {'id': '2', 'name': 'jane', 'age': '30', 'address': 'BKT'},
    {'id': '3', 'name': 'ken', 'age': '45', 'address': 'PKR'},
    {'id': '4', 'name': 'jonny', 'age': '25', 'address': 'KTM'},   
    {'id': '5', 'name': 'janney', 'age': '40', 'address': 'BKT'},
    {'id': '6', 'name': 'kenya', 'age': '45', 'address': 'PKR'}
]

filename="students_write.csv"

with open(filename, "w")as cw:
    field_name=students[0].keys() #["id", "name", "age"]
    csv_writer=csv.DictWriter(cw,fieldnames=field_name)
    csv_writer.writeheader()
    for student in students:
        if student["age"]>="25":
            csv_writer.writerow(student)