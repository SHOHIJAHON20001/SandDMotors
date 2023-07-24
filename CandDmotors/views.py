from django.shortcuts import render, get_object_or_404
from config.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from .models import Galareya
from django.http import HttpResponse
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
    return render(request, 'contact.html')


def mail_send(request):
    if request.method == 'POST':
        name = request.POST['name']
        sender_email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']

        email = EmailMessage(
            f"xabar jo'natuvchi: {sender_email}",
            f"Ismi: {name}\n\n Elektron pochta manzili: {sender_email}/n/n Telefon: {phone}\n\n Xabar: {msg}",
            sender_email,
            [EMAIL_HOST_USER],
        )
        email.fail_silently = False
        email.send()
        print(name, sender_email, phone, msg)
        return HttpResponse('Muvaffaqqiyatli')
    else:
        return HttpResponse("Muvaffaqqiyatsiz!!")