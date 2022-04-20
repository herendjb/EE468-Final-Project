from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def F1(request): #http://localhost:8000/f1
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select instructor.name from instructor order by instructor.name"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Instructor ordered by name<br><br>"

	for(name) in myresult:
   		s = s + name[0] + "<br>"

	return HttpResponse(s)

def F2(request): #http://localhost:8000/f2
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select instructor.dept_name, min(instructor.salary), max(instructor.salary), avg(instructor.salary) from instructor group by instructor.dept_name"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Table of min/max/avg salaries by dept<br><br>"
	s = s + "Dept     min         max      avg<br>"

	for(name) in myresult:
   		s = s + name[0] + " " + str(name[1]) + " " + str(name[2]) + " " + str(name[3]) + "<br>"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	return HttpResponse(s)

def F3(request): #http://localhost:8000/f3
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select distinct instructor.name, instructor.dept_name from instructor join student on (instructor.id=student.id)"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Table of Professor Name, Department, and total number of students<br><br>"

	for(name) in myresult:
   		s = s + name[0] + " " + name[1] + "<br>"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	return HttpResponse(s)

def F4(request): #http://localhost:8000/f4
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select teaches.course_id from teaches"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "F4<br><br>"

	for(name) in myresult:
   		s = s + name[0] + "<br>"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	return HttpResponse(s)

def F5(request): #http://localhost:8000/f5
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select student.name from student"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "F5<br><br>"

	for(name) in myresult:
   		s = s + name[0] + "<br>"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	return HttpResponse(s)

def F6(request): #http://localhost:8000/f6
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select teaches.course_id, teaches.semester, teaches.year from teaches"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Table courses offer by department in a gviven semester and year<br><br>"

	for(name) in myresult:
   		s = s + name[0] + " " + str(name[1]) + " " + str(name[2]) + "<br>"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	return HttpResponse(s)

def instructor(request): #http://localhost:8000/ins
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select instructor.id, instructor.name, instructor.dept_name, instructor.salary from instructor"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Instructor <br><br>"

	for(name) in myresult:
   		s = s + str(name[0]) + " " + name[1] + " " + name[2] + " " + str(name[3])+ "<br>"

	return HttpResponse(s)

def student(request): #http://localhost:8000/stu
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select student.id, student.name, student.dept, student.total_credits from student"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Student <br><br>"

	for(name) in myresult:
	   s = s + " " + str(name[0]) + " "+ name[1] + " " + name[2] + " " + str(name[3]) + " " + "<br>"

	return HttpResponse(s)

def department(request): #http://localhost:8000/dept/
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select department.dept_name, department.building, department.budget from department"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Department <br><br>"

	for(name) in myresult:
   		s = s + name[0] + " " + name[1] + " " + str(name[2]) + " " + "<br>"

	mycursor.close()
	mydb.close()
	return HttpResponse(s)
