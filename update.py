import mysql.connector as c

con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'emp')

cursor = con.cursor()

name = input("Enter your name")
age = int(input("Enter your age"))
# sal = int(input("Enter your salary"))

query = "update alpha set age = {} where name = '{}'".format(age,name)
cursor.execute(query)
con.commit()
print("Data updated successfully!!")