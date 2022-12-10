import mysql.connector as c

con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'emp')

cursor = con.cursor()

name = input("Enter your name")
age = int(input("Enter your age"))
sal = int(input("Enter your salary"))

query = "Insert into alpha values ('{}',{},{})".format(name,age,sal)
cursor.execute(query)
con.commit()
print("Data enterd successfully!!")