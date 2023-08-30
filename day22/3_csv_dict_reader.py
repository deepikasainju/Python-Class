import csv

filename="students.csv"
with open(filename, "r") as cr:
    for each in csv.DictReader(cr):
        print(each)


'''
{'id': '1', 'name': 'jon', 'age': '20', 'address': 'KTM'}
{'id': '2', 'name': 'jane', 'age': '30', 'address': 'BKT'}
{'id': '3', 'name': 'ken', 'age': '45', 'address': 'PKR'}
'''