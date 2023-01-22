from django.shortcuts import render,redirect
from .models import *
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


#  -------------------------Student Section ----------------------------------


@login_required(login_url="/login")
def index(request):
    return render(request,'index.html')


def show_students(request):
    student = Student.objects.all()
    return render(request,'show_students.html',{'student':student,})

def add_student(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        address = request.POST['address']

        student = Student(first_name=first_name,last_name=last_name,email=email,age=age,address=address)
        student.save()
        return redirect("/show_students")
    else:
    
        return render(request,'add_student.html')


def update_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']
        address = request.POST['address']

        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        student.age = age
        student.address = address
        student.save()
        return redirect("/show_students")
    else:
        return render(request,'update_student.html',{'student':student,})


def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/show_students")

#  ---------------------- Teacher Section -----------------------------------


def show_teachers(request):
    teacher = Teacher.objects.all()
    return render(request,'show_teachers.html',{'teacher':teacher,})


def add_teacher(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
       

        teacher = Teacher(first_name=first_name,last_name=last_name,email=email,)
        teacher.save()
        return redirect("/show_teachers")
    else:
    
        return render(request,'add_teacher.html')



def update_teacher(request,id):
    teacher = Teacher.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']


        teacher.first_name = first_name
        teacher.last_name = last_name
        teacher.email = email
     
        teacher.save()
        return redirect("/show_teachers")
    else:
        return render(request,'update_teacher.html',{'tch':teacher,})


def delete_teacher(request,id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect("/show_teachers")



#  -----------------  Course Section ---------------------------------------------

def show_courses(request):
    course = Course.objects.all()
    return render(request,'show_courses.html',{'course':course,})



def add_course(request):

    if request.method == "POST":
        course_name = request.POST['course_name']
        fees = request.POST['fees']
        duration = request.POST['duration']

        course = Course(course_name=course_name,fees=fees,duration=duration,)
        course.save()
        return redirect("/show_courses")
    else:
    
        return render(request,'add_course.html')



def update_course(request,id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        course_name = request.POST['course_name']
        fees = request.POST['fees']
        duration = request.POST['duration']


        course.course_name = course_name
        course.fees = fees
        course.duration = duration
     
        course.save()
        return redirect("/show_courses")
    else:
        return render(request,'update_course.html',{'crs':course,})


def delete_course(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("/show_courses")



# ------------------ Authentication and Authorization Section ------------------


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect("/login")
    else:  
        return render(request,'login.html')


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.info(request,"Email Already Exists")
            return redirect("/signup")
        
        
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Already Exists")
            return redirect("/signup")

        new_user = User.objects.create_user(email=email,first_name=first_name,last_name=last_name,username=username,password=password,)
        new_user.save()

        return redirect("/login")
    else:
        return render(request,'signup.html')


def logout(request):
    auth.logout(request)
    return redirect("/login")


