# JSON stands for javascript object notation
# JSON id file format with .json extension which is used to share data infromation over the internet
# python has a built-in module for json handling
# JSON is similar to [yhton dictionary as it is also written in key-value format. 
# But keys, and values in JSON must be enclosed in double-quotes. single-quotes are not allowed.
# integers and float values do not require quotes in JSON

# examples:
{"name":"maya", "age":45, "address":"KTM"} # valid JSON
{'name':'maya', 'age':45, 'address':'KTM'} # invalid JSON

[
    {"name":"maya", "age":45, "address":"KTM"},
    {"name":"maya", "age":45, "address":"KTM"}
    # valid JSON
]

# variable assign gareki dictionary nai hunxa
import json
filename="student.json"
student={"name":"maya", "age":45, "address":"KTM"} 
students=[
    {"name":"maya", "age":45, "address":"KTM"},
    {"name":"appy", "age":45, "address":"KTM"} 
]
with open(filename, "w+") as fp:
    data=json.dumps(students,indent=2)
    fp.write(data)
    fp.seek(0)
    data=json.loads(fp.read()) # list ma convert garxa str lai
    print(data)

name=data[0]["name"]
print(name) # maya