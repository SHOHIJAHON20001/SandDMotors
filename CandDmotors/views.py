from django.shortcuts import render
from config.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from .models import Galareya
# Create your views here.


def home(request):
    gallerys = Galareya.objects.all()
    context  = {
        'gallerys':gallerys
    }
    return render(request, 'index.html', context)

def gallery(request):
    gallerys = Galareya.objects.all()
    context  = {
        'gallerys':gallerys
    }
    return render(request, 'portfolio-details.html', context)



def send_mail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        email = EmailMessage(
            f"xabar jo'natuvchi: {email}",
            f"Ismi: {name}\n\n Elektron pochta manzili: {email}/n/n Telefon: {subject}\n\n Xabar: {message}",
            email,
            [EMAIL_HOST_USER],
        )
        email.fail_silently = False
        email.send()
    return render(request, 'contact.html', {'name':name})