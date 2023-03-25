import mysql.connector as SQL
try:
    sid=input("Enter StudentId=>")
    sname=input("Enter StudentName=>")
    br=input("Enter Student Branch=>")
    query="insert into studentinfo values("+sid+",'"+sname+"','"+br+"')"
    print(query)
    conn=SQL.connect(user="root",password="",database="mydata")
    cur=conn.cursor()
    cur.execute(query)
    if cur.rowcount==1:
        print("Record Inserted...")
        conn.commit()
    else:
        print("Record Not Inserted...")
    conn.close()
except Exception as e:
    print("Error:",e)
