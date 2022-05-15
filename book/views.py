from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from book.models import Author, Books 
from .form import Booksform, CustomUserCreationForm,Authorform,CustomUserCreationForm2
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from openpyxl import load_workbook
# Create your views here.

@login_required (login_url="login")
def index(request):
    
    return render(request,'index.html')


def allusers(request):
    u = User.objects.all()
    context = {'u':u}
    return render(request,'user/allusers.html',context)


def allbooks(request):
    book = Books.objects.all()
    context = {'book':book}
    return render(request,'book/allbook.html',context)

@login_required (login_url="login")
def upload(request):
    use = request.user
    ur = ''
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        ur = fs.url(name)
        
        data = load_workbook(filename = (settings.MED_ROOT + name))
        sheet = data.active
        rows = sheet.rows
        header = next(rows)
        
        for row in rows:
            val = [cell.value for cell in row]
            Books.objects.create(
                title = val[0],
                description = val[1],
                author = Author.objects.get(Id=val[2]),
                rating = val[3],
                user = use,
            )
        
    context = {'ur':ur}
    return render(request,'book/upload.html',context)

@login_required (login_url="login")
def addbook(request):
    use = request.user

    form1 = Authorform()
    if request.method == 'POST':
        form1 = Authorform(request.POST)
        if form1.is_valid():
            autho = form1.save(commit=False)
            a=autho.name
            if Author.objects.filter(name=a).exists():
                messages.error(request,'Author already exists!')
            else:
                autho.save()
                messages.success(request,'Author Save!')
    
    form2 = Booksform()
    if request.method == 'POST':
        form2 = Booksform(request.POST)
        if form2.is_valid():
            book = form2.save(commit=False)
            book.user = use
            book.save()
            messages.success(request,'Book Save!')
    
    context = {'form1':form1,'form2':form2}
    return render(request,'book/addbook.html',context)

@login_required (login_url="login")
def updatebook(request,pk):
    i = 1
    us = request.user
    book = Books.objects.get(Id=pk)
    form2 = Booksform(instance=book)

    if request.method == 'POST':
        form2 = Booksform(request.POST,instance=book)
        if form2.is_valid():
            if book.user == us : 
                form2.save()
                return redirect('allbook')
            else:
                messages.error(request,'Same User can only change the details !')
                
    cotext = {'form2':form2,'i':i}
    return render(request,'book/addbook.html',cotext)

@login_required (login_url="login")
def deletebook(request,pk):
    us = request.user
    book = Books.objects.get(Id=pk)
    
    if request.method =='POST':
        if book.user == us:
            book.delete()
            return redirect('allbook')
        
    context = {'object':book}
    return render(request,'delete.html',context)

@login_required (login_url="login")
def updateuser(request,pk):
    i = 1
    us = request.user
    use = User.objects.get(id=pk)
    form = CustomUserCreationForm2(instance=use)

    if request.method == 'POST':
        form = CustomUserCreationForm2(request.POST,instance=use)
        if form.is_valid():
            if use == us :
                
                form.save()
                return redirect('allbook')
            else:
                messages.error(request,'Same User can only change the details !')
                
    cotext = {'form':form,'i':i}
    return render(request,'user/register.html',cotext)



@login_required (login_url="login")
def deleteuser(request,pk):
    us = request.user
    use = User.objects.get(id=pk)
    
    if request.method =='POST':
        if use == us:
            use.delete()
            return redirect('allusers')
        else:
            messages.error(request,'Same User can only detele the User !')
    context = {'object':use}
    return render(request,'delete.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('indexpage')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'username does not exist')
       
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else'indexpage')
        else:
            messages.error (request,"username or password is incorrect") 
    
    return render(request, 'user/login.html')

def registeruser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'Registration successfull!')
            
        else:
            messages.error(request,'An error has beeen occurred buring registration')

    context = {'form':form }
    return render(request,"user/register.html",context)    
