from django.contrib import admin

from . models import Course,Course_taker,User

# Register your models here.

admin.site.register(Course)
admin.site.register(User)
admin.site.register(Course_taker)
