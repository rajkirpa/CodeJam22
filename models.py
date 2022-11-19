from django.db import models

# Create your models here.

class Courses(models.Model):
    id=models.CharField(max_length=4, primary_key=True)
    name=models.TextField(max_length=100)

    def __str__(self):
        return self.name
    
class Users(models.Model):
    id=models.CharField(max_length=9, primary_key=True)
    birth_year=models.IntegerField(default=0)
    nationality=models.TextField(max_length=20, default="")
    fullname=models.TextField(max_length=20)
    password=models.CharField(max_length=16,default="")

    def __str__(self):
        return self.fullname

class Course_takers(models.Model):
    """course is named course_id in table"""
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    """user is named user_id in table"""
    user=models.ForeignKey(Users, on_delete=models.CASCADE)

