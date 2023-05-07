from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from contacts.models import Contact
from cars.models import Car
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "welcome to your dashboard")
            return redirect('account:dashboard')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('account:login')
    return render(request, 'accounts/login.html')



def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists.')
                return redirect('account:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already exists.')
                    return redirect('account:register')
                else:
                    user = User.objects.create_user(
                        first_name=firstname,
                        last_name=lastname,
                        email=email,
                        username=username,
                        password=password,
                    )
                    user.save()
                    auth.login(request, user)
                    messages.success(request, 'You are registered successfully')
                    return redirect('/')
        else:
            messages.error(request, 'Password do not match')
            return redirect('account:register')
    return render (request, 'accounts/register.html')


@login_required(login_url= 'account:login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    context = {
        'user_inquiry': user_inquiry
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')
