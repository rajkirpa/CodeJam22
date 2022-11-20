from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users',views.users, name='users'),
    path('courses',views.courses, name='courses'),
    path('course_takers',views.course_takers, name='course_takers'),
    path('newUser',views.newUser, name='newUser'),
    path('newCourse',views.newCourse, name='newCourse'),
    path('newCourse_taker',views.newCourse_taker, name='newCourse_taker'),
]