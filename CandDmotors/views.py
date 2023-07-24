from django.shortcuts import render, get_object_or_404
from config.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
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
    print(gallerys)
    return render(request, 'gallery.html', context)

def gallery_details(request, car_id):
    gallerys = get_object_or_404(Galareya, id=car_id)
    return render(request, 'gallery_details.html', {'gallerys':gallerys})

def services(request):
    return render(request, 'services.html')


def our_team(request):
    return render(request, 'ourteam.html')

def contact(request):
    gallerys = Galareya.objects.all()[:6]
    context  = {
        'gallerys':gallerys
    }
    return render(request, 'contact.html', context)


def mail_send(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_address = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']

        email = EmailMessage(
            f"Avtomobil modeli: {subject}",
            f"Xabar Yuboruvchi: {name}\n\n Elektron pochta manzili: {email_address}\n\n Avtomobil modeli: {subject}\n\n Telefon raqam: {phone}",
            email_address,
            [EMAIL_HOST_USER],
        )
        email.send(fail_silently=False)
        print(name, email_address, subject)
        return render(request, 'contact.html', {'name': name})