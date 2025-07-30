from django.shortcuts import render
from django.http import HttpResponse
from users.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




#importing decorator
#using above authenticate module the django orm save the data automatically

# Create your views here.

#by default view is handaling get request

def user_login(request):

    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid(): #check whether the password is valid
            data=form.cleaned_data 
            user=authenticate(request,username=data['username'],password=data['password'])
#this check whether the user details are in orm if there user user successfully singin
            if user is not None:
                login(request,user)
                return HttpResponse("User authenticated and logged in")
            else:   
                return HttpResponse("invalid login")
    
    else:
        form=LoginForm()

    return render(request,'users/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def index(request):
    return render(request,'users/index.html')