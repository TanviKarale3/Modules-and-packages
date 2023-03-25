import mysql.connector as SQL
try:
    query="create table if not exists studentinfo(studentid integer,studentname varchar(25),studentbranch varchar(50))"
    conn=SQL.connect(user="root",password="",database="mydata")
    cur=conn.cursor()
    cur.execute(query)
    print("Table created...")
    conn.commit()
    conn.close()
except Exception as e:
    print("Error:",e)
