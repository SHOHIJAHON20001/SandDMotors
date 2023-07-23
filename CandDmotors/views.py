from django.shortcuts import render
from config.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from .models import Galareya
# Create your views here.


def home(request):
    gallerys = Galareya.objects.all()[:6]
    context  = {
        'gallerys':gallerys
    }
    return render(request, 'index.html', context)

def gallery(request):
    gallerys = Galareya.objects.all()
    context  = {
        'gallerys':gallerys,
    }
    return render(request, 'portfolio-details.html', context)



def contact(request):
    gallerys = Galareya.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        EmailMessage(
            subject,
            message,
            email,
            name,
            [EMAIL_HOST_USER],
        )
        return render(request, 'index.html', {'name':name, 'gallerys':gallerys})
    else:
        return render(request, 'index.html', {})