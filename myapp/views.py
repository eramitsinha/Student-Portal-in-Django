from django.shortcuts import render,redirect
from .models import Student
from django.core.mail import send_mail
# Create your views here.
def register(request):
	return render(request,"myapp/register.html")

def save(request):
	n1 = request.POST['n1']
	e1 = request.POST['e1']
	p1 = request.POST['p1']
	a1 = request.POST['a1']
	m1 = request.POST['m1']

	obj = Student(name=n1, email=e1, adhar=a1, password=p1, mobile=m1)
	obj.save()
	return render(request,"myapp/register.html",{'message':'Registration Successful'})

def login(request):
	return render(request,"myapp/login.html")

def logincheck(request):
	#fetch form values
	e1 = request.POST['e1']
	p1 = request.POST['p1']

	k = Student.objects.filter(email=e1, password=p1)
	if(k.count()==1):
		request.session['mysession'] = e1
		return redirect("dashboard")
	else:
		return render(request,"myapp/login.html",{'message':'Error! Invalid Email or Password.'})

def dashboard(request):
	# fetch session
	e1 = request.session['mysession']

	if(request.session.has_key('mysession')): #check if session is active
		return render(request,"myapp/dashboard.html")
	else:
		return redirect("login")

def logout(request):
	del request.session['mysession']
	return redirect("login")

def profile(request):
	# fetch session
	e1 = request.session['mysession']

	if(request.session.has_key('mysession')): #check if session is active
		
		#fetching user details who has logged in
		user_data = Student.objects.filter(email=e1)
		# select * from table where email=$e1

		return render(request,"myapp/profile.html",{"user_data":user_data})
	else:
		return redirect("login")

def students(request):
	user_data = Student.objects.all()
	return render(request,"myapp/students.html",{"user_data":user_data}) 

def edit(request):
	# fetch session
	e1 = request.session['mysession']

	if(request.session.has_key('mysession')): #check if session is active
		
		#fetching user details who has logged in
		user_data = Student.objects.filter(email=e1)
		# select * from table where email=$e1

		return render(request,"myapp/edit.html",{"user_data":user_data})
	else:
		return redirect("login")

def update(request):
	e1 = request.session['mysession']

	#form values fetch
	n1 = request.POST['n1']
	p1 = request.POST['p1']
	a1 = request.POST['a1']
	m1 = request.POST['m1']

	k = Student.objects.get(pk=e1) #pk - primary key
	k.name=n1
	k.mobile=m1
	k.adhar = a1
	k.mobile=m1
	k.save()
	return redirect("profile")

def contact(request):
	return render(request,"myapp/contact.html")

def send(request):
	# fetch form values
	n1 = request.POST['n1']
	m1 = request.POST['m1']
	message = request.POST['message']

	send_mail("New Email",message,"admin@gmail.com",['amit@gmail.com'])
	return render(request,"myapp/contact.html",{"message":"Email Sent"})

def upload(request):
	return render(request,"myapp/upload.html")