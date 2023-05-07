from django.shortcuts import render, redirect
from .models import *
from cars.models import *
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User



def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_at').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_at')
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = set(Car.objects.values_list("model", flat=True))
    year_search = set(Car.objects.values_list('year', flat=True))
    city_search = set(Car.objects.values_list('city', flat=True))
    body_style_search = set(Car.objects.values_list('body_style', flat=True))
    
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'year_search': year_search,
        'city_search': city_search,
        'body_style_search': body_style_search,
        
    }
    return render(request, 'pages/home.html', context)



def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Message.objects.create(
            name = name,
            email = email,
            subject = subject,
            phone = phone,
            message = message
        )
        admin_email = User.objects.get(is_superuser=True)
        to_email = admin_email.email
        
        msg = EmailMessage(
            subject,
            message,
            email,
            [to_email],
            )
        msg.send()
        contact.save()
        messages.success(request,"Thank you for contacting us, we will get back to you shortly.")
        return redirect('contacts')
    return render(request, 'contacts/contact.html')
