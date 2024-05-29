from django.shortcuts import render,HttpResponse,redirect
from .models import register

# Create your views here.

def homepage(request,id):
    user_data = register.objects.get(id=id)
    return render(request,'homepage.html',{'value':user_data})

def registerpage(request):
    if request.method == 'POST':
        getfirst = request.POST.get('firstname')
        getlast = request.POST.get('lastname')
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        getrepassword = request.POST.get('repassword')
        getgender = request.POST.get('gender')
        if getrepassword == getpassword:
            users = register()
            users.FIRSTNAME = getfirst
            users.LASTNAME = getlast
            users.USERNAME = getusername
            users.PASSWORD = getpassword
            users.GENDER = getgender
            users.save()
            return redirect('/login')
        else:
            return HttpResponse('please enter same password in confirm password')
    return render(request,'register.html')

def pending(request):
    details = register.objects.filter(Status=False)
    return render(request,'pending.html',{'value':details})
def approve(request,id):
    data = register.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/pending')


def login(request):
    if request.method == 'POST':
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')

        try:
            user = register.objects.get(USERNAME=getusername, PASSWORD=getpassword)
            return redirect(f'/homepage/{user.id}')
        except:
            return redirect('/register')

    return render(request,'login page.html',{'value':None})

def editpage(request):
    details = register.objects.all()
    return render(request,'editpage.html',{'value':details})

def edit(request,id):
    details = register.objects.all()
    user_data = register.objects.get(id=id)
    if request.method == 'POST':
        getfirst = request.POST.get('firstname')
        getlast = request.POST.get('lastname')
        getpassword = request.POST.get('password')
        user_data.FIRSTNAME = getfirst
        user_data.LASTNAME = getlast
        user_data.PASSWORD = getpassword
        user_data.save()
        return redirect('/editpage')
    return render(request,'editpage.html',{'value':details,'data':user_data})

def delete(request,id):
    data = register.objects.get(id=id).delete()
    return redirect('/editpage')

def approvedlist(request):
    data = register.objects.filter(Status=True)
    return render(request,'approved.html',{'value':data})

def adminlogin(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        if Username == 'admin123' and Password == 'admin@123':
            return redirect('/pending')
        else:
            return HttpResponse('invalid user')
    return render(request, 'adminlogin.html')

def enter(request):
    return render(request, 'enter.html')

def profile(request,id):
    user_data = register.objects.get(id=id)
    if request.method == 'POST':
        getfirst = request.POST.get('firstname')
        getlast = request.POST.get('lastname')
        getpassword = request.POST.get('password')
        getdesignation = request.POST.get('designation')
        getmail = request.POST.get('email')
        getpicture = request.FILES.get('picture',None)
        user_data.FIRSTNAME = getfirst
        user_data.LASTNAME = getlast
        user_data.PASSWORD = getpassword
        user_data.DESIGNATION = getdesignation
        user_data.MAIL = getmail
        user_data.PICTURE = getpicture

        user_data.save()
        return redirect(f'/homepage/{user_data.id}')
    return render(request, 'profile.html',{'data': user_data})