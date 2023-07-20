from django.shortcuts import render
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
# Create your views here.


def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'portfolio-details.html')

def send_mail(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        gmail = EmailMessage(
            f"Subject: {subject}",
            f"{message}",
            email,
            [EMAIL_HOST_USER]
        )
        gmail.send(fail_silently = True)
    return render(request, "contact.html", {"name":name})