from django.forms import ModelForm

from . models import Course,Course_taker,User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class Course_takerForm(ModelForm):
    class Meta:
        model = Course_taker
        fields = ['course','user']

