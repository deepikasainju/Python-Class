
from estd_connection import estd_connection

cursor=estd_connection() #cursor= estd connection ko object ho

# cursor.execute("DROP TABLE STUDENT")

sql="""
CREATE TABLE STUDENT(
    ID CHAR(20),
    NAME CHAR(20),
    AGE INT
)
"""

cursor.execute(sql) # sql string database ko query ma change gardinxa
print("table created successfully!!")