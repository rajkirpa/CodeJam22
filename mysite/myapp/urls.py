from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("signup", views.signup, name = "signup"),
    path("mainmenu", views.mainmenu, name="main-menu")
]
