from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.models import User,auth

from firstapp.forms import LoginForm  
from firstapp.models import Login 
from firstapp.models import Imagetable

from firstapp.forms import ContactForm  
from firstapp.models import Contact 

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
	return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def gallery(request):
	return render(request,'gallery.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def show(request):
	
	return render(request,'show.html')

def new(request):
	obj = Imagetable()
	obj.price = '600'

	return render(request,'new.html',{'obj':obj})	

def new1(request):  
    if request.method == "POST":  
        form = ContactForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/contact.html')  
            except:  
                pass  
    else:  
        form = ContactForm()  
        return render(request,'/contct.html',{'form':form})	 

@csrf_exempt	
def login(request):
    if request.method == 'POST':
	    username = request.POST['username']
	    emailid  = request.POST['emailid']
	    password = request.POST['password']

	    user = auth.authenticate(username=username,emailid=emailid,password=password)

	    if user is not None:
	    	auth.login(request,user)
	    	return redirect("/")
	    else:
	    	messages.info(request,"invalid credentials")
	    	return redirect("login")

    else:
        return render(request,'login.html')        

   
def registration(request):
   

    if request.method == 'POST':
	    username = request.POST['username']
	    email = request.POST['email']
	    password1 = request.POST['password1']
	    password2 = request.POST['password2']

	    if password1==password2:
	    	if User.objects.filter(username=username).exists():
	    		messages.info(request,'username taken')
	    		return redirect('registration.html')
	    	elif User.objects.filter(email=email).exists():
	    		messages.info(request,'email taken')
	    		return redirect('registration.html')
	    	else:
	        	user = User.objects.create_user(username=username, email=email, password=password1)
	        	user.save();
	        	print('user created')
	        	return redirect('login')


	    else:
	     	messages.info(request,'password not matching..')
	     	return redirect('registration.html') 
	    return redirect('/')
    else:
	    return render(request,'registration.html') 


def show1(request):
	
	return render(request,'show1.html')


def show2(request):
	
	return render(request,'show2.html')


def show3(request):
	
	return render(request,'show3.html')

def new2(request):

	return render(request,'new2.html')	

def new3(request):

	return render(request,'new3.html')	

def new4(request):

	return render(request,'new4.html')			



	
		







