
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404


def home(request):
    try:        
        return render(request, "myapp/home.html")    
    except:
        return Http404

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

def mainmenu(request):
    try:
        return render(request, "myapp/MainMenu.html")
    except:
        return Http404

