# if we want to connect a database from a program (python, javascript) then we need a database connector
# database connector connects your program with database
# mysqlclient, psycopg2 etc. are the connectors

def estd_connection():
    import psycopg2
    conn=psycopg2.connect(
        database="studentdb",
        user="postgres",
        password="shivasainju",
        host="127.0.0.1",
        port=5432
    )
    conn.autocommit=True
    print("connection is established successfully")
    cursor=conn.cursor()
    return cursor
if __name__=="__main__":
    estd_connection()