from django.shortcuts import render,redirect

from django.http import HttpResponse

from . models import Course,Course_taker,User

from . forms import UserForm,CourseForm,Course_takerForm

# Create your views here.

#conn = sqlite3.connect('db.sqlite3')

def index(request):
    return render(request, "index.html")

def users(request):
    #all lists should be in order, each index in every list will be for one user
    """user=[]
    '''names=[]
    ids=[]
    nationalities=[]
    years=[]'''
    cursor=conn.execute("SELECT id,birth_year,nationality,fullname FROM myapp_user")
    for row in cursor:
        '''names.append(row[3])
        ids.append(row[0])
        nationalities.append(row[1])
        years.append(row[2])'''
        user.append(row)

    conn.close()"""

    user=User.objects.all()
    context={"users_list":user}

    return render(request, "users.html", context)

def courses(request):
    course=Course.objects.all()
    context={"courses_list":course}
    return render(request, "courses.html",context)

def course_takers(request):
    course_taker=Course_taker.objects.all()
    context={"course_takers_list":course_taker}
    return render(request,"course_takers.html",context)

def newUser(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = UserForm()
    return render(request,"newUser.html",{"userform":form})

def newCourse(request):
    if request.method=='POST':
        form = CourseForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("/")
        
    else:
        form = CourseForm()
    return render(request,"newCourse.html",{"courseform":form})

def newCourse_taker(request):
    if request.method=='POST':
        form = Course_takerForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect("/")
        
    else:
        form = Course_takerForm()
    return render(request,"newCourse_taker.html",{"course_takerform":form})


