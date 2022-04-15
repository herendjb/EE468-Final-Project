#https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html

#python -m pip install mysql-connector-python
import mysql.connector

#to connect to mysql db on your own computer, use localhost
#to connect to a remote computer, use its IP address for host:
mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  passwd='99410Victor!', #"mypassword",
  auth_plugin='mysql_native_password',
  database="university",
)

#print(mydb)

mycursor = mydb.cursor()

#instructor

print('Instructor table')
sql="select instructor.id, instructor.name, instructor.dept_name, instructor.salary from instructor"
print(sql)

mycursor.execute(sql)
myresult = mycursor.fetchall()

print(mycursor.rowcount," instructors found")

for(name) in myresult:
   print(name)

#student

print('\nStudent table')
sql="select student .id, student .name, student .dept, student .total_credits from student"
print(sql)

mycursor.execute(sql)
myresult = mycursor.fetchall()

print(mycursor.rowcount," students found")

for(name) in myresult:
   print(name)

#department

print('\nDepartment table')
sql="select department.dept_name, department.building, department.budget from department"
print(sql)

mycursor.execute(sql)
myresult = mycursor.fetchall()

print(mycursor.rowcount," departments found")

for(name) in myresult:
   print(name)

mycursor.close()
mydb.close()
