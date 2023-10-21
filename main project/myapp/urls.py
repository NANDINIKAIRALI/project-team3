from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.HomePage,name="home"),
    path('register/',views.RegisterUser,name="register"),
    path('profile/',views.Profile,name="profile"),
    path('logout/',views.Logout,name="logout")
]