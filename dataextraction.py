import mysql.connector as c

con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'emp')

cursor = con.cursor()

query = "select * from alpha"
cursor.execute(query)

# fetchone -----> one data at a time
# fetchmany ----> def the number and u will get the output according to the number.
# fetchall -------> give output of all the data.

# data = cursor.fetchone()
# data = cursor.fetchmany(3)
data = cursor.fetchall()
print(data)