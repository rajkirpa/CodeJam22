from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("signup", views.signup, name = "signup"),
    path("mainmenu", views.mainmenu, name="main-menu"), 
    path("personalmenu", views.personalmenu, name = "personal"),
    path("studentmenu", views.studentmenu, name="student"),
    path("applicationmenu", views.applicationmenu, name = "application"),
    path("financialmenu", views.financialmenu, name="financial"),

    path('homepage', views.homepage, name='homepage'),
    path('homepage/users',views.users, name='users'),
    path('homepage/courses',views.courses, name='courses'),
    path('homepage/course_takers',views.course_takers, name='course_takers'),
    path('homepage/newUser',views.newUser, name='newUser'),
    path('homepage/newCourse',views.newCourse, name='newCourse'),
    path('homepage/newCourse_taker',views.newCourse_taker, name='newCourse_taker'),
]

