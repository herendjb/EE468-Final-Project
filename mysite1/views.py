from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

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
