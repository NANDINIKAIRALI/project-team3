from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Job  
from django.views.decorators.cache import never_cache

def HomePage(request):
     if request.method=='POST':
            username = request.POST.get('username')

            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
               login(request,user) #session
               #  return render(request,'profile.html')
               return redirect('profile')
            else:
               return redirect('home')
     return render(request,'home.html')
 
 
def RegisterUser(request):
     form=LoginForm()
     context = {'form':form}
     if request.method=='POST':
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')
     return render(request, 'register.html', context)
@login_required(login_url='home') 

@never_cache
def Profile(request):
      job = Job.objects.all()
      jobsearch=request.GET.get('job')
      if jobsearch!='' and jobsearch is not None:
         job=job.filter(job_name__icontains=jobsearch)

      context={'Job':job}
      return render(request,'profile.html',context)
def Logout(request):
      logout(request)
      return redirect('home')