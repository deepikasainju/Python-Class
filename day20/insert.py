from estd_connection import estd_connection

cursor=estd_connection()

id= input("enter student id:")
name=input("enter student name:")
age=input("enter your age:")

sql=f"""
INSERT INTO STUDENT (ID, NAME, AGE) VALUES ('{id}' , '{name}', {age})
"""

cursor.execute(sql)
print("student added successfully!!")