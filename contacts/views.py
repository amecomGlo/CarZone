from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from CarZone.settings import EMAIL_HOST_USER
# Create your views here.

def inquiry(request, slug):
    if request.method == 'POST':
        car_slug = request.POST['car_slug']
        car_title = request.POST['car_title']
        car_price = request.POST['car_price']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            contacted = Contact.objects.all().filter(user_id=user_id, car_slug=car_slug)
            if contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait untill we get back to you.')
                return redirect("product:detail", slug=car_slug)
        
        contact = Contact.objects.create(
            car_slug=car_slug,
            car_title=car_title,
            car_price = car_price,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city = city,
            state=state,
            email=email,
            phone=phone,
            message=message
        )
        
        admin_email = User.objects.get(is_superuser=True)
        to_email = admin_email.email
        # from_email = request.user.email
        subject = "New Product Inquiry",
        msg = EmailMessage(
            subject,
            "You have a new inquiry for"+ " " + car_title + ". Please login to your admin page for more info",
            email,
            [to_email],

            )
        msg.send()
        contact.save()
        messages.success(request, 'Thank you for contacting us, we will get back to you shortly.')
        return redirect("product:detail", slug=car_slug)

    
        
        
