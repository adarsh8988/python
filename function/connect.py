import mysql.connector
con=mysql.connector.connect(host="localhost",username="root",password="Akarsh!@2001",database="employees")
if con.is_connected():
    print("your database connect successfully")
curser=con.cursor()
# curser.execute("insert into employee values('harry' , 27 , 9889878897 , 'harry3434@gmail.com')")
# con.commit()
curser.execute("select * from employee")
zx=curser.fetchall()
print(zx)

    
