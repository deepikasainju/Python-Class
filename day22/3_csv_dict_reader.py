import csv

filename="students.csv"
with open(filename, "r") as cr:
    result=[]
    for each in csv.DictReader(cr): # dictionary ma convert grxa DictReader ley
        print(each)
        result.append(each)
print(result) # list ma dictionary aauxa


'''
{'id': '1', 'name': 'jon', 'age': '20', 'address': 'KTM'}
{'id': '2', 'name': 'jane', 'age': '30', 'address': 'BKT'}
{'id': '3', 'name': 'ken', 'age': '45', 'address': 'PKR'}
'''