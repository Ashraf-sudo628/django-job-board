from pickle import FALSE
from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

# Create your views here.

def send_message(request):
    myInfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
           fail_silently=False,
        )

    return render(request,'contact/contact.html',{'myInfo' : myInfo})
