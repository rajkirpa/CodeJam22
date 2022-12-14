# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from . models import Course,Course_taker,User
from . forms import UserForm,CourseForm,Course_takerForm

def home(request):
    try:        
        return render(request, "myapp/home.html")    
    except:
        return Http404


def mainmenu(request):
    try:
        return render(request, "myapp/MainMenu.html")
    except:
        return HttpResponseBadRequest("bro...")



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "myapp/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
    return render(request, "myapp/MainMenu.html")


def signup(request):
    if request.method == 'POST':
        student_id = request.POST['student_ID']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        password_conf = request.POST['password_conf']

        myUser = User.objects.create_user(student_id, password)
        myUser.first_name = fname
        myUser.last_name = lname

        myUser.save()

        messages.success(request, "Your account has been created")

        return redirect('signin')
    return render(request, "myapp/signup.html")


    
def homepage(request):
    return render(request, "myapp/homepage.html")

def users(request):
    user=User.objects.all()
    context={"users_list":user}

    return render(request, "myapp/users.html", context)

def courses(request):
    course=Course.objects.all()
    context={"courses_list":course}
    return render(request, "myapp/courses.html",context)

def course_takers(request):
    course_taker=Course_taker.objects.all()
    context={"course_takers_list":course_taker}
    return render(request,"myapp/course_takers.html",context)

def newUser(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/homepage")
    else:
        form = UserForm()
    return render(request,"myapp/newUser.html",{"userform":form})

def newCourse(request):
    if request.method=='POST':
        form = CourseForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("/homepage")
        
    else:
        form = CourseForm()
    return render(request,"myapp/newCourse.html",{"courseform":form})

def newCourse_taker(request):
    if request.method=='POST':
        form = Course_takerForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("/homepage")
        
    else:
        form = Course_takerForm()
    return render(request,"myapp/newCourse_taker.html",{"course_takerform":form})

def personalmenu(request):
    return HttpResponse("personal menu")

def studentmenu(request):
    return HttpResponse("student menu")

def applicationmenu(request):
    return HttpResponse("application menu")

def financialmenu(request):
    return HttpResponse("financial menu")