from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.shortcuts import render
from .forms import  LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import User,adminuser
from django.shortcuts import render, redirect
from .models import Notification  # Assuming you have a Notification model
from django.shortcuts import render
from .models import Notification
from django.shortcuts import render, redirect
from .models import Notification



def notification_page(request):
    notifications = Notification.objects.all()
    return render(request, 'notification.html', {'notifications': notifications})


def notification_view(request):
    notifications = Notification.objects.all()  # Fetch notifications from the database
    return render(request, 'notification.html', {'notifications': notifications})


def submit_message(request):
    if request.method == 'POST':
        message = request.POST.get('messageInput')
        Notification.objects.create(message=message)
        # return redirect('notification')  # Redirect to the notification page after submission
    return render(request, 'adminmessage.html')

def notification(request):
    notifications = Notification.objects.all()
    return render(request, 'notification.html', {'notifications': notifications})


def form_view(request):
    return render(request, 'form.html')

def display_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        return render(request, 'display.html', {'message': message})
    else:
        return render(request, 'display.html', {'message': ''})


# Create your views here.
def index(request):
    return render(request,"template/index.html")
'''
def stlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
            # Add logic to authenticate user (e.g., check against database)
             user =User(username=username,  password=password)
            # if user is not None:
            #     login(request,user)
             return redirect('home')  # Redirect to dashboard upon successful login
    else:
        form = LoginForm()
        return render(request, 'stlogin.html', {'form':form})
        
        
'''


def stlogin(request):
    page = 'stlogin'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password'].lower()

            try:
                user = User.objects.get(username=username )
            except User.DoesNotExist:
                messages.error(request, 'User Does Not Exist')
                return redirect('stlogin')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid Username or Password')
                return redirect('home')
        else:
            messages.error(request, 'Invalid Form Submission')
            return redirect('stlogin')
    else:
        form = LoginForm()

    context = {'page': page, 'form': form}
    return render(request, 'stlogin.html', context)

def streg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']  # Get confirm password field
            if password == confirm_password:  # Check if passwords match
                # Create and save user object to database
                user = User(username=username, email=email, password=password)
                user.save()
                print("User saved successfully!")  # Print success message
                # Redirect user to login page or show success message
                return redirect('stlogin')  # Example redirect to login page
            else:
                # Passwords don't match, handle accordingly (e.g., display error message)
                return render(request, 'streg.html', {'form': form, 'error_message': 'Passwords do not match'})
    else:
        form = RegistrationForm()
    return render(request, 'streg.html', {'form': form})

def adlogin(request):
    page = 'adlogin'
    if request.user.is_authenticated:
        return redirect('adminhome')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password'].lower()

            try:
                user = adminuser.objects.get(username=username )
            except adminuser.DoesNotExist:
                messages.error(request, 'User Does Not Exist')
                return redirect('adlogin')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('adminhome')
            else:
                messages.error(request, 'Invalid Username or Password')
                return redirect('adminhome')
        else:
            messages.error(request, 'Invalid Form Submission')
            return redirect('adlogin')
    else:
        form = LoginForm()

    context = {'page': page, 'form': form}
    return render(request, 'adlogin.html', context)


def dashboard(request):
    return render(request,"template/dashboard.html")

def adreg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Create user object and save to database
            user = adminuser(username=username, email=email, password=password)
            user.save()
            # Redirect to login page after successful registration
            return redirect('adlogin')
    else:
        form = RegistrationForm()
    return render(request, 'adreg.html', {'form': form})

def adminmessage(request):
    return render(request,"template/adminmessage.html")

# def home(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('pw')
    #     confirm_password = request.POST.get('cp')
    #     if password == confirm_password:
    #         user = User.ob
    # jects.create(username=username, password=password)
    #         user.save()
    #         return redirect('success1')
    #     else:
    #         return render(request, 'reg.html', {'error': 'Passwords do not match'})
    # retun render(request, 'login1.html')

    
def home(request):
    return render(request,"template/home.html") 
def bcaabout(request):
    return render(request,"template/bcaabout.html") 

def img3(request):
    return render(request,"template/img3.html")
def adminhome(request):
    return render(request,"template/adminhome.html")
def adminlogin(request):
    return render(request,"template/adminlogin.html")
def contact (request):
    return render(request,"template/contact.html")
def aboutlab(request):
    return render(request,"template/aboutlab.html")
def details(request):
    return render(request,"template/details.html")
def feedback(request):
    return render(request,"template/feedback.html")

def seatbca(request):
    return render(request,"template/seatbca.html")
def notification(request):
    return render(request,"template/notification.html")

def mphill(request):
    return render(request,"template/mphill.html")

def seatbsc(request):
    return render(request,"template/seatbsc.html")

def seatmscit(request):
    return render(request,"template/seatmscit.html")
    
def mess(request):
    return render(request,"template/mess.html")
