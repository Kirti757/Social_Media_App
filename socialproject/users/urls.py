from re import template
from django.urls import path
from users import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    
    
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),

    path('logout/', views.logout_view, name='logout'),
 

    #this is in built django gives us login and logout page also


]
