import mysql.connector as SQL
studentid=input("Enter Studentid")
try:
    query="delete from studentinfo where studentid=%s"
    conn=SQL.connect(user="root",password="",database="mydata")
    cur=conn.cursor()
    lst=[studentid]
    cur.execute(query,lst)
    if cur.rowcount==1:
        print("Record Deleted...")
        conn.commit()
    conn.close()
except Exception as e:
    print("Error:",e)
