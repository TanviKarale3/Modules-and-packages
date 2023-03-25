import mysql.connector as SQL
try:
    sid=input("Enter StudentId=>")
    sname=input("Enter StudentName=>")
    br=input("Enter Student Branch=>")
    query="insert into studentinfo values(%s,%s,%s)"
    conn=SQL.connect(user="root",password="",database="mydata")
    cur=conn.cursor()
    lst=[sid,sname,br]
    cur.execute(query,lst)
    if cur.rowcount==1:
        print("Record Inserted...")
        conn.commit()
    else:
        print("Record Not Inserted...")
    conn.close()
except Exception as e:
    print("Error:",e)
