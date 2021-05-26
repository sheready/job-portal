from django.shortcuts import render,redirect
from django.http import HttpResponse, request, response
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import JobForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    jobs = Jobs.objects.all()
    return render(request,'portal/homepage.html',{'jobs':jobs})

@login_required(login_url='login')
def hrpage(request):
    
    details = Hr.objects.all()
    jobs = Jobs.objects.all()
    context = {'details':details,'jobs':jobs}
    return render(request,'portal/hrpage.html',context)


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for' + user )
                return redirect('login')
            

        context = {'form':form}
        return render(request,'portal/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None: 
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username OR password is incorrect')
        
        

        context = {}
        return render(request,'portal/login.html',context)



def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def employee(request,pk_test):
    employee = Employee.objects.filter(id=pk_test)
    status = Hr.objects.all()
    context = {'employee':employee,'status':status}
    return render(request,'portal/employeepage.html',context)

@login_required(login_url='login')
def createjob(request):
    
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'portal/jobpost_form.html',context)

@login_required(login_url='login')
def updatejob(request,pk):

    jobs =Jobs.objects.get(id=pk)
    form = JobForm(instance=jobs)
    if request.method == 'POST':
        form = JobForm(request.POST,instance = jobs)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'portal/jobpost_form.html',context)

@login_required(login_url='login')
def deletejob(request,pk):
    jobs =Jobs.objects.get(id=pk)
    if request.method == 'POST':
        jobs.delete()
        return redirect('/')
    context = {'item':jobs}
    return render(request,'portal/deletejob.html',context)

