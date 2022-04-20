from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. <br> at the next line")

def index2(request):
    return HttpResponse("Hello, world. You're at the polls index2.")

def instructor(request):
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	print('Instructor table')
	sql="select instructor.id, instructor.name, instructor.dept_name, instructor.salary from instructor"
	print(sql)

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	print(mycursor.rowcount," instructors found")

	s = "Instructor <br><br>"

	for(name) in myresult:
   		s = s + name[1] + " " + name[2] + "<br>"

	return HttpResponse(s)

def student(request):
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	print('\nStudent table')
	sql="select student .id, student .name, student .dept, student .total_credits from student"
	print(sql)

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	print(mycursor.rowcount," students found")

	s = "Student <br><br>"

	for(name) in myresult:
	   s = s + name[1] + name[2]

	return HttpResponse(s)

def department(request):
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	print('\nDepartment table')
	sql="select department.dept_name, department.building, department.budget from department"
	print(sql)

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	print(mycursor.rowcount," departments found")

	s = "Department <br><br>"

	for(name) in myresult:
   		s = s + name[0] + name[1]

	mycursor.close()
	mydb.close()
	return HttpResponse(s)


