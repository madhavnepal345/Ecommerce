from django.shortcuts import render,redirect
from .forms import Login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

def user_login(request):
    if request.method=="POST":
        form=Login(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=['username'],password=['password'])
            if user is not None:
                login(request,user)
                return HttpResponse("the user is login in sucesfully")
            else:
                return HttpResponse("the crenditals is not matched")
    else:
        form=Login
        return render(request,"user-login.html",{'form':form})


def user_logout(request):
    logout(request)
    return redirect('logout.html')
