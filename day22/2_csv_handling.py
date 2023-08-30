# csv standas for comma separated values
# csv files have .csv extension

import json
import csv
filename="students.csv"

with open(filename, "r")as cr:
    result=[]
    for count, each_line in enumerate(csv.reader(cr)):
        if count==0:
            continue
        print(each_line)
        data=dict(id=each_line[0], name=each_line[1], age=each_line[2], address=each_line[3])
        result.append(data)

print(result)
"""[
    {'id': '1', 'name': 'jon', 'age': '20', 'address': 'KTM'}, 
    {'id': '2', 'name': 'jane', 'age': '30', 'address': 'BKT'}, 
    {'id': '3', 'name': 'ken', 'age': '45', 'address': 'PKR'}
]"""
        
        

