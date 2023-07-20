from django.urls import path
from .views import home, gallery, send_mail

urlpatterns = [
   path('', home, name='home'),
   path('gallery', gallery, name='gallery'),
   path('send_mail', send_mail, name='send_mail'),
]