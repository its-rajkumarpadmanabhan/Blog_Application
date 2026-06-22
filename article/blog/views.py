from django.shortcuts import render ,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'home.html')

def log(request):
    return render(request,'log.html')


def sign(request):
    user=None
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        print(username,password)

        try:
            user= User.objects.create_user(username=username,password=password)
            return redirect('log')
        except :
            return redirect('sign') 
        
  
    return render(request,'signup.html',{'user':user})

    
def user(request):
    return render(request,'userprofile.html')