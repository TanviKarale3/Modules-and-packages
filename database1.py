import mysql.connector as SQL
try:
    query="insert into studentinfo values(1111,'Tanvi','AI')"
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
