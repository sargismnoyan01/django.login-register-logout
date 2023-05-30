from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *

class HomeListViews(ListView):
    template_name='index.html'

    def get(self,request):
        leadership=LeaderShip.objects.get()
        youtube=Youtube.objects.all()
        ourstory=OurStory.objects.get()
        ourspeakers=OurSpeakers.objects.get()
        speakers=Speakers.objects.all()
        speakersf=Speakers.objects.first()
        days=Days.objects.all()
        daysf=Days.objects.first()
        subdays=SubDays.objects.all()
        become=Become.objects.get()
        ticket=Ticket.objects.all()
        contact=Contact.objects.get()
        site=Site.objects.get()
        form=ConForm


        context={
            'link':'Home',
            'leadership':leadership,
            'youtube':youtube,
            'ourstory':ourstory,
            'ourspeakers':ourspeakers,
            'speakers':speakers,
            'speakersf':speakersf,
            'days':days,
            'daysf':daysf,
            'subdays':subdays,
            'become':become,
            'ticket':ticket,
            'contact':contact,
            'form':form,
            'site':site,
                }
        return render(request,self.template_name,context)
    
    def post(self,request):
        leadership=LeaderShip.objects.get()
        youtube=Youtube.objects.all()
        ourstory=OurStory.objects.get()
        ourspeakers=OurSpeakers.objects.get()
        speakers=Speakers.objects.all()
        speakersf=Speakers.objects.first()
        days=Days.objects.all()
        daysf=Days.objects.first()
        subdays=SubDays.objects.all()
        become=Become.objects.get()
        ticket=Ticket.objects.all()
        contact=Contact.objects.get()
        if request.method=="POST":
            form=ConForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                form=ConForm()




        context={
            'link':'Home',
            'leadership':leadership,
            'youtube':youtube,
            'ourstory':ourstory,
            'ourspeakers':ourspeakers,
            'speakers':speakers,
            'speakersf':speakersf,
            'days':days,
            'daysf':daysf,
            'subdays':subdays,
            'become':become,
            'ticket':ticket,
            'form':form,
            'contact':contact,
                }
        

        return render(request,self.template_name,context)

    

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

