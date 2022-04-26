from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.contrib.auth import authenticate

def index(request):
    return HttpResponse("Hello, world.")

def login_admin(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/admin/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login_adm.html', {'form': form})

def login_professor(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/pro/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login_pro.html', {'form': form})

def login_student(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/stu/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login_stu.html', {'form': form})

def success(request):
    return HttpResponse("Success of form")

def get_main(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'main.html', {'form': form})

def get_admin(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'admin.html', {'form': form})

def get_f1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'f1.html', {'form': form})

def get_professor(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'professor.html', {'form': form})

def get_student(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'student.html', {'form': form})

def F1_1(request): #http://localhost:8000/f11
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost", 
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select instructor.name, instructor.dept_name, instructor.salary from instructor order by instructor.name"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Instructor ordered by name<br><br>"

	for(name) in myresult:
   		s = s + name[0] + " " + name[1] + " " + str(name[2]) + "<br>"

	return HttpResponse(s)

def F1_2(request): #http://localhost:8000/f12
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select instructor.name, instructor.dept_name, instructor.salary from instructor order by instructor.dept_name"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Instructor ordered by department name<br><br>"

	for(name) in myresult:
   		s = s + name[0] + " " + name[1] + " " + str(name[2]) + "<br>"

	return HttpResponse(s)

def F1_3(request): #http://localhost:8000/f13
	import mysql.connector
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd='99410Victor!', #"mypassword",
	  auth_plugin='mysql_native_password',
	  database="university",
	)

	mycursor = mydb.cursor()

	sql="select instructor.name, instructor.dept_name, instructor.salary from instructor order by instructor.salary"

	mycursor.execute(sql)
	myresult = mycursor.fetchall()

	s = "Instructor ordered by salary<br><br>"

	for(name) in myresult:
   		s = s + name[0] + " " + name[1] + " " + str(name[2]) + "<br>"

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

	s = "Create the list of course sections and the number of students enrolled in each section that the professor taught in a given semester<br><br>"

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

	s = "Create the list of students enrolled in a course section taught by the professor in a given semester<br><br>"

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

	s = "Table courses offer by department in a given semester and year<br><br>"

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






