from django.db import models

# Create your models here.

class Course(models.Model):
    id=models.CharField(max_length=4, primary_key=True)
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class User(models.Model):
    id=models.CharField(max_length=9, primary_key=True)
    birth_year=models.IntegerField(default=0)
    nationality=models.CharField(max_length=20, default="")
    fullname=models.CharField(max_length=20)
    password=models.CharField(max_length=16,default="")

    def __str__(self):
        return self.fullname

class Course_taker(models.Model):
    """course is named course_id in table"""
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    """user is named user_id in table"""
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.id
