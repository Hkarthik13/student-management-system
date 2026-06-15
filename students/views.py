from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        user=User.objects.create_user(username=username,password=password)
        user.save()
        return redirect('/students/login/')
    return render(request, 'register.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/students/')
        else:
            return render(request,'login.html',{'error':'Invalid username or password'})
    
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/students/login/')

@login_required(login_url='/students/login/')
def student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})

@login_required(login_url='/students/login/')
def add_student(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/')
    else:
        form=StudentForm()
    return render(request,'student_form.html',{'form':form})

@login_required(login_url='/students/login/')
def edit_student(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students/')
    else:
        form=StudentForm(instance=student)
    return render(request,'student_form.html',{'form':form})

@login_required(login_url='/students/login/')
def delete_student(request,id):
    student=get_object_or_404(Student,id=id)
    student.delete()
    return redirect('/students/')

@login_required(login_url='/students/login/')
def student_detail(request,id):
    student=get_object_or_404(Student,id=id)
    return render(request,'student_detail.html',{'student':student})

@login_required(login_url='/students/login/')
def student_search(request):
    query=request.GET.get('q')
    students=Student.objects.filter(name__icontains=query)
    return render(request,'student_list.html',{'students':students})
