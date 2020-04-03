from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == "POST":
        asset_id = request.POST['asset_id']
        name = request.POST['name']
        rollno = request.POST['rollno']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(asset_id=asset_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this asset')
                return redirect('dashboard')

        contact = Contact(asset_id=asset_id, name=name,rollno=rollno, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(request, 'Your request has been submitted')
        return redirect('dashboard')

