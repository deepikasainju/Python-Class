from estd_connection import estd_connection

cursor=estd_connection()

id= input("enter student id:")
to_change=input("enter the data you want to change")
changed_value=input(f"enter the new {to_change}")

sql=f"""
UPDATE STUDENT SET {to_change} ='{changed_value}' WHERE ID='{id}'
"""

cursor.execute(sql)
print("student updated successfully")