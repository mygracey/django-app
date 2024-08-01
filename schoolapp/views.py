from django.shortcuts import render,redirect
from .models import SchoolModel
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def indexPage(request):
    return render(request,'index.html')



def registerPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pword=request.POST.get('password')
        cpword=request.POST.get('cpassword')
        
        if pword==cpword:
            if uname=="" or email=="" or pword=="" or cpword=="":
                return HttpResponse("Please fill in all fields!")
            elif SchoolModel.objects.filter(username=uname,email=email,password=pword).exists():
             return redirect('/products')
            else:
                student=SchoolModel.objects.create(username=uname,email=email,password=pword)
                student.save()
                msg="Hi " + uname + " your account was successfully created.Proceed to login"
                return render(request,'index.html',{'msg':msg})
        else:
            HttpResponse("sorry, passwords don't match")
    return render(request,'register.html')


# @login_required(login_url="/register")
def productsPage(request):
    
    return render(request,'products.html')



def logoutPage(request):
    logout(request)
    return redirect('/logout')