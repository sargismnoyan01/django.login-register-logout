from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *



def RegisterPage(request):
    form=Create()
    if request.method=="POST":
        form=Create(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=Create()

    return render(request,'register.html',{'form':form})




def LoginPage(request):
    template_name='login.html'

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('register')

    return render(request,template_name)


def logout_request(request):
	logout(request)
	return redirect("home")


