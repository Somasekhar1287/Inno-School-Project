from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["Password"]
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return redirect("homepage:index")
            #render(request,"homepage/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('user_auth:signin')
    return render(request,"user_auth/signin.html")

def signup(request):
    pass
'''   if request.method=="POST":
        username=request.POST["username"]
        first_name=request.POST["firstName"]
        last_name=request.POST["lastName"]
        email=request.POST["email"]
        password=request.POST["Password"]
        
        user=User.objects.create_user(username,email,password)
        user.first_name=first_name
        user.last_name=last_name
        
        user.save()
        
        messages.success(request, "Your account is registered")
        return redirect('login:signin')
        
    return render(request,"user_auth/signup.html")
'''

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('homepage:index')
# Create your views here.
